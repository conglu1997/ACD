import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_processes = [
            "Photosynthesis",
            "Enzyme catalysis",
            "DNA mutation",
            "Magnetoreception in birds",
            "Olfaction (sense of smell)"
        ]
        quantum_phenomena = [
            "Quantum tunneling",
            "Quantum coherence",
            "Quantum entanglement",
            "Superposition",
            "Quantum oscillations"
        ]
        applications = [
            "Drug design",
            "Artificial photosynthesis",
            "Quantum sensors for medical diagnostics",
            "Optimizing chemical reactions",
            "Improving energy transfer in solar cells"
        ]
        tasks = [
            {
                "biological_process": random.choice(biological_processes),
                "quantum_phenomenon": random.choice(quantum_phenomena),
                "potential_application": random.choice(applications)
            },
            {
                "biological_process": random.choice(biological_processes),
                "quantum_phenomenon": random.choice(quantum_phenomena),
                "potential_application": random.choice(applications)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing simulation to model the biological process of {t['biological_process']} at the quantum level, focusing on the quantum phenomenon of {t['quantum_phenomenon']}. Then, analyze its implications for our understanding of life processes and potential applications in {t['potential_application']}. Your response should include the following sections:

1. Quantum-Biological System Analysis (250-300 words):
   a) Explain the current understanding of how {t['quantum_phenomenon']} may play a role in {t['biological_process']}.
   b) Discuss the challenges in studying this quantum-biological interaction experimentally.
   c) Identify the key parameters and variables that your simulation needs to account for.

2. Quantum Simulation Design (300-350 words):
   a) Describe the quantum computing approach you will use for your simulation (e.g., gate-based, adiabatic, or quantum annealing).
   b) Explain how you will model the biological system using quantum states and operations.
   c) Detail the steps of your quantum algorithm, including initialization, quantum operations, and measurement.
   d) Discuss how your simulation leverages quantum computing capabilities to model the biological process more effectively than classical methods.
   e) Provide a simple pseudocode or circuit diagram (using ASCII characters) of your quantum algorithm (10-15 lines).

3. Classical-Quantum Hybrid Approach (200-250 words):
   a) Describe any classical pre-processing or post-processing steps required for your simulation.
   b) Explain how you will integrate classical biological models with your quantum simulation.
   c) Discuss the advantages and limitations of your hybrid approach.

4. Simulation Validation and Analysis (200-250 words):
   a) Propose methods to validate your quantum simulation against experimental data or established theories.
   b) Describe how you would analyze the results of your simulation to gain insights into the biological process.
   c) Discuss potential sources of error or uncertainty in your simulation and how you would address them.

5. Implications and Applications (250-300 words):
   a) Analyze how your quantum simulation could enhance our understanding of {t['biological_process']} at the quantum level.
   b) Discuss the potential implications of your findings for broader theories in quantum biology.
   c) Explore how your simulation approach could be applied to {t['potential_application']}, providing specific examples.
   d) Identify any ethical considerations or potential risks associated with this research or its applications.

6. Future Directions (150-200 words):
   a) Propose two potential improvements or extensions to your quantum simulation approach.
   b) Suggest a novel research question in quantum biology that could be explored using your simulation method.
   c) Speculate on how advances in quantum computing hardware might impact the feasibility and accuracy of your simulation in the next decade.

Ensure your response demonstrates a deep understanding of quantum mechanics, biology, and complex systems modeling. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a well-designed quantum computing simulation for modeling {t['biological_process']} at the quantum level, focusing on {t['quantum_phenomenon']}",
            "The quantum simulation design is scientifically plausible and leverages quantum computing capabilities effectively",
            "The response demonstrates a deep understanding of quantum mechanics, biology, and complex systems modeling",
            "The proposed simulation validation and analysis methods are thorough and scientifically sound",
            f"The implications and potential applications in {t['potential_application']} are well-explored and innovative",
            "The response is well-structured, clear, and adheres to the specified word limits for each section",
            "The proposed future directions and research questions are insightful and demonstrate creative thinking in the field of quantum biology"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
