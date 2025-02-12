import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        climate_challenges = [
            "Drought resistance",
            "Heat tolerance",
            "Salinity adaptation",
            "Flood resilience"
        ]
        plant_types = [
            "Staple crop (e.g., rice, wheat, maize)",
            "Fruit-bearing tree",
            "Vegetable crop",
            "Legume"
        ]
        ai_techniques = [
            "Deep learning for genomic analysis",
            "Reinforcement learning for optimizing growth conditions",
            "Generative adversarial networks for synthetic biology",
            "Natural language processing for scientific literature mining"
        ]
        return {
            "1": {
                "climate_challenge": random.choice(climate_challenges),
                "plant_type": random.choice(plant_types),
                "ai_technique": random.choice(ai_techniques)
            },
            "2": {
                "climate_challenge": random.choice(climate_challenges),
                "plant_type": random.choice(plant_types),
                "ai_technique": random.choice(ai_techniques)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI-driven biotechnology system to enhance plant resilience to climate change, focusing on {t['climate_challenge']} for a {t['plant_type']}. Your system should incorporate {t['ai_technique']} as a key component. Then, analyze its potential impact on global food security and biodiversity. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the main components of your AI-driven biotechnology system.
   b) Explain how {t['ai_technique']} is integrated into the system.
   c) Detail the biotechnology methods used to enhance {t['climate_challenge']} in the {t['plant_type']}.
   d) Include a diagram or flowchart of your system's architecture (use text description if needed).

2. AI-Biotechnology Interface (250-300 words):
   a) Explain how your AI system interacts with and guides the biotechnology processes.
   b) Describe any novel algorithms or techniques developed for this specific application.
   c) Discuss how your system handles the complexity and variability inherent in biological systems.

3. Climate Adaptation Mechanisms (200-250 words):
   a) Detail the specific biological mechanisms your system targets to enhance {t['climate_challenge']}.
   b) Explain how these mechanisms are modified or optimized using AI and biotechnology.
   c) Discuss potential side effects or trade-offs of these adaptations.

4. Scaling and Implementation (200-250 words):
   a) Describe how your system could be scaled from laboratory to field applications.
   b) Discuss challenges in implementing this technology in different geographic and climatic regions.
   c) Propose strategies for ensuring equitable access to this technology globally.

5. Impact Analysis (250-300 words):
   a) Analyze the potential impact of your system on global food security, considering both positive and negative outcomes.
   b) Discuss how the widespread use of this technology might affect local and global biodiversity.
   c) Consider potential ecological consequences of introducing climate-adapted {t['plant_type']} varieties.

6. Ethical Considerations (200-250 words):
   a) Discuss ethical implications of using AI and biotechnology to modify plants for climate adaptation.
   b) Address concerns related to biodiversity, ecosystem balance, and potential unintended consequences.
   c) Propose guidelines for responsible development and deployment of this technology.

7. Future Research Directions (150-200 words):
   a) Suggest two potential areas for further research based on your system.
   b) Explain how these research directions could advance our understanding of climate adaptation, AI in biology, or sustainable agriculture.

Ensure your response demonstrates a deep understanding of artificial intelligence, biotechnology, climate science, and ecology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1550-1900 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed and scientifically plausible design for an AI-driven biotechnology system that effectively addresses {t['climate_challenge']} in {t['plant_type']} using {t['ai_technique']}.",
            "The explanation of how AI and biotechnology are integrated demonstrates a deep understanding of both fields and their potential synergies.",
            "The climate adaptation mechanisms are well-explained and grounded in current scientific understanding of plant biology and genetics.",
            "The scaling and implementation section provides realistic strategies and addresses potential challenges.",
            "The impact analysis thoroughly considers both positive and negative consequences on food security and biodiversity.",
            "The ethical considerations demonstrate a nuanced understanding of the complex issues surrounding this technology.",
            "The proposed future research directions are innovative and have the potential to significantly advance relevant fields.",
            "The overall response shows a strong grasp of AI, biotechnology, climate science, and ecology, with appropriate use of technical terminology and clear explanations of complex concepts.",
            "The response adheres to the specified format and word count guidelines for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
