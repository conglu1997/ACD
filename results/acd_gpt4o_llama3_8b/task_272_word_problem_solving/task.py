class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "A farmer has 10 apples. He gives 3 apples to each of his 2 friends. How many apples does he have left?"
            },
            "2": {
                "problem": "Sarah has twice as many books as John. If John has 7 books, how many books does Sarah have?" 
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following mathematical word problem:

Problem: {t['problem']}

Provide your answer as a single integer. Show your calculations and reasoning steps leading to the final answer."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        import re
        problem = t['problem']
        instructions = TaskFamily.get_instructions(t)
        answers = {
            "A farmer has 10 apples. He gives 3 apples to each of his 2 friends. How many apples does he have left?": 4,
            "Sarah has twice as many books as John. If John has 7 books, how many books does Sarah have?": 14
        }
        correct_answer = answers[problem]
        try:
            extracted_answer = int(re.search(r'\d+', submission).group())
            return 1.0 if extracted_answer == correct_answer else 0.0
        except:
            return 0.0
