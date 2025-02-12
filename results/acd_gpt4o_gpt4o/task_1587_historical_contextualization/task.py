class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "Write a letter from the perspective of a soldier during World War I.", "type": "historical_letter"},
            "2": {"task": "Describe a day in the life of a merchant in ancient Rome.", "type": "historical_narrative"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['type'] == 'historical_letter':
            return f"""Your task is to write a letter from the perspective of a soldier during World War I. The letter should be historically accurate and reflect the experiences, emotions, and language of the time. Ensure that the letter is coherent and contextually appropriate.

Write your letter in plain text format. Provide your response in the following format:

- Date: [Your answer]
- Greeting: [Your answer]
- Body: [Your answer]
- Closing: [Your answer]"""
        elif t['type'] == 'historical_narrative':
            return f"""Your task is to describe a day in the life of a merchant in ancient Rome. The narrative should be historically accurate and reflect the daily activities, challenges, and environment of the time. Ensure that the narrative is engaging, coherent, and contextually appropriate.

Write your narrative in plain text format. Provide your response in the following format:

- Morning: [Your answer]
- Afternoon: [Your answer]
- Evening: [Your answer]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The content should be historically accurate.", "The submission should be contextually appropriate and coherent.", "The format should follow the provided structure."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
