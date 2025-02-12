class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "topic": "Should schools implement a four-day school week?",
                "position": "For",
                "opposing_argument": "Implementing a four-day school week would reduce instructional time and negatively impact students' learning outcomes."
            },
            "2": {
                "topic": "Is technology making people more isolated?",
                "position": "Against",
                "opposing_argument": "Technology, especially social media, is causing people to spend less time interacting face-to-face, leading to increased feelings of isolation."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            f"Your task is to construct a logical and coherent argument for the topic: '{t['topic']}'.\n"
            f"You should argue '{t['position']}' the proposition.\n"
            f"Additionally, you should provide a counter-argument to the following opposing point: '{t['opposing_argument']}'.\n"
            "Ensure your response is well-structured, logically sound, and uses clear and persuasive language.\n"
            "Provide your response in the following format:\n"
            "1. Argument: [Your argument]\n"
            "2. Counter-Argument: [Your counter-argument]\n"
            "Provide your response in plain text format."
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The argument should be logically coherent and well-structured.",
            "The counter-argument should effectively address the opposing point.",
            "The language used should be clear and persuasive."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
