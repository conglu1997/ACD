import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        mitigation_strategies = [
            "Carbon capture and storage",
            "Reforestation and afforestation",
            "Renewable energy transition",
            "Sustainable agriculture practices",
            "Urban planning and green infrastructure"
        ]
        environmental_factors = [
            "Atmospheric CO2 levels",
            "Global average temperature",
            "Sea level rise",
            "Biodiversity index",
            "Extreme weather events frequency"
        ]
        time_scales = ["Short-term (5-10 years)", "Medium-term (20-30 years)", "Long-term (50-100 years)"]
        regions = ["Global", "North America", "Europe", "Asia", "Africa", "South America", "Australia"]
        
        return {
            "1": {
                "mitigation_strategy": random.choice(mitigation_strategies),
                "environmental_factor": random.choice(environmental_factors),
                "time_scale": random.choice(time_scales),
                "region": random.choice(regions)
            },
            "2": {
                "mitigation_strategy": random.choice(mitigation_strategies),
                "environmental_factor": random.choice(environmental_factors),
                "time_scale": random.choice(time_scales),
                "region": random.choice(regions)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system to model and predict the effectiveness of the climate change mitigation strategy '{t['mitigation_strategy']}' on the environmental factor '{t['environmental_factor']}' over a {t['time_scale']} period in the {t['region']} region. Your response should include:\n\n1. AI System Architecture (250-300 words):\n   a) Describe the key components of your AI system.\n   b) Explain how it integrates environmental science principles and data.\n   c) Discuss any novel machine learning techniques or algorithms it employs.\n\n2. Data Integration and Preprocessing (200-250 words):\n   a) Identify the types of data your system would require.\n   b) Explain how you would preprocess and integrate data from diverse sources.\n   c) Discuss challenges in data collection and how you'd address them.\n\n3. Modeling and Prediction Process (250-300 words):\n   a) Describe how your AI system models the relationship between the mitigation strategy and the environmental factor.\n   b) Explain the prediction process and how it accounts for the specified time scale and region.\n   c) Discuss how your system accounts for uncertainties and feedback loops in climate systems.\n\n4. Validation and Uncertainty Quantification (200-250 words):\n   a) Propose methods to validate your AI system's predictions.\n   b) Explain how you would quantify and communicate uncertainties in the model's outputs.\n   c) Discuss the limitations of your approach and potential areas for improvement.\n\n5. Practical Application and Policy Implications (150-200 words):\n   a) Describe how policymakers or environmental organizations could use your AI system.\n   b) Discuss potential challenges in implementing the system's recommendations.\n   c) Propose guidelines for responsible use of AI in climate policy decisions.\n\n6. Ethical Considerations and Broader Impacts (150-200 words):\n   a) Analyze potential ethical issues related to using AI for climate change mitigation modeling.\n   b) Discuss how your system might impact different stakeholders or regions.\n   c) Propose safeguards to ensure equitable and responsible use of the technology.\n\n7. Case Study (200-250 words):\n   Provide a concrete example or case study demonstrating how your AI system would be applied to a specific scenario within the given parameters. Include quantitative predictions or estimates where appropriate.\n\nEnsure your response demonstrates a deep understanding of both AI/machine learning and environmental science. Be creative in your approach while maintaining scientific plausibility and addressing real-world constraints. Use appropriate technical terminology and provide clear explanations for complex concepts.\n\nFormat your response with clear headings for each section. Your total response should be between 1400-1750 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both AI/machine learning and environmental science principles.",
            "The AI system design is innovative, plausible, and well-suited to the specific mitigation strategy, environmental factor, time scale, and region.",
            "The response addresses all required sections comprehensively and coherently.",
            "The proposed system effectively integrates diverse data sources and accounts for the complexities of climate systems.",
            "Ethical considerations and broader impacts are thoughtfully analyzed.",
            "The response includes a concrete case study with quantitative elements.",
            "The response is well-structured, clear, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
