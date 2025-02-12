class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "text": "I often find myself overwhelmed by the demands of everyday life. The constant pressure to succeed drains my energy, and I feel like I'm losing touch with my true self. Despite my accomplishments, I can't shake the feeling of inadequacy. I yearn for a simpler time when my happiness wasn't tied to my achievements."
            },
            "2": {
                "text": "I've always been the life of the party, but lately, I've been feeling disconnected. My friends say I'm the glue that holds our group together, yet I can't help but feel like an outsider. I put on a brave face, but deep down, I'm struggling to find genuine connections. My extroverted nature masks the loneliness I feel inside."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the given text to infer the psychological profile of the author. Your analysis should include:
1. Identification of key personality traits.
2. Description of the author's emotional states.
3. Possible motivations behind the author's feelings and behavior.

Text: {t['text']}

Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The analysis should identify key personality traits of the author.",
            "The analysis should describe the emotional states of the author.",
            "The analysis should infer possible motivations behind the author's feelings and behavior.",
            "The analysis should be coherent and well-structured.",
            "The analysis should show depth and insight into the author's psychological profile."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
