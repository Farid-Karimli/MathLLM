import os
import asyncio
import subprocess
from concurrent.futures import ProcessPoolExecutor

running_processes = []

def run_async(book, step, path): # -b {book} -p {path} -s {step}"
    path = path.replace(' ', '\\ ')
    process = subprocess.Popen(f"python3 async_parse.py -b {book} -p {path} -s {step}", shell=True)
    running_processes.append(process)
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

    loop = asyncio.get_running_loop()
    tasks = []
    with ProcessPoolExecutor() as executor:
        for step, book in enumerate(books): 
            tasks.append(loop.run_in_executor(executor, run_async, book, step, mathllm_folder))
    try:
        await asyncio.gather(*tasks)
    except KeyboardInterrupt:  # Ctrl+C detected
        print("Ctrl+C detected. Terminating subprocesses...")
        for process in running_processes:
            process.terminate()

    for process in running_processes:
        process.terminate()
            

if __name__ == "__main__":
    asyncio.run(main())
