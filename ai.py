import subprocess
import shlex

def ask_model(prompt: str, model: str = "tinyllama"):
    try:
        cmd = f'ollama run {model} \"{prompt}\"'
        result = subprocess.run(shlex.split(cmd),
                                capture_output=True,
                                text=True,
                                timeout=120)
        return result.stdout.strip() if result.stdout else "[No reply from model]"
    except Exception as e:
        return f"[AI Error: {e}]"
