
import os
from openai import OpenAI
import openai
import pandas as pd
from dotenv import load_dotenv
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import re
from time import sleep 
# Set your OpenAI API key here

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY') 
client = OpenAI()

chunksize = 4096

with open('examples.md', 'r') as f:
    content_example = f.read()

theorems_e = {"1.29": ("If $a$ and $b$ are real, then $(a, b)=a+b i$", "$$\n\\begin{aligned}\na+b i & =(a, 0)+(b, 0)(0,1) \\\\\n& =(a, 0)+(0, b)=(a, b) .\n\\end{aligned}\n$$"), 
            "1.31 (a)": ("If $z$ and $w$ are complex, then $\\overline{z+w}=\\bar{z}+\\bar{w}$", None),
            "1.31 (b)": ("If $z$ and $w$ are complex, then $\\overline{z w}=\\bar{z} \\cdot \\bar{w}$,$", None),
            "1.31 (c)": ("If $z$ and $w$ are complex, $z+\\bar{z}=2 \\operatorname{Re}(z), z-\\bar{z}=2 i \\operatorname{Im}(z)$,", None),
             "1.31 (d)": ("If $z$ and $w$ are complex, then $z \\bar{z}$ is real and positive (except when $z=0$ ).", "write $z=a+b i$, and note that $z \\bar{z}=a^{2}+b^{2}$.") }

definitions_e = {"1.30": "If $a, b$ are real and $z=a+b i$, then the complex number $\\bar{z}=a-b i$ is called the conjugate of $z$. The numbers $a$ and $b$ are the real part and the imaginary part of $z$, respectively.\n\nWe shall occasionally write\n\n$$\na=\\operatorname{Re}(z), \\quad b=\\operatorname{Im}(z)\n$$", 
               "1.32": "Definition If $z$ is a complex number, its absolute value $|z|$ is the nonnegative square root of $z \\bar{z}$; that is, $|z|=(z \\bar{z})^{1 / 2}$.\n\nThe existence (and uniqueness) of $|z|$ follows from Theorem 1.21 and part $(d)$ of Theorem 1.31.\n\nNote that when $x$ is real, then $\\bar{x}=x$, hence $|x|=\\sqrt{x^{2}}$. Thus $|x|=x$ if $x \\geq 0,|x|=-x$ if $x<0$."}

corollaries_e = {}

propositions_e = {}

example_output = {"theorems": theorems_e, "definitions": definitions_e, "corollaries": corollaries_e, "propositions": propositions_e}

example_output_empty = {"theorems": {}, "definitions": {}, "corollaries": {}, "propositions": {}}

example_2 = "5.12 Theorem Suppose $f$ is a real differentiable function on $[a, b]$ and suppose $f^{\\prime}(a)<\\lambda<f^{\\prime}(b)$. Then there is a point $x \\in(a, b)$ such that $f^{\\prime}(x)=\\lambda$.\n\nA similar result holds of course if $f^{\\prime}(a)>f^{\\prime}(b)$.\n\nProof Put $g(t)=f(t)-\\lambda t$. Then $g^{\\prime}(a)<0$, so that $g\\left(t_{1}\\right)<g(a)$ for some $t_{1} \\in(a, b)$, and $g^{\\prime}(b)>0$, so that $g\\left(t_{2}\\right)<g(b)$ for some $t_{2} \\in(a, b)$. Hence $g$ attains its minimum on $[a, b]$ (Theorem 4.16) at some point $x$ such that $a<x<b$. By Theorem 5.8, $g^{\\prime}(x)=0$. Hence $f^{\\prime}(x)=\\lambda$.\n\nCorollary If $f$ is differentiable on $[a, b]$, then $f^{\\prime}$ cannot have any simple discontinuities on $[a, b]$.\n\nBut $f^{\\prime}$ may very well have discontinuities of the second kind.\n\n## L'HOSPITAL'S RULE\n\nThe following theorem is frequently useful in the evaluation of limits."

