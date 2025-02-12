class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"practice": "Diwali, the Festival of Lights celebrated in India."},
            "2": {"practice": "The Japanese Tea Ceremony."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret and explain the following cultural practice. Provide a detailed explanation that includes the historical context, significance, and any relevant rituals or customs associated with it. Here is the cultural practice:\n\n{t['practice']}\n\nSubmit your solution in plain text format. Your response should include:\n1. An introduction to the practice.\n2. Historical background and origins.\n3. Significance of the practice in the culture.\n4. Description of any rituals or customs associated with the practice.\n5. Any interesting facts or additional information."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The explanation should be detailed and accurate.", "The historical context should be well-researched.", "The significance of the practice should be clearly explained.", "The description of rituals or customs should be comprehensive.", "Any additional information should be relevant and interesting."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
