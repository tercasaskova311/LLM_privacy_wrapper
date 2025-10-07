# LLMPrivacyWrapper

A lightweight Python utility that helps **mask and protect sensitive information** (like names, emails, phone numbers, and organizations) before sending text to large language models (LLMs).  
It can then **decode** or **normalize** model outputs for safer post-processing.

---

## Features

- **Privacy-first encoding:** Automatically replaces personal data (using spaCy NER and regex patterns).  
- **Decoding support:** Restores masked tokens or normalizes new entities in model outputs.  
- **Custom mappings:** Define your own replacement dictionary (e.g., `{"Alice": "NAME1"}`).  
- **LLM integration:** Simple wrapper to call your LLM client with sanitized inputs.  
- **NER-based masking:** Uses `spaCy` to detect and replace entities like `<person>`, `<org>`, `<gpe>`, etc.

---

## Installation

```bash
pip install spacy
python -m spacy download en_core_web_sm
```

## Usage
```
from llm_privacy_wrapper import LLMPrivacyWrapper

wrapper = LLMPrivacyWrapper({"Alice": "NAME1"})

text = "Alice is working at Google in Paris."
encoded = wrapper.encode(text)

print("Encoded:", encoded)
# Example output: NAME1 is working at <org> in <gpe>.

# Suppose you send 'encoded' to an LLM:
response = llm_client(encoded)

# You can then decode the response:
decoded = wrapper.decode(response)

```
