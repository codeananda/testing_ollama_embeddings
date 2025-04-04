from concurrent.futures import ThreadPoolExecutor, as_completed

import ollama
from fire import Fire
from loguru import logger
from tqdm import tqdm


def main(use_cpu: bool = False):

    with open("book-war-and-peace.txt", "r") as f:
        text = f.read()

    sentences = text.split(".")

    model = "nomic-embed-text-cpu" if use_cpu else "nomic-embed-text"

    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(ollama.embeddings, model=model, prompt=sentence)
            for sentence in sentences
        ]
        for future in tqdm(as_completed(futures), total=len(futures), unit="sentence"):
            try:
                result = future.result()
            except Exception as e:
                logger.error(f"Error: {e}")


if __name__ == "__main__":
    Fire(main)
