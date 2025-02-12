class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"city": "Paris", "days": 3},
            "2": {"city": "Tokyo", "days": 5}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given city and number of days:

City: {t['city']}
Number of Days: {t['days']}

Create a detailed tourist itinerary for a hypothetical visitor. Your itinerary should include:
1. A daily schedule with specific times for each activity in the format HH:MM (24-hour clock).
2. A mix of activities, including sightseeing (e.g., landmarks, parks), cultural experiences (e.g., museums, local events), and leisure (e.g., shopping, relaxation).
3. Dining options for each meal (breakfast, lunch, and dinner) with at least one local cuisine recommendation per day.
4. Transportation details between different locations (e.g., walking, public transport, taxi).
5. Variation in the itinerary to cover different parts of the city and provide a diverse experience.

Ensure your itinerary is well-organized, realistic, and provides a fulfilling experience for the visitor. Submit your response as a plain text string in the following format:

Day 1:
[Schedule for Day 1]

Day 2:
[Schedule for Day 2]

..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The itinerary should include a daily schedule with specific times for each activity in the format HH:MM (24-hour clock).",
            "The itinerary should include a mix of activities, cultural experiences, dining options with local cuisine, and transportation details.",
            "The itinerary should be well-organized, realistic, varied, and provide a fulfilling experience."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
