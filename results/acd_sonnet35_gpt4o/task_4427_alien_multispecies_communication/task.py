import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        species_traits = [
            "bioluminescent",
            "telepathic",
            "shape-shifting",
            "silicon-based",
            "hive-minded"
        ]
        communication_mediums = [
            "electromagnetic waves",
            "chemical signals",
            "gravitational fluctuations",
            "quantum entanglement",
            "plasma modulation"
        ]
        environmental_factors = [
            "high radiation levels",
            "extreme temperature fluctuations",
            "strong magnetic fields",
            "dense atmosphere",
            "low gravity"
        ]
        cultural_challenges = [
            "vastly different time perceptions",
            "conflicting ethical systems",
            "incompatible sensory organs",
            "divergent technological development",
            "fundamentally different cognitive processes"
        ]
        
        return {
            "1": {
                "species_trait": random.choice(species_traits),
                "communication_medium": random.choice(communication_mediums),
                "environmental_factor": random.choice(environmental_factors),
                "cultural_challenge": random.choice(cultural_challenges)
            },
            "2": {
                "species_trait": random.choice(species_traits),
                "communication_medium": random.choice(communication_mediums),
                "environmental_factor": random.choice(environmental_factors),
                "cultural_challenge": random.choice(cultural_challenges)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical communication system for a multi-species alien civilization where one species is {t['species_trait']}, primarily using {t['communication_medium']} for communication. The system must function in an environment with {t['environmental_factor']} and address the cultural challenge of {t['cultural_challenge']}. Your response should include the following sections:

1. Communication System Overview (300-350 words):
   a) Describe the key components and mechanisms of your alien communication system.
   b) Explain how it accommodates the {t['species_trait']} species and utilizes {t['communication_medium']}.
   c) Discuss how your system addresses the environmental challenge of {t['environmental_factor']}.
   d) Explain how your design considers the cultural challenge of {t['cultural_challenge']}.
   e) Include a conceptual diagram or schematic representation of your communication system (describe it in words, as if you were explaining a visual representation).

2. Linguistic and Information Theory Principles (250-300 words):
   a) Explain the underlying linguistic and information theory principles that make your system effective for multi-species communication.
   b) Discuss how {t['communication_medium']} is integrated with the biological traits of the {t['species_trait']} species.
   c) Address potential interactions between your communication system and the cognitive processes of different alien species.
   d) Propose a novel concept in xenolinguistics that emerges from your system design.

3. Technological Implementation (200-250 words):
   a) Outline the technological requirements for implementing your communication system.
   b) Discuss any challenges in developing and deploying the system across different alien species.
   c) Propose methods to ensure the system's compatibility with various alien physiologies and cognitive structures.
   d) Address how you would overcome challenges related to {t['environmental_factor']}.

4. Cross-Species Adaptation and Learning (200-250 words):
   a) Explain how different alien species would learn and adapt to use this communication system.
   b) Discuss potential misunderstandings or conflicts that could arise from cross-species communication.
   c) Propose strategies to mitigate these issues and promote effective inter-species dialogue.
   d) Consider how the system might evolve over time as species interact more frequently.

5. Ethical and Societal Implications (200-250 words):
   a) Identify and discuss key ethical concerns related to implementing this communication system across multiple alien species.
   b) Analyze the potential impact on the social structures and cultures of the participating alien civilizations.
   c) Propose ethical guidelines for the development and use of your cross-species communication system.
   d) Discuss how {t['cultural_challenge']} influences the ethical considerations of your design.

6. Future Developments and Scientific Applications (150-200 words):
   a) Suggest potential extensions or modifications of your communication system for other alien environments or species.
   b) Discuss how this technology might contribute to the field of xenology and our understanding of extraterrestrial intelligence.
   c) Propose areas for further research to advance cross-species communication technologies.

Ensure your response demonstrates a deep understanding of linguistics, information theory, biology, and speculative xenology. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and addressing real-world constraints.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response clearly describes a communication system for a multi-species alien civilization, accommodating a {t['species_trait']} species and utilizing {t['communication_medium']}, while addressing the environmental factor of {t['environmental_factor']} and the cultural challenge of {t['cultural_challenge']}.",
            "The design demonstrates a deep understanding of linguistics, information theory, biology, and speculative xenology, with appropriate use of scientific terminology and explanations.",
            "The communication system is innovative yet scientifically plausible, with a clear explanation of the underlying mechanisms and principles.",
            "The response adequately addresses potential challenges, ethical implications, and future developments related to cross-species communication.",
            "The submission is well-structured, following the required sections and word count guidelines.",
            "The proposed communication system and its analysis show creative problem-solving and interdisciplinary knowledge integration.",
            "The response includes a novel concept in xenolinguistics that emerges from the system design."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
