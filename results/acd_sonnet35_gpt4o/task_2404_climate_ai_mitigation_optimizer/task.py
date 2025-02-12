import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "region": "Southeast Asia",
                "time_horizon": "2050",
                "sectors": ["agriculture", "energy", "urban planning"],
                "constraint": "limited water resources"
            },
            {
                "region": "Sub-Saharan Africa",
                "time_horizon": "2070",
                "sectors": ["healthcare", "biodiversity", "food security"],
                "constraint": "rapid population growth"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that predicts climate change impacts and optimizes mitigation strategies for {t['region']} up to the year {t['time_horizon']}, focusing on the sectors of {', '.join(t['sectors'])}. Your system should address the constraint of {t['constraint']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the main components of your AI system for climate prediction and mitigation optimization.
   b) Explain how your system integrates climate models, sector-specific impact assessments, and optimization algorithms.
   c) Detail how your system addresses uncertainty and long-term projections.
   d) Discuss how your system incorporates real-time data and adaptive learning.

2. Data Integration and Processing (200-250 words):
   a) Identify the types of data your system would use for climate prediction and impact assessment.
   b) Explain how your system would handle data from diverse sources and scales.
   c) Describe any novel data processing or fusion techniques your system employs.

3. Climate Impact Prediction (250-300 words):
   a) Outline the approach your AI system uses to predict climate impacts in the specified sectors.
   b) Explain how your system accounts for complex interactions between different sectors and environmental factors.
   c) Describe how your system quantifies and communicates uncertainty in its predictions.

4. Mitigation Strategy Optimization (250-300 words):
   a) Describe the optimization algorithm(s) your system uses to develop mitigation strategies.
   b) Explain how your system balances competing objectives across different sectors.
   c) Detail how your system addresses the specified constraint in its optimization process.
   d) Provide an example of how your system might prioritize and sequence mitigation actions.

5. Ethical Considerations and Stakeholder Engagement (200-250 words):
   a) Discuss the ethical implications of using AI for climate change mitigation planning.
   b) Explain how your system incorporates principles of environmental justice and equity.
   c) Describe how your system could facilitate stakeholder engagement and participatory decision-making.

6. Evaluation and Adaptability (150-200 words):
   a) Propose a method for evaluating the effectiveness and accuracy of your system.
   b) Describe how your system could adapt to changing conditions or new scientific insights.
   c) Discuss the limitations of your approach and potential areas for improvement.

7. Global Implications (150-200 words):
   a) Analyze how your system could be scaled or adapted for use in other regions.
   b) Discuss the potential impact of widespread adoption of such systems on global climate mitigation efforts.
   c) Propose a framework for international collaboration using AI-driven climate mitigation systems.

Ensure your response demonstrates a deep understanding of climate science, artificial intelligence, and the complex interactions within socio-ecological systems. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility and practical considerations.

Format your response with clear headings for each section and subsections labeled a, b, c, d as appropriate. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of climate science, AI, and complex system modeling.",
            "The proposed AI system is innovative, scientifically plausible, and addresses the specified regions, sectors, and constraints.",
            "The response thoroughly covers all required sections with appropriate detail and technical depth.",
            "The ethical considerations and stakeholder engagement aspects are thoughtfully addressed.",
            "The response shows creative problem-solving and interdisciplinary knowledge integration."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
