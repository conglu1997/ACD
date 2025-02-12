import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "biological_process": "Protein folding",
                "quantum_feature": "Superposition",
                "information_theory_concept": "Entropy"
            },
            {
                "biological_process": "DNA replication",
                "quantum_feature": "Entanglement",
                "information_theory_concept": "Error correction"
            },
            {
                "biological_process": "Cellular signaling",
                "quantum_feature": "Quantum tunneling",
                "information_theory_concept": "Channel capacity"
            },
            {
                "biological_process": "Enzyme catalysis",
                "quantum_feature": "Quantum coherence",
                "information_theory_concept": "Mutual information"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system that simulates the biological process of {t['biological_process']} at the molecular level, integrating principles from quantum mechanics, biology, and information theory. Your system should specifically leverage the quantum feature of {t['quantum_feature']} and incorporate the information theory concept of {t['information_theory_concept']}. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the overall structure of your quantum bioinformatics simulator.
   b) Explain how it integrates quantum computing principles with biological modeling.
   c) Detail the key components and their roles in the simulation process.
   d) Discuss how {t['quantum_feature']} is implemented and utilized in your system.

2. Biological Process Modeling (250-300 words):
   a) Explain how your system models {t['biological_process']} at the molecular level.
   b) Describe the quantum algorithms or techniques used to simulate this process.
   c) Discuss how your approach improves upon classical simulation methods.

3. Information Theory Integration (200-250 words):
   a) Explain how {t['information_theory_concept']} is incorporated into your system.
   b) Discuss the relevance of this concept to the biological process and quantum simulation.
   c) Describe any novel insights or advantages gained by this integration.

4. Quantum-Classical Interface (200-250 words):
   a) Explain how your system interfaces between quantum and classical computing components.
   b) Discuss challenges in data input/output and how you address them.
   c) Describe any error correction or noise mitigation techniques employed.

5. Simulation Results and Analysis (250-300 words):
   a) Provide a hypothetical set of results from your quantum bioinformatics simulator.
   b) Analyze these results in the context of current biological understanding.
   c) Discuss any unexpected findings or potential new insights into {t['biological_process']}.

6. Comparative Analysis (200-250 words):
   a) Compare your quantum approach to classical computational methods for simulating {t['biological_process']}.
   b) Discuss the advantages and limitations of your system.
   c) Analyze the computational complexity and scalability of your approach.

7. Future Implications and Ethics (150-200 words):
   a) Discuss potential future applications of your quantum bioinformatics simulator.
   b) Explore ethical considerations in quantum-enhanced biological simulations.
   c) Propose guidelines for responsible development and use of such technology.

Ensure your response demonstrates a deep understanding of quantum computing, molecular biology, and information theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1550-1900 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of quantum computing, molecular biology, and information theory.",
            f"The system design effectively integrates {t['quantum_feature']} and {t['information_theory_concept']} in modeling {t['biological_process']}.",
            "The proposed quantum bioinformatics simulator is innovative, detailed, and scientifically plausible.",
            "The explanation of the biological process modeling is thorough and demonstrates how quantum computing enhances the simulation.",
            "The integration of information theory concepts is well-explained and justified.",
            "The quantum-classical interface and its challenges are adequately addressed.",
            "The hypothetical results and analysis demonstrate insight into the biological process and the potential of quantum simulation.",
            "The comparative analysis with classical methods is comprehensive and balanced.",
            "Future implications and ethical considerations are thoughtfully explored.",
            "The response maintains coherence and relevance throughout all sections and adheres to the specified word limits."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
