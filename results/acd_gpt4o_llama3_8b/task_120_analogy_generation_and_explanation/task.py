class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "concepts": ["time", "river"],
                "instructions": "Generate an analogy between the concepts of 'time' and 'river'. Explain the reasoning behind the analogy, describing how the two concepts are similar and why the analogy is appropriate. Submit your response as a plain text string with two sections: 'Analogy' and 'Explanation'."
            },
            "2": {
                "concepts": ["knowledge", "tree"],
                "instructions": "Generate an analogy between the concepts of 'knowledge' and 'tree'. Explain the reasoning behind the analogy, describing how the two concepts are similar and why the analogy is appropriate. Submit your response as a plain text string with two sections: 'Analogy' and 'Explanation'."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate an analogy between the following concepts: {t["concepts"]}. Explain the reasoning behind the analogy, describing how the two concepts are similar and why the analogy is appropriate. Submit your response as a plain text string with two sections: 'Analogy' and 'Explanation'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should include a valid analogy between the two given concepts.",
            "The response should include a clear and logical explanation of the analogy.",
            "The explanation should describe how the two concepts are similar and why the analogy is appropriate."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
