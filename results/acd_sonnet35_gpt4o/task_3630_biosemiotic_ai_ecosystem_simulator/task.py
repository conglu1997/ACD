import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            {
                "ecosystem_type": "Coral Reef",
                "key_species": "Coral Polyps",
                "environmental_factor": "Ocean Acidification"
            },
            {
                "ecosystem_type": "Temperate Forest",
                "key_species": "Mycorrhizal Fungi",
                "environmental_factor": "Climate Change"
            }
        ]
        return {str(i+1): ecosystem for i, ecosystem in enumerate(ecosystems)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates and analyzes biosemiotic processes in a {t['ecosystem_type']} ecosystem, focusing on the interplay between genetic, epigenetic, and environmental information. Your system should model how {t['key_species']} interpret and respond to {t['environmental_factor']}. Your response should include:

1. Biosemiotic Framework (250-300 words):
   a) Explain the key principles of biosemiotics relevant to your simulation.
   b) Describe how you will model sign processes and meaning-making in {t['key_species']}.
   c) Discuss how your framework incorporates genetic, epigenetic, and environmental information.

2. AI System Architecture (300-350 words):
   a) Outline the main components of your AI system and their functions.
   b) Explain how your system models the biosemiotic processes in the ecosystem.
   c) Describe any novel algorithms or approaches used in your design.
   d) Discuss how your system integrates different types of information (genetic, epigenetic, environmental).

3. Simulation Process (250-300 words):
   a) Describe how your system simulates the response of {t['key_species']} to {t['environmental_factor']}.
   b) Explain how biosemiotic processes are represented and evolve in your simulation.
   c) Discuss how your system accounts for feedback loops and emergent properties in the ecosystem.

4. Data Integration and Analysis (200-250 words):
   a) Describe the types of data your system would use and generate.
   b) Explain how you would validate your simulation against real-world observations.
   c) Discuss potential insights your system could provide about the {t['ecosystem_type']} ecosystem.

5. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical implications of simulating and analyzing biosemiotic processes.
   b) Address limitations of your approach and how they might be mitigated.

6. Interdisciplinary Implications (150-200 words):
   a) Explore how your biosemiotic AI system might contribute to fields like ecology, genetics, and information theory.
   b) Discuss potential applications of your system beyond theoretical biology.

Ensure your response demonstrates a deep understanding of biosemiotics, ecology, genetics, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words. Include a word count at the end of your response.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of biosemiotics and its application to the specified ecosystem.",
            "The AI system architecture is clearly described and integrates principles from biosemiotics, ecology, and genetics.",
            "The simulation process effectively models the response of the key species to the environmental factor.",
            "The response addresses data integration, validation, and potential insights from the simulation.",
            "Ethical considerations and limitations of the approach are adequately discussed.",
            "The interdisciplinary implications and potential applications of the system are explored.",
            "The response is well-structured, uses appropriate terminology, and provides clear explanations for complex concepts.",
            "The response falls within the specified word count of 1300-1600 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
