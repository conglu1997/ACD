class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Invent a device that allows humans to breathe underwater indefinitely. Incorporate an element of music into the device."},
            "2": {"prompt": "Describe a machine that can convert dreams into physical objects. Incorporate an element of light into the machine."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to invent and describe a fantastical device or concept based on the following prompt:

{t['prompt']}

Ensure your description is detailed, coherent, and imaginative. Your response should include the device's name, how it works, potential uses, and how the additional element (music/light) is incorporated. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should be detailed and coherent.",
            "The invention should be imaginative and fantastical.",
            "The response should include the device's name, how it works, potential uses, and incorporation of the additional element.",
            "The response should be in plain text format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
