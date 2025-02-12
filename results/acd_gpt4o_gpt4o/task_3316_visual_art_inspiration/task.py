class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"painting": "The Starry Night by Vincent van Gogh"},
            "2": {"painting": "The Persistence of Memory by Salvador Dalí"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to describe the following famous painting and then create an original fictional story inspired by it.

Painting: {t['painting']}

Your response should include:
1. A detailed and vivid description of the painting, including its key elements and overall mood.
2. An original fictional story inspired by the painting. The story should be coherent, creative, and reflect the themes or emotions evoked by the painting.

Provide your response in plain text format as follows:

Description:
[Your detailed description of the painting]

Story:
[Your original fictional story inspired by the painting]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a detailed and vivid description of the painting, capturing its key elements and overall mood.",
            "The fictional story should be original, coherent, and creatively inspired by the painting, reflecting its themes or emotions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
