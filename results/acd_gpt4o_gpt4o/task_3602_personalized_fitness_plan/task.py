class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"constraints": "30-year-old male, beginner level, goal to lose 10 pounds in 3 months, has access to a gym.", "dietary_preferences": "vegetarian"},
            "2": {"constraints": "25-year-old female, intermediate level, goal to build muscle, prefers home workouts.", "dietary_preferences": "gluten-free"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a personalized fitness plan for the following individual based on their constraints and dietary preferences:

Constraints: {t['constraints']}
Dietary Preferences: {t['dietary_preferences']}

Ensure that the fitness plan is detailed, realistic, and tailored to the individual's needs. The plan should include:
1. Weekly workout schedule
2. Types of exercises and their duration
3. Dietary recommendations
4. Tips for staying motivated and tracking progress

Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The fitness plan should be detailed and tailored to the individual's constraints and dietary preferences.",
            "The workout schedule should be realistic and achievable.",
            "The dietary recommendations should align with the given dietary preferences.",
            "The plan should include tips for staying motivated and tracking progress."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
