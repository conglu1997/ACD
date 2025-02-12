class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"text": "I just got a promotion at work! I am so excited and happy! However, I'm also a bit nervous about the new responsibilities and leaving my current team."},
            "2": {"text": "I failed my exam. I feel really down and disappointed. I put so much effort into studying, but it wasn't enough. Now I'm worried about my future."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following tasks:

1. Detect the primary emotion(s) expressed in the given text: '{t["text"]}'. Identify the emotion(s) accurately based on the context.

2. Generate a response that reflects an understanding of the detected emotion(s) and is contextually appropriate. The response should be empathetic and supportive, considering the emotional state of the individual.

Submit your responses as a plain text string in the following format:

Emotion Detection: [Your detected emotion(s)]
Response Generation: [Your response]

Example:
Emotion Detection: Happiness, Excitement, Nervousness
Response Generation: Congratulations on your promotion! It's completely normal to feel a bit nervous about new responsibilities, but remember that you earned this opportunity through your hard work. Take it one step at a time, and don't hesitate to ask for support if you need it."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The detected emotion(s) should accurately reflect the primary emotions expressed in the text.",
            "The generated response should be empathetic, nuanced, and contextually appropriate, reflecting an understanding of the detected emotion(s)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
