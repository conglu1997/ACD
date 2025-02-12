class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "mythology": "Greek",
                "theme": "origin of a natural phenomenon"
            },
            "2": {
                "mythology": "Norse",
                "theme": "hero's quest"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a detailed mythological tale inspired by {t['mythology']} mythology. The story should align with the thematic elements and characteristics of this mythology. The theme for your tale is '{t['theme']}'. Ensure that the narrative is cohesive, engaging, and includes culturally accurate elements that reflect the mythology's ethos, values, and common motifs. Your tale should be at least 500 words long. Submit your tale as a plain text string in the following format:

'Tale: [Your detailed mythological tale]'
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The tale should align with the thematic elements and characteristics of the chosen mythology.",
            "The narrative should be cohesive and engaging.",
            "The tale should be at least 500 words long.",
            "The story should include culturally accurate elements that reflect the ethos, values, and common motifs of the mythology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
