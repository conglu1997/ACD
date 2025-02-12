import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        species_environments = [
            {
                "species_type": "Aquatic cephalopods",
                "environment": "Deep ocean",
                "unique_trait": "Bioluminescent skin patterns"
            },
            {
                "species_type": "Arboreal mammals",
                "environment": "Dense rainforest",
                "unique_trait": "Prehensile tails"
            },
            {
                "species_type": "Social insects",
                "environment": "Underground colonies",
                "unique_trait": "Pheromone-based communication"
            },
            {
                "species_type": "Avian species",
                "environment": "Migratory patterns across continents",
                "unique_trait": "Syrinx-based vocalizations"
            }
        ]
        task1 = random.choice(species_environments)
        task2 = random.choice([se for se in species_environments if se != task1])
        return {
            "1": task1,
            "2": task2
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a hypothetical evolutionary trajectory of language development for the following non-human species:

Species type: {t['species_type']}
Environment: {t['environment']}
Unique trait: {t['unique_trait']}

Your response should include the following sections:

1. Species Characteristics (200-250 words):
   a) Describe the species' physical and cognitive characteristics relevant to language development.
   b) Explain how the environment influences their communication needs and abilities.
   c) Discuss how their unique trait could be co-opted or adapted for language use.

2. Evolutionary Pressure (200-250 words):
   a) Identify key evolutionary pressures that might drive language development in this species.
   b) Explain how these pressures interact with the species' environment and traits.
   c) Propose a timeline for the evolution of language in this species, with key milestones.

3. Language System Design (250-300 words):
   a) Describe the core features of the evolved language system (e.g., modality, syntax, semantics).
   b) Explain how these features are adapted to the species' biology and environment.
   c) Provide examples of how complex ideas might be expressed in this language system.
   d) Discuss any novel linguistic features that might emerge in this species' language.

4. Cognitive Adaptations (200-250 words):
   a) Describe the cognitive changes necessary to support this language system.
   b) Explain how these adaptations might affect other aspects of the species' cognition and behavior.
   c) Discuss potential limitations or trade-offs in cognitive evolution for language.

5. Comparative Analysis (200-250 words):
   a) Compare and contrast this hypothetical language system with human language.
   b) Identify any features that might be universal to all complex communication systems.
   c) Discuss how studying this hypothetical system could inform our understanding of human language evolution.

6. Speculative Implications (150-200 words):
   a) Propose how this species' language ability might further evolve in the future.
   b) Discuss potential implications for the species' social structure and culture.
   c) Suggest how this species' language ability might impact their ecosystem or planet.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and evolutionary biology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and speculative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above (1, 2, 3, 4, 5, 6). Begin each section with the heading on a new line, followed by your response for that section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must address all six required sections as outlined in the instructions.",
            "The language system design must be clearly adapted to the given species' characteristics and environment.",
            "The response must demonstrate a deep understanding of linguistics, cognitive science, and evolutionary biology.",
            "The proposed evolutionary trajectory and language system must be creative and novel while remaining scientifically plausible.",
            "The response must include appropriate technical terminology and clear explanations for complex concepts.",
            "The comparative analysis must provide meaningful insights into both the hypothetical language system and human language.",
            "The response must adhere to the specified word count range (1200-1500 words) and formatting requirements.",
            f"The response must specifically address the given species type ({t['species_type']}), environment ({t['environment']}), and unique trait ({t['unique_trait']})."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
