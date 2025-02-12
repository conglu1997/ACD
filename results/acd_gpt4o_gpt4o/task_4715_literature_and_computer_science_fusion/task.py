class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"text": "To be, or not to be, that is the question:\nWhether 'tis nobler in the mind to suffer\nThe slings and arrows of outrageous fortune,\nOr to take arms against a sea of troubles\nAnd by opposing end them.", "concept": "algorithmic complexity"},
            "2": {"text": "Two roads diverged in a yellow wood,\nAnd sorry I could not travel both\nAnd be one traveler, long I stood\nAnd looked down one as far as I could\nTo where it bent in the undergrowth;", "concept": "decision trees"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze the following literary text from the perspective of the specified computer science concept and explain the parallels and insights derived from this interdisciplinary approach:

Text: {t['text']}

Computer Science Concept: {t['concept']}

Your analysis should include:
1. A clear explanation of the computer science concept.
2. A detailed analysis of the literary text, relating its elements to the computer science concept.
3. Insights or new perspectives gained from this interdisciplinary approach.

Ensure your analysis is coherent, detailed, and demonstrates a deep understanding of both the literary text and the computer science concept. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should include a clear explanation of the computer science concept and a detailed analysis of the literary text, relating its elements to the concept."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
