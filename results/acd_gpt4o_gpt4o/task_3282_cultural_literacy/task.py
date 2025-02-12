class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "An image of a man standing in front of a crowd, making a speech. The background shows a large building with columns, and there are signs in the crowd that read 'I Have a Dream'. This event took place during the Civil Rights Movement in the United States."
            },
            "2": {
                "description": "A text description: 'A significant event in American history where women gathered in 1848 to discuss their rights and draft a declaration demanding equality. This event marked the beginning of the women's suffrage movement in the United States.'"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to identify and explain the significance of the historical or cultural event based on the following description:\n\n{t['description']}\n\nEnsure that your explanation includes relevant historical context, the key figures involved, and the impact of the event. Provide your response in plain text format with a length of at least 150 words. Your response should be in the following format:\n\nIdentification: [Name of the Event]\nExplanation: [Detailed Explanation]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should correctly identify the historical or cultural event.",
            "The explanation should include relevant historical context, key figures involved, and the impact of the event.",
            "The response should be at least 150 words long.",
            "The response should be in the format: Identification: [Name of the Event] Explanation: [Detailed Explanation]."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
