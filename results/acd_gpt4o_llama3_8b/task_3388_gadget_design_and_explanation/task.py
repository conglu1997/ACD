class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"requirement": "Design a gadget that can help people find their lost keys easily."},
            "2": {"description": "The gadget is a small, circular device that can be attached to a keyring. It has a button and a small speaker. When the button is pressed, the device emits a loud beeping sound. It also has a Bluetooth module that can be connected to a smartphone app, allowing the user to locate the keys on a map."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "requirement" in t:
            return f"""Design a novel gadget based on the following functional requirement. Your design should include a detailed description of the gadget's appearance, components, and how it works to fulfill the requirement. Ensure that your description is clear and comprehensive. Submit your design as a plain text string.

Functional Requirement: {t["requirement"]}"""
        elif "description" in t:
            return f"""Explain the functionality of the described gadget. Your explanation should include how the gadget works, the purpose of its components, and how it fulfills its intended function. Ensure that your explanation is clear and detailed. Submit your explanation as a plain text string.

Gadget Description: {t["description"]}"""
        return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if "requirement" in t:
            criteria = ["The gadget design should clearly describe the appearance and components.", "The design should explain how the gadget works to fulfill the requirement.", "The description should be clear and comprehensive."]
        elif "description" in t:
            criteria = ["The explanation should clearly describe how the gadget works.", "The explanation should detail the purpose of each component.", "The explanation should be clear and detailed."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
