class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "argument": "Climate change is a serious issue. Governments should take action to reduce carbon emissions."
            },
            "2": {
                "argument": "Exercise is important for health. People should exercise regularly to stay fit and healthy."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are given the following argument:

Argument: {t['argument']}

Your task is to improve this argument by enhancing its clarity, coherence, and persuasiveness. Make sure your improved version is logically structured, uses persuasive language, and clearly conveys the importance of the topic. Submit your improved argument as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The improved argument should be clearer and more coherent.",
            "The improved argument should use more persuasive language.",
            "The improved argument should better convey the importance of the topic."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
