class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "work1": "Mona Lisa by Leonardo da Vinci",
                "work2": "The Persistence of Memory by Salvador Dalí",
                "prompt": "Identify and explain the thematic similarities between the Mona Lisa by Leonardo da Vinci and The Persistence of Memory by Salvador Dalí."
            },
            "2": {
                "work1": "To Kill a Mockingbird by Harper Lee",
                "work2": "1984 by George Orwell",
                "prompt": "Identify and explain the thematic similarities between To Kill a Mockingbird by Harper Lee and 1984 by George Orwell."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Identify and explain the thematic similarities between the following works of art or literature. Your explanation should be clear, well-structured, and demonstrate a deep understanding of the themes present in both works. Here are the works:

1. {t['work1']}
2. {t['work2']}

Submit your explanation as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The explanation should clearly identify thematic similarities between the two works.",
            "The explanation should demonstrate a deep understanding of the themes present in both works.",
            "The response should be well-structured and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
