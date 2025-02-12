class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "shape": "triangle",
                "transformation": "rotation 90 degrees clockwise",
                "requirements": "Describe the initial shape and its properties, such as side lengths, angles, and orientation. Explain the transformation in detail and describe the resulting shape, including any changes in orientation or properties."
            },
            "2": {
                "shape": "rectangle",
                "transformation": "scaling by a factor of 2 along the x-axis",
                "requirements": "Describe the initial shape and its properties, such as side lengths, angles, and orientation. Explain the transformation in detail and describe the resulting shape, including any changes in dimensions or properties."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Describe and reason about the following geometric shape and its transformation:

Shape: {t['shape']}

Transformation: {t['transformation']}

Requirements: {t['requirements']}

Your response should include a detailed description of the initial shape, an explanation of the transformation, and a detailed description of the resulting shape. Submit your response as a plain text string with the following sections:

1. Initial Shape Description: [Describe the initial shape and its properties, such as side lengths, angles, and orientation]
2. Transformation Explanation: [Explain the transformation in detail]
3. Resulting Shape Description: [Describe the resulting shape, including any changes in orientation or properties]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The initial shape description should be accurate and detailed, including side lengths, angles, and orientation.",
            "The transformation explanation should be clear, detailed, and correct.",
            "The resulting shape description should be accurate, including any changes in orientation or properties."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
