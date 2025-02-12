import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environmental_challenges = [
            "ocean plastic pollution",
            "air pollution in urban areas",
            "soil degradation in agricultural lands",
            "freshwater scarcity in arid regions"
        ]
        ecosystems = [
            "coral reef",
            "temperate forest",
            "arctic tundra",
            "grassland savanna"
        ]
        biomimetic_inspirations = [
            "lotus leaf (superhydrophobicity)",
            "gecko feet (adhesion)",
            "spider silk (strength and flexibility)",
            "butterfly wings (photonic structures)"
        ]
        return {
            "1": {
                "challenge": random.choice(environmental_challenges),
                "ecosystem": random.choice(ecosystems),
                "inspiration": random.choice(biomimetic_inspirations)
            },
            "2": {
                "challenge": random.choice(environmental_challenges),
                "ecosystem": random.choice(ecosystems),
                "inspiration": random.choice(biomimetic_inspirations)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a biomimetic nanotechnology system inspired by {t['inspiration']} to address the environmental challenge of {t['challenge']}. Then, analyze its potential impact on a {t['ecosystem']} ecosystem. Your response should include the following sections:\n\n1. Nanosystem Design (300-350 words):\n   a) Describe the key components and functionality of your biomimetic nanotechnology system.\n   b) Explain how your design incorporates principles from the specified biological inspiration.\n   c) Detail how your system addresses the given environmental challenge.\n   d) Include a diagram or schematic representation of your nanosystem (describe it textually).\n\n2. Fabrication and Deployment (250-300 words):\n   a) Outline the process for manufacturing your nanotechnology system.\n   b) Describe how the system would be deployed in the target environment.\n   c) Discuss any challenges in scaling up production and implementation.\n   d) Propose solutions to these challenges.\n\n3. Environmental Impact Analysis (250-300 words):\n   a) Analyze the potential positive and negative impacts of your system on the specified ecosystem.\n   b) Discuss how your system might interact with various components of the ecosystem (e.g., flora, fauna, abiotic factors).\n   c) Predict any potential cascading effects on the food web or ecosystem services.\n   d) Propose methods for monitoring and mitigating any adverse effects.\n\n4. Ethical and Regulatory Considerations (200-250 words):\n   a) Discuss ethical implications of introducing engineered nanosystems into natural environments.\n   b) Propose guidelines for responsible development and use of biomimetic nanotechnology in ecosystem engineering.\n   c) Outline potential regulatory frameworks needed to govern the use of such technologies.\n\n5. Future Developments and Applications (200-250 words):\n   a) Suggest potential improvements or iterations of your nanosystem.\n   b) Propose two other environmental challenges that could be addressed using similar biomimetic nanotechnology approaches.\n   c) Discuss how your system might be adapted for use in different ecosystems or environments.\n\n6. Interdisciplinary Implications (150-200 words):\n   a) Explain how your biomimetic nanotechnology system contributes to our understanding of natural systems.\n   b) Discuss potential applications of your approach in fields such as materials science, medicine, or space exploration.\n   c) Propose a research question that emerges from this work, bridging nanotechnology and ecological studies.\n\nEnsure your response demonstrates a deep understanding of biomimicry, nanotechnology, and ecological principles. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and environmental responsibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1350-1650 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding and integration of biomimicry principles inspired by {t['inspiration']}.",
            f"The nanotechnology system effectively addresses the environmental challenge of {t['challenge']}.",
            f"The analysis thoroughly considers the potential impact on a {t['ecosystem']} ecosystem.",
            "The fabrication and deployment plan is well-thought-out and addresses potential challenges.",
            "The environmental impact analysis is comprehensive, considering both positive and negative effects.",
            "Ethical and regulatory considerations are thoroughly discussed with thoughtful guidelines proposed.",
            "Future developments and applications are innovative and well-reasoned.",
            "The interdisciplinary implications are insightfully analyzed.",
            "The response demonstrates creativity while maintaining scientific accuracy and plausibility.",
            "All sections of the response are complete and adhere to the word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
