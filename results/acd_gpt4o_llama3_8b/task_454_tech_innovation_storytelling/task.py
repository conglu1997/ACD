class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "title": "Future Home Technology",
                "requirements": "Write a fictional story set in the near future where a new home automation system revolutionizes daily living. Describe the functionalities of the system in detail and integrate it into a coherent narrative that highlights its impact on the characters' lives."
            },
            "2": {
                "title": "Space Exploration Gadget",
                "requirements": "Write a fictional story about an interstellar mission that utilizes a newly invented gadget to overcome challenges in space. Describe the gadget's functionalities in detail and weave it into a compelling narrative that showcases its importance to the mission's success."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a fictional story based on the following title and requirements:

Title: {t['title']}

Requirements: {t['requirements']}

Your response should include a detailed description of the technological innovation, its functionalities, and a coherent narrative that demonstrates its integration into the story. Submit your story as a plain text string with the following sections:

1. Innovation Description: [Describe the technological innovation and its functionalities]
2. Narrative: [Write a fictional story that integrates the innovation into the plot]

Example Format:

Innovation Description: [Your description here]
Narrative: [Your narrative here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The story should include a detailed and plausible description of the technological innovation.",
            "The narrative should coherently integrate the innovation into the plot.",
            "The story should be creative and engaging."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
