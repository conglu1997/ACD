class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "A festival involving dragon boat races, celebrated with rice dumplings wrapped in bamboo leaves."},
            "2": {"description": "An ancient form of martial arts featuring stylized movements and poses, often performed in colorful lion costumes."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to identify the cultural origin of the artifact, tradition, or practice described below:

Description: {t['description']}

Provide the cultural origin in plain text format. Ensure that your identification is based on accurate cultural knowledge and reasoning. Your response should be a single sentence identifying the cultural origin."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should accurately identify the cultural origin of the described artifact, tradition, or practice."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
