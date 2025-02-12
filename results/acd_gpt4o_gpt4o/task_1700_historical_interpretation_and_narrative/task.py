class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Interpret the significance of the fall of the Berlin Wall in 1989 and its impact on global politics."},
            "2": {"prompt": "Write a historical narrative about the journey of Christopher Columbus in 1492, focusing on his motivations, experiences, and the consequences of his voyage."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret the following historical event or draft a historical narrative based on the given prompt:\n\n{t['prompt']}\n\nEnsure that your response is historically accurate, well-structured, and provides a comprehensive analysis or narrative. Provide your response in plain text format. Structure your response as follows:\n1. Introduction: [Your introduction]\n2. Main Body: [Your main body]\n3. Conclusion: [Your conclusion]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should be historically accurate.", "The response should be well-structured and comprehensive."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
