class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "plan", "scenario": "launching a new tech product", "criteria": "The plan should include a market analysis, target audience identification, marketing strategy, and an action plan."},
            "2": {"task_type": "evaluate", "plan": "1. Conduct market research to identify potential competitors and customer needs. 2. Define the target audience and create customer personas. 3. Develop a marketing strategy that includes online advertising, social media campaigns, and influencer partnerships. 4. Create an action plan with specific milestones for product development, marketing, and sales.", "question": "What are the potential risks and mitigation strategies for this plan?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "plan":
            instructions = f"""Your task is to develop a strategic business plan for the following scenario:

Scenario: {t['scenario']}

Ensure your plan includes the following components:
1. Market analysis: Provide a detailed analysis of the current market, including key competitors and customer needs.
2. Target audience identification: Define the target audience and create detailed customer personas.
3. Marketing strategy: Develop a comprehensive marketing strategy that includes online advertising, social media campaigns, and influencer partnerships.
4. Action plan: Create a detailed action plan with specific milestones for product development, marketing, and sales.

Provide your strategic business plan in plain text format, with each component clearly labeled. For example:

1. Market Analysis: [Your market analysis]
2. Target Audience: [Your target audience identification]
3. Marketing Strategy: [Your marketing strategy]
4. Action Plan: [Your action plan]"""
        else:
            instructions = f"""Your task is to evaluate the following strategic business plan and answer the question based on the information provided:

Plan: {t['plan']}

Question: {t['question']}

Provide your answer in plain text format, clearly identifying the potential risks and their mitigation strategies. For example:

1. Risk: [Identify the risk]
   Mitigation Strategy: [Provide the mitigation strategy]
2. Risk: [Identify the risk]
   Mitigation Strategy: [Provide the mitigation strategy]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "plan":
            criteria = ["The plan should include a detailed market analysis, target audience identification, comprehensive marketing strategy, and a detailed action plan.", "The plan should be coherent, actionable, and well-structured."]
        else:
            criteria = ["The response should correctly identify potential risks and provide appropriate mitigation strategies."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
