class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"product": "Smartphone", "theme": "Minimalism", "target_audience": "Young professionals"},
            "2": {"service": "Online Language Learning Platform", "theme": "Cultural Enrichment", "target_audience": "Travel Enthusiasts"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'product' in t:
            return f"""Your task is to create a persuasive advertisement for the following product:

Product: {t['product']}
Theme: {t['theme']}
Target Audience: {t['target_audience']}

Ensure your advertisement is engaging, persuasive, and tailored to the target audience. Highlight the key features of the product and how it aligns with the theme. The advertisement should be concise, ideally no more than 150 words. Provide your advertisement in plain text format."""
        else:
            return f"""Your task is to create a persuasive advertisement for the following service:

Service: {t['service']}
Theme: {t['theme']}
Target Audience: {t['target_audience']}

Ensure your advertisement is engaging, persuasive, and tailored to the target audience. Highlight the key features of the service and how it aligns with the theme. The advertisement should be concise, ideally no more than 150 words. Provide your advertisement in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The advertisement should be engaging and persuasive.", "The advertisement should be tailored to the target audience.", "The key features of the product/service should be highlighted.", "The advertisement should align with the given theme.", "The advertisement should be concise, ideally no more than 150 words."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
