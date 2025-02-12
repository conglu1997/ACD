class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "event": "The American Revolution",
                "hypothetical_change": "What if the colonies had lost the Battle of Saratoga?"
            },
            "2": {
                "event": "The fall of the Roman Empire",
                "hypothetical_change": "What if Julius Caesar had never been assassinated?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Your task is to simulate an alternative historical scenario based on the following hypothetical change to a key historical event. Describe how this change could have altered the course of history, including potential political, social, and economic impacts. Ensure your response is coherent, logical, and historically plausible.\n\nHistorical Event: {t['event']}\nHypothetical Change: {t['hypothetical_change']}\n\nProvide your response in plain text format."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should be coherent and historically plausible.",
            "The response should address potential political, social, and economic impacts.",
            "The response should logically follow from the hypothetical change."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