output_2 = '{"theorems": {"5.12": ["Suppose $f$ is a real differentiable function on $[a, b]$ and suppose $f^{\\prime}(a)<\\\\lambda<f^{\\prime}(b)$. Then there is a point $x \\\\in(a, b)$ such that $f^{\\prime}(x)=\\\\lambda$.", "Put $g(t)=f(t)-\\\\lambda t$. Then $g^{\\prime}(a)<0$, so that $g\\\\left(t_{1}\\\\right)<g(a)$ for some $t_{1} \\\\in(a, b)$, and $g^{\\prime}(b)>0$, so that $g\\\\left(t_{2}\\\\right)<g(b)$ for some $t_{2} \\\\in(a, b)$. Hence $g$ attains its minimum on $[a, b]$ (Theorem 4.16) at some point $x$ such that $a<x<b$. By Theorem 5.8, $g^{\\prime}(x)=0$. Hence $f^{\\prime}(x)=\\\\lambda$."], "L\'HOSPITAL\'S RULE": "The following theorem is frequently useful in the evaluation of limits."}, "definitions": {}, "corollaries": {"Corollary": "If $f$ is differentiable on $[a, b]$, then $f^{\\prime}$ cannot have any simple discontinuities on $[a, b]$. But $f^{\\prime}$ may very well have discontinuities of the second kind."}, "propositions": {}}'

example_3 = '10.23 Theorem Suppose $T$ is a $\\mathscr{C}^{\\prime}$-mapping of an open set $E \\subset R^{n}$ into an open set $V \\subset R^{m}, S$ is a $\\mathscr{C}^{\\prime}$-mapping of $V$ into an open set $W \\subset R^{p}$, and $\\omega$ is a $k$-form in $W$, so that $\\omega_{S}$ is a $k$-form in $V$ and both $\\left(\\omega_{S}\\right)_{T}$ and $\\omega_{S T}$ are $k$-forms in $E$, where $S T$ is defined by $(S T)(\\mathbf{x})=S(T(\\mathbf{x}))$. Then\n\n$$\n\\left(\\omega_{S}\\right)_{T}=\\omega_{S T}\n$$\n\nProof If $\\omega$ and $\\lambda$ are forms in $W$, Theorem 10.22 shows that\n\n$$\n\\left((\\omega \\wedge \\lambda)_{S}\\right)_{T}=\\left(\\omega_{S} \\wedge \\lambda_{S}\\right)_{T}=\\left(\\omega_{S}\\right)_{T} \\wedge\\left(\\lambda_{S}\\right)_{T}\n$$\n\nand\n\n$$\n(\\omega \\wedge \\lambda)_{S T}=\\omega_{S T} \\wedge \\lambda_{S T}\n$$\n\nThus if (71) holds for $\\omega$ and for $\\lambda$, it follows that (71) also holds for $\\omega \\wedge \\lambda$. Since every form can be built up from 0 -forms and 1 -forms by addition and multiplication, and since (71) is trivial for 0 -forms, it is enough to prove (71) in the case $\\omega=d z_{q}, q=1, \\ldots, p$. (We denote the points of $E, V, W$ by $\\mathbf{x}, \\mathbf{y}, \\mathbf{z}$, respectively.)\n\nLet $t_{1}, \\ldots, t_{m}$ be the components of $T$, let $s_{1}, \\ldots, s_{p}$ be the components of $S$, and let $r_{1}, \\ldots, r_{p}$ be the components of $S T$. If $\\omega=d z_{q}$, then\n\n$$\n\\omega_{s}=d s_{q}=\\sum_{j}\\left(D_{j} s_{q}\\right)(\\mathbf{y}) d y_{j}\n$$\n\nso that the chain rule implies\n\n$$\n\\begin{aligned}\n\\left(\\omega_{S}\\right)_{T} & =\\sum_{j}\\left(D_{j} s_{q}\\right)(T(\\mathbf{x})) d t_{j} \\\\\n& =\\sum_{j}\\left(D_{j} s_{q}\\right)(T(\\mathbf{x})) \\sum_{i}\\left(D_{i} t_{j}\\right)(\\mathbf{x}) d x_{i} \\\\\n& =\\sum_{i}\\left(D_{i} r_{q}\\right)(\\mathbf{x}) d x_{i}=d r_{q}=\\omega_{S T} .\n\\end{aligned}\n$$'

