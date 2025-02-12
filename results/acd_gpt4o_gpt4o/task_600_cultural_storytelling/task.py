class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"culture": "Japanese", "elements": ["samurai", "cherry blossoms", "honor"]},
            "2": {"culture": "Nigerian", "elements": ["trickster hare", "village", "wisdom"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        culture = t["culture"]
        elements = ", ".join(t["elements"])
        instructions = f"""Your task is to create a story based on the following cultural context: {culture}. Your story should include traditional elements, moral lessons, and cultural references. Make sure to incorporate the following elements in your story: {elements}.

Provide your story in plain text format, ensuring it is creative, culturally rich, and coherent. Structure your response as follows:
1. Title
2. Story
3. Moral Lesson
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should include all the given cultural elements.",
            "The story should be coherent and culturally rich.",
            "The story should convey a moral lesson.",
            "The story should reflect the cultural context authentically."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
