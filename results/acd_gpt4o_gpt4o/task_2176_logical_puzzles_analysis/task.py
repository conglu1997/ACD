class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "A man says he always lies. Is he telling the truth?"},
            "2": {"puzzle": "A barber is the 'one who shaves all those, and those only, who do not shave themselves'. Does the barber shave himself?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze the following logical puzzle or paradox and explain its resolution or implications:\n\n{t['puzzle']}\n\nYour explanation should be clear, logically sound, and demonstrate critical thinking. Ensure that you provide a step-by-step analysis and any necessary background information for understanding the puzzle. Submit your analysis in plain text format.\n\nFormat your response as follows:\n\nPuzzle Analysis: [Your detailed analysis]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation should be clear and logically sound.",
            "The submission should demonstrate critical thinking and an understanding of the puzzle.",
            "The analysis should be detailed, providing a step-by-step breakdown of the puzzle.",
            "Any necessary background information for understanding the puzzle should be included."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