output_3 = '{"theorems": {"10.23": ["Suppose $T$ is a $\\\\mathscr{C}^{\\\\prime}$-mapping of an open set $E \\\\subset R^{n}$ into an open set $V \\\\subset R^{m}, S$ is a $\\\\mathscr{C}^{\\\\prime}$-mapping of $V$ into an open set $W \\\\subset R^{p}$, and $\\\\omega$ is a $k$-form in $W$, so that $\\\\omega_{S}$ is a $k$-form in $V$ and both $\\\\left(\\\\omega_{S}\\\\right)_{T}$ and $\\\\omega_{S T}$ are $k$-forms in $E$, where $S T$ is defined by $(S T)(\\\\mathbf{x})=S(T(\\\\mathbf{x}))$. Then\\n\\n$$\\n\\\\left(\\\\omega_{S}\\\\right)_{T}=\\\\omega_{S T}\\n$$","If $\\omega$ and $\\lambda$ are forms in $W$, Theorem 10.22 shows that\n\n$$\n\\left((\\omega \\wedge \\lambda)_{S}\\right)_{T}=\\left(\\omega_{S} \\wedge \\lambda_{S}\\right)_{T}=\\left(\\omega_{S}\\right)_{T} \\wedge\\left(\\lambda_{S}\\right)_{T}\n$$\n\nand\n\n$$\n(\\omega \\wedge \\lambda)_{S T}=\\omega_{S T} \\wedge \\lambda_{S T}\n$$\n\nThus if (71) holds for $\\omega$ and for $\\lambda$, it follows that (71) also holds for $\\omega \\wedge \\lambda$. Since every form can be built up from 0 -forms and 1 -forms by addition and multiplication, and since (71) is trivial for 0 -forms, it is enough to prove (71) in the case $\\omega=d z_{q}, q=1, \\ldots, p$. (We denote the points of $E, V, W$ by $\\mathbf{x}, \\mathbf{y}, \\mathbf{z}$, respectively.)\n\nLet $t_{1}, \\ldots, t_{m}$ be the components of $T$, let $s_{1}, \\ldots, s_{p}$ be the components of $S$, and let $r_{1}, \\ldots, r_{p}$ be the components of $S T$. If $\\omega=d z_{q}$, then\n\n$$\n\\omega_{s}=d s_{q}=\\sum_{j}\\left(D_{j} s_{q}\\right)(\\mathbf{y}) d y_{j}\n$$\n\nso that the chain rule implies\n\n$$\n\\begin{aligned}\n\\left(\\omega_{S}\\right)_{T} & =\\sum_{j}\\left(D_{j} s_{q}\\right)(T(\\mathbf{x})) d t_{j} \\\\\n& =\\sum_{j}\\left(D_{j} s_{q}\\right)(T(\\mathbf{x})) \\sum_{i}\\left(D_{i} t_{j}\\right)(\\mathbf{x}) d x_{i} \\\\\n& =\\sum_{i}\\left(D_{i} r_{q}\\right)(\\mathbf{x}) d x_{i}=d r_{q}=\\omega_{S T} .\n\\end{aligned}\n$$" ], "definitions": {}, "corollaries": {}, "propositions": {}}'


def extract_theorems(chapter_text):
    global content_example, example_output, example_2, output_2, example_3, output_3
    while True:
        try: 
            response = client.chat.completions.create(
                model="gpt-3.5-turbo-1106",
                messages=[
                {"role": "system", "content": f"You are a machine that takes as input a chapter from a math text and must \
                returns 4 dictionaries. Dictionary 1 will be called 'theorems' and will consist of key, value parirs\
                where they keys are the theorem number and letter, and the values is a tuple (statement, proof)\
                where the statement contains the theorem statment and the proof contains the text of the proof. \
                Dictionary 2 will be called 'definitions' and its keys will consist of the definition numbers and letter, and \
                its values will consist of values that are the statement of the definition.\
                In addition, if there are any notes left by the author with regards to notation or common uses of the definition, inscribe it in the definition as well. \
                The second to last dictionary will be called 'corollaries' and its keys will consist of the corollary number and letter, \
                its values will similariy also be (statement, proof) pairs relating to at as in the previous two examples.\
                The last dictionary wil be called 'propositions' and will have the same structure as 'theorems.'\
                For any of these cases, if there is no proof provided( the proof is left as an exercise to the reader or something else)\
                simply fill the proof value as a None type in python. They way you will return all of these\
                is one large dictionary that will have as keys 'theorems', 'definitions', 'corollaries', 'propositions', and each value of those keys\
                will be the corresponding dictionary. If the chapter does not seem like it is from a math text, it may be the appendix, introduction\
                    or some other part of the book that hasn't gotten to the material yet. In that case just return the {json.dumps(example_output_empty)} and \
                        nothing else. Lastly for any variable names, make sure to always double escape the backslash."},
                {"role": "user", "content": content_example},
                {"role": "assistant", "content": json.dumps(example_output)},
                {"role": "user", "content": example_2},
                {"role": "assistant", "content": output_2},
                {"role": "user", "content": example_3},
                {"role": "assistant", "content": output_3},
                {"role": "user", "content": chapter_text}],
                temperature=0.1,
            )
            break
        except openai.RateLimitError as e:
            sleep(60)
    return response.choices[0].message.content

