class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "role": "CEO of a tech startup",
                "scenario": "Your company is negotiating a partnership with a larger corporation. The larger corporation wants a 40% stake in your company in exchange for a significant investment. Your goal is to negotiate a deal that minimizes the stake given away while still securing the investment."
            },
            "2": {
                "role": "Union representative",
                "scenario": "You are negotiating with the management of a large manufacturing company for better working conditions and higher wages for the workers. The management is willing to improve working conditions but is hesitant to increase wages significantly. Your goal is to negotiate the best possible outcome for the workers while avoiding a strike."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Engage in the following strategic negotiation scenario. Take on the specified role and aim to achieve the best possible outcome. Consider the perspectives of all parties involved and use strategic thinking and negotiation skills to reach a favorable agreement.

Role: {t['role']}

Scenario: {t['scenario']}

Your response should include the following sections:
1. Initial Strategy: Outline your initial approach to the negotiation, including your primary goals and any concessions you are willing to make.
2. Negotiation Process: Describe the key steps and tactics you would use during the negotiation, including any counteroffers or compromises.
3. Final Outcome: Summarize the final agreement you aimed to achieve and explain why it is the best possible outcome given the scenario.

Submit your response as a plain text string with the sections clearly labeled."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The initial strategy should be clearly outlined with primary goals and concessions.", "The negotiation process should include key steps and tactics, including any counteroffers or compromises.", "The final outcome should be summarized and justified as the best possible agreement given the scenario."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
