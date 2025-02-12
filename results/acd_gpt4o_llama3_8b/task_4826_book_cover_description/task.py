class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "cover_description": "A dark forest with tall, dense trees. In the center, a glowing orb hovers above a stone pedestal. The title 'The Enchanted Grove' is written in elegant, gold script at the top. The background is a deep, twilight blue with hints of mist floating around the trees."
            },
            "2": {
                "cover_description": "A bustling medieval marketplace with various stalls selling colorful goods. In the foreground, a young woman in a hooded cloak looks over her shoulder, revealing a hidden dagger at her side. The title 'The Hidden Merchant' is displayed in bold, rustic font at the bottom. The sky is a vibrant sunset orange, casting long shadows over the marketplace."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Based on the provided description of a fictional book cover, generate an imaginative and detailed narrative that could fit as the back cover blurb for the book. Ensure your narrative includes:
1. A brief plot summary.
2. Key characters and their roles.
3. The central conflict or mystery.

Your response should be engaging, coherent, and relevant to the given cover description. Submit your response as a plain text string in the following format:

Response: [Your narrative here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The narrative should be relevant to the described book cover.",
            "The response should include a brief plot summary.",
            "The response should introduce key characters and their roles.",
            "The response should describe the central conflict or mystery."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
