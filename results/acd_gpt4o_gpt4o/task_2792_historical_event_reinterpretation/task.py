class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "event": "The signing of the Declaration of Independence in 1776.",
                "alternative_scenario": "What if the Declaration of Independence was never signed?"
            },
            "2": {
                "event": "The fall of the Berlin Wall in 1989.",
                "alternative_scenario": "What if the Berlin Wall had never fallen?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task involves two parts:\n\n1. Accurately recount the historical event provided. Include key details such as dates, major figures involved, and the significance of the event.\n\nEvent: {t['event']}\n\n2. Creatively reinterpret or create an alternative history scenario based on the provided prompt. Ensure that your reinterpretation is coherent and logically explores the implications of the scenario.\n\nAlternative Scenario: {t['alternative_scenario']}\n\nProvide your response in plain text format, structured as follows:\n\n1. Historical Account: [Your recounting of the event]\n2. Alternative Scenario: [Your creative reinterpretation]\n\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The historical account should be accurate and include key details.",
            "The alternative scenario should be coherent and logically explore the implications of the scenario.",
            "The response should demonstrate a clear understanding of the historical context."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
