import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        exoplanet_types = [
            "Super-Earth",
            "Ocean world",
            "Desert planet"
        ]
        terraforming_challenges = [
            "Atmospheric composition adjustment",
            "Temperature regulation",
            "Gravity adaptation"
        ]
        biotechnology_approaches = [
            "Engineered extremophiles",
            "Synthetic photosynthesis",
            "Biogeochemical cycling"
        ]
        tasks = [
            {
                "exoplanet_type": planet,
                "terraforming_challenge": challenge,
                "biotechnology_approach": approach
            }
            for planet in exoplanet_types
            for challenge in terraforming_challenges
            for approach in biotechnology_approaches
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI-driven system for terraforming exoplanets using advanced biotechnology and nanotechnology, then analyze its potential impact on space exploration and human colonization. Focus on a {t['exoplanet_type']} with the primary terraforming challenge of {t['terraforming_challenge']}, utilizing {t['biotechnology_approach']} as a key biotechnology approach. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI-driven terraforming system.
   b) Explain how AI, biotechnology, and nanotechnology are integrated in your design.
   c) Detail how your system addresses the specific terraforming challenge on the given exoplanet type.
   d) Include a brief description of a diagram representing your system's structure and processes.

2. Terraforming Process (250-300 words):
   a) Outline the steps involved in terraforming the exoplanet using your system.
   b) Explain how the specified biotechnology approach is utilized in the process.
   c) Describe any novel techniques or technologies developed for this specific scenario.

3. AI Decision-Making and Adaptation (200-250 words):
   a) Explain how your AI system makes both short-term and long-term decisions during the terraforming process.
   b) Describe how it adapts to unexpected challenges or changes in the exoplanet's environment.
   c) Discuss any ethical considerations programmed into the AI's decision-making process.
   d) Address potential unintended consequences of the AI-driven terraforming process and how they might be mitigated.

4. Timeframe and Efficiency Analysis (150-200 words):
   a) Estimate the timeframe required for your system to terraform the exoplanet.
   b) Analyze the energy efficiency and resource utilization of your approach.
   c) Compare your system's efficiency to theoretical models of terraforming.

5. Impact on Space Exploration and Colonization (200-250 words):
   a) Discuss how your system could revolutionize space exploration and colonization efforts.
   b) Analyze potential socioeconomic and political implications of successful exoplanet terraforming.
   c) Explore how this technology might influence human evolution and adaptation to new environments.

6. Challenges and Future Developments (150-200 words):
   a) Identify potential obstacles or limitations in implementing your system.
   b) Propose innovative solutions or areas for future research to address these challenges.
   c) Suggest potential spin-off technologies that could benefit life on Earth.

Ensure your response demonstrates a deep understanding of astrophysics, biotechnology, nanotechnology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates understanding of astrophysics, biotechnology, nanotechnology, and artificial intelligence.",
            "The system architecture integrates AI, biotechnology, and nanotechnology effectively.",
            "The terraforming process addresses the specific challenge and exoplanet type.",
            "The AI decision-making process covers both short-term and long-term aspects and considers ethical implications.",
            "Potential unintended consequences of terraforming are discussed with proposed mitigation strategies.",
            "The timeframe and efficiency analysis is reasonable and well-justified.",
            "The impact on space exploration and colonization is thoroughly analyzed.",
            "Challenges are identified and innovative, scientifically plausible solutions are proposed.",
            "The response is well-structured with clear headings for each section.",
            "The response uses appropriate technical terminology and provides clear explanations for complex concepts."
        ]
        return float(eval_with_llm_judge(instructions, submission, criteria))