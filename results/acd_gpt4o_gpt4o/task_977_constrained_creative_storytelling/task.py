class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "opening_sentence": "On a cold winter's night, Alex discovered a hidden door in the attic.",
                "constraints": ["The story must include a talking animal.", "The story must end with a surprising twist."]
            },
            "2": {
                "opening_sentence": "As the sun set over the horizon, Jamie found an old map tucked inside an ancient book.",
                "constraints": ["The story must involve a time travel element.", "The story must have a moral lesson at the end."]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to write a short story based on the following opening sentence and constraints.

Opening Sentence: {t['opening_sentence']}

Constraints: {', '.join(t['constraints'])}

Ensure your story is creative, coherent, and adheres to all the given constraints. The story should be at least 300 words long and written in plain text format.

Response Format:
Your response should be a single continuous narrative in plain text format, without any additional headings or sections.

**Important Note:** Make sure to strictly follow the constraints provided. Stories that do not adhere to the constraints will not be considered successful.

Example Response:
"On a cold winter's night, Alex discovered a hidden door in the attic. To his surprise, a talking cat emerged from the door, claiming to be a wizard from another realm. Alex and the cat embarked on a thrilling adventure, uncovering secrets about Alex's family. In the end, it was revealed that the talking cat was actually Alex's long-lost brother, transformed by a curse, which Alex managed to break." [continue the story adhering to the constraints]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story must start with the given opening sentence.",
            "The story must include all specified constraints.",
            "The story must be creative and coherent.",
            "The story must be at least 300 words long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
