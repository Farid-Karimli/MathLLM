import requests
import os
from dotenv import load_dotenv
import json
from tqdm import tqdm
import time

def convert_pdf_to_md(path, url, textbook_name):
    load_dotenv()

    APP_ID = os.getenv('APP_ID')
    APP_KEY = os.getenv('APP_KEY')


    headers = {
        'Content-Type': 'application/json',
        'app_id': APP_ID,
        'app_key': APP_KEY,
    }

    url_to_convert = url

    # Construct the data dictionary
    data = {
        "url": url_to_convert,
        'enable_spell_check': True,
        "conversion_formats": {"md": True}
    }

    json_data = json.dumps(data)

    try:
        response = requests.post('https://api.mathpix.com/v3/pdf', headers=headers, data=json_data)
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        exit(1) 

    
    pdf_id =  json.loads(response.text)['pdf_id']


    headers.pop('Content-Type')
    
    with tqdm(total=100, desc="Processing", unit="%") as pbar:
        while True: 
            try:
                response = requests.get(f'https://api.mathpix.com/v3/pdf/{pdf_id}', headers=headers)
                response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code

            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                continue

            response_json = json.loads(response.text)
            new_progress = response_json['percent_done'] - pbar.n
            pbar.update(new_progress)

            if response_json['status'] == 'completed':
                break

            if response_json['status'] == 'error':
                print(response_json['error'])
                exit(1)
           
            # delay so as not to call request the site too much.
            time.sleep(3)

    try:
        response = requests.get(f'https://api.mathpix.com/v3/pdf/{pdf_id}.md', headers=headers)
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code

        with open(f'{path}{textbook_name}.md', 'wb') as file:
            file.write(response.content)
            print(f"File {textbook_name}.md downloaded successfully.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        exit(1) 
    
    return 


def main():
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

    for book, url in books.items(): 
        convert_pdf_to_md(os.path.join(raw_data, book, ""),url,book)
    

if __name__ == "__main__":
    main()