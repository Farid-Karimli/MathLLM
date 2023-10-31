
import os
import openai

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


def extract_theorems(chapter_text):
    global content_example, example_output
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
            {"role": "user", "content": f"{content_example}"},
        {"role": "assistant", "content": f"{example_output}"},
        {"role": "user", "content": f"{chapter_text}"}],
        temperature=0.01,
    )
    return response.choices[0].message['content'].strip()


def extract_references(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
          messages=[
        {"role": "system", "content": "You are a machine that takes as input Math Theorems and returns\
        any lemmas, previous theorems, or definitions referenced in the theorem's proof. In the provided \
        math theorem, it will some previous theorems, definitions, and lemmas that are used in constructing \
        the proof.Your job is to filter the text and just return the names of the definitions, lemmas, \
        and previous theorems it uses to prove the result. You should only output the names and numbers\
        of the corresponding  theorems, lemmas, definitions and nothing else. "},
            {"role": "user", "content": f"Here is the theorem and proof: Theorem: 1.21: Prove that every\
            euclidean space is a metric space. \
        Pf: By Lemma 1.18, we have that every euclidean spaces satisfy the triangle inequality."},
        {"role": "assistant", "content": "Lemma 1.18"},
        {"role": "user", "content": f"Here is the theorem and proof: \n{text} \n"}],
        temperature=0.01,
    )
    return response.choices[0].message['content'].strip()

def merge_dictionaries(dict1, dict2):
    return dict2.update(dict1)

def string_to_dicts(theorem_def_corrolaires_text):
    #code that splits string based on theorem, def, corollaries strings
    # return theorems, def, corollaries
    return

def process_latex_files(folder_path, output_file, memoized_theorems):
    theorems = {}
    definitions = {}
    corollaries = {}

    training_data = []
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
    return 

    

def main():
    mathllm_folder = 'path_to_your_MathLLM_folder'
    real_analysis_folder = os.path.join(mathllm_folder, 'raw_data', 'real_analysis')
    functional_analysis_folder = os.path.join(mathllm_folder, 'raw_data', 'functional_analysis')
    training_data_folder = os.path.join(mathllm_folder, 'training_data')
    
    # Initialize a dictionary to memoize theorems and lemmas
    memoized_theorems = {}
    
    process_latex_files(real_analysis_folder, os.path.join(training_data_folder, 'real_analysis_training_data.txt'), memoized_theorems)
    process_latex_files(functional_analysis_folder, os.path.join(training_data_folder, 'functional_analysis_training_data.txt'), memoized_theorems)

if __name__ == "__main__":
    main()
