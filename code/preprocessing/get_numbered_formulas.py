import requests
import pdf2image 
import numpy as np
from PIL import Image
import pytesseract
import re
import os
from dotenv import load_dotenv
import json
import os
import io 
import pandas as pd
import PyPDF2
import csv 
from itertools import islice
import asyncio
from tqdm import tqdm


load_dotenv()
APP_ID = os.getenv('APP_ID')
APP_KEY = os.getenv('APP_KEY')

headers = {
        'app_id': APP_ID,
        'app_key': APP_KEY,
    }

chunksize = 50

def convert_to_base_64(image):
    buffer = io.BytesIO()
    # Save the image to this buffer in a specific format like 'JPEG' or 'PNG'
    image.save(buffer, format='JPEG')
    # Retrieve the binary string
    binary_string = buffer.getvalue()
    return binary_string

pattern = r" 0\\n\( (\d+ \d+ \d+ \d+) ((?:0\\n\d+ \d+ \d+ \d+ \d+ )+)0\\n\) \d+ \d+ \d+ \d+"
compiled_pattern = re.compile(pattern)

pattern_2 = r"(\(\d+\))"
compiled_pattern_2 = re.compile(pattern_2)

async def get_latex(image, formula):
    global headers
    files = {
        'file': convert_to_base_64(image),
        'options_json': (None, json.dumps({'math_inline_delimiters': ['$', '$'], 'rm_spaces': True, 'formats': ['text']})),
    }
    try:
        response = requests.post('https://api.mathpix.com/v3/text', headers=headers, files=files)
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        exit(1) 

    latex_response = json.loads(response.text)['text']

    try:
        str_formula_num = re.findall(compiled_pattern_2, latex_response)[0]
    except:
        str_formula_num = f'({formula})'

    latex_response = latex_response.replace(re.findall(compiled_pattern_2, str_formula_num)[0], '').strip()
    formula_num = int(str_formula_num)
        
    return {formula_num: latex_response}

async def get_formulas(image):
    global compiled_pattern
    output_lst = []
    data = pytesseract.image_to_boxes(Image.fromarray(np.asarray(image)[:, 0:1200]))
    # Define the regex pattern
    matches = re.findall(compiled_pattern, repr(data))
    for match in matches:
        if int(match[1].split(' ')[1:][2]) < 700:
            bottom, top =int(match[0].split(' ')[1]), int(match[0].split(' ')[3])
            formula_number = int(''.join([x[0] for x in match[1].split(r'\n')[1:]]))
            cropped_formula = Image.fromarray(np.asarray(image)[- top -100:-bottom + 100])
            output_lst.append((formula_number, cropped_formula))

    return output_lst

def get_num_pages(pdf):
    pdf_file = io.BytesIO(pdf.content)
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    num_pages = len(pdf_reader.pages)
    return num_pages

 
async def extract_formulas(step, url, folder_path, book):
    global chunksize

    pdf = requests.get(url, stream=True)
    num_pages = get_num_pages(pdf)

    def chunker(size):
        it = list(range(num_pages))
        iterator = iter(it)
        while chunk := list(islice(iterator, size)):
            yield chunk[0], chunk[-1]
        
    formula_headers = ['Formula', 'Statement']

    with open(f"{folder_path}/formulas.csv", 'a+', newline='', encoding='utf-8') as formulas_file:
        formula_writer = csv.DictWriter(formulas_file, fieldnames=formula_headers)

        formula_writer.writeheader()

        tasks = []
        for f_page, l_page in chunker(chunksize):
                # Split content into chunks
                task = asyncio.create_task(pdf2image.convert_from_bytes(pdf.content, first_page=f_page, last_page=l_page, thread_count=10, grayscale=True))
                tasks.append(task)
        
        second_tasks = []
        for image_tasks in asyncio.as_completed(tasks):
            for image in await image_tasks: 
                task_two = asyncio.create_task(get_formulas(image))
                second_tasks.append(task_two)

        third_tasks = []
        for task in asyncio.as_completed(second_tasks):
            for (formula, statement) in await task:
                task_three = asyncio.create_task(get_latex(statement, formula))
                third_tasks.append(task_three)

        num_chunks = len(list(chunker(chunksize)))
        pbar = tqdm(total = num_chunks, desc=f"Processing book: {book}", position=step + 1)

        for step, task in enumerate(asyncio.as_completed(third_tasks)):
            formula_temp = await task 
            for key, value in formula_temp.items(): 
                formula_writer.writerow({'Formula': key, 'Statement': value})
            if step % 50 == 0 or step == num_chunks - 1:
                pbar.update(1)

        pbar.close()
    
    return



async def main():
    # we are working in MathLLM/code/preprocessing directory
    mathllm_folder = os.path.dirname(os.path.dirname(os.getcwd()))

    books = {'principles_of_mathematical_analysis': 'https://download.tuxfamily.org/openmathdep/analysis_real/Principles_of_Mathematical_Analysis-Rudin.pdf', 
             'real_and_complex_analysis': 'https://59clc.files.wordpress.com/2011/01/real-and-complex-analysis.pdf', 
            'functional_analysis':'https://www.mymathscloud.com/api/download/modules/University/Textbooks/functional-analysis/Functional%20Analysis%20Rudin.pdf?id=48928539' }

    # create raw_data folder if not there already
    raw_data = os.path.join(mathllm_folder, "raw_data", "")
    if not os.path.exists(raw_data):
        os.makedirs(raw_data)

    # for every book, create corresponding folder in raw_data folder
    for book in books:
        temp = os.path.join(raw_data, book, "")
        if not os.path.exists(temp):
            os.makedirs(temp)

    for step, (book, url) in enumerate(books.items()): 
        await extract_formulas(step, url, os.path.join(raw_data, book, ""),book)

    
if __name__ == "__main__":
    asyncio.run(main())
    print('Done')

