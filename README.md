# Testing Ollam Embeddings

A quick repo to test how fast different GPUs from vast.ai can create embeddings with ollama.

Use a Vast.AI image that has Ollama already in it. SSH into it and do

```bash
git clone https://github.com/codeananda/testing_ollama_embeddings.git
cd testing_ollama_embeddings
./setup_vast_gpu.sh
python embed_text.py # with optional params here to test speed of GPU vs. CPU and sequential vs. in parallel
```
