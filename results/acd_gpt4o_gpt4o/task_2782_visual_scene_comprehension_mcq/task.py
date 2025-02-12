class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "A park scene with a playground, a pond with ducks, and people having a picnic under a large oak tree. There are children playing on the swings, a man reading a book on a bench, and a woman walking a dog.",
                "question": "What is the woman doing in the park?",
                "choices": ["A. Reading a book on a bench", "B. Walking a dog", "C. Playing on the swings", "D. Having a picnic"]
            },
            "2": {
                "description": "A busy city street with tall buildings, cars honking, and people rushing to work. There is a coffee shop on the corner, a bus stop with a line of people, and a street musician playing the guitar.",
                "question": "What is the street musician doing?",
                "choices": ["A. Playing the guitar", "B. Waiting at the bus stop", "C. Rushing to work", "D. Drinking coffee"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to answer the following multiple-choice question based on the detailed description of the visual scene provided.

Description: {t['description']}

Question: {t['question']}

Choices:
{chr(10).join(t['choices'])}

Choose the correct answer by providing the corresponding letter (A, B, C, or D)."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        correct_answers = {
            "What is the woman doing in the park?": "B",
            "What is the street musician doing?": "A"
        }
        criteria = [f"The correct answer is {correct_answers[t['question']]}."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
