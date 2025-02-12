import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_domains = [
            "Emotions",
            "Colors",
            "Abstract Concepts",
            "Nature",
            "Technology",
            "Human Body"
        ]
        return {
            "1": {"domain": random.choice(linguistic_domains)},
            "2": {"domain": random.choice(linguistic_domains)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        domain = t['domain']
        return f"""Create a 'linguistic periodic table' for words related to {domain}. Your task is to design a systematic classification of words that draws parallels with the chemical periodic table. Follow these steps:

1. Element Selection (100-150 words):
   a) Choose 12 words related to {domain}.
   b) Explain your selection criteria, considering phonetic and semantic properties.

2. Classification System (200-250 words):
   a) Create a classification system for your words, inspired by the periodic table.
   b) Define at least three 'dimensions' for classification (e.g., number of syllables, emotional valence, concreteness).
   c) Explain how each dimension relates to a feature of the chemical periodic table (e.g., atomic number, period, group).

3. Table Design (ASCII art or detailed description):
   Create a visual representation of your linguistic periodic table. Use ASCII art if possible, or provide a detailed textual description of the table's layout.

4. Element Analysis (200-250 words):
   a) Choose three 'elements' (words) from your table.
   b) For each, explain its position in the table and how it relates to neighboring 'elements'.
   c) Discuss any patterns or trends you observe in your table.

5. Practical Application (150-200 words):
   a) Propose a practical application for your linguistic periodic table in language learning, natural language processing, or another relevant field.
   b) Explain how this system could provide insights into the nature of language or facilitate language-related tasks.

6. Limitations and Extensions (100-150 words):
   a) Discuss at least two limitations of your classification system.
   b) Suggest one way to extend or improve your linguistic periodic table.

Ensure your response demonstrates a deep understanding of both linguistic principles and the structure of the chemical periodic table. Be creative in drawing parallels between chemistry and linguistics while maintaining scientific plausibility.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all six required sections comprehensively.",
            "The word selection and classification system demonstrate a clear understanding of linguistic properties and creative parallel-drawing with the chemical periodic table.",
            "The table design effectively visualizes the classification system and shows clear inspiration from the periodic table of elements.",
            "The element analysis shows depth of understanding of the created system and insightful observations about patterns or trends.",
            "The practical application proposed is innovative and well-reasoned, showing potential real-world value of the linguistic periodic table.",
            "The limitations and extensions discussed show critical thinking about the system's strengths and weaknesses.",
            "The overall response demonstrates strong interdisciplinary thinking, creatively combining linguistics and chemistry concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
