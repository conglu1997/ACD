import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'quantum_principle': 'Quantum entanglement',
                'biological_structure': 'Cell membrane',
                'information_encoding': 'Amplitude encoding'
            },
            {
                'quantum_principle': 'Quantum superposition',
                'biological_structure': 'DNA molecule',
                'information_encoding': 'Phase encoding'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum-biological communication system for a microscopic organism, integrating principles from quantum physics, molecular biology, and information theory. Use the following specifications:

Quantum Principle: {t['quantum_principle']}
Biological Structure: {t['biological_structure']}
Information Encoding: {t['information_encoding']}

Your task:
1. Briefly explain the given quantum principle, biological structure, and information encoding method (2-3 sentences each).
2. Design a quantum-biological communication system that incorporates these elements. Describe its key components and functioning (5-6 sentences).
3. Explain how your system encodes, transmits, and decodes information at the quantum-biological level (4-5 sentences).
4. Provide two specific examples of how your system could be used by the microscopic organism to communicate or process information.
5. Analyze the potential advantages and limitations of your system compared to classical biological communication methods (3-4 sentences).
6. Discuss the implications of your system for our understanding of quantum effects in biological systems and potential applications in fields such as medicine or computing (3-4 sentences).
7. Propose an experiment to detect or verify the quantum-biological communication in a laboratory setting (3-4 sentences).

Format your response with clear headings for each section. Ensure your design is creative yet grounded in scientific principles, demonstrating a deep understanding of quantum physics, molecular biology, and information theory."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation of the quantum principle, biological structure, and information encoding method is accurate and clear.",
            "The quantum-biological communication system design creatively incorporates the given elements in a scientifically plausible manner.",
            "The explanation of information encoding, transmission, and decoding demonstrates a deep understanding of both quantum and biological processes.",
            "The examples provided are specific, relevant, and illustrate the system's potential use by microscopic organisms.",
            "The analysis of advantages and limitations shows critical thinking and comparison with classical methods.",
            "The discussion of implications demonstrates an understanding of the broader scientific context and potential applications.",
            "The proposed experiment is feasible and relevant to detecting or verifying the quantum-biological communication.",
            "The overall response showcases interdisciplinary knowledge integration and creative scientific thinking."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
