class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task": "generate_riddle",
                "constraints": "The riddle should be about time and should be suitable for children."
            },
            "2": {
                "task": "solve_riddle",
                "riddle": "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task'] == 'generate_riddle':
            return f"Generate a riddle based on the following constraints: {t['constraints']} Ensure the riddle is creative, engaging, and fits the specified theme. The riddle should have a clear and logical solution. Submit your riddle as a plain text string in the following format: 'Riddle: [Your riddle] Solution: [The solution to your riddle]'."
        elif t['task'] == 'solve_riddle':
            return f"Solve the following riddle: {t['riddle']} Provide a clear and concise answer as a plain text string in the format: 'Answer: [Your answer]'."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task'] == 'generate_riddle':
            validation_criteria = [
                "The riddle should be about the specified theme.",
                "The riddle should be suitable for the specified audience.",
                "The riddle should be creative and engaging.",
                "The riddle should have a clear and logical solution.",
                "The riddle should be in the correct format: 'Riddle: [Your riddle] Solution: [The solution to your riddle]'."
            ]
        elif t['task'] == 'solve_riddle':
            validation_criteria = [
                "The answer should be correct.",
                "The answer should be concise and clearly stated.",
                "The answer should be in the correct format: 'Answer: [Your answer]'."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
