import os
from openai import AsyncOpenAI
import asyncio
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
client = AsyncOpenAI()

chunksize = 4096

function_schema = {
    "name": "parse_math_text",
    "description": "A function that takes as input a chapter from a math text and returns 4 dictionaries with theorems, definitions, corollaries, and propositions.",
    "parameters": {
        "type": "object",
        "properties": {
            "theorems": {
                "type": "object",
                "description": "Dictionary of theorems, keyed by theorem number and letter. Each value is an object with the theorem statement and its proof.",
                "properties": {
                    "statement": {
                        "type": "string",
                        "description": "The statement of the theorem."
                    },
                    "proof": {
                        "type": ["string", "null"],
                        "description": "The proof of the theorem. If the proof is not provided, this will be null."
                    }
                }
            },
            "definitions": {
                "type": "object",
                "description": "Dictionary of definitions, keyed by definition number and letter. Each value is the statement of the definition, including any notes on notation or common usage."
            },
            "corollaries": {
                "type": "object",
                "description": "Dictionary of corollaries, similar to theorems, keyed by corollary number and letter. Each value is an object with the corollary statement and its proof.",
                "properties": {
                    "statement": {
                        "type": "string",
                        "description": "The statement of the corollary."
                    },
                    "proof": {
                        "type": ["string", "null"],
                        "description": "The proof of the corollary. If the proof is not provided, this will be null."
                    }
                }
            },
            "propositions": {
                "type": "object",
                "description": "Dictionary of propositions, structured like theorems, keyed by proposition number and letter. Each value is an object with the proposition statement and its proof.",
                "properties": {
                    "statement": {
                        "type": "string",
                        "description": "The statement of the proposition."
                    },
                    "proof": {
                        "type": ["string", "null"],
                        "description": "The proof of the proposition. If the proof is not provided, this will be null."
                    }
                }
            }
        },
        "required": ["theorems", "definitions", "corollaries", "propositions"]
    }
}



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

with open('example_2.md', 'r') as f:
    example_4 = f.read()

output_4 = {'theorems': {}, 'definitions': {'2.18 (a)': 'For a metric space X and a point $p \\in X$:A neighborhood of $p$ is a set $N_{r}(p)$ consisting of all $q$ such that $d(p, q)<r$, for some $r>0$. The number $r$ is called the radius of $N_{r}(p)$.', '2.18 (b)': 'For a metric space X and a point $p \\in X$: A point $p$ is a limit point of the set $E$ if every neighborhood of $p$ contains a point $q \\neq p$ such that $q \\in E$.', '2.18 (c)': 'For a metric space X and a point $p \\in X$, and $E \\subset X$: If $p \\in E$ and $p$ is not a limit point of $E$, then $p$ is called an isolated point of $E$.', '2.18 (d)': 'For a metric space X and $E \\subset X$: $E$ is closed if every limit point of $E$ is a point of $E$.', '2.18 (e)': 'For a metric space X and a point $p \\in X$, and $E \\subset X$: A point $p$ is an interior point of $E$ if there is a neighborhood $N$ of $p$ such that $N \\subset E$.', '2.18 (f)': 'For a metric space X and $E \\subset X$: $E$ is open if every point of $E$ is an interior point of $E$.', '2.18 (g)': 'For a metric space X and points $p \\in X$, and $E \\subset X$: The complement of $E$ (denoted by $E^{c}$ ) is the set of all points $p \\in X$ such that $p \\notin E$.', '2.18 (h)': 'For a metric space X  $E \\subset X$: $E$ is perfect if $E$ is closed and if every point of $E$ is a limit point of $E$.', '2.18 (i)': 'For a metric space X and $E \\subset X$: $E$ is bounded if there is a real number $M$ and a point $q \\in X$ such that $d(p, q)<M$ for all $p \\in E$.', '2.18 (j)': 'For a metric space X and $E \\subset X$: $E$ is dense in $X$ if every point of $X$ is a limit point of $E$, or a point of $E$ (or both). Let us note that in $R^{1}$ neighborhoods are segments, whereas in $R^{2}$ neighborhoods are interiors of circles.'}, 'corollaries': {}, 'propositions': {}}

def create_sample_resopnses(json_input):
    return {"role": "assistant", "content": None, "function_call": {"name": "parse_math_text", "arguments": json_input}}

