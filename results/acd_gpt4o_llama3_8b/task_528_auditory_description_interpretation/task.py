class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "You hear the sound of waves crashing against the shore, seagulls calling in the distance, and children laughing and playing in the sand. There is also the faint sound of an ice cream truck's jingle in the background, and the rustling of palm trees in the breeze."},
            "2": {"description": "You hear the sounds of a bustling city street: car horns honking, people chatting as they walk by, a street musician playing a lively tune on a saxophone, the distant siren of an ambulance, and the rhythmic clatter of a subway train passing below."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Based on the following auditory description, generate a coherent narrative or explanation that accurately captures the scene. Ensure your narrative is detailed, vivid, and logically structured.

Auditory Description:
{t['description']}

Your narrative should be at least 150 words long and should accurately reflect all the auditory details provided in the description. Avoid adding any information that is not mentioned in the description. Submit your narrative as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The narrative should be detailed and vivid.",
            "The narrative should accurately reflect all the auditory details provided.",
            "The narrative should be logically structured.",
            "The narrative should be at least 150 words long.",
            "The narrative should avoid adding any information not mentioned in the description."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
