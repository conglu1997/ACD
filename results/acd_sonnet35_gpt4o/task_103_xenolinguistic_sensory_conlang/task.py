import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        alien_species = [
            {
                "name": "Chromavores",
                "sensory_system": "Ability to perceive and manipulate quantum states of particles",
                "environment": "A gaseous planet with constant electromagnetic fluctuations"
            },
            {
                "name": "Resonants",
                "sensory_system": "Echolocation-based perception with the ability to generate and modulate complex sound waves",
                "environment": "A dense, always-dark aquatic world with constantly shifting currents"
            }
        ]
        
        language_aspects = [
            "Create a naming system for objects based on their quantum properties",
            "Design a tense system that incorporates the idea of quantum superposition",
            "Develop a way to express abstract concepts like 'beauty' or 'justice' using quantum-related metaphors",
            "Invent a system of 'verbs' that describe actions in terms of sound wave manipulation",
            "Create a method for expressing spatial relationships using echolocation principles",
            "Design a way to communicate emotional states through sound frequency and amplitude modulation"
        ]
        
        return {
            "1": {
                "species": random.choice(alien_species),
                "aspect1": random.choice(language_aspects),
                "aspect2": random.choice(language_aspects)
            },
            "2": {
                "species": random.choice(alien_species),
                "aspect1": random.choice(language_aspects),
                "aspect2": random.choice(language_aspects)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a constructed language (conlang) for the {t['species']['name']} species.\n\n" \
               f"Species characteristics:\n" \
               f"- Sensory system: {t['species']['sensory_system']}\n" \
               f"- Environment: {t['species']['environment']}\n\n" \
               f"Your task is to:\n\n" \
               f"1. Create a basic structure for the language that utilizes the unique sensory abilities of the species and adapts to their environment. Your language design should:\n" \
               f"   a) Describe the primary mode of communication\n" \
               f"   b) Explain how information is encoded and transmitted\n" \
               f"   c) Describe how the language accounts for environmental challenges\n\n" \
               f"2. Address the following specific aspects in your language design:\n" \
               f"   a) {t['aspect1']}\n" \
               f"   b) {t['aspect2']}\n\n" \
               f"3. Provide examples of how this language would express the following concepts:\n" \
               f"   a) Time\n" \
               f"   b) Quantity\n" \
               f"   c) Relationship (e.g., familial, social, or spatial)\n\n" \
               f"4. Create a sample 'sentence' or communication unit in your language, and explain its structure and meaning.\n\n" \
               f"5. Analyze potential challenges humans might face in learning or translating this language.\n\n" \
               f"Ensure your response is creative yet grounded in scientific principles of linguistics and the given sensory system. Organize your answer using clear headings for each section. Your total response should not exceed 750 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The language design clearly incorporates the unique sensory abilities of the species and adapts to their environment.",
            "The language structure is internally consistent and demonstrates creative problem-solving in addressing the given aspects.",
            "Examples provided for expressing time, quantity, and relationships are innovative and logically follow from the language's design principles.",
            "The sample 'sentence' or communication unit is well-explained and consistent with the language's structure.",
            "The analysis of potential challenges for humans learning or translating the language shows deep consideration of the fundamental differences between human and alien sensory experiences.",
            "The overall design demonstrates a strong understanding of linguistic principles while creatively applying them to a non-human sensory system."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
