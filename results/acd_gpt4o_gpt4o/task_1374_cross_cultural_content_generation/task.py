class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"content": "A short story about friendship.", "target_culture": "Japanese", "constraints": ["must include cultural elements like festivals (e.g., Hanami, Tanabata) or traditions (e.g., tea ceremony)", "should evoke a sense of harmony and respect", "should be at least 200 words long"]},
            "2": {"content": "A motivational speech for a corporate event.", "target_culture": "Brazilian", "constraints": ["must include references to local values (e.g., family, community) or famous personalities (e.g., Ayrton Senna)", "should be inspiring, energetic, and at least 200 words long"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Adapt the following content to fit the target cultural context while adhering to the given constraints:

Content: {t['content']}
Target Culture: {t['target_culture']}
Constraints: {', '.join(t['constraints'])}

Provide your adapted content in a clear and coherent format, ensuring it is appropriate and resonates with the target audience. The content should be at least 200 words long. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The adapted content should be culturally appropriate and resonate with the target audience.", "The content should adhere to the given constraints.", "The content should be at least 200 words long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
