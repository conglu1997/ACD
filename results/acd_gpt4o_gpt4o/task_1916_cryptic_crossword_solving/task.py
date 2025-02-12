class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"clue": "Start to finish, it’s a race (5)"},
            "2": {"clue": "Ring and ring again (4)"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Your task is to solve the following cryptic crossword clue: '{t['clue']}'. Provide your answer in plain text format. Ensure your answer is a single word and matches the given number of letters."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        clues_answers = {
            "Start to finish, it’s a race (5)": "relay",
            "Ring and ring again (4)": "peal"
        }
        correct_answer = clues_answers[t['clue']]
        criteria = [f"The answer should be exactly '{correct_answer}'"]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
