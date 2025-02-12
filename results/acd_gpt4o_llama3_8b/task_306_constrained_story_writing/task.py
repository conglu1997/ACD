class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "title": "A Day in the Future",
                "constraints": [
                    "Include a character who is a time traveler.",
                    "Mention a futuristic gadget.",
                    "The story must end with a twist."
                ]
            },
            "2": {
                "title": "The Hidden Treasure",
                "constraints": [
                    "Include a map.",
                    "A secret code must be deciphered.",
                    "The story must have a happy ending."
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Write a short story with the title '{t['title']}'. Your story must incorporate the following elements and adhere to the given constraints:

Constraints:
1. {t['constraints'][0]}
2. {t['constraints'][1]}
3. {t['constraints'][2]}

Ensure that your story is coherent, creative, and follows a logical structure. The story should be between 300 and 500 words long. Submit your story as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The story must include a character who meets the specified role.",
            "The specified elements must be mentioned in the story.",
            "The story must adhere to the given constraints.",
            "The story must be coherent, creative, and logically structured.",
            "The story must be between 300 and 500 words long."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
