class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "system_description": "A web application for online shopping, including user authentication, product catalog, shopping cart, and payment processing."
            },
            "2": {
                "system_description": "A machine learning pipeline for image classification, including data collection, preprocessing, model training, evaluation, and deployment."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        system_description = t["system_description"]
        return f"""Analyze and describe the architecture of the given technical system. Your description should include:

1. The main components of the system.
2. The interactions between the components.
3. Key design principles and patterns used.
4. Any potential challenges or considerations in the design.

System Description: {system_description}

Submit your response as a plain text string in paragraph format, ensuring that your analysis is clear, detailed, technically accurate, and comprehensive."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should include all main components of the system.", "The interactions between the components should be clearly described.", "Key design principles and patterns should be identified.", "Potential challenges or considerations should be mentioned.", "The response should be technically accurate and comprehensive."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
