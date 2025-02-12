class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'problem': 'Prove that the sum of the first n odd numbers is equal to n^2. Provide a step-by-step explanation for your proof.'},
            '2': {'problem': 'Solve the quadratic equation x^2 - 4x + 4 = 0 and provide a detailed step-by-step explanation for your solution.'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Solve the following mathematical problem and provide a detailed step-by-step explanation for your solution: {t['problem']} \nEnsure that each step is clearly explained and logically follows from the previous step. Submit your solution as a plain text string in the following format:\n\nSolution: \nStep 1: [First step]\nStep 2: [Second step]\n...\nStep N: [N-th step]\nFinal Answer: [Your final answer here]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The solution should correctly solve the problem.", "The explanation should be detailed, clear, and logically structured in a step-by-step manner."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
