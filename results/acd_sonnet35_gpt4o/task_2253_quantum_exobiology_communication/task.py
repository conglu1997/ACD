import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_properties = [
            "entanglement",
            "superposition",
            "quantum tunneling",
            "quantum coherence"
        ]
        alien_environments = [
            "gas giant atmosphere",
            "subsurface ocean",
            "neutron star surface",
            "binary star system"
        ]
        communication_challenges = [
            "extreme distances",
            "time dilation effects",
            "signal interference",
            "energy efficiency"
        ]
        return {
            "1": {
                "quantum_property": random.choice(quantum_properties),
                "alien_environment": random.choice(alien_environments),
                "communication_challenge": random.choice(communication_challenges)
            },
            "2": {
                "quantum_property": random.choice(quantum_properties),
                "alien_environment": random.choice(alien_environments),
                "communication_challenge": random.choice(communication_challenges)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum-based communication system for a hypothetical extraterrestrial species living in a {t['alien_environment']}, utilizing the quantum property of {t['quantum_property']}, and addressing the communication challenge of {t['communication_challenge']}. Your response should include:

1. Extraterrestrial Species Design (200-250 words):
   a) Describe the key biological and cognitive characteristics of the species, considering their environment.
   b) Explain how their physiology and sensory systems are adapted to their environment.
   c) Hypothesize about their natural communication methods.

2. Quantum Communication System (250-300 words):
   a) Outline the core components and functioning of your quantum communication system.
   b) Explain how it incorporates the specified quantum property.
   c) Describe how the system is adapted to the species' biology and environment.
   d) Detail how it addresses the given communication challenge.

3. Information Encoding and Transmission (200-250 words):
   a) Propose a method for encoding information in your quantum system.
   b) Explain the transmission process, including any unique aspects due to the alien environment.
   c) Discuss how your system ensures information integrity over extreme distances or conditions.

4. Theoretical Implications (150-200 words):
   a) Discuss how your system might advance our understanding of quantum physics or exobiology.
   b) Propose a hypothesis about the nature of information or consciousness based on your design.
   c) Speculate on how this communication system might influence the species' evolution or culture.

5. Potential Earth Applications (150-200 words):
   a) Suggest how elements of your design could be applied to Earth-based communication systems.
   b) Discuss any technological breakthroughs that would be necessary to implement aspects of your system.
   c) Propose an experiment that could test a key principle of your communication system.

Ensure your response demonstrates a deep understanding of quantum physics, exobiology, and information theory. Be creative and speculative in your approach while maintaining scientific plausibility. Use technical terminology appropriately and provide explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 950-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all five required sections comprehensively.",
            f"The communication system design clearly incorporates the quantum property of {t['quantum_property']} and is adapted to the {t['alien_environment']}.",
            f"The design effectively addresses the communication challenge of {t['communication_challenge']}.",
            "The extraterrestrial species design is creative yet biologically plausible given the environment.",
            "The response demonstrates a deep understanding of quantum physics, exobiology, and information theory principles.",
            "The proposed system is innovative and original, showing interdisciplinary knowledge integration and speculative scientific reasoning."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
