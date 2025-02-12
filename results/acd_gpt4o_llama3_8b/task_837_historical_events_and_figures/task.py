class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Analyze the significance of the fall of the Berlin Wall in 1989. Include its impact on both Germany and the broader world."},
            "2": {"prompt": "Create a hypothetical scenario where Leonardo da Vinci meets Albert Einstein. Describe their interaction and what they might discuss."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        prompt = t["prompt"]
        return f"""Complete the following task based on the given prompt:\n\n{prompt}\n\nSubmit your response as a plain text string. Your response should be structured as follows:\n\nTask 1 - Analysis:\n[Detailed analysis here, 200-300 words]\n\nTask 2 - Hypothetical Scenario:\n[Generated scenario here, 200-300 words]\n\nInteraction Description:\n[Description of interaction and discussion here, 200-300 words]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should demonstrate a clear understanding of the historical event and its significance.",
            "The hypothetical scenario should be creative and plausible given the historical figures involved.",
            "The interaction description should be coherent and insightful, reflecting the personalities and knowledge of the figures.",
            "The response should follow the given format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
