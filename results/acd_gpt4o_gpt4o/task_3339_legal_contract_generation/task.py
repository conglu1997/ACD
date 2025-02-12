class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "Create a freelance contract for a graphic designer hired to create a logo. Include terms for payment, delivery timeline, and intellectual property rights."
            },
            "2": {
                "legal_text": "The party of the first part shall indemnify and hold harmless the party of the second part from any and all claims, liabilities, damages, and expenses arising from the party of the first part's use of the premises."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "scenario" in t:
            return (
                "Your task is to generate a legal contract based on the following scenario. "
                "Ensure the contract is clear, precise, and covers all necessary legal terms relevant to the scenario. "
                "Include sections for Payment Terms, Delivery Timeline, and Intellectual Property Rights. "
                "Provide the contract in plain text format."
                f'\n\nScenario: {t["scenario"]}'
            )
        elif "legal_text" in t:
            return (
                "Your task is to translate the following legal text into plain English. "
                "Ensure that the translation is accurate and conveys the same meaning as the original legal text. "
                "Provide your translation in plain text format."
                f'\n\nLegal Text: {t["legal_text"]}'
            )
        return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if "scenario" in t:
            criteria = [
                "The contract should be clear, precise, and cover all necessary legal terms relevant to the scenario.",
                "The format should be consistent with standard legal contracts.",
                "The contract should include sections for Payment Terms, Delivery Timeline, and Intellectual Property Rights."
            ]
        elif "legal_text" in t:
            criteria = [
                "The translation should be accurate and convey the same meaning as the original legal text.",
                "The translation should use simple and clear language."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
