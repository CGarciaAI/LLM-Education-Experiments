# LLM Testing Sample - MagicSchool Application

# This notebook demonstrates how I test and compare large language models (LLMs) for educational applications.

import pandas as pd

# Example prompts
prompts = [
    "Explain photosynthesis to 5th graders.",
    "Create a math word problem for 7th grade students.",
    "Summarize the Civil War for high school students."
]

# Mock responses from LLMs (replace with real outputs if safe to share)
responses = {
    "ChatGPT": ["Simple explanation of photosynthesis...", "Math word problem...", "Civil War summary..."],
    "Claude": ["Photosynthesis explained...", "Math problem...", "Civil War overview..."],
    "Gemini": ["Photosynthesis for students...", "Math word problem...", "Civil War summary..."],
    "Perplexity": ["Explanation of photosynthesis...", "Math problem example...", "Civil War summary..."]
}

# Create a DataFrame to compare responses
df = pd.DataFrame(responses, index=prompts)
df.index.name = "Prompt"
df
