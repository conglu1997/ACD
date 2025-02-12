class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"text": "I can't believe it! After all this hard work, I finally got the promotion I've been dreaming about. I'm over the moon!"},
            "2": {"text": "I don't know how much longer I can keep doing this. Every day feels like a struggle and I'm constantly exhausted. It's like I'm stuck in a never-ending cycle of despair."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return "Your task is to analyze the given text and identify the underlying sentiment and emotional tone conveyed by the author. Your analysis should include a brief summary of the text, the identified sentiment (e.g., positive, negative, neutral), and the specific emotional tones (e.g., joy, sadness, anger, etc.). Format your response as follows:\n\n1. Summary: [Your brief summary of the text]\n2. Sentiment: [Identified sentiment]\n3. Emotional Tones: [Identified emotional tones]\n\nText: {text}".format(text=t["text"])

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The analysis should include a brief summary of the text, the identified sentiment, and the specific emotional tones."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
