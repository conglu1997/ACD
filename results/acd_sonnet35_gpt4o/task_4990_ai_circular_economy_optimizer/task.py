import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        industries = [
            {
                "industry": "Electronics manufacturing",
                "focus": "Rare earth metal recycling"
            },
            {
                "industry": "Fashion and textiles",
                "focus": "Sustainable fiber production and clothing reuse"
            }
        ]
        return {str(i+1): industry for i, industry in enumerate(industries)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that optimizes circular economy strategies for the {t['industry']} industry, with a focus on {t['focus']}. Your system should balance economic growth with environmental sustainability. Then, analyze its potential impact on global resource management.

Circular economy principles aim to eliminate waste and maximize resource efficiency by keeping products, components, and materials at their highest utility and value at all times. This involves designing out waste and pollution, keeping products and materials in use, and regenerating natural systems.

Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI circular economy optimizer.
   b) Explain how your system integrates data from economic, environmental, and industry-specific sources.
   c) Detail the AI/ML techniques used (e.g., reinforcement learning, multi-objective optimization).
   d) Provide a high-level diagram of your system architecture (described textually).

2. Circular Economy Modeling (200-250 words):
   a) Explain how your system models circular economy principles for the given industry.
   b) Describe the key parameters and variables considered in your optimization process.
   c) Discuss how your system handles trade-offs between economic and environmental objectives.
   d) Explain any novel approaches or algorithms employed in your model.

3. Data Integration and Analysis (200-250 words):
   a) Specify the types of data your system would use and potential sources.
   b) Explain how your system processes and analyzes this data to inform decision-making.
   c) Describe how your system handles uncertainties and variability in the data.
   d) Discuss any challenges in data integration specific to the given industry and how you address them.

4. Optimization Strategies (250-300 words):
   a) Outline the specific circular economy strategies your system would optimize for the given industry.
   b) Explain how your system evaluates and ranks different strategies.
   c) Provide an example scenario demonstrating your system's optimization process.
   d) Discuss how your system adapts its strategies based on changing economic or environmental conditions.

5. Impact Analysis (200-250 words):
   a) Analyze the potential economic impact of implementing your AI-optimized strategies in the given industry.
   b) Discuss the environmental benefits and any potential drawbacks or challenges.
   c) Explain how your system's recommendations might affect global resource management.
   d) Consider potential ripple effects on related industries or supply chains.

6. Ethical and Social Considerations (150-200 words):
   a) Identify potential ethical issues arising from the use of AI in optimizing circular economy strategies.
   b) Discuss how your system addresses issues of fairness, transparency, and accountability.
   c) Consider the potential social impacts, both positive and negative, of implementing your system's recommendations.
   d) Propose guidelines for responsible development and use of AI in circular economy optimization.

7. Future Developments (100-150 words):
   a) Suggest two potential enhancements or extensions to your AI system.
   b) Discuss how emerging technologies could be integrated to improve your system's capabilities.
   c) Propose a research question that could further advance AI-driven circular economy optimization.

Ensure your response demonstrates a deep understanding of artificial intelligence, environmental science, economics, and the specific industry. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific and practical plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must include all seven required sections with appropriate content for each.",
            "The system architecture should clearly integrate AI techniques with circular economy principles.",
            "The circular economy modeling should be specific to the given industry and focus area.",
            "The optimization strategies should balance economic and environmental objectives.",
            "The impact analysis should consider both economic and environmental effects.",
            "The response should demonstrate interdisciplinary knowledge and creative problem-solving.",
            "The ethical considerations should be thoughtful and relevant to the specific application."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
