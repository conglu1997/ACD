import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        alien_species = [
            {
                "name": "Luminarians",
                "biology": "Bioluminescent organisms with multiple light-emitting organs",
                "environment": "Deep ocean planet with no sunlight"
            },
            {
                "name": "Gravitons",
                "biology": "Silicon-based lifeforms with variable density",
                "environment": "High-gravity planet with extreme atmospheric pressure"
            },
            {
                "name": "Chronomites",
                "biology": "Beings that experience time non-linearly",
                "environment": "Planet near a black hole with severe time dilation effects"
            }
        ]
        return {str(i+1): species for i, species in enumerate(random.sample(alien_species, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a communication system for the {t['name']} alien species.

Species characteristics:
- Biology: {t['biology']}
- Environment: {t['environment']}

Your task is to:

1. Create a detailed communication system that utilizes the unique biological features of the species and adapts to their environment. Your system should:
   a) Describe the primary mode of communication (e.g., visual, auditory, chemical)
   b) Explain how information is encoded and transmitted
   c) Describe how the system accounts for environmental challenges

2. Provide examples of how this communication system would represent the following concepts:
   a) Danger
   b) Cooperation
   c) Abstract idea (e.g., 'future' or 'beauty')

3. Analyze the advantages and limitations of this communication system compared to human language (3-4 sentences).

4. Explain how this communication system might influence the species' cognitive processes and social structures (3-4 sentences).

5. Propose an experiment to test the efficiency of this communication system in transmitting complex information (2-3 sentences).

6. Discuss potential challenges in establishing interspecies communication between humans and this alien species (2-3 sentences).

Ensure your response is creative yet grounded in scientific principles. Organize your answer using clear headings for each section. Your total response should not exceed 750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The communication system must be tailored to the {t['name']} species, considering their biology and environment",
            "The system should be logically consistent and scientifically plausible",
            "The response should provide specific examples of how concepts are communicated",
            "The analysis should consider advantages, limitations, and cognitive/social implications",
            "The proposed experiment should be relevant and potentially insightful",
            "The response should discuss challenges in interspecies communication",
            "The response should be well-organized with clear headings for each section",
            "The total response should not exceed 750 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
