import os
import openai
import ast
import pandas as pd

# Set your OpenAI API key here
openai.api_key = 'your-api-key'

content_example = """1.29 Theorem If $a$ and $b$ are real, then $(a, b)=a+b i$.

Proof

$$
\begin{aligned}
a+b i & =(a, 0)+(b, 0)(0,1) \\
& =(a, 0)+(0, b)=(a, b)
\end{aligned}
$$

1.30 Definition If $a, b$ are real and $z=a+b i$, then the complex number $\bar{z}=a-b i$ is called the conjugate of $z$. The numbers $a$ and $b$ are the real part and the imaginary part of $z$, respectively.

We shall occasionally write

$$
a=\operatorname{Re}(z), \quad b=\operatorname{Im}(z)
$$

1.31 Theorem If $z$ and $w$ are complex, then
(a) $\overline{z+w}=\bar{z}+\bar{w}$
(b) $\overline{z w}=\bar{z} \cdot \bar{w}$,
(c) $z+\bar{z}=2 \operatorname{Re}(z), z-\bar{z}=2 i \operatorname{Im}(z)$,
(d) $z \bar{z}$ is real and positive (except when $z=0$ ).

Proof $(a),(b)$, and $(c)$ are quite trivial. To prove $(d)$, write $z=a+b i$, and note that $z \bar{z}=a^{2}+b^{2}$.

1.32 Definition If $z$ is a complex number, its absolute value $|z|$ is the nonnegative square root of $z \bar{z}$; that is, $|z|=(z \bar{z})^{1 / 2}$.

The existence (and uniqueness) of $|z|$ follows from Theorem 1.21 and part $(d)$ of Theorem 1.31.

Note that when $x$ is real, then $\bar{x}=x$, hence $|x|=\sqrt{x^{2}}$. Thus $|x|=x$ if $x \geq 0,|x|=-x$ if $x<0$."""


theorems_e = {"1.29": ("If $a$ and $b$ are real, then $(a, b)=a+b i$", """$$
\begin{aligned}
a+b i & =(a, 0)+(b, 0)(0,1) \\
& =(a, 0)+(0, b)=(a, b)
\end{aligned}
$$"""), 
            "1.31 (a)": ("If $z$ and $w$ are complex, then $\overline{z+w}=\bar{z}+\bar{w}$", None),
            "1.31 (b)": ("If $z$ and $w$ are complex, then $\overline{z w}=\bar{z} \cdot \bar{w}$", None),
            "1.31 (c)": ("If $z$ and $w$ are complex, then $z+\bar{z}=2 \operatorname{Re}(z), z-\bar{z}=2 i \operatorname{Im}(z)$", None),
             "1.31 (d)": ("$z \bar{z}$ is real and positive (except when $z=0$ )", "write $z=a+b i$, and note that $z \bar{z}=a^{2}+b^{2}$.") }


definitions_e = {"1.30": "If $a, b$ are real and $z=a+b i$, then the complex number\
                $\bar{z}=a-b i$ is called the conjugate of $z$. The numbers $a$ and $b$ are \
               the real part and the imaginary part of $z$, respectively. (where$$a=\operatorname{Re}(z), \quad b=\operatorname{Im}(z)$$ )", 
               "1.32": "If $z$ is a complex number, its absolute value $|z|$ is the nonnegative square root of $z \bar{z}$; that is, $|z|=(z \bar{z})^{1 / 2}$.\
                (The existence (and uniqueness) of $|z|$ follows from Theorem 1.21 and part $(d)$ of Theorem 1.31. Note that when $x$ is real, then $\bar{x}=x$,\
                      hence $|x|=\sqrt{x^{2}}$. Thus $|x|=x$ if $x \geq 0,|x|=-x$ if $x<0$.)"}

corollaries_e = {}

example_output = {"theorems": theorems_e, "definitions": definitions_e, "corollaries": corollaries_e}

content_example_2 = """"""

