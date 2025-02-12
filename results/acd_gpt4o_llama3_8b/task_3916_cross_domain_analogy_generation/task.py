class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept1": "quantum mechanics", "concept2": "baking"},
            "2": {"concept1": "ecosystem", "concept2": "corporate structure"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        concept1 = t["concept1"]
        concept2 = t["concept2"]
        return f"""Generate an analogy that links the concept of '{concept1}' with the concept of '{concept2}'. Your analogy should clearly explain how the aspects of the first concept relate to the aspects of the second concept in a creative and coherent manner. Submit your response as a plain text string in the format:\n\nAnalogy: [Your analogy]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analogy should be creative and clearly link the two given concepts.",
            "The analogy should demonstrate a deep understanding of both concepts.",
            "The analogy should be coherent and logically sound."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
