class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "statement": "Climate change is the most critical issue of our time, and immediate action is necessary to mitigate its effects.",
                "topic": "renewable energy"
            },
            "2": {
                "statement": "Education is the foundation of a prosperous society, and investing in education benefits everyone.",
                "topic": "universal healthcare"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the given persuasive statement and generate a new, compelling argument on the specified topic.

Statement: {t['statement']}
Topic: {t['topic']}

Your response should include:
1. An analysis of the given statement, explaining its main points and persuasive techniques used.
2. A new persuasive argument on the specified topic, utilizing effective rhetorical strategies.

Example response format:
- Analysis: The statement 'Climate change is the most critical issue of our time, and immediate action is necessary to mitigate its effects.' emphasizes the urgency and severity of climate change, appealing to the audience's sense of responsibility and fear of future consequences.
- New Argument: Renewable energy is not only essential for reducing greenhouse gas emissions but also for creating sustainable economic growth and energy independence. Investing in renewable energy sources like solar and wind power can lead to job creation, technological innovation, and a cleaner environment.

Ensure your analysis is thorough and your new argument is persuasive and well-structured. Submit your response as a plain text string in the following format:
- Analysis: [Your analysis here]
- New Argument: [Your new argument here]

Make sure to follow the specified format exactly and provide a compelling argument using effective rhetorical techniques."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The analysis should accurately capture the main points and persuasive techniques of the given statement.",
            "The new argument should be compelling and relevant to the specified topic.",
            "The response should follow the specified format precisely.",
            "The new argument should demonstrate logical reasoning and effective use of rhetorical strategies.",
            "The new argument should be original and insightful."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
