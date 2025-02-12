class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Write a story about a lost treasure from the perspective of two characters: a daring explorer and a skeptical scientist. Each perspective should provide unique insights and contribute to the overall narrative.",
            },
            "2": {
                "prompt": "Write a story about a mysterious forest from the perspective of two characters: a curious child and a cautious ranger. Each perspective should provide unique insights and contribute to the overall narrative.",
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given prompt:

Prompt:
{t['prompt']}

Your response should include the following:
1. Perspective 1: Write the story from the first character's perspective. Ensure that this perspective provides unique insights and contributes to the overall narrative.
2. Perspective 2: Write the story from the second character's perspective. Ensure that this perspective provides unique insights and contributes to the overall narrative.

Both perspectives should be coherent, logically consistent with each other, and create a unified story. Each perspective should be at least 300 words long. Ensure that the perspectives do not repeat information verbatim and add unique elements to the story. The perspectives should influence each other, showing interconnectedness in the narrative. Submit your response as a plain text string with each perspective clearly labeled.

Example response format:

Perspective 1: [Story from the first character's perspective]
Perspective 2: [Story from the second character's perspective]

Ensure your submission follows this format and meets all criteria.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "Each perspective should be at least 300 words long.",
            "Both perspectives should provide unique insights and contribute to the overall narrative.",
            "The story should be coherent and logically consistent across both perspectives.",
            "Each perspective should be clearly labeled.",
            "The perspectives should not repeat information verbatim and should add unique elements to the story.",
            "The perspectives should influence each other, showing interconnectedness in the narrative."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
