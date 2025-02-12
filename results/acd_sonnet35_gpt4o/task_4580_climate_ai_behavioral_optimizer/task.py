import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        climate_factors = [
            "Greenhouse gas emissions",
            "Deforestation",
            "Ocean acidification",
            "Melting ice caps"
        ]
        behavioral_factors = [
            "Loss aversion",
            "Social norms",
            "Temporal discounting",
            "Status quo bias"
        ]
        ai_techniques = [
            "Reinforcement learning",
            "Bayesian networks",
            "Agent-based modeling",
            "Natural language processing"
        ]
        
        tasks = {}
        for i in range(2):
            climate_factor = random.choice(climate_factors)
            behavioral_factor = random.choice(behavioral_factors)
            ai_technique = random.choice(ai_techniques)
            
            tasks[str(i+1)] = {
                "climate_factor": climate_factor,
                "behavioral_factor": behavioral_factor,
                "ai_technique": ai_technique
            }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""This task is part of a task family designed to assess your ability to integrate knowledge from multiple disciplines and apply it to complex global challenges.

Design an AI system that integrates climate science models with behavioral economics to optimize climate change mitigation strategies and predict their societal impacts. Your system should focus on addressing {t['climate_factor']} while considering the behavioral factor of {t['behavioral_factor']}. Incorporate {t['ai_technique']} as a key AI technique in your system.

For example, your system might analyze historical data on {t['climate_factor']} and use {t['ai_technique']} to predict future trends. It could then model how {t['behavioral_factor']} influences people's responses to various mitigation strategies, and optimize policy recommendations accordingly.

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the main components of your AI system and how they interact.
   b) Explain how your system integrates climate science models with behavioral economics principles.
   c) Detail how {t['ai_technique']} is implemented in your system.
   d) Discuss how your system handles uncertainty and adapts to new data.

2. Climate Modeling and Prediction (250-300 words):
   a) Explain how your system models and predicts the impact of {t['climate_factor']}.
   b) Describe how it incorporates various data sources and handles data quality issues.
   c) Discuss any novel approaches your system uses to improve climate predictions.

3. Behavioral Economics Integration (250-300 words):
   a) Describe how your system models and predicts human behavior related to climate change mitigation.
   b) Explain how it incorporates {t['behavioral_factor']} into its predictions and strategy optimization.
   c) Discuss how your system balances short-term individual incentives with long-term collective benefits.

4. Strategy Optimization (250-300 words):
   a) Explain how your system generates and evaluates potential mitigation strategies.
   b) Describe how it optimizes strategies based on both climate impact and behavioral factors.
   c) Provide an example of how your system might propose and refine a specific mitigation strategy.

5. Ethical Considerations and Societal Impact (200-250 words):
   a) Discuss potential ethical issues arising from the use of your AI system in climate policy decisions.
   b) Explain how your system addresses issues of fairness and equity in its strategy optimization.
   c) Analyze potential unintended consequences of implementing AI-driven climate strategies.

6. Limitations and Future Directions (150-200 words):
   a) Identify potential limitations of your AI system.
   b) Propose future research directions or improvements to address these limitations.
   c) Discuss how this technology could evolve to better address global climate challenges.

Ensure your response demonstrates a deep understanding of climate science, behavioral economics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and ethical responsibility.

Format your response with clear headings for each section, numbered as above. Include the word count for each section in parentheses at the end of the section. Your total response should be between 1400-1700 words.

Cite at least 3 relevant scientific papers or reputable sources to support your system design and theoretical foundations. Include these citations at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['climate_factor']} and its role in climate change, with specific examples or data",
            f"The system effectively incorporates the behavioral factor of {t['behavioral_factor']} in its modeling and strategy optimization, providing clear examples of its application",
            f"The use of {t['ai_technique']} is well-explained and appropriately integrated into the system design, with details on its implementation",
            "The response shows creative problem-solving and innovative approaches to climate change mitigation, proposing novel strategies or methods",
            "Ethical considerations and potential societal impacts are thoroughly addressed, with specific scenarios or case studies",
            "The response adheres to the specified word count and formatting requirements, with each section properly developed",
            "At least 3 relevant scientific papers or reputable sources are cited to support the system design, and their relevance is clearly explained"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
