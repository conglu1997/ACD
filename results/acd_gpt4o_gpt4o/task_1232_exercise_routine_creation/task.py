class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"goal": "weight loss"},
            "2": {"goal": "muscle gain"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create an exercise routine tailored to the specific fitness goal provided below. After creating the routine, provide a brief explanation of the benefits of each exercise included in the routine.

Fitness Goal: {t['goal']}

Your response should include:
1. A list of exercises with the number of sets and repetitions for each.
2. A brief explanation of how each exercise contributes to the fitness goal.

Ensure your routine is well-structured and your explanations are clear and accurate. Provide your response in plain text format. Here is an example format for your response:

Routine:
1. Squats - 3 sets of 15 reps
2. Push-ups - 3 sets of 10 reps
3. Plank - 3 sets of 1 minute

Explanation:
1. Squats: Help in building lower body strength and burning calories.
2. Push-ups: Enhance upper body strength and improve cardiovascular fitness.
3. Plank: Strengthen core muscles and improve overall stability.

Response format:
Routine: [Your list of exercises with sets and repetitions]
Explanation: [Your explanation of the benefits of each exercise]

Please ensure that your routine is realistic and appropriate for the given fitness goal."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a list of exercises with sets and repetitions.",
            "The explanation should clearly relate each exercise to the given fitness goal."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
