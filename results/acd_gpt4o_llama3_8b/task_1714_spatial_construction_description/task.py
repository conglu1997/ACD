class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "shape": "a cube",
                "materials": "6 identical square cardboard pieces, glue",
                "instructions": "Describe the steps to construct a cube using 6 identical square cardboard pieces and glue. Your description should be detailed, logically ordered, and include all necessary steps. Submit your response as a plain text string in the following format:\n\nSteps:\n1. [First step]\n2. [Second step]\n..."
            },
            "2": {
                "shape": "a pyramid",
                "materials": "4 identical triangular cardboard pieces, 1 square cardboard piece, glue",
                "instructions": "Describe the steps to construct a pyramid using 4 identical triangular cardboard pieces, 1 square cardboard piece, and glue. Your description should be detailed, logically ordered, and include all necessary steps. Submit your response as a plain text string in the following format:\n\nSteps:\n1. [First step]\n2. [Second step]\n..."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return t["instructions"]

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The steps should be clear and logically ordered.",
            "The description should accurately describe how to construct the specified shape using the given materials.",
            "The response should be in the specified format with numbered steps."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
