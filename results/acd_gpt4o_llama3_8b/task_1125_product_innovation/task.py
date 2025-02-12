class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "product_idea": "A portable solar-powered water purifier.",
                "target_market": "Rural communities in developing countries"
            },
            "2": {
                "product_idea": "A smart wearable device that monitors and improves posture.",
                "target_market": "Office workers in urban areas"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a detailed plan to bring the following innovative product to market.

Product Idea: {t['product_idea']}
Target Market: {t['target_market']}

Your plan should include the following components:
1. Product Description: A detailed description of the product, including its features and benefits.
2. Market Analysis: An analysis of the target market, including potential customers and competitors.
3. Marketing Strategy: A strategy for promoting the product to the target market.
4. Development Plan: A step-by-step plan for developing the product, including any technical requirements and milestones.
5. Financial Plan: An outline of the financial considerations, including budget, pricing, and funding sources.

Submit your response as a plain text string in the following format:
Product Description: [Your product description]
Market Analysis: [Your market analysis]
Marketing Strategy: [Your marketing strategy]
Development Plan: [Your development plan]
Financial Plan: [Your financial plan]

Ensure that each component is comprehensive, logically structured, and original. Your plan should demonstrate creativity, feasibility, and thoroughness."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The product description should be detailed and clearly explain the features and benefits.",
            "The market analysis should provide insights into the target market and competitors.",
            "The marketing strategy should be creative and well-suited to the target market.",
            "The development plan should be thorough, include technical requirements and milestones, and be feasible.",
            "The financial plan should outline budget, pricing, and potential funding sources.",
            "The entire plan should be original and demonstrate creativity."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
