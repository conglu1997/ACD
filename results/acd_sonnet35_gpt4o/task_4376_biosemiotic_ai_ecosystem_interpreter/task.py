import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            {
                "ecosystem": "Coral Reef",
                "key_species": "Coral Polyps",
                "environmental_factor": "Ocean Acidification"
            },
            {
                "ecosystem": "Boreal Forest",
                "key_species": "Bark Beetles",
                "environmental_factor": "Rising Temperatures"
            },
            {
                "ecosystem": "Savanna Grassland",
                "key_species": "Acacia Trees",
                "environmental_factor": "Changing Rainfall Patterns"
            },
            {
                "ecosystem": "Mangrove Swamp",
                "key_species": "Mangrove Trees",
                "environmental_factor": "Sea Level Rise"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(ecosystems, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that interprets and translates biosemiotic signals within a {t['ecosystem']} ecosystem, focusing on {t['key_species']} as a key species and {t['environmental_factor']} as a critical environmental factor. Then, use your system to analyze and predict ecosystem changes. Your response should include the following sections:

1. AI System Architecture (300-350 words):
   a) Describe the main components of your AI system for interpreting biosemiotic signals.
   b) Explain how your system integrates principles from biosemiotics, ecology, and artificial intelligence.
   c) Detail how the system processes and interprets different types of biosemiotic signals.
   d) Include a simple text-based diagram or flowchart of your system architecture (this can be done using ASCII characters or simple text formatting).

2. Biosemiotic Signal Analysis (250-300 words):
   a) Identify and describe at least three types of biosemiotic signals relevant to the {t['ecosystem']} ecosystem.
   b) Explain how your AI system detects and interprets these signals, particularly those related to {t['key_species']}.
   c) Discuss how your system distinguishes between different levels of semiosis (e.g., vegetative, animal, and cultural semiosis).

3. Environmental Factor Integration (200-250 words):
   a) Describe how your system incorporates data on {t['environmental_factor']} into its analysis.
   b) Explain the potential impacts of {t['environmental_factor']} on biosemiotic processes in the ecosystem.
   c) Discuss how your AI system might detect early warning signs of ecosystem stress related to this factor.

4. Ecosystem Change Prediction (250-300 words):
   a) Outline the process your AI system uses to predict ecosystem changes based on biosemiotic signal analysis.
   b) Provide an example scenario of how your system might predict a specific change in the {t['ecosystem']}.
   c) Explain how your system accounts for the complex, non-linear nature of ecosystem dynamics in its predictions.

5. Ethical Considerations and Limitations (200-250 words):
   a) Discuss potential ethical implications of using AI to interpret and predict ecosystem changes.
   b) Address the limitations of your system, particularly in capturing the full complexity of biosemiotic processes.
   c) Propose guidelines for the responsible use and development of biosemiotic AI systems in ecological research and management.

6. Interdisciplinary Implications (150-200 words):
   a) Explore how this biosemiotic AI approach might benefit other scientific fields or applications.
   b) Discuss the potential impact of this technology on our understanding of communication in living systems.
   c) Propose an interdisciplinary research project that could emerge from this work.

Ensure your response demonstrates a deep understanding of biosemiotics, ecology, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1350-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The AI system design effectively integrates biosemiotics, ecology, and artificial intelligence principles for the {t['ecosystem']} ecosystem.",
            f"The response demonstrates a deep understanding of biosemiotic signals relevant to {t['key_species']} and the {t['ecosystem']}.",
            f"The system's approach to incorporating and analyzing {t['environmental_factor']} is well-explained and plausible.",
            "The ecosystem change prediction process is logically presented and accounts for ecosystem complexity.",
            "Ethical considerations and limitations are thoroughly addressed.",
            "The discussion of interdisciplinary implications is insightful and demonstrates creative thinking.",
            "The overall response is innovative, scientifically plausible, and well-structured.",
            "All required sections and subpoints are addressed in the response."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