async def extract_theorems(chapter_text):
    global content_example, example_output, example_2, output_2, example_3, output_3, example_4, output_4
    while True:
        try: 
            response = await client.chat.completions.create(
                model="gpt-3.5-turbo-1106",
                messages=[
                {"role": "system", "content": "You are a machine that takes as input chapters from a math text. \
                You must extract the relevant data from this input to use as arguments to pass into the given function provided.\
                If the theorem/corollary/definition/proposition has multiple parts, i.e. (a), (b), (c), etc., then \
                 you must parse the main statement and add the necessary information from it to each of the cases, and treat it as its own theorem/corollary/definition/proposition;\
                  e.g. Theorem 10 (a), Theorem 10 (b), etc. .\
                  If the chapter does not seem like it is from a math text, it may be the appendix, introduction\
                or some other part of the book that hasn't gotten to the material yet, then just pass in empty arguments\
                to the function and nothing else."},
                {"role": "user", "content": "Parse, add, and extract the relevant data from this input to use as arguments to pass into the given function provided:" + content_example},
                create_sample_resopnses(json.dumps(example_output)),
                {"role": "user", "content": "Parse, add, and extract the relevant data from this input to use as arguments to pass into the given function provided:" + example_2},
                create_sample_resopnses(output_2),
                {"role": "user", "content": "Parse, add, and extract the relevant data from this input to use as arguments to pass into the given function provided:" + example_3},
                create_sample_resopnses(output_3),
                {"role": "user", "content": "Parse, add, and extract the relevant data from this input to use as arguments to pass into the given function provided:" + example_4},
                create_sample_resopnses(json.dumps(output_4)),
                {"role": "user", "content": "Parse, add, and extract the relevant data from this input to use as arguments to pass into the given function provided:" + chapter_text}],
                functions=[function_schema],
                function_call={"name": "parse_math_text"},
                temperature=0,
            )
            try:
                ret = json.loads(response.choices[0].message.function_call.arguments.strip())
            except Exception as e:
                ret = example_output_empty
                with open("json_errors.log", "a+") as logf:
                    logf.write(f'{e=}, step_reason = {response.choices[0].finish_reason} for text: {chapter_text} \n')
            break
        except openai.RateLimitError as e:
            await asyncio.sleep(60)
        except Exception as e:
            await asyncio.sleep(5)
            continue
    
    # keep track of which keys were not found for which text
    with open("incomplete_dict_errors.log", "a+") as logf:
        for key,_ in example_output_empty.items():
            try:
                ret[key]
            except:
                logf.write(f'{key=} not found for text: {chapter_text} \n')
    return ret

def string_to_dicts(ret_dict):
    # using get with empty dictionary in case gpt fails on output
    return ret_dict.get('theorems',{}), ret_dict.get('definitions', {}), ret_dict.get('corollaries', {}), ret_dict.get('propositions', {})


async def extract_correct_theorems(chunk):
    # Await the coroutine and then process its result
    theorems_result = await extract_theorems(chunk)
    return string_to_dicts(theorems_result)
    
def merge_dictionaries(dict1, dict2):
    return dict1.update(dict2)


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

async def process_md_files(folder_path, output_dir):
    global chunksize
    theorems = {}
    definitions = {}
    corollaries = {}
    propositions = {}

    tasks = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.md'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            # Split content into chunks
            chunks = get_chunks(content)
            for chunk in chunks:
                # Create and append the task
                task = asyncio.create_task(extract_correct_theorems(chunk))
                tasks.append(task)

    pbar = tqdm(total=len(chunks), desc=f"Processing file {filename}")
    # Wait for all tasks to complete
    for task in asyncio.as_completed(tasks):
        theorems_temp, definitions_temp, corollaries_temp, propositions_temp = await task
        theorems.update(theorems_temp)
        definitions.update(definitions_temp)
        corollaries.update(corollaries_temp)
        propositions.update(propositions_temp)
        pbar.update(1)

    pbar.close()
                    

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


async def main():
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
        await process_md_files(os.path.join(mathllm_folder, f'raw_data/{book}'), os.path.join(mathllm_folder, f'training_data/{book}'))
    

if __name__ == "__main__":
    asyncio.run(main())
