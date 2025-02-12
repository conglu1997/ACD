import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        climate_factors = [
            "ocean acidification",
            "rising sea temperatures",
            "changing ocean currents"
        ]
        marine_mammals = [
            "bottlenose dolphins",
            "humpback whales",
            "sea otters"
        ]
        cognitive_processes = [
            "echolocation",
            "social cognition",
            "spatial memory"
        ]
        conservation_strategies = [
            "marine protected areas",
            "acoustic pollution reduction",
            "prey species management"
        ]
        return {
            "1": {
                "climate_factor": random.choice(climate_factors),
                "marine_mammal": random.choice(marine_mammals),
                "cognitive_process": random.choice(cognitive_processes),
                "conservation_strategy": random.choice(conservation_strategies)
            },
            "2": {
                "climate_factor": random.choice(climate_factors),
                "marine_mammal": random.choice(marine_mammals),
                "cognitive_process": random.choice(cognitive_processes),
                "conservation_strategy": random.choice(conservation_strategies)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that integrates neuroscience, marine biology, and climate science to model and predict the effects of climate change on marine mammal cognition and behavior, then propose conservation strategies based on the predictions. Focus on the following elements:\n\nClimate Factor: {t['climate_factor']}\nMarine Mammal: {t['marine_mammal']}\nCognitive Process: {t['cognitive_process']}\nConservation Strategy: {t['conservation_strategy']}\n\nYour response should include:\n\n1. AI System Architecture (300-350 words):\n   a) Describe the key components of your AI system for modeling marine mammal cognition and behavior.\n   b) Explain how your system integrates data from neuroscience, marine biology, and climate science.\n   c) Detail how the system models the impact of the specified climate factor on the cognitive process.\n   d) Discuss how your system accounts for species-specific adaptations and vulnerabilities.\n   e) Include a diagram or flowchart illustrating your system's architecture (describe it textually).\n\n2. Data Integration and Analysis (250-300 words):\n   a) Explain how your system collects and processes data related to the specified climate factor and its effects on marine ecosystems.\n   b) Describe the methods used to analyze the impacts on the specified cognitive process, including any novel approaches.\n   c) Discuss how the system accounts for individual differences and population-level trends in the marine mammal species.\n   d) Explain how your system handles the complexity and variability of marine ecosystems.\n\n3. Predictive Modeling (250-300 words):\n   a) Detail how your AI system generates predictions about the long-term effects of climate change on the specified marine mammal and cognitive process.\n   b) Explain any machine learning algorithms or statistical methods used in your predictive modeling.\n   c) Discuss how your system validates its predictions and handles uncertainty.\n   d) Provide a hypothetical example of a specific prediction your system might make, including quantitative estimates if possible.\n\n4. Conservation Strategy Development (200-250 words):\n   a) Explain how your system uses its predictions to inform the specified conservation strategy.\n   b) Describe how the AI evaluates the potential effectiveness of different conservation approaches.\n   c) Discuss how your system balances short-term and long-term conservation goals.\n   d) Propose a novel way to implement or enhance the specified conservation strategy based on your AI's insights.\n\n5. Ethical Considerations (150-200 words):\n   a) Identify potential ethical issues related to using AI to predict and influence marine mammal behavior and ecosystems.\n   b) Discuss the implications of using predictive models to guide conservation efforts.\n   c) Address concerns about data collection methods and their potential impact on marine mammals.\n   d) Propose guidelines for the ethical development and use of such AI systems in marine conservation.\n\n6. Limitations and Future Directions (150-200 words):\n   a) Discuss the main limitations of your current AI system and approach.\n   b) Suggest two potential improvements or extensions to your system for future development.\n   c) Propose a research agenda to validate and refine your AI system's predictions and conservation recommendations.\n\nEnsure your response demonstrates a deep understanding of neuroscience, marine biology, climate science, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.\n\nFormat your response with clear headings for each section, numbered as above. Your total response should be between 1300-1600 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, marine biology, climate science, and artificial intelligence, integrating these disciplines effectively.",
            "The proposed AI system architecture is innovative, scientifically plausible, and clearly explained, with a logical flow from data integration to conservation strategy development.",
            "The submission addresses all required sections comprehensively, providing insightful analysis of the system's potential applications, limitations, and ethical implications.",
            "The response shows strong interdisciplinary knowledge integration, combining concepts from multiple scientific fields to address a complex environmental challenge.",
            "The writing is clear, well-structured, and uses appropriate technical terminology throughout, with adequate explanations for complex concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
