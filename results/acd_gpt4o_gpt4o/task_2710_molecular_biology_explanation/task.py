class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "process": "DNA replication",
                "question": "Explain the process of DNA replication in a way that a high school student can understand."
            },
            "2": {
                "process": "Protein synthesis",
                "question": "Describe the process of protein synthesis, including transcription and translation, in a manner understandable to a non-specialist."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to explain a complex process in molecular biology in a clear and understandable manner.\n\nProcess: {t['process']}\n\nQuestion: {t['question']}\n\nProvide your explanation in plain text format, structured as follows:\n\nExplanation: [Your explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The explanation should be scientifically accurate.", "The explanation should be clear and understandable to the target audience.", "The explanation should cover all key steps of the process."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
