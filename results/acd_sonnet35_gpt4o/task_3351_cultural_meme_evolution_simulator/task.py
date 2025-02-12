import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        meme_scenarios = [
            {
                "meme_type": "Technological innovation",
                "cognitive_bias": "Confirmation bias",
                "social_structure": "Hierarchical society",
                "environmental_factor": "Resource scarcity"
            },
            {
                "meme_type": "Religious belief",
                "cognitive_bias": "In-group favoritism",
                "social_structure": "Egalitarian network",
                "environmental_factor": "Natural disaster frequency"
            },
            {
                "meme_type": "Political ideology",
                "cognitive_bias": "Availability heuristic",
                "social_structure": "Small-world network",
                "environmental_factor": "Economic inequality"
            },
            {
                "meme_type": "Linguistic innovation",
                "cognitive_bias": "Bandwagon effect",
                "social_structure": "Scale-free network",
                "environmental_factor": "Cultural contact intensity"
            }
        ]
        return {
            "1": random.choice(meme_scenarios),
            "2": random.choice(meme_scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and implement a computational model that simulates the evolution and spread of cultural memes across different societies. Your model should focus on the meme type of {t['meme_type']}, incorporate the cognitive bias of {t['cognitive_bias']}, consider a {t['social_structure']} social structure, and account for the environmental factor of {t['environmental_factor']}. Provide your response in the following format:

1. Model Architecture (300-350 words):
   a) Describe the key components of your cultural meme evolution simulator.
   b) Explain how your model integrates cognitive science, AI, and cultural anthropology principles.
   c) Detail how you represent and evolve memes in your system.
   d) Discuss how your model incorporates the specified cognitive bias, social structure, and environmental factor.
   e) Include a high-level diagram or pseudocode snippet illustrating a core aspect of your model.

2. Meme Representation and Evolution (250-300 words):
   a) Explain how you represent {t['meme_type']} memes in your model.
   b) Describe the mechanisms for meme mutation, recombination, and selection.
   c) Discuss how {t['cognitive_bias']} influences meme transmission and adoption in your model.
   d) Provide an example of how a specific meme might evolve in your simulation.

3. Social Network and Environmental Modeling (200-250 words):
   a) Detail how you model the {t['social_structure']} structure in your simulation.
   b) Explain how {t['environmental_factor']} affects meme spread and evolution in your model.
   c) Discuss any feedback loops between meme evolution, social structures, and environmental factors.

4. Simulation and Analysis (250-300 words):
   a) Describe how you would run a simulation using your model.
   b) Explain the key metrics you would use to analyze meme evolution and cultural change.
   c) Discuss how your model could generate insights about real-world cultural dynamics.
   d) Propose a hypothesis about {t['meme_type']} evolution that your model could test.
   e) Address the limitations and potential biases in your model.

5. Interdisciplinary Implications (150-200 words):
   a) Discuss how your model could inform research in cognitive science, AI, and cultural anthropology.
   b) Propose an innovative application of your model in a field such as marketing, public policy, or education.
   c) Suggest how your approach could be extended to model other complex social phenomena.

Ensure your response demonstrates a deep understanding of cognitive science, artificial intelligence, and cultural anthropology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1150-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address all five required sections as outlined in the instructions.",
            f"The model must specifically incorporate the meme type of {t['meme_type']}, the cognitive bias of {t['cognitive_bias']}, a {t['social_structure']} social structure, and the environmental factor of {t['environmental_factor']}.",
            "The response must demonstrate a deep understanding of cognitive science, artificial intelligence, and cultural anthropology.",
            "The proposed model must be innovative while remaining scientifically plausible.",
            "The response must include appropriate technical terminology and clear explanations for complex concepts.",
            "The response must adhere to the specified word count range (1150-1400 words) and formatting requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
