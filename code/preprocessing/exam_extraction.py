import re
import csv

def extract_real_analysis_questions(latex_content):
    sections = re.split(r'\\begin\{enumerate\}', latex_content)
    #real_analysis_pattern = r'\\item \(Real Analysis\)' # for Fall12, 13
    real_analysis_pattern = r'\\item \(RA\)' # for Fall14-22
    extracted_questions = []
    for section in sections:
        if re.search(real_analysis_pattern, section):
            extracted_questions.append('\\begin{enumerate}' + section.strip())
    return extracted_questions

# Define the output CSV file path
output_csv_path = 'D:/python/MathLLM/raw_data/exams/validation/Real_Analysis_Questions.csv'

# Open the CSV file for writing
with open(output_csv_path, mode='a', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # write the header
    # csv_writer.writerow(['Year', 'Question'])

    # Process each LaTeX file and write the questions to the CSV file
    for i in range(18, 23):
        file_path = f'D:/python/MathLLM/raw_data/exams/validation/Fall{i}.tex'
        with open(file_path, 'r') as file:
            latex_content = file.read()

        real_analysis_questions = extract_real_analysis_questions(latex_content)

        for question in real_analysis_questions:
            # Write the year and the question to the CSV file
            csv_writer.writerow([f'Fall{i}', question])
