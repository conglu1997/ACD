class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "visual_elements": [
                    "A giant floating clock with melting numbers.",
                    "A landscape with multicolored mountains and a purple sky.",
                    "A river flowing upwards towards the sky.",
                    "Transparent fish swimming through the air.",
                    "A tree with leaves made of glass that reflect the surroundings."]
            },
            "2": {
                "visual_elements": [
                    "A tree with leaves made of fire.",
                    "A cityscape with skyscrapers made of glass.",
                    "A dragon flying above the city, casting a shadow on the buildings.",
                    "Floating islands with waterfalls cascading into the void.",
                    "A sky filled with swirling galaxies and shooting stars."]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a detailed and vivid description of the following abstract visual scene based on the given visual elements:

Visual Elements:
- {t['visual_elements'][0]}
- {t['visual_elements'][1]}
- {t['visual_elements'][2]}
- {t['visual_elements'][3]}
- {t['visual_elements'][4]}

Ensure your description is at least 200 words long, engages the reader's senses, and captures the surreal and abstract nature of the scene. Use descriptive language to convey the visual elements and create a coherent and imaginative narrative. Submit your description as a plain text string in the following format:

Description: [Your detailed description here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The description should be at least 200 words long.",
            "The description should engage the reader's senses.",
            "The description should capture the surreal and abstract nature of the scene.",
            "The description should use descriptive language to convey the visual elements.",
            "The description should create a coherent and imaginative narrative."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