example_output_2 = """"""


def extract_theorems(chapter_text):
    global content_example, example_output, content_example_2, example_output_2
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
          messages=[
        {"role": "system", "content": "You are a machine that takes as input a chapter from a math text and must \
         returns 3 dictionaries. Dictionary 1 will be called 'theorems' and will consist of key, value parirs\
         where they keys are the theorem number and letter, and the values is a tuple (statement, proof)\
         where the statement contains the theorem statment and the proof contains the text of the proof. \
         Dictionary 2 will be called 'definitions' and its keys will consist of the definition numbers and letter, and \
        its values will consist of values that are the statement of the definition.\
         In addition, if there are any notes left by the author with regards to notation or common uses of the definition, inscribe it in the definition as well. \
         The last dictionary will be called 'corollaries' and its keys will consist of the corollary number and letter, \
         its values will similariy also be (statement, proof) pairs relating to at as in the previous two examples.\
         For any of these cases, if there is no proof provided( the proof is left as an exercise to the reader or something else)\
         simply fill the proof value as a None type in python. They way you will return all of these\
         is one large dictionary that will have as values {'theorems', 'definitions', 'corollaries'}, and each value of those keys\
         will be the corresponding dictionary."},
        {"role": "user", "content": content_example},
        {"role": "assistant", "content": f"{example_output}"},
        {"role": "user", "content": content_example_2},
        {"role": "assistant", "content": f"{example_output_2}"},
        {"role": "user", "content": chapter_text}],
        temperature=0.01,
    )
    return response.choices[0].message['content'].strip()

example_text_1 = """1.37 (a): Theorem Suppose $\mathrm{x}, \mathrm{y}, \mathrm{z} \in R^{k}$, and $\alpha$ is real. Then $|\mathbf{x}| \geq 0$. Pf: None"""

example_text_2 = """1.37 (d): Theorem Suppose $\mathrm{x}, \mathrm{y}, \mathrm{z} \in R^{k}$, and $\alpha$ is real. Then $|\mathbf{x} \cdot \mathbf{y}| \leq|\mathbf{x}||\mathbf{y}|$. Pf: is an immediate consequence of the Schwarz inequality."""

example_text_3 = """1.37 (e): Theorem Suppose $\mathrm{x}, \mathrm{y}, \mathrm{z} \in R^{k}$, and $\alpha$ is real. Then $|\mathbf{x}+\mathbf{y}| \leq|\mathbf{x}|+|\mathbf{y}|$;. Pf: By $(d)$ we have

$$
\begin{aligned}
|x+y|^{2} & =(x+y) \cdot(x+y) \\
& =x \cdot x+2 x \cdot y+y \cdot y \\
& \leq|x|^{2}+2|x||y|+|y|^{2} \\
& =(|\mathbf{x}|+|\mathbf{y}|)^{2}
\end{aligned}
$$

so that $(e)$ is proved."""

example_text_4 = """ Theorem 2.24 (b): For any collection $\left\{G_{\alpha}\right\}$ of open sets, $\bigcup_{\alpha} G_{\alpha}$ is open. Proof: By Theorem 2.22,

$$
(21) \left(\bigcap_{a} F_{a}\right)^{c}=\bigcup_{a}\left(F_{\alpha}^{c}\right),
$$

and $F_{\alpha}^{c}$ is open, by Theorem 2.23. Hence $(a)$ implies that (21) is open so that $\bigcap_{a} F_{\alpha}$ is closed.

"""

