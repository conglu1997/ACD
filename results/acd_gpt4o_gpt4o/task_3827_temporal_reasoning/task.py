class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"text": "John started working at the company on January 1, 2010. He was promoted to manager on June 1, 2015. He left the company on December 31, 2020.", "questions": ["How many years did John work at the company?", "How long was John a manager?"]},
            "2": {"text": "Alice's flight was scheduled to depart at 3:00 PM, but it was delayed by 2 hours. She arrived at her destination 5 hours after departure. Her friend, Bob, picked her up 30 minutes after she arrived.", "questions": ["What time did Alice's flight actually depart?", "What time did Bob pick Alice up?"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to extract and reason about temporal information from the given text to answer the questions accurately.

Text:
{t['text']}

Questions:
1. {t['questions'][0]}
2. {t['questions'][1]}

Instructions:
1. Read the text carefully.
2. Extract relevant temporal information.
3. Use the extracted information to answer the questions accurately.
4. Provide detailed reasoning for your answers.

Your response should be in the following format:
Answers:
1. [Answer to question 1]
Reasoning: [Detailed reasoning for question 1]

2. [Answer to question 2]
Reasoning: [Detailed reasoning for question 2]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The answers should be accurate based on the temporal information in the text.", "The reasoning should be detailed and logically sound."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
