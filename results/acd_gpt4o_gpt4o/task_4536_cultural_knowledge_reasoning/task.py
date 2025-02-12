class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "cultural_practice", "prompt": "Explain the significance of the Japanese tea ceremony and describe the main steps involved in it."},
            "2": {"type": "historical_context", "prompt": "Discuss the cultural and historical significance of the Renaissance period in Europe. Include key figures and their contributions."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "cultural_practice":
            return f"""Your task is to explain the significance of the Japanese tea ceremony and describe the main steps involved in it. Provide a detailed explanation that covers the cultural importance and the procedural aspects of the ceremony. Structure your response in the following format: \n- Significance of the tea ceremony \n- Main steps involved \n- Any notable cultural elements."""
        else:
            return f"""Your task is to discuss the cultural and historical significance of the Renaissance period in Europe. Include key figures and their contributions. Provide a detailed discussion that covers the cultural impact, key historical events, and notable figures. Structure your response in the following format: \n- Overview of the Renaissance \n- Cultural significance \n- Key figures and their contributions."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "cultural_practice":
            criteria = ["The response should accurately explain the significance of the Japanese tea ceremony.", "The description should include the main steps involved in the ceremony.", "The response should highlight any notable cultural elements."]
        else:
            criteria = ["The response should accurately discuss the cultural and historical significance of the Renaissance period.", "The discussion should include key figures and their contributions."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
