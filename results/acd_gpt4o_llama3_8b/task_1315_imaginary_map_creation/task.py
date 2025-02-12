class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "criteria": "Create an imaginary map of a fantasy island that includes the following features: a central mountain range, three rivers originating from the mountains, two forests, a coastal town, and a hidden cave. Describe each feature's location, size, and characteristics in detail."
            },
            "2": {
                "criteria": "Design an imaginary map of a futuristic city that includes the following features: a central skyscraper district, a network of elevated highways, three parks, an underground transportation system, and a residential area with public gardens. Describe each feature's location, size, and characteristics in detail."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Based on the following criteria, create an imaginary map and provide a detailed description of it. Your description should include the placement, size, and characteristics of each feature mentioned in the criteria. Ensure that your description is coherent, vivid, and logically consistent.

Criteria: {t['criteria']}

Submit your description as a plain text string with the following format:

Map Description:
[Your description here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should include all specified features.",
            "The placement, size, and characteristics of the features should be described clearly and logically.",
            "The overall description should be coherent, vivid, and creative."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0