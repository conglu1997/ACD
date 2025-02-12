class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "interpretation", "problem": "If a train travels at a speed of 60 km/h and covers a distance of 180 km, how long does it take for the train to complete the journey?"},
            "2": {"type": "generation", "expression": "3x + 5 = 20"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['type'] == 'interpretation':
            return f"""Your task is to interpret the given mathematical word problem and provide a clear, step-by-step solution.

Problem: {t['problem']}

Your response should include:
1. The mathematical steps to solve the problem.
2. The final answer with appropriate units if applicable.
3. Ensure your response is formatted as follows:
- Step-by-step solution: [Your detailed steps]
- Final answer: [Your final answer with units]

Provide your response in plain text format.

Example:
Problem: If a car travels at a speed of 50 km/h for 3 hours, how far does it travel?
- Step-by-step solution: Distance = Speed * Time; Distance = 50 km/h * 3 h = 150 km
- Final answer: 150 km"""
        elif t['type'] == 'generation':
            return f"""Your task is to generate a mathematical word problem based on the given expression.

Expression: {t['expression']}

Your response should include:
1. A clear and coherent word problem that corresponds to the given expression.
2. The problem should involve real-world scenarios and be solvable using the provided expression.
3. Ensure your response is formatted as follows:
- Word problem: [Your generated word problem]

Provide your response in plain text format.

Example:
Expression: 2x + 3 = 11
- Word problem: Sarah has 3 more than twice the number of apples as John. If Sarah has 11 apples, how many apples does John have?
- Solution: 2x + 3 = 11; 2x = 8; x = 4. John has 4 apples."""
        else:
            raise ValueError("Unknown task type.")

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['type'] == 'interpretation':
            criteria = [
                "The mathematical steps to solve the problem should be accurate and clear.",
                "The final answer should be correct and include appropriate units if applicable.",
                "The response should follow the required format."
            ]
        elif t['type'] == 'generation':
            criteria = [
                "The generated word problem should correspond accurately to the given expression.",
                "The word problem should be coherent and involve real-world scenarios.",
                "The response should follow the required format."
            ]
        else:
            raise ValueError("Unknown task type.")
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
