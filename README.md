
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
│   ├── chapter1.tex
│   ├── chapter2.tex
│   └── ...
│
└── functional_analysis/
    ├── chapter1.tex
    ├── chapter2.tex
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
