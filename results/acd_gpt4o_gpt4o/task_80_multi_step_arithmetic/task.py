class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "A farmer has 17 sheep and 24 cows. He buys 3 more sheep and then sells 5 cows. How many animals does he have in total now?"
            },
            "2": {
                "problem": "Jenny had $120. She spent $45 on groceries and then earned $30 by selling homemade cookies. How much money does Jenny have now?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following arithmetic word problem. Carefully perform each step and provide the final answer as a single number.

Problem: {t['problem']}

Provide your answer as a single number without any additional text."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        try:
            correct_answers = {
                "1": 39,  # 17 sheep + 3 sheep + 24 cows - 5 cows = 39 animals
                "2": 105  # $120 - $45 + $30 = $105
            }
            task_id = list(t.keys())[0]
            correct_answer = correct_answers[task_id]
            return 1.0 if float(submission.strip()) == correct_answer else 0.0
        except Exception:
            return 0.0
