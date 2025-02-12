class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"lyrics": "Is this the real life? Is this just fantasy? Caught in a landslide, no escape from reality.", "theme": "dreams vs. reality"},
            "2": {"lyrics": "Imagine all the people living life in peace. You may say I'm a dreamer, but I'm not the only one.", "theme": "world peace"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following tasks based on the given prompts:

1. Interpret the meaning of the following song lyrics:

Lyrics: {t['lyrics']}

Provide a detailed interpretation of the meaning or message conveyed by the lyrics. Your interpretation should be insightful and consider both literal and metaphorical meanings.

2. Generate new song lyrics based on the following theme: {t['theme']}

Ensure that the lyrics are coherent, contextually appropriate, and capture the essence of the given theme. Submit your response as a plain text string with the following sections:
1. Interpretation: [Your interpretation]
2. Generated Lyrics: [Your new song lyrics]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a detailed and insightful interpretation of the song lyrics.",
            "The interpretation should consider both literal and metaphorical meanings.",
            "The generated lyrics should be coherent and contextually appropriate.",
            "The generated lyrics should capture the essence of the given theme."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
