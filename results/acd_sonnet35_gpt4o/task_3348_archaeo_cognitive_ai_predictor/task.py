import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        archaeological_periods = [
            "Neolithic",
            "Bronze Age",
            "Iron Age",
            "Classical Antiquity",
            "Medieval Period"
        ]
        cognitive_aspects = [
            "Spatial reasoning",
            "Numerical cognition",
            "Social cognition",
            "Metaphorical thinking",
            "Temporal perception"
        ]
        future_timeframes = [
            "100 years",
            "500 years",
            "1000 years",
            "5000 years",
            "10000 years"
        ]
        
        return {
            "1": {
                "archaeological_period": random.choice(archaeological_periods),
                "cognitive_aspect": random.choice(cognitive_aspects),
                "future_timeframe": random.choice(future_timeframes)
            },
            "2": {
                "archaeological_period": random.choice(archaeological_periods),
                "cognitive_aspect": random.choice(cognitive_aspects),
                "future_timeframe": random.choice(future_timeframes)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that reconstructs ancient languages and thought patterns from archaeological evidence of the {t['archaeological_period']}, with a focus on {t['cognitive_aspect']}. Then, use this information to predict linguistic and cognitive evolution {t['future_timeframe']} into the future. Your response should include the following sections:\n\n1. AI System Architecture (300-350 words):\n   a) Describe the key components of your AI system for reconstructing ancient languages and thought patterns.\n   b) Explain how your system integrates archaeological data, linguistic analysis, and cognitive modeling.\n   c) Detail how your AI handles uncertainty and incomplete data in its reconstructions.\n   d) Include a high-level diagram or flowchart of your AI system architecture.\n\n2. Ancient Language and Cognition Reconstruction (250-300 words):\n   a) Explain how your AI system reconstructs the language of the {t['archaeological_period']}.\n   b) Describe the methods used to infer thought patterns and {t['cognitive_aspect']} from archaeological evidence.\n   c) Provide an example of a reconstructed linguistic feature or cognitive pattern, with supporting evidence.\n\n3. Future Prediction Methodology (250-300 words):\n   a) Outline how your AI system extrapolates from past linguistic and cognitive evolution to predict future changes.\n   b) Explain how it accounts for technological and environmental factors in its predictions.\n   c) Describe any novel algorithms or techniques used for long-term linguistic and cognitive forecasting.\n\n4. Predicted Future Scenario (200-250 words):\n   a) Present a detailed scenario of predicted linguistic and cognitive changes {t['future_timeframe']} into the future.\n   b) Focus on how {t['cognitive_aspect']} might evolve and impact language use.\n   c) Discuss potential societal implications of these predicted changes.\n\n5. Ethical Considerations and Limitations (150-200 words):\n   a) Identify potential ethical issues in reconstructing past cultures and predicting future cognitive evolution.\n   b) Discuss the limitations of your AI system and the reliability of its predictions.\n   c) Propose guidelines for the responsible use of such technology in archaeological and futuristic studies.\n\n6. Interdisciplinary Implications (150-200 words):\n   a) Explain how your AI system and its findings could impact multiple fields of study.\n   b) Suggest two potential research projects that could stem from your work.\n   c) Discuss how this approach might change our understanding of human cognitive evolution.\n\nEnsure your response demonstrates a deep understanding of archaeology, linguistics, cognitive science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and speculative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1300-1600 words. Include the high-level diagram or flowchart of your AI system architecture as mentioned in section 1."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of archaeology, linguistics, cognitive science, and artificial intelligence.",
            "The AI system architecture is innovative, plausible, and well-explained, integrating all required elements (archaeological data, linguistic analysis, and cognitive modeling).",
            "The ancient language and cognition reconstruction process is clearly described and plausible, with a specific example provided.",
            "The future prediction methodology is well-explained and takes into account relevant factors such as technology and environment.",
            "The predicted future scenario is detailed, creative, and logically consistent with the given timeframe and cognitive aspect.",
            "Ethical considerations and limitations are thoughtfully discussed, with proposed guidelines for responsible use.",
            "The interdisciplinary implications are well-considered, with plausible research projects and impact on human cognitive evolution understanding.",
            "The response includes a high-level diagram or flowchart of the AI system architecture.",
            "The response addresses all required sections coherently and falls within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
