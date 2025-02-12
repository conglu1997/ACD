class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"profile": {"name": "John", "age": 30, "location": "San Francisco", "interests": ["technology", "science fiction", "gaming"], "past_purchases": ["smartphone", "gaming console"], "preferred_brands": ["Sony", "Apple"]}, "recommendation_type": "product"},
            "2": {"profile": {"name": "Emma", "age": 25, "location": "New York", "interests": ["cooking", "travel", "fashion"], "past_purchases": ["cookbook", "travel guide"], "preferred_brands": ["Gucci", "Tefal"]}, "recommendation_type": "content"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate personalized {t['recommendation_type']} recommendations for the user based on their profile and preferences. Ensure that your recommendations are relevant, thoughtful, and tailored to the user's interests, past behavior, and preferred brands. Provide your response in plain text format.\n\nUser Profile: {t['profile']}\n\nResponse format:\n1. Recommendation 1: [Your recommendation]\n2. Recommendation 2: [Your recommendation]\n3. Recommendation 3: [Your recommendation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The recommendations should be relevant to the user's interests, past behavior, and preferred brands.", "The recommendations should be thoughtful and personalized.", "The response should follow the specified format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
