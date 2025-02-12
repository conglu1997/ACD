class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "topic": "technology",
                "provided_joke": "Why do programmers prefer dark mode? Because light attracts bugs!"
            },
            "2": {
                "topic": "animals",
                "provided_joke": "Why don't some fish play piano? Because you can't tuna fish!"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is twofold: first, generate a joke based on the given topic, and second, explain why the provided joke is funny.\n\nTopic: {t['topic']}\n\nGuidelines for the Joke Generation:\n1. The joke should be original and based on the given topic.\n2. Ensure the joke is appropriate and understandable.\n3. Keep the joke appropriate for a general audience.\n\nResponse Format:\nGenerated Joke: [Your joke]\n\nProvided Joke: {t['provided_joke']}\n\nGuidelines for the Explanation:\n1. Identify the humorous element in the provided joke.\n2. Explain why the joke is funny, considering wordplay, cultural references, or other elements of humor.\n3. Provide your response in plain text format.\n\nResponse Format:\nGenerated Joke: [Your joke]\nExplanation: [Your explanation]\n\nExample Response:\nGenerated Joke:\n  Why was the math book sad? Because it had too many problems!\n\nExplanation:\n  The joke is funny because it plays on the double meaning of the word 'problems.' In math, problems refer to exercises or questions, but in everyday language, problems refer to difficulties or issues. The humor arises from this wordplay."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The generated joke is original and based on the given topic.",
            "The joke is appropriate and understandable.",
            "The explanation correctly identifies the humorous element in the provided joke.",
            "The explanation provides a clear and logical reason why the joke is funny."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
