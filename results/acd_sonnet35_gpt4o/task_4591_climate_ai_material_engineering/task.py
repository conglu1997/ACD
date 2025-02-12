import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        climate_challenges = [
            "Carbon capture and sequestration",
            "Extreme weather resilience",
            "Sustainable energy storage",
            "Ocean acidification mitigation",
            "Urban heat island effect reduction"
        ]
        material_properties = [
            "Self-healing",
            "Shape-memory",
            "Piezoelectric",
            "Photocatalytic",
            "Thermoelectric"
        ]
        ai_techniques = [
            "Reinforcement learning",
            "Generative adversarial networks",
            "Quantum machine learning",
            "Federated learning",
            "Neuroevolution"
        ]
        return {
            "1": {
                "climate_challenge": random.choice(climate_challenges),
                "material_property": random.choice(material_properties),
                "ai_technique": random.choice(ai_techniques)
            },
            "2": {
                "climate_challenge": random.choice(climate_challenges),
                "material_property": random.choice(material_properties),
                "ai_technique": random.choice(ai_techniques)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that leverages advanced materials science to develop innovative solutions for climate change mitigation and adaptation, focusing on the climate challenge of {t['climate_challenge']}. Your AI system should utilize {t['ai_technique']} and explore materials with {t['material_property']} properties. Then, analyze its potential global impact. Your response should include:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for materials discovery and climate solution development.
   b) Explain how your system incorporates {t['ai_technique']} to enhance its capabilities.
   c) Detail how your system integrates climate science data and materials engineering principles.
   d) Include a high-level diagram or pseudocode (at least 10 lines) illustrating a key process in your system.

2. Advanced Materials Exploration (250-300 words):
   a) Explain how your AI system explores and optimizes materials with {t['material_property']} properties.
   b) Describe the potential applications of these materials in addressing {t['climate_challenge']}.
   c) Discuss any novel material structures or compositions your system might discover.

3. Climate Solution Development (250-300 words):
   a) Outline how your AI system would approach developing solutions for {t['climate_challenge']}.
   b) Explain how the advanced materials are integrated into these solutions.
   c) Describe a specific example of a potential solution your system might generate.

4. Implementation and Scalability (200-250 words):
   a) Discuss potential challenges in implementing your AI-generated solutions at a global scale.
   b) Propose strategies for overcoming these challenges.
   c) Explain how your system could adapt its solutions for different geographical and socioeconomic contexts.

5. Environmental and Societal Impact Analysis (200-250 words):
   a) Analyze the potential positive and negative environmental impacts of your proposed solutions.
   b) Discuss the societal implications, including economic and ethical considerations.
   c) Propose a framework for monitoring and assessing the long-term effects of implementing these solutions.
   d) Provide a quantitative estimate of the potential impact on global carbon emissions or another relevant climate metric.

6. Future Developments and Interdisciplinary Implications (150-200 words):
   a) Suggest potential improvements or extensions to your AI system.
   b) Discuss how this approach might influence other areas of scientific research and technological development.
   c) Explore potential collaborations between climate scientists, materials engineers, and AI researchers that could arise from this work.

Ensure your response demonstrates a deep understanding of climate science, materials engineering, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of climate science, materials engineering, and artificial intelligence, particularly in relation to {t['climate_challenge']}, {t['material_property']} properties, and {t['ai_technique']}.",
            f"The AI system design effectively incorporates {t['ai_technique']} and explores materials with {t['material_property']} properties to address {t['climate_challenge']}.",
            "The approach to climate solution development is innovative, scientifically plausible, and clearly explained.",
            "The environmental and societal impact analysis is thorough, demonstrates critical thinking, and includes a quantitative estimate of potential impact.",
            "The response addresses all required sections with appropriate depth, clarity, and follows the specified format.",
            "The high-level diagram or pseudocode provided is sufficiently detailed (at least 10 lines) and accurately represents a key process in the proposed system.",
            "The proposed future developments and interdisciplinary implications are insightful, well-reasoned, and demonstrate a holistic understanding of the field.",
            "The response maintains scientific accuracy throughout and avoids speculative claims without proper justification."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
