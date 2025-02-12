class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "genre": "mystery",
                "structure": "The story must start with a crime being discovered, followed by an investigation, and end with the resolution of the crime."
            },
            "2": {
                "genre": "science fiction",
                "structure": "The story must begin with a scientific breakthrough, followed by an unexpected consequence, and end with a resolution that highlights a lesson learned from the experience."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Write a story in the {t['genre']} genre that adheres to the following structure:

Structure: {t['structure']}

Ensure your story is coherent, engaging, and follows the given structural guidelines. Your story should be at least 300 words long and should clearly reflect the genre and structure specified. Submit your story as a plain text string.

Example:

Genre: Fantasy
Structure: The story must start with a prophecy, followed by a quest, and end with the fulfillment of the prophecy.

Story:
Once upon a time, in a land far away, a prophecy was foretold about a young hero who would embark on a quest to save the kingdom. The hero, guided by a wise old mentor, faced numerous challenges and adversaries. Along the journey, the hero discovered inner strength and wisdom. In the end, the hero's courage and determination led to the fulfillment of the prophecy, bringing peace and prosperity to the realm. The trials and tribulations faced by the hero not only showcased bravery but also the importance of wisdom and perseverance."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The story should be coherent and engaging.",
            "The story should adhere to the given structural guidelines.",
            "The story should reflect the specified genre.",
            "The story should be at least 300 words long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
