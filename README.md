
# Fine-Tuning LLMs for Real Analysis Problems

## Authors
- Ben Badnani (bbadnani@bu.com)
- Cindy Zhang (xyz0906@bu.edu)
- Farid Karimli (faridkar@bu.edu)

## Abstract
Large language models usually struggle with complex mathematical questions. This project aims to address this issue by fine-tuning GPT-3.5 Turbo on a corpus of Real Analysis and Functional Analysis texts. The ultimate goal is to provide relevant and helpful information for Real Analysis questions, specifically those found on the Harvard Math Entrance Exam.

## Previous Work
This project builds upon the work of Yiran Wu, Feiran Jia, et al., who developed a methodology to solve mathematical problems by chaining GPT-4 with Python. They utilized GPT-4 to recognize math problems and subsequently generate related Python code to solve them.

## Project Organization
```
raw_data/
│
├── real_analysis/
│   ├── real_analysis.md
│
└── functional_analysis/
    ├── functional_analysis.md
    └── ...
```
The `raw_data` directory contains the LaTeX files of each chapter from the books on Real Analysis and Functional Analysis. These files are used to fine-tune the LLM.

## Getting Started

(Include instructions on how to set up and run the project here)

## Usage

(Provide examples and explanations on how to use the project here)

## Contributing
To contribute to the dataset:
1. Add new LaTeX files of chapters from books on Real Analysis or Functional Analysis to the respective folders in `raw_data`.
2. Follow the naming convention `chapterX.tex`, where `X` is the chapter number.
3. Create a pull request with a brief description of the added content.

(Include additional contribution guidelines here if necessary)

## License

(Include information about the project's license here)

## Contact

For any inquiries or further information, feel free to contact:

- Ben Badnani: [bbadnani@bu.com](mailto:bbadnani@bu.com)
- Cindy Zhang: [xyz0906@bu.edu](mailto:xyz0906@bu.edu)
- Farid Karimli: [faridkar@bu.edu](mailto:faridkar@bu.edu)


## TODO:

1) Farid and Cindy work on preprocessing the textbooks.
2) Ben will finish script that will result in 3 csvs for each textbook. definitions.csv, theorems.csv, and corollaries.csv. Each csv will contain as columns a theorem number and letter, the theorem statement, the proof statement (for corollaries and theorems), the number and letter of any theorems used in the proof of the theorem in question, and the those theorem statements.

3) Using this, we can create a (input theorem statement, statements of theorems/corollaries/definitions used in its proof) training data set.
4) Next we write a script to fine-tune gpt-3.5 turbo on this training data set.
5) Finally, we take this fine-tuned gpt-3.5 model, feed it the real analysis questions from the math harvard entrance exam.
6) Then we get back as output proposed theorems/corollaries/definitions that are predicted to be needed in a proof of the statement/problem.
7) We then feed the original question as well as these predicted definitions/theorems/corollaries to gpt-4 as zero-shot learning context and compare its answer as to when its just given the problem statement itself. 
