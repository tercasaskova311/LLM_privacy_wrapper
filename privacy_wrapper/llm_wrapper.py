import re
import spacy
from typing import Dict, Optional

class LLMPrivacyWrapper:
    def __init__(self, replacement: Optional[Dict[str, str]] = None, nlp_model="en_core_web_sm"):
        self.replacement = replacement or {}
        self.reverse_replacement = {v: k for k, v in self.replacement.items()}
        self.nlp = spacy.load(nlp_model)

        self.pattern = {
            "email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
            "phone": r"\+?\d[\d-]{7,}\d",
            "person": r"\b[A-Z][a-z]+(?: [A-Z][a-z]+)*\b",
            "org": r"\b[A-Z][a-zA-Z0-9& ]+(?: Inc| LLC| Ltd| Corporation| Corp| Company)?\b"
        }

    def encode(self, text: str) -> str:
        # Encode replacements
        for key, value in self.replacement.items():
            text = re.sub(re.escape(key), value, text)
        # You could also use spaCy here for NER masking
        doc = self.nlp(text)
        for ent in doc.ents:
            if ent.text not in self.replacement.values():
                placeholder = f"<{ent.label_.lower()}>"
                text = text.replace(ent.text, placeholder)
        return text

    def decode(self, text, replacement):
        for key, value in self.replacement.items():
            text = re.sub(re.escape(key), value, text)
        
        for label, pattern in self.patterns.items():
            text = re.sub(pattern, f"<{label}>", text)
        
        doc = self.nlp(text)
        for ent in doc.ents:
            placeholder = f"<{ent.label_.lower()}>"
            text = re.sub(re.escape(ent.text), placeholder)
        return text
    
    def query(self, text: str, client, model, max_tokens=100):
        encoded_text = self.encode(text)
        completion = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": encoded_text}],
            max_tokens=max_tokens
        )
        response = completion.choices[0].message.content
        return self.decode(response)

wrapper = LLMPrivacyWrapper({"Alice": "NAME1"})
text = "Alice is working at Google in Paris."
encoded = wrapper.encode(text)
print(encoded)

