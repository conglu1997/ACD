class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "tech_description": "A wearable device that can read and interpret human emotions in real-time, providing feedback to the user through a mobile application.",
            },
            "2": {
                "tech_description": "A drone equipped with advanced AI and sensors, capable of autonomous navigation in dense urban environments for delivering small packages.",
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate an innovative use case for the following fictional technology based on its description:

Technology Description:
{t['tech_description']}

Ensure your use case is practical, detailed, and demonstrates a clear understanding of the technology's potential applications. Submit your use case as a plain text string in the following format:

Use Case: [Your use case]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The use case should be innovative and practical.",
            "The use case should demonstrate a clear understanding of the technology's potential applications.",
            "The use case should be detailed and well-articulated."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
