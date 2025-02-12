class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "concept": "Black Holes",
                "age_group": "8-10"
            },
            "2": {
                "concept": "Photosynthesis",
                "age_group": "6-8"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to explain the following scientific concept in a way that is easily understandable for children in the specified age group:\n\nConcept: {t['concept']}\nAge Group: {t['age_group']}\n\nYour explanation should adhere to the following guidelines:\n1. Use simple language and avoid technical jargon.\n2. Make the explanation engaging and relatable for the age group.\n3. Ensure that the explanation is accurate and informative.\n\nProvide your response in plain text format.\n\nExample Response:\nFor the concept of rain for ages 6-8: 'Rain happens when water droplets in the clouds get too heavy and fall down to the ground like tiny drops. This helps plants grow and keeps everything green!'"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation uses simple language and avoids technical jargon.",
            "The explanation is engaging and relatable for the specified age group.",
            "The explanation is accurate and informative."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
