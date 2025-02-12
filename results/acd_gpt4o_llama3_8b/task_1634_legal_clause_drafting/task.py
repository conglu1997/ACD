class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task": "draft_clause",
                "requirements": "Draft a non-disclosure agreement (NDA) clause that specifies the obligations of the receiving party to maintain the confidentiality of the disclosing party's information. Ensure the clause covers the scope of confidentiality, duration, exceptions, and remedies."
            },
            "2": {
                "task": "draft_clause",
                "requirements": "Draft a force majeure clause for a service contract that limits liability for both parties in the event of unforeseen circumstances such as natural disasters, pandemics, or other events beyond their control. Ensure the clause includes the definition of force majeure events, obligations of parties during such events, and the duration of relief."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Draft a legal clause based on the following requirements: {t['requirements']} Ensure the clause is precise, clear, and adheres to standard legal language. Submit your clause as a plain text string in the format: 'Clause: [Your drafted clause]'."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The clause should be precise and clear.",
            "The clause should adhere to standard legal language.",
            "The clause should meet the specified requirements.",
            "The clause should be written in correct format and legal style."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
