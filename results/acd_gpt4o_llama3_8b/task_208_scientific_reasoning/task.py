class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "phenomenon": "Plants in a garden are observed to grow faster when classical music is played for them compared to when no music is played.",
                "constraints": [
                    "The music is played for 2 hours every day.",
                    "The plants are of the same species and are given the same amount of water and sunlight."
                ]
            },
            "2": {
                "phenomenon": "A group of students who slept for 8 hours performed better in exams compared to those who slept for 4 hours.",
                "constraints": [
                    "The students were from the same class and studied the same material.",
                    "The exams were conducted at the same time of day."
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        phenomenon = t["phenomenon"]
        constraints = "\n".join(t["constraints"])
        return f"""Based on the given phenomenon, generate a scientific hypothesis and explain your reasoning. The phenomenon is: {phenomenon}\n
Here are the constraints:\n{constraints}\n
Submit your hypothesis and explanation as a plain text string in the following format: 'Hypothesis: [Your hypothesis]\nExplanation: [Your explanation]'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The hypothesis should be scientifically plausible.", "The explanation should logically follow from the phenomenon and constraints."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
