import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            {
                "name": "Norse",
                "deities": ["Odin", "Thor", "Freyja", "Loki"],
                "concepts": ["Yggdrasil", "Ragnarok", "Valhalla", "Mjolnir"],
                "message": "The Valkyries ride forth"
            },
            {
                "name": "Aztec",
                "deities": ["Quetzalcoatl", "Tlaloc", "Huitzilopochtli", "Xipe Totec"],
                "concepts": ["Xibalba", "Tonalpohualli", "Nahual", "Ollin"],
                "message": "The fifth sun rises"
            },
            {
                "name": "Greek",
                "deities": ["Zeus", "Athena", "Apollo", "Hades"],
                "concepts": ["Olympus", "Tartarus", "Elysium", "Fate"],
                "message": "Oracles speak in riddles"
            }
        ]
        task1, task2 = random.sample(cultures, 2)
        return {
            "1": task1,
            "2": task2
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a constructed language (conlang) - an artificially created language - based on {t['name']} mythology, then use it to encode and decode culturally significant messages. Your task has four parts:

1. Conlang Creation (200-250 words):
   a) Develop a phonetic inventory inspired by {t['name']} mythological names and concepts.
   b) Create basic grammatical rules that reflect the culture's worldview.
   c) Generate a lexicon of at least 20 words/phrases crucial to expressing ideas in {t['name']} mythology.
   d) Incorporate a simple cryptographic element into the language structure.

2. Cultural Analysis (150-200 words):
   a) Explain how your conlang reflects {t['name']} mythological concepts and cultural values.
   b) Discuss how the language's structure and cryptographic element relate to the culture's views on knowledge and secrecy.

3. Message Encoding (100-150 words):
   a) Encode the following message using your cryptolang: "{t['message']}"
   b) Explain the encoding process step by step.
   c) Describe any cultural connotations or hidden meanings in the encoded message.

4. Message Decoding (100-150 words):
   a) Provide a short encoded message (different from the one in part 3) in your cryptolang.
   b) Explain the decoding process step by step.
   c) Reveal the decoded message and its cultural significance to the {t['name']} mythology.

Ensure your response demonstrates a deep understanding of linguistic principles, cryptography, and {t['name']} mythology. Be creative in your design while maintaining internal consistency and cultural relevance.

Format your response with clear headings for each section. Your total response should be between 550-750 words. Adhering to the word count for each section is crucial for a complete and balanced response.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a conlang based on {t['name']} mythology with at least 20 words/phrases in the lexicon",
            "The conlang incorporates a simple cryptographic element in its structure",
            f"The response includes an encoding of the message: '{t['message']}' with a step-by-step explanation",
            "The response includes a different encoded message and its step-by-step decoding process",
            f"The response provides cultural analysis of the conlang, relating it to {t['name']} mythological concepts and cultural values",
            f"The response demonstrates knowledge of {t['name']} mythology, including references to at least two deities ({', '.join(t['deities'])}) and two concepts ({', '.join(t['concepts'])})",
            "The response is formatted with clear headings for each section and is between 550-750 words in total"
        ]
        score = sum(eval_with_llm_judge(instructions, submission, [criterion]) for criterion in criteria) / len(criteria)
        return score
