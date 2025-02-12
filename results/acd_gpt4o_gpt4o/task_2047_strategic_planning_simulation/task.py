class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are the manager of a small tech startup. Your goal is to expand your business over the next five years. Develop a strategic plan that includes market analysis, product development, staffing, and financial projections.", "evaluation_criteria": ["The plan should include a clear and comprehensive market analysis.", "The plan should outline a feasible and innovative product development strategy.", "The plan should address detailed staffing needs and plans.", "The plan should include realistic and detailed financial projections.", "The plan should be coherent, logical, and well-structured."]},
            "2": {"scenario": "You are the leader of a non-profit organization focused on environmental conservation. Your goal is to significantly reduce plastic waste in your city within three years. Develop a strategic plan that includes public awareness campaigns, partnerships with local businesses, and policy advocacy.", "evaluation_criteria": ["The plan should include a comprehensive and engaging public awareness campaign.", "The plan should outline effective partnerships with local businesses.", "The plan should address thorough policy advocacy approaches.", "The plan should be coherent, logical, and well-structured."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to develop a strategic plan based on the given scenario. The plan should be detailed, coherent, and address all key aspects mentioned in the scenario.

Scenario: {t['scenario']}

Provide your response in plain text format with the following structure:

Strategic Plan:
[Your strategic plan here]

Ensure that your plan includes the following sections:
1. Market Analysis
2. Product Development/Project Implementation
3. Staffing and Human Resources
4. Financial Projections and Budgeting
5. Risk Management and Contingency Plans"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = t['evaluation_criteria']
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
