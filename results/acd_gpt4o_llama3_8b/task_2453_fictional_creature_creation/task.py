import json

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "characteristics": [
                    "Has wings",
                    "Lives in the ocean",
                    "Can change color",
                    "Feeds on sunlight"
                ]
            },
            "2": {
                "characteristics": [
                    "Has multiple heads",
                    "Breathes fire",
                    "Dwells in caves",
                    "Sees in the dark"
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create and describe a fictional creature based on the following characteristics: {', '.join(t['characteristics'])}. Ensure that your description includes:

1. The creature's physical appearance.
2. Its habitat and behaviors.
3. Any unique abilities or traits it possesses.
4. How it interacts with its environment and other creatures.

Submit your response as a plain text string in the following format:

Creature Description:
[Your detailed description]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The description should include the creature's physical appearance, habitat, behaviors, unique abilities, and interactions with its environment.",
            "The description should be creative, coherent, and detailed.",
            "The submission should be well-organized and clearly written."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
