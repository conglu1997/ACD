class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "A lost treasure in a modern city", "constraints": "The story must include a mysterious map, a talking animal, and a surprising twist."},
            "2": {"theme": "An unexpected friendship in space", "constraints": "The story must involve a malfunctioning spaceship, an alien species, and a heartfelt conversation."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a short story based on the given theme and constraints. The story should be coherent, creative, and adhere to the specified guidelines.

Theme:
{t['theme']}

Constraints:
{t['constraints']}

Provide your story below. Your response should include:
1. A clear and engaging narrative.
2. Adherence to the given theme and constraints.
3. Coherent and logical progression of events.
4. Original and creative elements that enhance the overall story."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The story should adhere to the given theme and constraints.", "The narrative should be clear and engaging.", "The progression of events should be coherent and logical.", "The story should include original and creative elements that enhance the overall narrative."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