incorrect_json_1 = '{"theorems": {"2.42": ["Every bounded infinite subset of $R^{k}$ has a limit point in $R^{k}$.", "Being bounded, the set $E$ in question is a subset of a $k$-cell $I \\subset R^{k}$. By Theorem 2.40, $I$ is compact, and so $E$ has a limit point in $I$, by Theorem 2.37."], "2.43": ["Let $P$ be a nonempty perfect set in $R^{k}$. Then $P$ is uncountable.", "Since $P$ has limit points, $P$ must be infinite. Suppose $P$ is countable, and denote the points of $P$ by $\\mathbf{x}_{1}, \\mathbf{x}_{2}, \\mathbf{x}_{3}, \\ldots$ We shall construct a sequence $\\left\\{V_{n}\\right\\}$ of neighborhoods, as follows.\\n\\nLet $V_{1}$ be any neighborhood of $\\mathbf{x}_{1}$. If $V_{1}$ consists of all $\\mathbf{y} \\in R^{k}$ such that $\\left|\\mathbf{y}-\\mathbf{x}_{1}\\right|<r$, the closure $\\bar{V}_{1}$ of $V_{1}$ is the set of all $\\mathbf{y} \\in R^{k}$ such that $\\left|\\mathbf{y}-\\mathbf{x}_{1}\\right| \\leq \\boldsymbol{r}$.\\n\\nSuppose $V_{"}'

corrected_json_1  = '{"theorems": {"2.42": ["Every bounded infinite subset of $R^{k}$ has a limit point in $R^{k}$.", "Being bounded, the set $E$ in question is a subset of a $k$-cell $I \\\\subset R^{k}$. By Theorem 2.40, $I$ is compact, and so $E$ has a limit point in $I$, by Theorem 2.37."], "2.43": ["Let $P$ be a nonempty perfect set in $R^{k}$. Then $P$ is uncountable.", "Since $P$ has limit points, $P$ must be infinite. Suppose $P$ is countable, and denote the points of $P$ by $\\\\mathbf{x}_{1}, \\\\mathbf{x}_{2}, \\\\mathbf{x}_{3}, \\\\ldots We shall construct a sequence $\\\\left\\\\{V_{n}\\\\right\\\\}$ of neighborhoods, as follows. Let $V_{1}$ be any neighborhood of $\\\\mathbf{x}_{1}$. If $V_{1}$ consists of all $\\\\mathbf{y} \\\\in R^{k}$ such that $\\\\left|\\\\mathbf{y}-\\\\mathbf{x}_{1}\\\\right|<r$, the closure $\\\\bar{V}_{1}$ of $V_{1}$ is the set of all $\\\\mathbf{y} \\\\in R^{k}$ such that $\\\\left|\\\\mathbf{y}-\\\\mathbf{x}_{1}\\\\right| \\\\leq \\\\boldsymbol{r}$. ..."]}, "definitions": {}, "corollaries": {}, "propositions": {}}'

