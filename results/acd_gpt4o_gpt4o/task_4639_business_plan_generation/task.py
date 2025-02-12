class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "parameters": {
                    "business_type": "Online Retail",
                    "initial_investment": 100000,
                    "target_market": "Young Adults",
                    "unique_selling_proposition": "Eco-friendly products"
                }
            },
            "2": {
                "business_plan": "The business will focus on selling eco-friendly products through an online platform. The initial investment will be used to develop the website, procure inventory, and market the products to the target market of young adults. The business aims to achieve profitability within the first year by leveraging social media marketing and partnerships with influencers."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "parameters" in t:
            return f"""Your task is to generate a detailed business plan based on the following parameters:

Business Type: {t['parameters']['business_type']}
Initial Investment: ${t['parameters']['initial_investment']}
Target Market: {t['parameters']['target_market']}
Unique Selling Proposition: {t['parameters']['unique_selling_proposition']}

Your business plan should include sections on Market Analysis, Marketing Strategy, Operational Plan, Financial Projections, and Risk Analysis. Ensure that your plan is coherent, practical, and well-structured. Clearly integrate the unique selling proposition into each section of the business plan. Provide your response in plain text format with the following structure:

1. Market Analysis
2. Marketing Strategy
3. Operational Plan
4. Financial Projections
5. Risk Analysis
"""
        else:
            return f"""Your task is to analyze the feasibility of the following business plan:

{t['business_plan']}

Your analysis should include an assessment of the market potential, marketing strategy, operational plan, financial projections, and potential risks. Provide a detailed explanation of whether you think this business plan is feasible and why. Clearly evaluate the integration of the unique selling proposition into the business plan. Provide your response in plain text format with the following structure:

1. Market Potential
2. Marketing Strategy
3. Operational Plan
4. Financial Projections
5. Risk Analysis
6. Overall Feasibility
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "parameters" in t:
            criteria = [
                "The business plan includes sections on Market Analysis, Marketing Strategy, Operational Plan, Financial Projections, and Risk Analysis.",
                "The business plan is coherent, practical, and well-structured.",
                "The business plan addresses the unique selling proposition effectively.",
                "The financial projections are realistic and based on the initial investment.",
                "The risk analysis identifies potential challenges and mitigation strategies.",
                "The business plan integrates the unique selling proposition into the overall strategy effectively."
            ]
        else:
            criteria = [
                "The analysis includes an assessment of market potential, marketing strategy, operational plan, financial projections, and potential risks.",
                "The analysis provides a detailed explanation of the feasibility of the business plan.",
                "The analysis identifies strengths and weaknesses in the business plan.",
                "The overall feasibility assessment is logical and well-supported by the analysis.",
                "The analysis evaluates the integration of the unique selling proposition into the business plan."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
