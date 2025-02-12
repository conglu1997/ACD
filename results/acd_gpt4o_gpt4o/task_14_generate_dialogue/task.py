class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "Two friends discussing their plans for the weekend. One friend prefers outdoor activities while the other prefers indoor activities.", "characters": ["Alice", "Bob"]},
            "2": {"scenario": "A customer and a shopkeeper negotiating the price of an antique item. The customer believes the item is overpriced and tries to bargain.", "characters": ["Customer", "Shopkeeper"]},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a coherent and engaging dialogue based on the following scenario and characters:

Scenario: {t['scenario']}
Characters: {', '.join(t['characters'])}

Ensure the dialogue is natural, context-appropriate, and maintains a consistent tone. The conversation should be at least 10 exchanges long, with each character contributing to the dialogue. Provide the dialogue in plain text format without additional formatting."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The dialogue should be coherent.", "The dialogue should be engaging.", "The dialogue should be context-appropriate.", "The dialogue should maintain a consistent tone.", "The dialogue should be at least 10 exchanges long.", "The dialogue should have a natural flow."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
