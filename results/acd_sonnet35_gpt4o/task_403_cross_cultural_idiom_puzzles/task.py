import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        idioms = [
            {"language": "English", "idiom": "It's raining cats and dogs", "meaning": "It's raining very heavily"},
            {"language": "Spanish", "idiom": "Estar en la luna", "meaning": "To be distracted or not paying attention"},
            {"language": "Japanese", "idiom": "猫の手も借りたい", "meaning": "To be extremely busy"},
            {"language": "French", "idiom": "Avoir le cafard", "meaning": "To feel sad or depressed"},
            {"language": "German", "idiom": "Ich verstehe nur Bahnhof", "meaning": "I don't understand anything"}
        ]
        puzzle_types = ["rebus", "word scramble", "fill in the blank", "crossword clue"]
        
        return {
            "1": {
                "idiom": random.choice(idioms),
                "puzzle_type": random.choice(puzzle_types)
            },
            "2": {
                "idiom": random.choice(idioms),
                "puzzle_type": random.choice(puzzle_types)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"This task involves creating and solving puzzles based on idiomatic expressions from different languages and cultures. Follow these steps:\n\n1. Create a {t['puzzle_type']} puzzle based on the {t['idiom']['language']} idiom: '{t['idiom']['idiom']}' (meaning: {t['idiom']['meaning']}).\n2. Provide a step-by-step solution to your puzzle, explaining how it relates to the original idiom and its meaning.\n3. Create a new idiom in English that conveys a similar meaning to the original idiom, but uses imagery or concepts from a different culture of your choice.\n4. Explain how your new idiom captures the essence of the original and how it relates to the chosen culture.\n\nProvide your response in the following format:\nPuzzle: [Your {t['puzzle_type']} puzzle]\nSolution: [Step-by-step solution and explanation]\nNew idiom: [Your new English idiom]\nExplanation: [Your explanation of the new idiom]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The {t['puzzle_type']} puzzle is creative and clearly based on the given idiom.",
            "The solution is correct and well-explained, showing how it relates to the original idiom and its meaning.",
            "The new English idiom conveys a similar meaning to the original idiom.",
            "The new idiom uses imagery or concepts from a different culture, and this is well-explained.",
            "The explanation clearly articulates how the new idiom captures the essence of the original and relates to the chosen culture."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
