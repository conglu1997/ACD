import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_processes = [
            "protein folding",
            "DNA replication",
            "cellular signaling",
            "photosynthesis",
            "neural signal transmission",
            "enzyme catalysis",
            "membrane transport",
            "RNA interference"
        ]
        quantum_principles = [
            "superposition",
            "entanglement",
            "tunneling",
            "coherence",
            "quantum walks",
            "quantum annealing",
            "quantum error correction",
            "quantum Fourier transform"
        ]
        return {
            "1": {
                "biological_process": random.choice(biological_processes),
                "quantum_principle": random.choice(quantum_principles)
            },
            "2": {
                "biological_process": random.choice(biological_processes),
                "quantum_principle": random.choice(quantum_principles)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum computing system that simulates the biological process of {t['biological_process']} at the molecular level, incorporating the quantum principle of {t['quantum_principle']}. This task is speculative and may go beyond current technological capabilities. Your response should be in essay format, addressing the following points:

1. System Architecture (300-350 words):
   a) Describe the overall structure of your quantum bioinformatics simulation system.
   b) Explain how it incorporates principles from quantum mechanics, molecular biology, and information theory.
   c) Detail how the system models the specified biological process at the quantum level.
   d) Discuss how the given quantum principle is utilized in your simulation.

2. Quantum-Biological Interface (250-300 words):
   a) Explain how your system translates biological data into quantum states.
   b) Describe the mapping between biological features and quantum parameters.
   c) Discuss challenges in this translation process and how you address them.

3. Simulation Algorithm (250-300 words):
   a) Propose a quantum algorithm for simulating the specified biological process.
   b) Explain how this algorithm incorporates both quantum mechanical and biological principles.
   c) Describe how the algorithm ensures accuracy and efficiency in the simulation.

4. Information Theory Application (200-250 words):
   a) Discuss how information theory concepts are applied in your quantum bioinformatics system.
   b) Explain how these concepts enhance the simulation or analysis of the biological process.
   c) Propose a novel metric or approach for quantifying information in your quantum-biological system.

5. Potential Insights and Applications (250-300 words):
   a) Predict potential new insights about the biological process that could be gained from your quantum simulation.
   b) Propose two specific hypotheses that could be tested using your system.
   c) Discuss potential applications of your system in fields such as drug discovery, personalized medicine, or synthetic biology.

6. Technical Challenges and Solutions (200-250 words):
   a) Identify key technical challenges in implementing your quantum bioinformatics simulation system.
   b) Propose solutions or approaches to address these challenges.
   c) Discuss any limitations of current quantum hardware or algorithms that may impact your system.

7. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss ethical implications of using quantum simulations for biological research.
   b) Address potential misuses or unintended consequences of this technology.
   c) Propose a roadmap for future development of quantum bioinformatics, including key milestones and research questions.

Ensure your response demonstrates a deep understanding of quantum mechanics, molecular biology, and information theory. Be innovative in your approach while maintaining scientific plausibility. Use technical terminology appropriately and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1600-1950 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system must simulate the biological process of {t['biological_process']} at the molecular level.",
            f"The system must incorporate the quantum principle of {t['quantum_principle']}.",
            "The response must include a detailed system architecture that integrates quantum mechanics, molecular biology, and information theory.",
            "The response must explain how biological data is translated into quantum states.",
            "The response must propose a quantum algorithm for simulating the specified biological process.",
            "The response must discuss the application of information theory concepts in the quantum bioinformatics system.",
            "The response must predict potential new insights and propose testable hypotheses.",
            "The response must identify technical challenges and propose solutions.",
            "The response must address ethical considerations and propose future directions for quantum bioinformatics.",
            "The response must be well-structured with clear headings for each section and demonstrate a deep understanding of the relevant scientific principles.",
            "The response must be in essay format and within the specified word limit (1600-1950 words)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
