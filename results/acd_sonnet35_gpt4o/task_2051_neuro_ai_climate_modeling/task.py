import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "brain_region": "Hippocampus",
                "climate_phenomenon": "El Niño",
                "ecosystem": "Coral Reefs"
            },
            {
                "brain_region": "Prefrontal Cortex",
                "climate_phenomenon": "Arctic Amplification",
                "ecosystem": "Tundra"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a brain-inspired artificial intelligence system for advanced climate modeling and ecosystem prediction, focusing on the {t['brain_region']} as a model for AI architecture, the climate phenomenon of {t['climate_phenomenon']}, and its impact on the {t['ecosystem']} ecosystem. Your response should include the following sections:\n\n1. Neuro-AI Architecture (250-300 words):\n   a) Describe the key features of the {t['brain_region']} and how they inspire your AI system design.\n   b) Explain how your AI architecture mimics neural processes for climate modeling.\n   c) Discuss how this brain-inspired approach differs from traditional climate modeling techniques.\n   d) Provide a schematic diagram or pseudocode snippet illustrating a key aspect of your system.\n\n2. Climate Modeling Integration (200-250 words):\n   a) Explain how your system models the {t['climate_phenomenon']} phenomenon.\n   b) Describe the data inputs and processing methods used by your AI system.\n   c) Discuss how your system handles the complexity and non-linearity of climate systems.\n\n3. Ecosystem Prediction (200-250 words):\n   a) Detail how your AI system predicts the impact of {t['climate_phenomenon']} on the {t['ecosystem']} ecosystem.\n   b) Explain the key variables and interactions your model considers.\n   c) Describe a novel feature of your system that enhances ecosystem prediction accuracy.\n\n4. Comparative Analysis (150-200 words):\n   a) Compare your neuro-AI approach to traditional climate and ecosystem modeling techniques.\n   b) Discuss potential advantages and limitations of your brain-inspired system.\n   c) Propose a method to validate your system's predictions against real-world data.\n\n5. Ethical Considerations and Societal Impact (150-200 words):\n   a) Discuss potential ethical issues related to using brain-inspired AI for climate predictions.\n   b) Explore the societal implications of highly accurate ecosystem forecasting.\n   c) Propose guidelines for the responsible development and use of such systems.\n\n6. Future Developments (100-150 words):\n   a) Suggest two potential advancements or extensions of your system.\n   b) Speculate on how this technology might evolve in the next decade.\n\nEnsure your response demonstrates a deep understanding of neuroscience, artificial intelligence, climate science, and ecology. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts.\n\nFormat your response with clear headings for each section. Your total response should be between 1050-1350 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, AI, climate science, and ecology.",
            "The proposed neuro-AI architecture is innovative and clearly inspired by the specified brain region.",
            "The climate modeling and ecosystem prediction aspects are well-integrated and scientifically plausible.",
            "The comparative analysis shows insight into the advantages and limitations of the proposed approach.",
            "Ethical considerations and societal impacts are thoughtfully discussed.",
            "The response is well-structured, coherent, and within the specified word limit.",
            "The proposed system demonstrates a clear and novel integration of brain-inspired AI with climate and ecosystem modeling."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
