class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A traditional Japanese tea ceremony.", "instruction": "Describe the cultural significance and key elements of a traditional Japanese tea ceremony. Ensure your description is respectful and captures the essence of the ceremony. Your response should be at least 200 words long."},
            "2": {"scenario": "A conversation between a tourist and a local in a small Italian village.", "instruction": "Generate a dialogue between a tourist and a local in a small Italian village where the local shares insights about their culture and traditions. The dialogue should reflect mutual respect and curiosity. Ensure the dialogue includes at least 10 exchanges."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task involves demonstrating cultural understanding and empathy. Please follow the specific instructions for the given scenario:

Scenario: {t['scenario']}

{t['instruction']}

Ensure that your response is respectful, culturally sensitive, and accurately represents the cultural elements mentioned. Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should be respectful and culturally sensitive.",
            "The response should accurately represent the cultural elements mentioned.",
            "The response should demonstrate empathy and understanding towards the culture.",
            "The response should meet the specified length and depth requirements."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
