class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "goal": "Determine the effect of different amounts of sunlight on plant growth.",
                "type": "description"
            },
            "2": {
                "experiment": [
                    "1. Plant seeds in three pots with identical soil.",
                    "2. Place one pot in direct sunlight, one pot in partial sunlight, and one pot in the shade.",
                    "3. Water the plants equally every day.",
                    "4. Measure the height of the plants every week for four weeks.",
                    "5. Analyze the data to determine which amount of sunlight resulted in the tallest plants."
                ],
                "type": "analysis",
                "errors": [
                    "The experiment does not account for other variables such as temperature and humidity.",
                    "The frequency of measurements (once a week) might not be sufficient to capture the growth trend accurately."
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['type'] == 'description':
            return f"""Your task is to describe the steps of a scientific experiment to achieve the following goal: {t['goal']}. Ensure your description is clear, logically sequenced, and includes all necessary controls and variables. Provide your response in plain text format."""
        elif t['type'] == 'analysis':
            return f"""Your task is to analyze the following experiment and identify any errors or missing steps. Provide a detailed analysis that includes what is done correctly, what is missing or incorrect, and suggest improvements. Here is the experiment:

{t['experiment']}

Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if t['type'] == 'description':
            criteria = [
                "The description should be clear and logically sequenced.",
                "All necessary controls and variables should be included.",
                "The steps should be detailed enough to replicate the experiment."
            ]
        elif t['type'] == 'analysis':
            criteria = [
                "The analysis should correctly identify errors and missing steps.",
                "Suggestions for improvement should be reasonable and enhance the experiment's validity."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
