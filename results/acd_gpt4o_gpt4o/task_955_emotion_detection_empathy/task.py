class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"text": "I just lost my job today and I don't know how I will pay my bills. I feel completely hopeless."},
            "2": {"text": "I finally graduated after years of hard work and dedication. I'm so proud of myself and excited for the future."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return """You are provided with a short text conveying an emotion. Your task is to perform the following:
1. Identify the primary emotion conveyed in the text (e.g., sadness, joy, anger, etc.).
2. Generate an empathetic response that acknowledges the identified emotion and offers support or encouragement.

Text:
{t['text']}

Example response format:
1. Emotion: [Identified emotion]
2. Empathetic Response: [Your empathetic response here]

Example 1:
Text: 'I just lost my job today and I don't know how I will pay my bills. I feel completely hopeless.'
1. Emotion: Sadness
2. Empathetic Response: I'm really sorry to hear that you're going through this. It's completely understandable to feel hopeless in this situation, but please know that there are resources and people who can help you through this tough time.

Example 2:
Text: 'I finally graduated after years of hard work and dedication. I'm so proud of myself and excited for the future.'
1. Emotion: Joy
2. Empathetic Response: Congratulations on your achievement! It's wonderful to see all your hard work paying off, and your excitement for the future is truly inspiring. Wishing you all the best in your next steps!

Ensure that your identified emotion accurately reflects the text and your empathetic response is appropriate and supportive."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The identified emotion should accurately reflect the primary emotion conveyed in the text.",
            "The empathetic response should be appropriate, supportive, and acknowledge the identified emotion."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
