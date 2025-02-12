class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"experiment": "How to extract DNA from strawberries."},
            "2": {"experiment": "How to measure the pH of a solution using pH paper."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        experiment = t["experiment"]
        instructions = f"""Your task is to describe how to perform the following scientific experiment:

Experiment: {experiment}

Your description should include:
1. A list of necessary equipment and materials.
2. A step-by-step procedure.
3. Any safety precautions that should be taken.

Ensure your description is clear, detailed, and suitable for someone with a basic understanding of scientific principles. Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should include all necessary equipment and materials.", "The procedure should be detailed and easy to follow.", "Safety precautions should be mentioned and relevant."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