def extract_references(text):
    global example_text_1, example_text_2, example_text_3, example_text_4
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
          messages=[
        {"role": "system", "content": "You are a machine that takes as input Math Theorems and returns\
        any previous theorems, corollaries, or definitions referenced in the theorem's proof.\
        Your job is to filter the text and just return the identifying numbers and letters of the definitions, corollaries, \
        and previous theorems it uses to prove the result. If there is no reference to any previous corollaries, theorems, or definitions \
        in the proof, then you should return the string None.\
        If a theorem/definition/corollary is mentioned by name only and no identifying letter or number, just output the name provided.\
        If a theorem proof only mentions a letter that refers to previous theorem, then the theorem number is the same as the one being proved. \
        The final format of your returned output should be as follows {'theorems_ref': theorems_ref, 'corollaries_ref': corollaries_ref, 'def_ref':def_ref}, \
        where theorems_ref is a list containing all the theorem identifying number(s) and (possibly letter)s, and the same for corollaries_ref, and  def_ref."},
        {"role": "user", "content": example_text_1},
        {"role": "assistant", "content": "{'theorems_ref': None,'corollaries_ref': None, 'def_ref' None}"},
        {"role": "user", "content": example_text_2},
        {"role": "assistant", "content": "{'theorems_ref': None, 'corollaries_ref': None, 'def_ref': ['Schwarz inequality']}"},
        {"role": "user", "content": example_text_3},
        {"role": "assistant", "content": "{'theorems_ref': ['1.37 (d)'], 'corollaries_ref': None, 'def_ref': None}"},
        {"role": "user", "content": example_text_4},
        {"role": "assistant", "content": "{'theorems_ref': ['2.22', '2.23', '2.24 (a)'], 'corollaries_ref': None, 'def_ref': None}"},
        {"role": "user", "content": f"Here is the theorem and proof: \n{text} \n"}],
        temperature=0.01,
    )
    return response.choices[0].message['content'].strip()

def merge_dictionaries(dict1, dict2):
    return dict1.update(dict2)

def string_to_dicts(theorem_def_corrolaires_text):
    dictionary = ast.literal_eval(theorem_def_corrolaires_text)
    return dictionary['theorems'], dictionary['definitions'], dictionary['corollaries']

def process_latex_files(folder_path, output_dir):
    theorems = {}
    definitions = {}
    corollaries = {}

    for filename in os.listdir(folder_path):
        if filename.endswith('.tex'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # Use GPT-3.5 Turbo to parse the LaTeX content and extract theorems
                theorems_temp, defitions_temp, corollaries_temp = string_to_dicts(extract_theorems(content))
                theorems = merge_dictionaries(theorems, theorems_temp)
                definitions = merge_dictionaries(definitions, defitions_temp)
                corollaries = merge_dictionaries(corollaries, corollaries_temp)
    # build up dataframe consisting of these elements
    theorems_pd = pd.DataFrame.from_dict(theorems)
    definitions_pd = pd.DataFrame.from_dict(definitions)
    corollaries_pd =  pd.DataFrame.from_dict(corollaries)

    theorems_pd.to_csv(f"{output_dir}/theorems.csv", encoding='utf-8', index=False)
    definitions_pd.to_csv(f"{output_dir}/definitions.csv", encoding='utf-8', index=False)
    corollaries_pd.to_csv(f"{output_dir}/corollaries.csv", encoding='utf-8', index=False)
    return 


def main():
    # we are working in MathLLM/code/preprocessing directory

    mathllm_folder = os.path.dirname(os.path.dirname(os.getcwd()))

    books = [item for item in os.listdir(mathllm_folder) if os.path.isdir(os.path.join(mathllm_folder, item))]
    # get list of books
    
    # create training_data folder if not there already
    training_data_dir = os.path.join(mathllm_folder, "training_data", "")
    if not os.path.exists(training_data_dir):
        os.makedirs(training_data_dir)

    # for every book in raw_data, create corresponding folder in training_data folder

    for book in books:
        temp = os.path.join(training_data_dir, book, "")
        if not os.path.exists(temp):
            os.makedirs(temp)

    for book in books: 
        process_latex_files(os.path.join(mathllm_folder, f'raw_data/{book}'), os.path.join(mathllm_folder, f'training_data/{book}'))
    

if __name__ == "__main__":
    main()
