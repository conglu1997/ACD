import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum coherence",
            "quantum measurement"
        ]
        biological_processes = [
            "photosynthesis",
            "enzyme catalysis",
            "DNA mutation",
            "cellular respiration",
            "neural signaling"
        ]
        atmospheric_components = [
            "methane",
            "oxygen",
            "carbon dioxide",
            "water vapor",
            "ammonia"
        ]
        information_theory_concepts = [
            "entropy",
            "mutual information",
            "channel capacity",
            "error correction",
            "data compression"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "biological_process": random.choice(biological_processes),
                "atmospheric_component": random.choice(atmospheric_components),
                "information_theory_concept": random.choice(information_theory_concepts)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "biological_process": random.choice(biological_processes),
                "atmospheric_component": random.choice(atmospheric_components),
                "information_theory_concept": random.choice(information_theory_concepts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing algorithm to detect and analyze potential biosignatures in exoplanet atmospheres, incorporating principles of quantum biology and information theory. Your algorithm should focus on the quantum principle of {t['quantum_principle']}, the biological process of {t['biological_process']}, the atmospheric component {t['atmospheric_component']}, and the information theory concept of {t['information_theory_concept']}. Your response should include the following sections:

1. Quantum Algorithm Design (300-350 words):
   a) Describe the overall structure and key components of your quantum algorithm.
   b) Explain how your algorithm incorporates the specified quantum principle.
   c) Detail how the algorithm interfaces with classical data processing systems.
   d) Provide a high-level quantum circuit diagram or pseudocode (describe it textually).

2. Biosignature Analysis Approach (250-300 words):
   a) Explain how your algorithm detects and analyzes the specified atmospheric component.
   b) Describe how your approach models the specified biological process as a potential biosignature.
   c) Discuss how quantum effects might enhance the detection or analysis of biosignatures.

3. Information Processing and Interpretation (250-300 words):
   a) Explain how your algorithm applies the specified information theory concept to biosignature data.
   b) Describe the data structures and quantum operations used to process spectral information.
   c) Discuss how your algorithm handles noise and uncertainty in exoplanet atmospheric data.

4. Quantum-Classical Hybrid System (200-250 words):
   a) Describe how your quantum algorithm integrates with classical pre- and post-processing steps.
   b) Explain any novel techniques used to maximize the advantages of both quantum and classical computing.
   c) Discuss potential challenges in implementing this hybrid system and propose solutions.

5. Performance Analysis and Comparison (200-250 words):
   a) Propose methods to evaluate the performance and accuracy of your quantum biosignature detector.
   b) Compare the expected performance of your algorithm to classical methods for exoplanet atmospheric analysis.
   c) Discuss the potential advantages and limitations of your quantum approach.

6. Implications and Future Directions (150-200 words):
   a) Discuss the broader implications of your quantum biosignature detector for astrobiology and exoplanet research.
   b) Propose two potential improvements or extensions to your algorithm.
   c) Suggest a novel research question that could be explored using your quantum biosignature detector as a foundation.

Ensure your response demonstrates a deep understanding of quantum computing, astrobiology, and information theory. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should demonstrate a clear understanding of the quantum principle {t['quantum_principle']} and how it can be applied to biosignature detection.",
            f"The algorithm should effectively incorporate the biological process of {t['biological_process']} and the atmospheric component {t['atmospheric_component']} in its biosignature analysis approach.",
            f"The information theory concept of {t['information_theory_concept']} should be well-integrated into the data processing and interpretation part of the algorithm.",
            "The response should address the challenges of implementing a quantum-classical hybrid system for exoplanet atmospheric analysis.",
            "The proposed performance analysis should be relevant and well-thought-out, considering the unique aspects of quantum computing in this application."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
