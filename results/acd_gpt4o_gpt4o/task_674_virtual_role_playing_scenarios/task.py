class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are the CEO of a company facing a major PR crisis. A product your company released has been found to have a serious defect, causing harm to users. You need to decide on a course of action to address the issue and mitigate damage to the company's reputation. Consider aspects such as public statements, product recalls, and internal investigations. Additionally, your decision must take into account the financial impact, legal implications, and the company's long-term strategy."},
            "2": {"scenario": "You are a diplomat tasked with negotiating a peace treaty between two warring nations. Both sides have been in conflict for years, with deep-seated grievances and a history of failed negotiations. Your goal is to propose a peace plan that addresses key issues for both sides and fosters long-term stability. Consider aspects such as territorial disputes, economic cooperation, and cultural exchanges. Additionally, your proposal must consider the interests of international stakeholders, historical context, and potential future conflicts."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to engage in the following virtual role-playing scenario and make decisions based on the given context. After making your decisions, provide detailed reasoning behind each decision.

Scenario: {t['scenario']}

Your response should be detailed and cover the following aspects:
1. Key decisions you make in the scenario.
2. Detailed reasoning behind each decision, considering various factors.
3. Potential outcomes and implications of your decisions.
4. Possible challenges and how you plan to address them.

Provide your response in plain text format without additional formatting. Ensure your decisions are well thought out, realistic, and consider the various factors involved in the scenario. Structure your response as follows:

- Key Decisions: [Your decisions]
- Reasoning: [Your detailed reasoning behind each decision]
- Potential Outcomes: [The potential outcomes and implications of your decisions]
- Challenges: [Possible challenges and how you plan to address them]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should include key decisions.", "The reasoning behind each decision should be detailed and logical.", "The potential outcomes should be realistic and consider various factors.", "The response should address possible challenges and how to address them.", "The response should be clear and well-structured."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
