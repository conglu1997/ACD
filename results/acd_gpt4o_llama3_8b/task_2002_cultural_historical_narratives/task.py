class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Describe a traditional Japanese tea ceremony, including key elements and their significance.", "instructions": "Generate a detailed description of a traditional Japanese tea ceremony. Your description should include key elements such as the setting, utensils, steps in the ceremony, and the cultural significance of each element. Ensure that your narrative is accurate, coherent, and culturally respectful."},
            "2": {"prompt": "Narrate the events leading up to the signing of the Declaration of Independence, highlighting key figures and motivations.", "instructions": "Generate a detailed narrative of the events leading up to the signing of the Declaration of Independence in the United States. Your narrative should include key figures, their motivations, and significant events that influenced the decision to declare independence. Ensure that your narrative is accurate, coherent, and historically contextualized."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        prompt = t["prompt"]
        instructions = t["instructions"]
        return f"""{instructions}

Prompt: {prompt}

Submit your response as a plain text string. Ensure that your description or narrative is detailed, accurate, and contextually appropriate."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description or narrative should be detailed and coherent.",
            "The content should be accurate and contextually appropriate.",
            "The narrative should include key elements or figures mentioned in the prompt.",
            "The submission should be culturally respectful and historically contextualized." ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
