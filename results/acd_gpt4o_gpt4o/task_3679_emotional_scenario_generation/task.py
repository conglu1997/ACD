class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "Generate a scenario that evokes a sense of deep sadness.", "emotion": "sadness"},
            "2": {"task": "Generate a scenario that evokes a sense of overwhelming joy.", "emotion": "joy"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate an original scenario that evokes a sense of {t['emotion']}. The scenario should be detailed and contextually appropriate, demonstrating an understanding of human psychology and emotional expression. Ensure that the scenario is coherent and vividly describes the situation to elicit the intended emotion. The emotional impact should be described in a way that explains how the scenario evokes the intended emotion.

Write your scenario in plain text format. Provide your response in the following format:

- Setting: [Your answer]
- Characters: [Your answer]
- Events: [Your answer]
- Emotional Impact: [Your answer]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [f"The scenario should evoke a sense of {t['emotion']}.", "The submission should be contextually appropriate and coherent.", "The format should follow the provided structure.", "The scenario should be original and not derived from existing works."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
