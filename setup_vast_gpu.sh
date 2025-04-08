#!/bin/bash
sudo apt update && sudo apt upgrade -y && sudo apt install btop -y

# Install nomic-embed-text
ollama pull nomic-embed-text

pip install --upgrade pip
pip install ollama pandas tqdm loguru fire nomic[local] pydantic

# Create GPU version of nomic-embed-text
ollama show nomic-embed-text --modelfile > modelfile.txt
echo "PARAMETER num_gpu 0" >> modelfile.txt
ollama create nomic-embed-text-cpu -f modelfile.txt