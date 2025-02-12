import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "quantum entanglement",
            "quantum superposition",
            "quantum tunneling"
        ]
        astrobiological_challenges = [
            "extreme radiation",
            "microgravity adaptation",
            "extraterrestrial biosignature detection"
        ]
        ethical_dilemmas = [
            "resource allocation",
            "first contact protocols",
            "planetary protection"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "astrobiological_challenge": random.choice(astrobiological_challenges),
                "ethical_dilemma": random.choice(ethical_dilemmas)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "astrobiological_challenge": random.choice(astrobiological_challenges),
                "ethical_dilemma": random.choice(ethical_dilemmas)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system for deep space exploration that integrates quantum computing, astrobiology, and ethical decision-making principles. Your system should focus on the quantum principle of {t['quantum_principle']}, address the astrobiological challenge of {t['astrobiological_challenge']}, and incorporate ethical considerations related to {t['ethical_dilemma']}. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for deep space exploration.
   b) Explain how it incorporates the specified quantum principle.
   c) Discuss how it addresses the given astrobiological challenge.
   d) Outline how ethical considerations are integrated into the system's decision-making process.

2. Quantum-Astrobiological Interface (250-300 words):
   a) Detail how {t['quantum_principle']} is utilized in your system's approach to {t['astrobiological_challenge']}.
   b) Explain how this quantum-astrobiological interface enhances deep space exploration capabilities.
   c) Provide an example of a specific exploration scenario that leverages this interface.

3. Ethical Decision-Making Framework (200-250 words):
   a) Describe the AI's ethical decision-making framework, focusing on {t['ethical_dilemma']}.
   b) Explain how this framework interacts with the quantum and astrobiological components.
   c) Discuss potential conflicts between exploration goals and ethical considerations.

4. Deep Space Mission Simulation (250-300 words):
   a) Simulate a deep space exploration mission using your AI system.
   b) Describe how the system would handle a complex scenario involving the specified quantum principle, astrobiological challenge, and ethical dilemma.
   c) Analyze the potential outcomes and implications of the AI's decisions.

5. Limitations and Future Developments (150-200 words):
   a) Discuss the current limitations of your proposed system.
   b) Suggest potential advancements or improvements for future iterations.
   c) Speculate on the long-term implications of such AI systems for space exploration and human knowledge.

Ensure your response demonstrates a deep understanding of quantum computing, astrobiology, artificial intelligence, and ethical philosophy. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1150-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must include a clear description of an AI system for deep space exploration that incorporates {t['quantum_principle']}, addresses {t['astrobiological_challenge']}, and considers ethical issues related to {t['ethical_dilemma']}.",
            "The system architecture should be well-defined and demonstrate integration of quantum computing, astrobiology, and ethical decision-making.",
            "The quantum-astrobiological interface should be explained in detail, with a clear example provided.",
            "The ethical decision-making framework should be thoroughly described and integrated with the technical aspects of the system.",
            "The deep space mission simulation should demonstrate the system's capabilities in handling complex scenarios.",
            "The response should show a deep understanding of quantum computing, astrobiology, AI, and ethical philosophy, using appropriate terminology and concepts from each field."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
