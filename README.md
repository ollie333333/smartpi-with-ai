# SmartPi Local AI

Offline AI chatbot package for Raspberry Pi using Ollama + TinyLlama.

## Install

1) Pull a local model:
\`\`\`
ollama pull tinyllama
\`\`\`

2) Create and activate venv:
\`\`\`
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install .
\`\`\`

## Run

- Terminal chat: \`smartpi-terminal\`  
- GUI chat (requires display): \`smartpi-chat\`

