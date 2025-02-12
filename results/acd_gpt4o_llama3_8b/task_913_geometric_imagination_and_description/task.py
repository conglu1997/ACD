class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "shape": "a 3D pyramid composed of 4 layers of cubes",
                "instructions": "Visualize a 3D pyramid composed of 4 layers of cubes. Describe the structure in detail and provide step-by-step instructions on how to recreate it using descriptive language. Ensure that your instructions are clear, logical, and precise, suitable for someone to follow without visual aids. Submit your response as a plain text string with two sections: 'Description' and 'Instructions'."
            },
            "2": {
                "shape": "a complex polygonal pattern composed of 5 different shapes",
                "instructions": "Visualize a complex polygonal pattern composed of 5 different shapes. Describe the pattern in detail and provide step-by-step instructions on how to recreate it using descriptive language. Ensure that your instructions are clear, logical, and precise, suitable for someone to follow without visual aids. Submit your response as a plain text string with two sections: 'Description' and 'Instructions'."
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
            "The response should include a clear and detailed description of the specified geometric shape or pattern.",
            "The instructions should be logically sequenced and precise, suitable for someone to follow without visual aids.",
            "The submission should adhere to the specified format with two sections: 'Description' and 'Instructions'.",
            "The description should cover all relevant aspects of the shape or pattern, including dimensions and relationships between components.",
            "The instructions should provide clear steps for assembling or drawing the shape or pattern."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
