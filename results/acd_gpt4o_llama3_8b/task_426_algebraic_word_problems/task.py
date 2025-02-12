class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "A farmer has chickens and cows. There are a total of 20 animals and 54 legs. How many chickens and how many cows does the farmer have?"
            },
            "2": {
                "problem": "A bookstore sold a total of 120 books in a week. They sold 40 more fiction books than non-fiction books. How many fiction and non-fiction books did they sell?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following algebraic word problem by translating it into mathematical equations and solving for the unknowns. Provide your solution in a clear and concise manner.\n\nProblem:\n{t['problem']}\n\nFormat your response as follows:\n1. State the equations you derived from the problem.\n2. Solve the equations step-by-step.\n3. Clearly state the final answer.\n\nFor Task 1, clearly state the number of chickens and cows. For Task 2, clearly state the number of fiction and non-fiction books."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["problem"].startswith("A farmer has chickens and cows."): 
            criteria = [
                "The solution should state the correct number of chickens and cows.",
                "The solution should include the equations used to solve the problem.",
                "The equations should be derived correctly from the problem statement.",
                "The final answer should be mathematically correct."
            ]
        elif t["problem"].startswith("A bookstore sold a total of 120 books"): 
            criteria = [
                "The solution should state the correct number of fiction and non-fiction books.",
                "The solution should include the equations used to solve the problem.",
                "The equations should be derived correctly from the problem statement.",
                "The final answer should be mathematically correct."
            ]
        else:
            return 0.0
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
