class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem_statement": "Create a step-by-step algorithm for assembling a piece of flat-pack furniture. Include all necessary steps from unpacking the materials to the final assembly."
            },
            "2": {
                "problem_statement": "Create a step-by-step algorithm for preparing a basic meal (e.g., spaghetti with tomato sauce). Include all necessary steps from gathering ingredients to serving the meal."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            "Your task is to create a detailed, step-by-step algorithm for solving the following everyday problem."
            " Ensure your algorithm is clear, logically structured, and includes all necessary steps. Provide your response in plain text format and make sure to address the following points:\n\n"
            "1. Start with an introduction to the problem.\n"
            "2. List all the materials or ingredients needed.\n"
            "3. Provide a detailed, step-by-step procedure to solve the problem.\n"
            "4. Ensure each step is clear and logically follows from the previous step.\n"
            "5. Conclude with a final check or summary of the process."
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The introduction clearly states the problem.",
            "All necessary materials or ingredients are listed.",
            "The steps are detailed and logically structured.",
            "Each step is clear and follows logically from the previous step.",
            "The conclusion includes a final check or summary of the process."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
