class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"product": "A new eco-friendly water bottle that keeps drinks cold for 24 hours.", "description": "Create an engaging advertisement for an eco-friendly water bottle that emphasizes its unique selling points: eco-friendliness and the ability to keep drinks cold for 24 hours. The advertisement should be suitable for social media platforms and targeted towards environmentally conscious consumers."},
            "2": {"advertisement": "A print ad for a luxury car brand that shows a sleek car on a mountain road with the tagline 'Experience the Pinnacle of Performance.'", "description": "Analyze the given print advertisement for a luxury car brand. Discuss the effectiveness of the ad in terms of its visual appeal, messaging, and target audience. Provide a detailed explanation of why this ad might or might not be effective in attracting potential buyers."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'product' in t:
            return f"""Your task is to create an engaging advertisement for the following product:

Product: {t['product']}

{t['description']}

Ensure your advertisement includes:
1. A catchy headline.
2. A persuasive body text that highlights the unique selling points.
3. A call to action.
4. Suitable format for social media platforms.
5. Targeted towards environmentally conscious consumers.

Provide your advertisement in plain text format.

Example response format:
Headline: [Your catchy headline]
Body Text: [Your persuasive body text]
Call to Action: [Your call to action]
"""
        else:
            return f"""Your task is to analyze the following advertisement:

Advertisement: {t['advertisement']}

{t['description']}

Ensure your analysis includes:
1. An examination of the visual elements and their appeal.
2. An analysis of the messaging and how it communicates the brand's values.
3. An identification of the target audience and why this ad might appeal to them.
4. A detailed explanation of the ad's effectiveness or lack thereof.

Provide your analysis in plain text format.

Example response format:
Visual Appeal: [Examination of visual elements]
Messaging: [Analysis of messaging]
Target Audience: [Identification of target audience]
Effectiveness: [Explanation of effectiveness]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a catchy headline.",
            "The response should include a persuasive body text that highlights the unique selling points.",
            "The response should include a call to action.",
            "The response should be suitable for social media platforms.",
            "The response should be targeted towards environmentally conscious consumers."
        ] if 'product' in t else [
            "The response should examine the visual elements and their appeal.",
            "The response should analyze the messaging and how it communicates the brand's values.",
            "The response should identify the target audience and why this ad might appeal to them.",
            "The response should provide a detailed explanation of the ad's effectiveness or lack thereof."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
