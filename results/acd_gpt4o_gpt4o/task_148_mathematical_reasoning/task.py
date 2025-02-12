class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "A farmer has chickens and cows. There are 20 heads and 56 legs. How many chickens and how many cows are there?"},
            "2": {"problem": "Solve the following system of equations for x and y: 2x + 3y = 12 and 3x - y = 3."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following mathematical problem and provide a detailed reasoning for your solution. Ensure that your solution is accurate, logically sound, and well-structured. Here is the problem:\n\n{t['problem']}\n\nSubmit your solution in plain text format. Your response should include:\n1. A restatement of the problem.\n2. Identification of the variables and equations involved.\n3. A step-by-step breakdown of the solution process.\n4. The final solution.\n5. A brief explanation of why the solution is correct."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The solution should be accurate.", "The reasoning should be detailed and logically sound.", "The solution should be well-structured and coherent.", "All intermediate steps and calculations should be included.", "The final solution should be clearly stated.", "A brief explanation of why the solution is correct should be included."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
