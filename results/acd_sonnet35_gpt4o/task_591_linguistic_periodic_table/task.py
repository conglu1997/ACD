import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_features = [
            "phonemes",
            "morphemes",
            "syntax",
            "semantics",
            "pragmatics"
        ]
        material_properties = [
            "conductivity",
            "malleability",
            "reactivity",
            "density",
            "luminescence"
        ]
        return {
            "1": {
                "linguistic_feature": random.choice(linguistic_features),
                "material_property": random.choice(material_properties)
            },
            "2": {
                "linguistic_feature": random.choice(linguistic_features),
                "material_property": random.choice(material_properties)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a 'periodic table' of fictional elements based on linguistic principles, then use it to describe the properties of a fictional material. Your task has the following parts:

1. Linguistic Periodic Table Design (250-300 words):
   a) Create a system for organizing linguistic elements (based on {t['linguistic_feature']}) into a periodic table-like structure.
   b) Explain the organizing principle and how it relates to the chosen linguistic feature.
   c) Describe at least 10 'elements' in your table, including their symbols, names, and basic properties.
   d) Explain how the position of an element in your table relates to its linguistic properties.

2. Table Visualization (ASCII art):
   Create a simple ASCII art representation of your linguistic periodic table. Use characters like '|', '-', '+', and letters to represent elements and their relationships.

3. Fictional Material Description (200-250 words):
   a) Describe a fictional material composed of elements from your linguistic periodic table.
   b) Explain how the linguistic properties of its component elements contribute to its {t['material_property']}.
   c) Provide a 'chemical formula' for your material using the symbols from your table.

4. Analytical Comparison (150-200 words):
   a) Compare and contrast your linguistic periodic table with the chemical periodic table.
   b) Discuss potential applications of your system in linguistic analysis or language learning.
   c) Propose one way your system could be expanded or improved for future use.

Ensure your response demonstrates a deep understanding of both linguistic principles and the structure of the chemical periodic table. Be creative in your design while maintaining internal consistency and logical relationships between elements.

Format your response with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The linguistic periodic table must be based on the linguistic feature of {t['linguistic_feature']}.",
            "The response must include a clear explanation of the organizing principle and how it relates to the chosen linguistic feature.",
            "At least 10 'elements' must be described, including their symbols, names, and basic properties.",
            "An ASCII art representation of the linguistic periodic table must be provided.",
            f"A fictional material must be described, explaining how its component elements contribute to its {t['material_property']}.",
            "A 'chemical formula' for the fictional material must be provided using symbols from the table.",
            "The response must include a comparison between the linguistic periodic table and the chemical periodic table.",
            "Potential applications of the system in linguistic analysis or language learning must be discussed.",
            "The response must demonstrate a deep understanding of both linguistic principles and the structure of the chemical periodic table.",
            "The design must be creative while maintaining internal consistency and logical relationships between elements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
