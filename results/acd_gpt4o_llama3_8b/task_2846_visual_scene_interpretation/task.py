class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scene_description": "A bustling city square at noon. People are walking in all directions, some carrying shopping bags, others talking on phones. A street performer is playing the violin near a fountain. There are pigeons pecking at crumbs on the ground, and children chasing after them. Tall buildings surround the square, with windows reflecting the bright sunlight. A food cart to the left sells hot dogs, and a line of people is waiting to be served."
            },
            "2": {
                "scene_description": "A serene beach at sunset. The sky is painted with hues of orange, pink, and purple. The waves gently lap against the shore, and a few seagulls are flying overhead. A couple is walking hand in hand along the water's edge, leaving footprints in the wet sand. In the distance, a sailboat is gliding across the water, its sails catching the last light of the day. Palm trees sway gently in the breeze, and a beach bar to the right has a few patrons enjoying drinks under straw umbrellas."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Based on the following scene description, generate a coherent and accurate written description or story that captures the essence of the scene.

Scene Description: {t['scene_description']}

Your response should be vivid and detailed, accurately portraying the visual elements and atmosphere of the scene. Submit your response as a plain text string in the following format:

Description: [Your description here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The response should be vivid and detailed.", "The response should accurately portray the visual elements of the scene.", "The response should capture the atmosphere of the scene."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
