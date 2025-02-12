import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_processes = [
            "photosynthesis",
            "enzyme catalysis",
            "DNA mutation",
            "olfaction (smell)"
        ]
        quantum_effects = [
            "quantum tunneling",
            "quantum coherence",
            "quantum entanglement",
            "zero-point energy"
        ]
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                'biological_process': random.choice(biological_processes),
                'quantum_effect': random.choice(quantum_effects)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design and implement a quantum simulation model for the biological process of {t['biological_process']}, focusing on the potential influence of {t['quantum_effect']}. Your response should include the following sections:\n\n1. Quantum-Biological Model Design (300-350 words):\n   a) Describe the key components of your quantum simulation model for {t['biological_process']}.\n   b) Explain how you incorporate {t['quantum_effect']} into your model.\n   c) Discuss how your model bridges quantum mechanics and biology.\n   d) Provide a high-level diagram or pseudocode representing the core algorithm of your simulation.\n\n2. Quantum Effects in Biology (250-300 words):\n   a) Explain the potential role of {t['quantum_effect']} in {t['biological_process']}.\n   b) Describe how quantum effects might enhance or alter the efficiency of this biological process.\n   c) Discuss existing evidence or theories supporting quantum effects in this area of biology, citing at least two relevant scientific papers.\n\n3. Simulation Implementation (250-300 words):\n   a) Detail the mathematical framework used to model the quantum-biological system.\n   b) Explain how you handle the interface between quantum and classical regimes in your simulation.\n   c) Describe any novel computational techniques used to manage the complexity of the simulation.\n   d) Provide at least one example calculation or equation central to your model.\n\n4. Results and Analysis (200-250 words):\n   a) Present the expected outcomes of your quantum-biological simulation, including at least one quantitative prediction.\n   b) Compare these results to those from classical models of {t['biological_process']}.\n   c) Analyze the implications of your findings for our understanding of quantum biology.\n\n5. Experimental Validation (200-250 words):\n   a) Propose an experimental setup to test the predictions of your quantum-biological model.\n   b) Describe the key measurements and observations needed to validate your simulation.\n   c) Discuss potential challenges in experimentally verifying quantum effects in biological systems.\n\n6. Critical Evaluation (150-200 words):\n   a) Identify and discuss at least three potential limitations or challenges in your proposed model.\n   b) Suggest how these limitations might be addressed in future research.\n\n7. Implications and Future Directions (150-200 words):\n   a) Discuss the broader implications of quantum effects in biology.\n   b) Propose two potential applications stemming from your quantum-biological model.\n   c) Suggest areas for future research in quantum biology.\n\nEnsure your response demonstrates a deep understanding of both quantum mechanics and biology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1500-1800 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of both quantum mechanics and the biological process of {t['biological_process']}",
            f"The quantum simulation model effectively incorporates {t['quantum_effect']} and explains its potential influence on {t['biological_process']}",
            "The proposed model and analysis are scientifically plausible and innovative",
            "The response includes all required sections with appropriate detail and depth",
            "The response cites at least two relevant scientific papers",
            "The response includes at least one example calculation or equation",
            "The response provides at least one quantitative prediction",
            "The critical evaluation identifies and discusses at least three potential limitations or challenges",
            "The implications and future directions proposed are insightful and well-reasoned"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
