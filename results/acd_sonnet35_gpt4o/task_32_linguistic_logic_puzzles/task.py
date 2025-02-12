import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        puzzles = [
            {
                "language": "Japanese",
                "property": "pitch accent",
                "example": "hashi (chopsticks) vs. hashi (bridge)"
            },
            {
                "language": "Chinese",
                "property": "tones",
                "example": "mā (mother) vs. má (hemp) vs. mǎ (horse) vs. mà (scold)"
            },
            {
                "language": "Arabic",
                "property": "root system",
                "example": "k-t-b (write) -> kitāb (book), kātib (writer), maktab (office)"
            },
            {
                "language": "English",
                "property": "heteronyms",
                "example": "lead (to guide) vs. lead (metal)"
            }
        ]
        return {
            "1": random.choice(puzzles),
            "2": random.choice(puzzles)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Create a logic puzzle based on the linguistic property of {t['property']} in {t['language']}. Your puzzle should:\n\n1. Briefly explain the linguistic property (1-2 sentences).\n2. Provide an example of how this property works, similar to: {t['example']}.\n3. Present a logical puzzle that requires understanding this property to solve.\n4. Include the solution to your puzzle.\n\nEnsure your puzzle is challenging but solvable, and demonstrates a clear understanding of the linguistic property and its logical implications.\n\nProvide your response in the following format:\nExplanation: [Your explanation of the linguistic property]\nExample: [Your example of the property]\nPuzzle: [Your logic puzzle]\nSolution: [The solution to your puzzle]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately explains the {t['property']} property in {t['language']}.",
            "The example provided clearly illustrates the linguistic property.",
            "The logic puzzle is well-constructed and requires understanding of the linguistic property to solve.",
            "The puzzle is challenging but solvable, demonstrating creativity and logical thinking.",
            "The solution to the puzzle is provided and is correct based on the given information."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
