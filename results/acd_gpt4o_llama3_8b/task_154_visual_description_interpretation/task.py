class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "The image shows a bustling marketplace in a small town. Stalls are lined up in rows, with vendors selling various goods such as fruits, vegetables, and handmade crafts. People are walking around, some carrying bags of purchases. In the background, there is a tall clock tower that stands out against the clear blue sky. Children are playing near a fountain in the center of the market, and a street musician is playing a guitar near the entrance.",
            },
            "2": {
                "description": "The image depicts a serene beach at sunset. The sky is painted with shades of orange, pink, and purple as the sun dips below the horizon. Waves gently lap at the shore, where a few seashells and pieces of driftwood are scattered. A couple is walking hand-in-hand along the water's edge, leaving footprints in the wet sand. In the distance, a lighthouse stands on a rocky outcrop, its light beginning to shine as night approaches.",
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Based on the following detailed description of an image, generate a coherent narrative or explanation that accurately captures the scene. Ensure your narrative is detailed, vivid, and logically structured.

Description:
{t['description']}

Your narrative should be at least 150 words long and should accurately reflect the details provided in the description. Avoid adding any information that is not mentioned in the description. Submit your narrative as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The narrative should accurately reflect the details provided in the description.",
            "The narrative should be logically structured and coherent.",
            "The narrative should be at least 150 words long.",
            "The narrative should avoid adding any information that is not mentioned in the description."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
