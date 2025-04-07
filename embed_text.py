from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Literal

import ollama
from fire import Fire
from loguru import logger
from pydantic import validate_call
from tqdm import tqdm


@validate_call
def main(
    mode: Literal["nomic", "ollama"] = "nomic",
    use_cpu: bool = False,
    sequential: bool = False,
):

    with open("book-war-and-peace.txt", "r") as f:
        text = f.read()

    sentences = text.split(".")

    match mode:
        case "nomic":
            _embed_with_nomic(sentences, sequential, use_cpu)
        case "ollama":
            _embed_with_ollama(sentences, sequential, use_cpu)
        case _:
            raise ValueError(f"Invalid mode: {mode}")


def _embed_with_nomic(sentences, sequential, use_cpu):
    pass


def _embed_with_ollama(sentences, sequential, use_cpu):
    model = "nomic-embed-text-cpu" if use_cpu else "nomic-embed-text"
    if sequential:
        for sentence in tqdm(sentences, unit="sentence"):
            ollama.embeddings(model=model, prompt=sentence)
    else:

        with ThreadPoolExecutor() as executor:
            futures = [
                executor.submit(ollama.embeddings, model=model, prompt=sentence)
                for sentence in sentences
            ]
            for future in tqdm(
                as_completed(futures), total=len(futures), unit="sentence"
            ):
                try:
                    result = future.result()
                except Exception as e:
                    logger.error(f"Error: {e}")


if __name__ == "__main__":
    Fire(main)
