class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Design a map layout for a small medieval village. The village should include the following elements: a central marketplace, a church to the north of the marketplace, a river running from the east to the west on the southern edge of the village, five cottages scattered around the marketplace, a blacksmith's forge to the west of the marketplace, and a small forest to the east of the village."},
            "2": {"description": "Design a map layout for a science fiction space station. The station should include the following elements: a central command center, a docking bay to the north of the command center, residential quarters to the west, an engineering bay to the east, a medical bay to the south, and a recreational area adjacent to the residential quarters."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to design a map layout based on the following description:

{t['description']}

Create a detailed textual description of your map layout. Ensure that the placement of each element is clear and logical based on the given description. Your response should be well-structured and easy to follow. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The layout should include all the specified elements.",
            "The placement of each element should be logical based on the description.",
            "The layout should be clear, well-structured, and easy to follow."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
