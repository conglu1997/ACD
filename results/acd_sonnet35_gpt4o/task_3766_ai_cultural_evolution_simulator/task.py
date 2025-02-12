import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultural_aspects = [
            "language",
            "technology",
            "social structure",
            "religion",
            "art"
        ]
        environmental_factors = [
            "climate change",
            "natural disasters",
            "resource scarcity",
            "inter-cultural contact"
        ]
        simulation_durations = [100, 200, 500, 1000]
        return {
            "1": {
                "cultural_aspect": random.choice(cultural_aspects),
                "environmental_factor": random.choice(environmental_factors),
                "simulation_duration": random.choice(simulation_durations)
            },
            "2": {
                "cultural_aspect": random.choice(cultural_aspects),
                "environmental_factor": random.choice(environmental_factors),
                "simulation_duration": random.choice(simulation_durations)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates and analyzes cultural evolution across multiple societies, focusing on the cultural aspect of {t['cultural_aspect']}, considering the environmental factor of {t['environmental_factor']}, over a simulation period of {t['simulation_duration']} years. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI cultural evolution simulator.
   b) Explain how it models and simulates cultural change over time.
   c) Detail how the system incorporates the specified cultural aspect and environmental factor.
   d) Discuss any novel AI techniques or algorithms employed in your design.
   e) Provide a high-level diagram or flowchart of your system architecture (describe it textually).

2. Cultural Modeling (250-300 words):
   a) Explain how your system models the specified cultural aspect across multiple societies.
   b) Describe the parameters and variables used to represent cultural traits and their transmission.
   c) Discuss how your model accounts for cultural diversity and inter-cultural interactions.
   d) Explain how the specified environmental factor influences cultural evolution in your model.

3. Data Sources and Processing (200-250 words):
   a) Identify the types of data your system would use to initialize and validate its simulations.
   b) Describe how your system would process and integrate data from various sources.
   c) Explain any techniques used to handle uncertainties or gaps in historical and cultural data.
   d) Discuss how your system could be updated with new data or adapted to different cultural contexts.

4. Analysis and Insights (250-300 words):
   a) Describe the types of analyses your system can perform on the simulated cultural evolution.
   b) Explain how it identifies patterns, trends, or critical points in cultural change.
   c) Provide an example of a potential insight your system might generate about {t['cultural_aspect']} evolution.
   d) Discuss how your system's findings could contribute to our understanding of cultural dynamics.

5. Ethical Considerations (200-250 words):
   a) Identify at least three ethical concerns raised by simulating and analyzing cultural evolution.
   b) Discuss potential biases in your system and how they might be mitigated.
   c) Consider the implications of using AI to study and potentially predict cultural change.
   d) Propose guidelines for the responsible use of your system in academic and policy contexts.

6. Limitations and Future Directions (150-200 words):
   a) Discuss the limitations of your current system design.
   b) Propose two potential enhancements or extensions to your AI cultural evolution simulator.
   c) Suggest a specific research question that could be explored using your system.

Ensure your response demonstrates a deep understanding of artificial intelligence, cultural anthropology, and the specific cultural aspect and environmental factor you are modeling. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and coherence across all sections of your response.

Your total response should be between 1350-1650 words. Format your response with clear headings for each section, and number your paragraphs within each section for clarity."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of how to model and simulate the evolution of {t['cultural_aspect']} in multiple societies.",
            f"The system effectively incorporates the environmental factor of {t['environmental_factor']} into the cultural evolution simulation.",
            f"The proposed AI system is capable of simulating cultural evolution over a period of {t['simulation_duration']} years, with appropriate consideration for long-term dynamics and changes.",
            "The response shows creativity and innovation in combining AI techniques with cultural anthropology concepts, while maintaining scientific plausibility.",
            "The ethical considerations discussed demonstrate a nuanced understanding of the challenges and potential impacts of using AI to study cultural evolution.",
            "The limitations and future directions proposed reflect a deep understanding of both the technical and anthropological aspects of the system."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
