import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        alien_species = [
            {
                "name": "Luminous Cephalopoids",
                "environment": "Deep ocean planet with bioluminescent ecosystem",
                "physiology": "Octopus-like bodies with light-emitting chromatophores and electroreceptors"
            },
            {
                "name": "Crystalline Hive-Minds",
                "environment": "Low-gravity planet with silicon-based geology",
                "physiology": "Interconnected crystalline structures with piezoelectric properties"
            }
        ]
        return {str(i+1): species for i, species in enumerate(random.sample(alien_species, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biologically-based communication system for the alien species: {t['name']}

Environment: {t['environment']}
Physiology: {t['physiology']}

Your task is to create a detailed description of a communication system that this alien species could use, based on their unique biology and environment. Your response should include:

1. Communication Mechanism (250-300 words):
   a) Describe the primary method of communication used by the species.
   b) Explain how this method is rooted in their physiology and adapted to their environment.
   c) Discuss any secondary or auxiliary communication methods.

2. Information Encoding (200-250 words):
   a) Explain how information is encoded in the communication system.
   b) Describe the basic units of meaning (analogous to phonemes or morphemes in human language).
   c) Discuss how complex ideas or concepts are represented.

3. Syntax and Grammar (200-250 words):
   a) Outline the basic rules governing the structure of messages in this system.
   b) Explain how these rules relate to the species' cognitive processes and environmental needs.
   c) Provide examples of how messages are constructed.

4. Evolutionary Advantages (150-200 words):
   a) Discuss why this communication system would be advantageous for the species.
   b) Explain how it might have evolved.
   c) Describe any potential limitations or vulnerabilities of the system.

5. Interaction with Technology (150-200 words):
   a) Speculate on how this species might interface with technology using their communication system.
   b) Describe a hypothetical device or tool that could augment or translate their communication.

6. Comparison to Human Communication (100-150 words):
   a) Compare and contrast this alien communication system with human language.
   b) Discuss what insights about communication this system might provide to human linguists.

Ensure your response is scientifically plausible and consistent with the given physiological and environmental constraints. Be creative in your approach while maintaining logical coherence. Use appropriate scientific terminology and provide clear explanations for your design choices.

Format your response with clear headings for each section. Your total response should be between 1050-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The communication system is logically consistent with the alien species' physiology and environment",
            "The response demonstrates creativity and originality in the communication system design",
            "The explanation shows a deep understanding of biology, physics, and communication theory",
            "The response addresses all required sections with appropriate detail",
            "The proposed communication system is fundamentally different from human language while remaining plausible",
            "The response maintains scientific plausibility throughout"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