incorrect_json_2 = '{"theorems": {}, "definitions": {"1.4": "Throughout Chap. 1, the set of all rational numbers will be denoted by $Q$." "1.5": "Let $S$ be a set. An order on $S$ is a relation, denoted by <, with the following two properties:\\n\\n(i) If $x \\in S$ and $y \\in S$ then one and only one of the statements is true.\\n\\n$$\\nx<y, \\quad x=y, \\quad y<x\\n$$\\n\\n(ii) If $x, y, z \\in S$, if $x<y$ and $y<z$, then $x<z$.\\n\\nThe statement \\" $x<y$ \\" may be read as \\" $x$ is less than $y$ \\" or \\" $x$ is smaller than $y$ \\" or \\" $x$ precedes $y$ \\". It is often convenient to write $y>x$ in place of $x<y$. The notation $x \\leq y$ indicates that $x<y$ or $x=y$, without specifying which of these two is to hold. In other words, $x \\leq y$ is the negation of $x>y$."}}'

corrected_json_2 ='{"theorems": {}, "definitions": {"1.4": "Throughout Chap. 1, the set of all rational numbers will be denoted by $Q$.", "1.5": "Let $S$ be a set. An order on $S$ is a relation, denoted by <, with the following two properties:\\n\\n(i) If $x \\\\in S$ and $y \\\\in S$ then one and only one of the statements\\n\\nis true.\\n\\n$$\\nx<y, \\\\quad x=y, \\\\quad y<x\\n$$\\n\\n(ii) If $x, y, z \\\\in S$, if $x<y$ and $y<z$, then $x<z$.\\n\\nThe statement \\"$x<y$\\" may be read as \\"$x$ is less than $y$\\" or \\"$x$ is smaller than $y$\\" or \\"$x$ precedes $y$\\".\\n\\nIt is often convenient to write $y>x$ in place of $x<y$.\\n\\nThe notation $x \\\\leq y$ indicates that $x<y$ or $x=y$, without specifying which of these two is to hold. In other words, $x \\\\leq y$ is the negation of $x>y$.", "1.6": "An ordered set is a set $S$ in which an order is defined.\\n\\nFor example, $Q$ is an ordered set if $r<s$ is defined to mean that $s-r$ is a positive rational number.", "1.7": "Suppose $S$ is an ordered set, and $E \\\\subset S$. If there exists a $\\\\beta \\\\in S$ such that $x \\\\leq \\\\beta$ for every $x \\\\in E$, we say that $E$ is bounded above, and call $\\\\beta$ an upper bound of $E$.\\n\\nLower bounds are defined in the same way (with $\\\\geq$ in place of $\\\\leq$ ).", "1.8": "Suppose $S$ is an ordered set, $E \\\\subset S$, and $E$ is bounded above. Suppose there exists an $\\\\alpha \\\\in S$ with the following properties:\\n\\n(i) $\\\\alpha$ is an upper bound of $E$.\\n\\n(ii) If $\\\\gamma<\\\\alpha$ then $\\\\gamma$ is not an upper bound of $E$.\\n\\nThen $\\\\alpha$ is called the least upper bound of $E."}, "corollaries": {}, "propositions": {}}'


def fix_JSON(json_string, error):

    global incorrect_json_1, corrected_json_1, incorrect_json_2, corrected_json_2
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
          messages=[
        {"role": "system", "content": f"You are a machine that takes as input incorrectly formatted JSON strings \
         with the error associated with them as a tuple (JSON string, error), and returns these JSON strings in a corrected format.\
         You must only return the corrected JSON string and nothing else! The JSON must also be formatted according {json.dumps(example_output_empty)}. So if it missing any keys, you must fill them in and give them empty values."},
        {"role": "user", "content": f"({incorrect_json_1}, JSONDecodeError: Invalid \escape: line 1 column 167 (char 166))"},
        {"role": "assistant", "content": corrected_json_1},
         {"role": "user", "content": f"({incorrect_json_2}, JSONDecodeError: Expecting ',' delimiter: line 1 column 119 (char 118)"},
        {"role": "assistant", "content": corrected_json_2},
        {"role": "user", "content": f"({json_string},{error})"}],
        temperature=0.1,
    )
    return response.choices[0].message.content

def extract_correct_theorems(chunk):
    # Process completed futures as they complete
    count = 0
    while True:
        if count == 0:
        # Extract results from the future
            temp_ret = extract_theorems(chunk).strip()
        try:
            temp_ret = string_to_dicts(temp_ret)
            break
        except Exception as exc:
            #print(temp_ret)
            #print(f"{exc.__class__.__name__}: {exc}")
            temp_ret = fix_JSON(temp_ret, f"{exc.__class__.__name__}: {exc}")
            count += 1
            if count > 10: 
                print(repr(chunk))
                print('\n')
                print(repr(temp_ret))
                return json.dumps(example_output_empty)

    return temp_ret




