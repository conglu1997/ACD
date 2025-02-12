class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"topic": "time"},
            "2": {"topic": "love"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given topic:

Topic: {t['topic']}

Generate a metaphorical description or explanation for the given topic. Your metaphor should be creative, coherent, and effectively convey the essence of the topic through the use of metaphorical language. Ensure that your metaphor is original and demonstrates a deep understanding of the topic.

Submit your response as a plain text string in the following format:
Metaphor: [Your metaphor]

Example Response:
Metaphor: Time is a relentless river, flowing endlessly towards the horizon, carrying us along its currents, never to return to the same moment twice."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The metaphor should be creative and original.",
            "The metaphor should effectively convey the essence of the given topic.",
            "The metaphor should be coherent and make logical sense.",
            "The metaphor should demonstrate a deep understanding of the topic."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
