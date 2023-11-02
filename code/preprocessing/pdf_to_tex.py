from pix2text import Pix2Text, merge_line_texts
import os
import sys

#  - - - - - - - - - - - - - - - - - -
#  - -
#  - -  This script is used to convert images of the pdf pages of a book to latex files.
#  - -  Latex files are outputted in the working directory.
#  - -
#  - -  usage:
#  - -
#  - -  pip install -r requirements.txt
#  - -
#  - -  python pdf_to_tex.py
#  - - - - - - - - - - - - - - - - - -


# Folder path that contains the images of the pdf - CHANGE
FOLDER_PATH = "/Users/faridkarimli/Downloads/ilovepdf_pages-to-jpg"

images = sorted(os.listdir(FOLDER_PATH))[1:]
# print(images)

# Start page number of each chapter - CHANGE
CHAPTERS = {
    '1': 11,
    '2': 34,
    '3': 57,
    '4': 93,
    '5': 113,
    '6': 133,
    '7': 153,
    '8': 182,
    '9': 214,
    '10': 255,
    '11': 310
}
# Last page of the chapters - CHANGE
LAST_PAGE = 346

# Create a latex file for the output of chapter 1
for chapter in CHAPTERS:
    print("Chapter number: ", chapter)

    # Create a latex file for the output of each chapter
    chp = open(f"chap_{chapter}.tex", "w")

    # Check if this is the last chapter
    if chapter == list(CHAPTERS.keys())[-1]:  
        end_page = LAST_PAGE + 1 
    else:
        end_page = CHAPTERS[str(int(chapter) + 1)] 

    for i in range(CHAPTERS[chapter], end_page):
        print("Page number: ", i)

        # Change the filenames to what you have
        if i < 10:
            img_fp = os.path.join(
                FOLDER_PATH, f"rudin_page-000{i}.jpg")  # CHANGE
        elif i < 100:
            img_fp = os.path.join(
                FOLDER_PATH, f"rudin_page-00{i}.jpg")  # CHANGE
        else:
            img_fp = os.path.join(
                FOLDER_PATH, f"rudin_page-0{i}.jpg")   # CHANGE

        p2t = Pix2Text(analyzer_config=dict(model_name='mfd'))
        # # can also use `p2t.recognize(img_fp)`
        outs = p2t(img_fp, resized_shape=608)

        # To get just the text contents, use:
        only_text = merge_line_texts(outs, auto_line_break=True)

        # Replace significant whitespace with a single space
        only_text = ' '.join(only_text.split())
        chp.write(only_text)

    print("Chapter ", chapter, " is done.")
