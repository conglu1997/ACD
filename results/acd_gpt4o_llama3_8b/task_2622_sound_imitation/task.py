class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A bustling city street during rush hour, with cars honking, people talking, and street vendors calling out."
            },
            "2": {
                "scenario": "A serene forest in the early morning, with birds chirping, leaves rustling in the wind, and a distant stream flowing."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a descriptive representation of the sounds in the following scenario:

Scenario: {t['scenario']}

Your description should be between 200 to 300 words and should vividly convey the auditory experience of the scenario. Focus on capturing the essence of the sounds, their sources, and the overall atmosphere created by these sounds. Use sensory language to make the description immersive and engaging.

Submit your description as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The description should be between 200 to 300 words.", "The description should vividly convey the auditory experience of the scenario.", "The description should be immersive and engaging, using sensory language."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
