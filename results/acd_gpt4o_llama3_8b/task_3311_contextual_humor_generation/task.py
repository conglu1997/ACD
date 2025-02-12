class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "context": "A job interview for a position as a software engineer.",
                "elements": ["a pun about coding", "a reference to a popular tech company"]
            },
            "2": {
                "context": "A speech at a wedding reception.",
                "elements": ["a joke about marriage", "a reference to a famous love story"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a humorous response based on the following context and elements:

Context:
{t['context']}

Ensure that your response includes the following elements:
- {t['elements'][0]}
- {t['elements'][1]}

The response should be contextually appropriate, genuinely funny, and make sense within the given scenario. Submit your response as a plain text string in the following format:

Humorous Response:
[Your response here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should include all specified elements.",
            "The response should be contextually appropriate.",
            "The response should be genuinely funny."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