def merge_dictionaries(dict1, dict2):
    return dict1.update(dict2)

def string_to_dicts(theorem_def_corrolaires_text):
    dictionary = json.loads(theorem_def_corrolaires_text)
    return dictionary['theorems'], dictionary['definitions'], dictionary['corollaries'], dictionary['propositions']

def get_chunks(document_content):
    global chunksize
    # Pattern to match the start of each relevant section
    pattern = r"^\d+\.\d+ (Theorem|Definition|Proposition|Corollary)"

    # Compile the regex pattern
    compiled_pattern = re.compile(pattern, re.MULTILINE)

    # Find all matches in the document content
    matches = list(compiled_pattern.finditer(document_content))

    # List to hold each chunk of text
    chunks = []

    # Function to find the penultimate occurrence of a pattern
    def find_penultimate(text, pattern):
        matches = list(re.finditer(pattern, text))
        if len(matches) > 1:
            return matches[-2].start()
        else:
            return None

    # Iterate through matches and create chunks of text
    for i in range(len(matches)):
        start = matches[i].start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(document_content)

        # Create a chunk and ensure its length is at most 4096 characters
        while end - start > chunksize:
            # Find the penultimate occurrence of any section header within this chunk
            penultimate_match_start = find_penultimate(document_content[start:end], pattern)
            if penultimate_match_start is not None:
                end = start + penultimate_match_start
            else:
                # If there is no penultimate occurrence, we must break at the current match
                break

        # Add the valid chunk to the list
        chunk = document_content[start:end].strip()
        chunks.append(chunk)
        start = end  # Start the next chunk where the last one was cut off

    # Now `chunks` contains all the segments of the document.
    return chunks


def process_md_files(folder_path, output_dir):
    global chunksize
    theorems = {}
    definitions = {}
    corollaries = {}
    propositions = {}

    with ThreadPoolExecutor(max_workers=8) as executor:
        for filename in os.listdir(folder_path):
            if filename.endswith('.md'):
                file_path = os.path.join(folder_path, filename)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                # Split content into chunks and submit to the executor
                chunks = get_chunks(content)
                future_to_content = {}
                for chunk in chunks: #increments smaller than chunksize to allow for window to see any missed text for theorem possibly
                    # Submit the extract_theorems function to the executor
                    future = executor.submit(extract_correct_theorems, chunk)
                    future_to_content[future] = chunk
                        
                pbar = tqdm(total=len(chunks), desc=f"Processing file {filename}")
                
                for future in as_completed(future_to_content):
                    theorems_temp, defitions_temp, corollaries_temp, propositions_temp = future.result()
                    theorems.update(theorems_temp)
                    definitions.update(defitions_temp)
                    corollaries.update(corollaries_temp)
                    propositions.update(propositions_temp)
                    pbar.update(1)

                
    # build up dataframe consisting of these elements
    theorems_pd = pd.DataFrame.from_dict(theorems)
    definitions_pd = pd.DataFrame.from_dict(definitions)
    corollaries_pd =  pd.DataFrame.from_dict(corollaries)
    propositions_pd =  pd.DataFrame.from_dict(propositions)

    theorems_pd.to_csv(f"{output_dir}/theorems.csv", encoding='utf-8', index=False)
    definitions_pd.to_csv(f"{output_dir}/definitions.csv", encoding='utf-8', index=False)
    corollaries_pd.to_csv(f"{output_dir}/corollaries.csv", encoding='utf-8', index=False)
    propositions_pd.to_csv(f"{output_dir}/propositions.csv", encoding='utf-8', index=False)

    return 


def main():
    # we are working in MathLLM/code/preprocessing directory

    mathllm_folder = os.path.dirname(os.path.dirname(os.getcwd())) 

    books = [item for item in os.listdir(f'{mathllm_folder}/raw_data') if os.path.isdir(os.path.join(f'{mathllm_folder}/raw_data', item))]
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
        process_md_files(os.path.join(mathllm_folder, f'raw_data/{book}'), os.path.join(mathllm_folder, f'training_data/{book}'))
    

if __name__ == "__main__":
    main()
