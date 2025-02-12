class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "context": "A customer is calling a tech support representative to resolve an issue with their internet connection.",
                "constraints": "The tech support representative must remain polite and professional throughout, and must mention checking the router, restarting the modem, and scheduling a technician visit if the issue persists. The dialogue should be between 8-12 lines long."
            },
            "2": {
                "context": "Two friends are discussing their plans for the weekend.",
                "constraints": "The dialogue must include a mention of going to the beach, trying a new restaurant, and one friend expressing concern about the weather. The dialogue should be between 8-12 lines long."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a coherent and contextually appropriate dialogue based on the given context and constraints:

Context: {t['context']}
Constraints: {t['constraints']}

Ensure that the dialogue is natural, follows the context, and adheres to the specified constraints. Submit your response as a plain text string in the following format:

[Dialogue]

Example format:
Customer: Hi, I'm having trouble with my internet connection.
Tech Support: I'm sorry to hear that. Have you tried checking the router?
Customer: Yes, I have. It still doesn't work.
Tech Support: Let's try restarting the modem. If that doesn't help, we can schedule a technician visit.
Customer: I'll restart the modem now.
Tech Support: Please let me know if it works.
Customer: It's still not working.
Tech Support: I'll schedule a technician to visit your place."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The dialogue should be coherent and contextually appropriate.",
            "The dialogue should adhere to the specified constraints.",
            "The tone and style of the dialogue should match the given context.",
            "The dialogue should be between 8-12 lines long."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
