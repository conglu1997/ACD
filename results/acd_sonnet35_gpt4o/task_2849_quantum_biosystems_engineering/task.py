import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_bio_systems = [
            {
                "system": "Quantum-enhanced photosynthesis",
                "application": "Improved solar energy harvesting",
                "quantum_effect": "Coherent energy transfer"
            },
            {
                "system": "Quantum-guided enzyme catalysis",
                "application": "Novel pharmaceutical synthesis",
                "quantum_effect": "Quantum tunneling"
            },
            {
                "system": "Quantum-based magnetoreception",
                "application": "Bio-inspired navigation technologies",
                "quantum_effect": "Radical pair mechanism"
            },
            {
                "system": "Quantum coherence in protein folding",
                "application": "Engineered proteins for targeted drug delivery",
                "quantum_effect": "Quantum superposition"
            }
        ]
        return {
            "1": random.choice(quantum_bio_systems),
            "2": random.choice(quantum_bio_systems)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum-enhanced biological system based on {t['system']} for the application of {t['application']}. Your task is to create a detailed proposal for this quantum biosystem, addressing the following points:

1. System Overview (200-250 words):
   - Describe the key components of your quantum-enhanced biological system.
   - Explain how it incorporates the quantum effect of {t['quantum_effect']}.
   - Discuss how this system improves upon existing non-quantum biological processes.

2. Quantum-Biological Mechanism (250-300 words):
   - Detail the proposed mechanism by which quantum effects enhance the biological process.
   - Explain how quantum coherence is maintained in a typically noisy biological environment.
   - Discuss any biomolecular structures or processes that facilitate quantum effects.

3. Engineering and Implementation (200-250 words):
   - Propose a method for engineering or modifying biological systems to harness quantum effects.
   - Describe any artificial components or interfaces needed to implement your system.
   - Discuss potential challenges in realizing this system and propose solutions.

4. Performance Analysis (200-250 words):
   - Predict the performance improvements of your quantum-enhanced system compared to classical systems.
   - Describe methods to measure and verify quantum effects in your biological system.
   - Discuss any potential trade-offs or limitations of your approach.

5. Applications and Implications (150-200 words):
   - Explore potential applications of your quantum biosystem beyond the initial specified application.
   - Discuss broader implications for our understanding of quantum biology and life processes.
   - Consider any ethical implications or potential risks associated with this technology.

Ensure your response demonstrates a deep understanding of both quantum mechanics and biological processes. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility. Format your response using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of both quantum mechanics and biological processes.",
            f"The proposed quantum biosystem clearly incorporates the quantum effect of {t['quantum_effect']}.",
            f"The system effectively addresses the application of {t['application']}.",
            "The quantum-biological mechanism is well-explained and scientifically plausible.",
            "The engineering and implementation section addresses practical considerations and challenges.",
            "The performance analysis includes quantitative predictions and verification methods.",
            "The response explores broader applications and implications of the proposed system.",
            "The submission demonstrates creativity while maintaining scientific rigor.",
            "The response is well-structured with clear headings for each section as requested."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
