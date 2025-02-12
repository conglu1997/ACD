import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = [
            "quantum coherence",
            "quantum entanglement",
            "quantum tunneling",
            "superposition"
        ]
        biological_systems = [
            "photosynthetic complexes",
            "enzyme catalysis",
            "DNA",
            "neural networks"
        ]
        computational_tasks = [
            "optimization problems",
            "pattern recognition",
            "database searching",
            "cryptography"
        ]
        constraints = [
            "room temperature operation",
            "minimal energy consumption",
            "self-replication capability",
            "biocompatibility"
        ]
        return {
            "1": {
                "quantum_effect": random.choice(quantum_effects),
                "biological_system": random.choice(biological_systems),
                "computational_task": random.choice(computational_tasks),
                "constraint": random.choice(constraints)
            },
            "2": {
                "quantum_effect": random.choice(quantum_effects),
                "biological_system": random.choice(biological_systems),
                "computational_task": random.choice(computational_tasks),
                "constraint": random.choice(constraints)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum biological computer that harnesses {t['quantum_effect']} in {t['biological_system']} to perform {t['computational_task']}, while satisfying the constraint of {t['constraint']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum biological computer.
   b) Explain how {t['quantum_effect']} is utilized in {t['biological_system']}.
   c) Detail how this quantum-biological integration enables {t['computational_task']}.
   d) Explain how your design satisfies the constraint of {t['constraint']}.
   e) Include a diagram or schematic representation of your system (describe it textually).

2. Quantum-Biological Interface (250-300 words):
   a) Explain the mechanisms that allow quantum effects to persist in the biological environment.
   b) Describe how quantum information is encoded, processed, and read out from the biological system.
   c) Discuss any novel techniques or structures used to maintain quantum coherence while meeting the {t['constraint']} requirement.

3. Computational Model (200-250 words):
   a) Describe the computational paradigm of your system (e.g., gate-based, adiabatic, measurement-based).
   b) Explain how {t['computational_task']} is mapped onto your quantum biological system.
   c) Compare the theoretical performance of your system to classical computers for the given task.

4. Fabrication and Scalability (200-250 words):
   a) Propose methods for creating or isolating the quantum-active biological components.
   b) Discuss how your system could be scaled up for practical applications while maintaining {t['constraint']}.
   c) Address potential challenges in maintaining quantum effects as the system size increases.

5. Potential Applications (150-200 words):
   a) Suggest three potential applications of your quantum biological computer beyond {t['computational_task']}.
   b) For each application, explain how the unique properties of your system provide advantages over existing technologies.

6. Ethical and Safety Considerations (150-200 words):
   a) Discuss the ethical implications of creating hybrid quantum-biological systems.
   b) Address potential safety concerns and propose guidelines for responsible development and use of this technology.

7. Critical Analysis (200-250 words):
   a) Provide a critical analysis of your proposed quantum biological computer, discussing its strengths and potential weaknesses.
   b) Compare your system to a hypothetical classical biological computer designed for the same task.
   c) Identify any assumptions or speculative elements in your design and discuss their implications.

8. Quantum-Classical Hybrid Approaches (150-200 words):
   a) Discuss potential quantum-classical hybrid approaches that could enhance your system's performance or practicality.
   b) Explain how these hybrid approaches might address some of the limitations of a purely quantum biological system.

9. Novel Quantum Effects (100-150 words):
   a) Propose a novel quantum effect not listed in the given options that could potentially be harnessed in biological systems for computation.
   b) Briefly explain how this effect might be utilized and what advantages it could offer.

10. Future Research Directions (150-200 words):
    a) Identify key challenges or limitations in your current design, particularly related to {t['constraint']}.
    b) Propose two specific research directions to overcome these challenges or extend the capabilities of quantum biological computers.

Ensure your response demonstrates a deep understanding of quantum physics, biology, and computer science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1850-2350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should demonstrate a clear understanding of how {t['quantum_effect']} can be harnessed in {t['biological_system']} for computation.",
            f"The system design should effectively explain how {t['computational_task']} can be performed using the proposed quantum biological computer.",
            f"The proposed design should adequately address the constraint of {t['constraint']}.",
            "The response should show interdisciplinary knowledge integration across quantum physics, biology, and computer science.",
            "The proposed quantum biological computer should be innovative while maintaining scientific plausibility.",
            "The response should include a thoughtful critical analysis of the proposed system and a comparison with a classical biological computer.",
            "The discussion of quantum-classical hybrid approaches should be insightful and well-reasoned.",
            "The proposed novel quantum effect should be creative and potentially applicable to biological systems.",
            "The response should address ethical considerations and future research directions adequately."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
