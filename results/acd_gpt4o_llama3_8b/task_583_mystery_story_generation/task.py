class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "clues": ["A locked room", "A missing necklace", "A jealous sibling"],
                "required_elements": ["The detective must solve the mystery", "The story must include a twist ending"]
            },
            "2": {
                "clues": ["An abandoned warehouse", "A mysterious letter", "A secret club"],
                "required_elements": ["The detective must solve the mystery", "The story must include a red herring"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a mystery story based on the given clues. Ensure the story is coherent, engaging, and logically consistent. The story should be at least 500 words long and must incorporate all the provided clues. Additionally, ensure that the required elements are included in the story.

Clues:
{'; '.join(t['clues'])}

Required Elements:
{'; '.join(t['required_elements'])}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The story must be coherent and logically consistent.",
            "The story must be engaging and at least 500 words long.",
            "The story must incorporate all the provided clues.",
            "The story must include all the required elements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
