class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"criteria": "A society that values individual freedom above all else, with minimal government intervention and a strong emphasis on personal responsibility.", "description": "A society where individuals are encouraged to pursue their own goals without interference. There is minimal regulation, and social services are privatized. The economy is driven by entrepreneurship and innovation, and citizens take pride in self-reliance."},
            "2": {"criteria": "A society that prioritizes communal well-being and equality, with extensive government support and social programs.", "description": "A society where resources are distributed equally among citizens. The government provides comprehensive social services, including healthcare, education, and housing. Community activities and cooperation are highly encouraged, and the economy is centrally planned to ensure equal opportunities for all."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        criteria = t["criteria"]
        description = t["description"]
        instructions = f"""Your task involves two parts:\n\n1. Critique: Critique the following description of a fictional society based on the given criteria:\n\nCriteria: {criteria}\nDescription: {description}\n\n2. Design: Design a fictional society based on the given criteria. Ensure your description is detailed and coherent, covering aspects such as governance, economy, social structure, and cultural values.\n\nResponse Format:\nCritique: <Your critique>\nDesigned Society: <Your description>\n\nProvide both parts in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The critique should address the alignment of the given description with the criteria, highlighting strengths and weaknesses.",
            "The designed society should adhere to the given criteria and be detailed and coherent.",
            "The designed society should cover aspects such as governance, economy, social structure, and cultural values."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
