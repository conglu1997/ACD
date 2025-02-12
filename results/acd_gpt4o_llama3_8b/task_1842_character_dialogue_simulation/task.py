class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "Three friends are planning a surprise birthday party for a mutual friend. Each friend has a distinct personality: one is very organized and detail-oriented, another is laid-back and spontaneous, and the third is anxious and indecisive."
            },
            "2": {
                "scenario": "A team of four colleagues is discussing how to approach a challenging project. Each colleague has a distinct personality: one is highly analytical, another is creative and innovative, the third is practical and down-to-earth, and the fourth is skeptical and critical."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Simulate a realistic conversation between multiple characters based on the given scenario. Each character should have a distinct personality as described, and their dialogue should reflect these personalities. Ensure the conversation is coherent and flows naturally.

Scenario: {t['scenario']}

Personality descriptions:
- Organized and detail-oriented: Likes to plan everything meticulously and is very focused on details.
- Laid-back and spontaneous: Prefers to go with the flow and make decisions on the spot.
- Anxious and indecisive: Frequently worries about potential problems and has difficulty making decisions.
- Highly analytical: Focuses on data and logical reasoning to make decisions.
- Creative and innovative: Thinks outside the box and comes up with original ideas.
- Practical and down-to-earth: Prefers realistic and feasible solutions.
- Skeptical and critical: Often questions ideas and looks for potential flaws.

Submit your response as a plain text string in the following format:

Character 1 (Personality): [Dialogue]
Character 2 (Personality): [Dialogue]
Character 3 (Personality): [Dialogue]
..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The dialogue should reflect each character's distinct personality.",
            "The conversation should be coherent and flow naturally."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
