#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

echo "Updating and upgrading system packages..."
sudo apt update && sudo apt upgrade -y

echo "Installing btop..."
sudo apt install btop -y

echo "Pulling nomic-embed-text Ollama model..."
ollama pull nomic-embed-text

echo "Installing Poetry..."
# Download and execute the official Poetry installer script
curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to the PATH for the current script session
# Assumes the default installation directory ~/.local/bin
export PATH="$HOME/.local/bin:$PATH"

echo "Verifying Poetry installation..."
poetry --version

echo "Installing Python dependencies using Poetry..."
# This command assumes pyproject.toml is in the current directory
poetry install

echo "Creating CPU-only version of nomic-embed-text..."
# Get the original modelfile content
ollama show nomic-embed-text --modelfile > modelfile.txt
# Append the parameter to force CPU usage (num_gpu 0 means use CPU)
# Note: Ollama documentation often suggests num_gpu -1 for CPU,
# but 0 might also work depending on the version/context.
# Using -1 for clarity based on common examples.
echo "PARAMETER num_gpu -1" >> modelfile.txt
# Create the new model variant
ollama create nomic-embed-text-cpu -f modelfile.txt
echo "CPU model 'nomic-embed-text-cpu' created."


echo "Setup complete!"
