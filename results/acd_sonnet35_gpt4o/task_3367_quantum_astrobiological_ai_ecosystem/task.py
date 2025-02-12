import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "quantum coherence",
            "quantum entanglement",
            "quantum tunneling"
        ]
        astrobiological_challenges = [
            "extreme radiation",
            "microgravity",
            "limited resources"
        ]
        ecosystem_types = [
            "aquatic",
            "terrestrial",
            "atmospheric"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "astrobiological_challenge": random.choice(astrobiological_challenges),
                "ecosystem_type": random.choice(ecosystem_types)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "astrobiological_challenge": random.choice(astrobiological_challenges),
                "ecosystem_type": random.choice(ecosystem_types)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical AI-managed ecosystem for exoplanet colonization that incorporates principles of quantum biology and astrobiology. Your system should focus on the quantum principle of {t['quantum_principle']}, address the astrobiological challenge of {t['astrobiological_challenge']}, and be designed for a {t['ecosystem_type']} environment. Your response should include the following sections:

1. System Overview (250-300 words):
   a) Describe the key components of your quantum-biological AI ecosystem.
   b) Explain how it incorporates the specified quantum principle.
   c) Discuss how it addresses the given astrobiological challenge.
   d) Outline how the AI manages and optimizes the ecosystem.

2. Quantum-Biological Mechanisms (200-250 words):
   a) Detail how {t['quantum_principle']} is utilized in your ecosystem's biological processes.
   b) Explain how these quantum effects enhance the ecosystem's ability to thrive in an exoplanetary environment.
   c) Provide an example of a specific organism or process that leverages this quantum principle.

3. AI Management Systems (200-250 words):
   a) Describe the AI architecture used to manage the ecosystem.
   b) Explain how the AI monitors and maintains quantum coherence in the biological systems.
   c) Discuss how the AI adapts the ecosystem to address {t['astrobiological_challenge']}.

4. Ecosystem Dynamics (200-250 words):
   a) Explain how your {t['ecosystem_type']} ecosystem functions in an exoplanetary environment.
   b) Describe the key species or components and their interactions.
   c) Discuss how the ecosystem achieves stability and resilience.

5. Colonization Implications (150-200 words):
   a) Analyze the potential benefits and risks of using this system for exoplanet colonization.
   b) Discuss ethical considerations related to introducing this ecosystem to a new planet.
   c) Propose guidelines for responsible development and use of quantum-biological AI ecosystems.

6. Future Developments (100-150 words):
   a) Suggest two potential advancements or extensions of your system.
   b) Speculate on how this technology might evolve over the next century of space colonization.

Ensure your response demonstrates a deep understanding of quantum biology, artificial intelligence, and astrobiology. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum biology, AI, and astrobiology.",
            "The proposed system effectively incorporates the specified quantum principle and addresses the given astrobiological challenge.",
            "The ecosystem design is innovative, scientifically plausible, and suitable for the specified environment type.",
            "The AI management system is well-described and integrates effectively with the quantum-biological processes.",
            "The response addresses all required sections and stays within the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
