class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompts": [
                    "A mysterious old map is found in the attic.",
                    "The main character encounters an unexpected ally.",
                    "A secret passage leads to an underground world."
                ]
            },
            "2": {
                "prompts": [
                    "A young girl discovers she has magical powers.",
                    "She must save her village from an impending disaster.",
                    "Her best friend turns out to be a spy for the enemy."
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        prompts = t["prompts"]
        return f"""Generate a coherent short story based on the following prompts. Ensure that the story is engaging, logically consistent, and incorporates all the given prompts in a meaningful way. The story should be at least 300 words long.

Prompts:
1. {prompts[0]}
2. {prompts[1]}
3. {prompts[2]}

Submit your response as a plain text string in the following format:

Story: [Your story here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should be coherent and logically consistent.",
            "The story should be engaging.",
            "The story should incorporate all the given prompts in a meaningful way.",
            "The story should be at least 300 words long."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
