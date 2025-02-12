import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ancient_civilizations = ['Sumerian', 'Etruscan', 'Mayan', 'Indus Valley']
        linguistic_features = ['phonology', 'morphology', 'syntax', 'semantics']
        historical_mysteries = [
            'purpose of a specific architectural structure',
            'meaning of an undeciphered inscription',
            'reason for the civilization\'s decline',
            'nature of their religious practices'
        ]
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                "civilization": random.choice(ancient_civilizations),
                "linguistic_feature": random.choice(linguistic_features),
                "mystery": random.choice(historical_mysteries),
                "synthetic_data": TaskFamily.generate_synthetic_data()
            }
        return tasks

    @staticmethod
    def generate_synthetic_data() -> str:
        consonants = 'ptkbdgmnŋszʃʒxhrl'
        vowels = 'aeiou'
        word_structures = ['CV', 'CVC', 'CVCV', 'CVCCV']
        words = []
        patterns = ['tala', 'kitu', 'meno', 'sapi', 'ruka']
        for _ in range(5):
            structure = random.choice(word_structures)
            word = ''
            for char in structure:
                if char == 'C':
                    word += random.choice(consonants)
                else:
                    word += random.choice(vowels)
            words.append(word)
        words.extend(patterns)
        random.shuffle(words)
        return ', '.join(words)

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Reconstruct aspects of the ancient {t['civilization']} language based on the following limited linguistic data, with a focus on {t['linguistic_feature']}, and use your reconstruction to propose a solution to the historical mystery: {t['mystery']}. \n\nLinguistic data: {t['synthetic_data']}\n\nYour task has the following components:\n\n1. Linguistic Data Analysis (200-250 words):\n   a) Analyze the provided linguistic data for the {t['civilization']} language.\n   b) Identify patterns and key features of the language's {t['linguistic_feature']}.\n   c) Explain how you would use comparative linguistics principles to expand upon this limited data.\n\n2. Language Reconstruction (250-300 words):\n   a) Propose a partial reconstruction of the {t['civilization']} language's {t['linguistic_feature']}, based on the provided data.\n   b) Provide at least 3 examples of reconstructed words or phrases, clearly derived from the given data.\n   c) Explain your reasoning for each major reconstruction decision, citing specific patterns in the data.\n\n3. Historical Context (150-200 words):\n   a) Describe the relevant historical and cultural context of the {t['civilization']}.\n   b) Explain how this context informs your language reconstruction and approach to the mystery.\n\n4. Mystery Solution (200-250 words):\n   a) Apply your reconstructed language to address the mystery: {t['mystery']}.\n   b) Provide an explanation of how at least 2 specific linguistic features from your reconstruction support your proposed solution.\n   c) Discuss 1 alternative interpretation and explain why your solution is more plausible.\n\n5. Validation and Limitations (150-200 words):\n   a) Propose 2 specific methods to validate your language reconstruction and mystery solution.\n   b) Discuss at least 2 limitations of your approach and potential sources of error.\n\nEnsure your response demonstrates an understanding of historical linguistics, the specific ancient civilization, and logical problem-solving. Use appropriate terminology and provide clear explanations. Be creative while maintaining plausibility.\n\nFormat your response using clear headings for each section, exactly as numbered above. Begin each section with the heading (e.g., '1. Linguistic Data Analysis:') on a new line, followed by your response for that section. Ensure that each subsection (a, b, c, etc.) is clearly addressed in your response."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates an understanding of historical linguistics and the {t['civilization']} civilization.",
            f"The analysis of the provided linguistic data for the {t['linguistic_feature']} identifies some patterns and features.",
            f"The partial reconstruction of the language's {t['linguistic_feature']} is reasonably supported by at least 3 examples derived from the given data.",
            f"The proposed solution to the mystery of {t['mystery']} is logical and supported by at least 2 specific linguistic features from the reconstruction.",
            "The response includes 1 alternative interpretation for the mystery and an argument for the proposed solution.",
            "The response proposes 2 methods for validation and discusses at least 2 limitations of the approach.",
            "The writing is clear, structured, uses appropriate terminology, and follows the required format.",
            "The response addresses all required subsections (a, b, c, etc.) for each main section."
        ]
        score = sum([eval_with_llm_judge(instructions, submission, [criterion]) for criterion in criteria])
        return score / len(criteria)
