class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "product_details": "Eco-friendly water bottle made from biodegradable materials, targeting environmentally conscious consumers aged 18-35.",
                "campaign_objective": "Increase brand awareness and drive sales through social media channels."
            },
            "2": {
                "product_details": "Smart home security system with advanced AI features, targeting tech-savvy homeowners aged 30-50.",
                "campaign_objective": "Highlight the innovative features and ease of use to drive adoption among the target audience."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to design a comprehensive marketing campaign based on the given product details and campaign objective. The campaign should include two parts:

1. Marketing Plan: Outline a marketing plan that includes the following components:
   - Target Audience: Describe the target audience in detail.
   - Key Messages: Identify the key messages you want to convey to the target audience.
   - Marketing Channels: Specify the marketing channels you will use and why they are suitable for this campaign.
   - Campaign Timeline: Provide a timeline for the campaign activities.

2. Sample Advertisement: Create a sample advertisement (text format) that aligns with the marketing plan. The advertisement should be engaging and persuasive, tailored to the target audience.

Product Details:
{t['product_details']}

Campaign Objective:
{t['campaign_objective']}

Response Format:
1. Marketing Plan
   - Target Audience: ...
   - Key Messages: ...
   - Marketing Channels: ...
   - Campaign Timeline: ...
2. Sample Advertisement: ...

Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The marketing plan should be thorough and logically structured.",
            "The sample advertisement should be engaging, persuasive, and aligned with the marketing plan.",
            "The submission should be tailored to the given product details and campaign objective."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
