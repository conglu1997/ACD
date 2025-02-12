class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"topic": "Should school uniforms be mandatory?", "stance": "for"},
            "2": {"topic": "Is technology making us more isolated?", "stance": "against"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a persuasive argument based on the following topic and stance:

Topic: {t['topic']}
Stance: {t['stance']}

Your argument should be clear, logical, and persuasive. Aim to convince the reader of your stance on the topic. The argument should be between 150 and 300 words long."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The argument should be clear and logical.", "The argument should use persuasive language.", "The argument should be between 150 and 300 words long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
