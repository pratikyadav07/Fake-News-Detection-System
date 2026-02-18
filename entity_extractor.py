import spacy
import re

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)

    entities = {
        "PERSON": [],
        "ORG": [],
        "MONEY": [],
        "DATE": [],
        "NUMBERS": []
    }

    for ent in doc.ents:
        if ent.label_ in entities:
            entities[ent.label_].append(ent.text)

    numbers = re.findall(r"\$?\d+(\.\d+)?\s?(billion|million)?", text, re.I)
    entities["NUMBERS"] = numbers

    return entities
