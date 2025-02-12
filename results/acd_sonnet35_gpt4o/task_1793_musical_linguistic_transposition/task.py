import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_structures = [
            {
                "name": "Sonata Form",
                "description": "A musical structure consisting of three main sections: exposition, development, and recapitulation.",
                "linguistic_elements": ["nouns", "verbs", "adjectives"]
            },
            {
                "name": "Fugue",
                "description": "A contrapuntal composition technique with a main theme (subject) that is introduced and then repeated in different voices throughout the piece.",
                "linguistic_elements": ["pronouns", "adverbs", "conjunctions"]
            }
        ]
        return {
            "1": random.choice(musical_structures),
            "2": random.choice(musical_structures)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Your task is to create a linguistic mapping for the musical structure of {t['name']} using the linguistic elements {', '.join(t['linguistic_elements'])}. Then, use this mapping to generate a short creative text. Follow these steps:\n\n1. Structure Understanding (75-100 words):\n   Briefly explain the concept of {t['name']} in music theory and its key components. {t['description']}\n\n2. Mapping (250-300 words):\n   a) Explain how you will map the properties of {t['name']} onto the linguistic elements {', '.join(t['linguistic_elements'])}.\n   b) Provide specific examples of how each component of {t['name']} is represented in your linguistic system.\n   c) Explain how your mapping preserves the musical structure.\n\n3. Creative Text Generation (200-250 words):\n   a) Generate a short creative text (e.g., a poem, a short story, or a dialogue) using your linguistic mapping.\n   b) Ensure that your text adheres to the structure of {t['name']}.\n   c) Highlight or explain how each component of {t['name']} is manifested in your text.\n\n4. Analysis and Application (150-200 words):\n   a) Discuss the challenges you faced in creating this mapping and generating the text.\n   b) Explain how this exercise demonstrates the relationship between musical structures and language.\n   c) Provide a specific example of how your mapping could be applied in a real-world context (e.g., in computational linguistics, music education, or another field).\n\nEnsure your response demonstrates a deep understanding of the musical structure, creativity in mapping and text generation, and clear explanations of how the musical properties are preserved in your linguistic system."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should demonstrate a clear understanding of the {t['name']} structure in music theory.",
            f"The mapping between {t['name']} and the linguistic elements {', '.join(t['linguistic_elements'])} should be logical and well-explained.",
            "The creative text should adhere to both the musical structure and linguistic rules.",
            "The analysis should provide insightful reflections on the challenges and potential applications of this musical-linguistic mapping."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
