import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        structures = [
            {
                'name': 'Group',
                'properties': ['closure', 'associativity', 'identity element', 'inverse element'],
                'example': 'The set of integers under addition forms a group.'
            },
            {
                'name': 'Ring',
                'properties': ['closure under addition and multiplication', 'associativity', 'distributivity', 'additive identity', 'additive inverse'],
                'example': 'The set of integers under addition and multiplication forms a ring.'
            }
        ]
        
        linguistic_elements = ['nouns', 'verbs', 'adjectives', 'adverbs']
        
        return {
            "1": {
                "structure": random.choice(structures),
                "linguistic_elements": random.sample(linguistic_elements, 2)
            },
            "2": {
                "structure": random.choice(structures),
                "linguistic_elements": random.sample(linguistic_elements, 2)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Your task is to create a linguistic mapping for the algebraic structure of a {t['structure']['name']} using the linguistic elements {' and '.join(t['linguistic_elements'])}. Then, use this mapping to generate a short creative text. Follow these steps:\n\n1. Structure Understanding (50-75 words):\n   Briefly explain the concept of a {t['structure']['name']} in abstract algebra and its key properties ({', '.join(t['structure']['properties'])}).\n\n2. Mapping (250-300 words):\n   a) Explain how you will map the properties of a {t['structure']['name']} onto the linguistic elements {' and '.join(t['linguistic_elements'])}.\n   b) Provide specific examples of how each property is represented in your linguistic system.\n   c) Explain how your mapping preserves the mathematical structure of the {t['structure']['name']}.\n\n3. Creative Text Generation (200-250 words):\n   a) Generate a short creative text (e.g., a poem, a short story, or a dialogue) using your linguistic mapping.\n   b) Ensure that your text adheres to the properties of a {t['structure']['name']}.\n   c) Highlight or explain how each property of the {t['structure']['name']} is manifested in your text.\n\n4. Analysis and Application (150-200 words):\n   a) Discuss the challenges you faced in creating this mapping and generating the text.\n   b) Explain how this exercise demonstrates the relationship between abstract mathematical structures and language.\n   c) Provide a specific example of how your mapping could be applied in a real-world context (e.g., in linguistics, computer science, or another field).\n\nEnsure your response demonstrates a deep understanding of the algebraic structure, creativity in mapping and text generation, and clear explanations of how the mathematical properties are preserved in your linguistic system."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately explains the concept and properties of a {t['structure']['name']}.",
            f"The mapping of the {t['structure']['name']} properties to the linguistic elements {' and '.join(t['linguistic_elements'])} is coherent and well-explained.",
            "The mapping preserves the mathematical structure of the algebraic structure.",
            "The creative text adheres to the properties of the algebraic structure.",
            "The response demonstrates creativity in both the mapping and text generation.",
            "The analysis provides insightful commentary on the challenges and implications of the exercise.",
            "A specific real-world application of the mapping is provided and well-explained.",
            "The response follows the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
