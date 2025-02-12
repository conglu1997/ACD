class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task_type": "creation",
                "theme": "time",
                "prompts": [
                    "Create an original riddle based on the theme of 'time'.",
                    "Ensure that the riddle is challenging, creative, and has a clear, logical answer."
                ]
            },
            "2": {
                "task_type": "solving",
                "riddle": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
                "prompts": [
                    "Solve the given riddle.",
                    "Provide a clear explanation of your reasoning process."
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'creation':
            return f"""Create an original riddle based on the theme of '{t['theme']}'. Ensure that the riddle is challenging, creative, and has a clear, logical answer. Format your response as follows:\n\nRiddle: [Your original riddle]\nAnswer: [The answer to your riddle]\n\nYour riddle should be engaging, thought-provoking, and well-constructed."""
        elif t['task_type'] == 'solving':
            return f"""Solve the given riddle. Provide a clear explanation of your reasoning process. Ensure to include both the solution and the explanation in your response. Format your response as follows:\n\nSolution: [Your solution]\nExplanation: [Your explanation]\n\nRiddle: {t['riddle']}\n\nEnsure your solution is logical and well-explained."""
        else:
            return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'creation':
            criteria = [
                "The riddle should be based on the given theme.",
                "The riddle should be challenging, creative, and have a clear, logical answer."
            ]
        elif t['task_type'] == 'solving':
            criteria = [
                "The solution should correctly solve the riddle.",
                "The explanation should clearly outline the reasoning process."
            ]
        else:
            criteria = []
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
