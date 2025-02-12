import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum decoherence",
            "wave function collapse",
            "quantum interference"
        ]
        linguistic_features = [
            "semantic ambiguity",
            "syntactic structure",
            "pragmatic inference",
            "lexical entanglement",
            "phonological patterns",
            "morphological complexity"
        ]
        text_genres = [
            "scientific abstract",
            "poetry",
            "legal document",
            "social media post"
        ]
        return {
            "1": {
                "quantum_concept1": random.choice(quantum_concepts),
                "quantum_concept2": random.choice([c for c in quantum_concepts if c != quantum_concepts[0]]),
                "linguistic_feature": random.choice(linguistic_features),
                "text_genre": random.choice(text_genres)
            },
            "2": {
                "quantum_concept1": random.choice(quantum_concepts),
                "quantum_concept2": random.choice([c for c in quantum_concepts if c != quantum_concepts[0]]),
                "linguistic_feature": random.choice(linguistic_features),
                "text_genre": random.choice(text_genres)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design two quantum-inspired language models based on the principles of {t['quantum_concept1']} and {t['quantum_concept2']}, focusing on the linguistic feature of {t['linguistic_feature']}. Then, use your models to analyze and generate text in the genre of {t['text_genre']}. Your task has the following parts:

1. Quantum Language Model Design (400-450 words):
   a) Explain how you incorporate {t['quantum_concept1']} into your first language model.
   b) Describe how you incorporate {t['quantum_concept2']} into your second language model.
   c) Compare and contrast how these quantum principles interact with the linguistic feature of {t['linguistic_feature']}.
   d) Provide a mathematical or algorithmic representation of both models.
   e) Discuss any novel linguistic phenomena that might emerge from these quantum-linguistic interactions.

2. Text Analysis (300-350 words):
   a) Choose a short text (about 100 words) in the genre of {t['text_genre']}.
   b) Analyze this text using both of your quantum language models.
   c) Compare the results of the two models and explain any differences.
   d) Discuss how these analyses differ from traditional linguistic analysis.
   e) Identify any insights or patterns revealed by your quantum-inspired approaches.

3. Text Generation (250-300 words):
   a) Use both of your quantum language models to generate short texts (about 50 words each) in the genre of {t['text_genre']}.
   b) Explain the generation processes and how they incorporate the respective quantum principles.
   c) Compare the generated texts and discuss how they reflect both quantum and linguistic properties.

4. Information Theoretical Analysis (250-300 words):
   a) Analyze the information content of your generated texts using quantum information theory.
   b) Compare this to classical information theoretical measures.
   c) Discuss any implications for our understanding of language and information.
   d) Explain how the two quantum concepts lead to different information theoretical interpretations, if applicable.

5. Implications and Future Directions (250-300 words):
   a) Discuss potential applications of your quantum language models in linguistics, computer science, or physics.
   b) Propose an experiment to test the validity or usefulness of your models.
   c) Speculate on how this approach might change our understanding of language or quantum systems.
   d) Compare the potential impact of the two quantum concepts on future language technology development.

6. Glossary (100-150 words):
   Provide a brief glossary of key terms used in your response, including at least two terms each from quantum mechanics, linguistics, and information theory.

Ensure your response demonstrates a deep understanding of quantum mechanics, linguistics, and information theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

If you reference specific theories, research, or frameworks, please provide brief citations or references.

Format your response with clear headings for each section and use the provided sub-points (a, b, c, ...) to structure your answer. Your total response should be between 1550-1850 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both quantum mechanics and linguistics, accurately comparing and contrasting two quantum concepts.",
            "The quantum language model designs are creative, well-explained, and scientifically plausible, with clear distinctions between the two models.",
            "The text analysis and generation sections show a clear application of both quantum-inspired models, with insightful comparisons between them.",
            "The information theoretical analysis provides insightful comparisons between quantum and classical approaches, distinguishing between the two quantum concepts.",
            "The implications and future directions section offers creative yet grounded ideas for further research, considering the potential impact of both quantum concepts.",
            "The glossary accurately defines key terms from quantum mechanics, linguistics, and information theory.",
            "The overall response balances creativity with scientific rigor and interdisciplinary integration.",
            "The submission includes appropriate citations or references where relevant.",
            "The response adheres to the specified word count range and follows the structured format provided in the instructions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
