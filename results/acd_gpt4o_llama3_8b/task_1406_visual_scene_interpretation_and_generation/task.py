class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scene_description": "You are in a lush, green forest. Tall trees with thick canopies block most of the sunlight, creating a cool, shaded environment. In the distance, you hear the sound of a babbling brook. There is a small clearing with a wooden bench and a colorful array of wildflowers. Interpret this scene and describe the emotions it evokes and potential activities one might engage in."
            },
            "2": {
                "scene_elements": ["A bustling city street", "Neon lights", "Rain-soaked pavement", "People with umbrellas", "A street musician playing a saxophone"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "scene_description" in t:
            return f"""Interpret the following visual scene based on the detailed description provided:

Scene Description: '{t['scene_description']}'

Ensure that your interpretation includes the emotions the scene evokes and potential activities one might engage in within this scene. Submit your response as a plain text string in the following format:

Interpretation: [Your interpretation]"""
        else:
            return f"""Generate a detailed description of a visual scene based on the specified elements:

Scene Elements: {', '.join(t['scene_elements'])}

Ensure that your description is vivid, evocative, and captures the essence of each element. Submit your response as a plain text string in the following format:

Description: [Your description]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "scene_description" in t:
            validation_criteria = [
                "The interpretation must accurately reflect the emotions evoked by the scene.",
                "The interpretation must suggest potential activities relevant to the scene."]
        else:
            validation_criteria = [
                "The description must be vivid and evocative.",
                "The description must appropriately capture the essence of each specified element."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
