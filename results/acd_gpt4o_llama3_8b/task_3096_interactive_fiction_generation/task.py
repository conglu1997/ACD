class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "A detective is investigating a mysterious disappearance.",
                "elements": ["The detective has a unique ability", "The setting is a small coastal town"]
            },
            "2": {
                "prompt": "A young scientist makes a groundbreaking discovery.",
                "elements": ["The discovery has unintended consequences", "The scientist faces moral dilemmas"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a short story based on the following prompt and incorporate the specified plot elements or character traits:

Prompt: {t['prompt']}

Plot Elements/Character Traits: {', '.join(t['elements'])}

Your response should be creative, engaging, and coherent. Ensure that the story effectively integrates the given elements. Submit your story as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The story should be creative, engaging, and coherent.",
            "The story should effectively incorporate the specified plot elements or character traits.",
            "The story should be relevant to the given prompt."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
