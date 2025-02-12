import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_concept": "Quantum Fourier Transform",
                "biological_process": "DNA replication",
                "sequencing_challenge": "Repetitive sequences",
                "dna_sequence": "ATCGATCGATCGATCGATCG",
                "quantum_state": "|ψ⟩ = (|0⟩ + |1⟩) / √2"
            },
            {
                "quantum_concept": "Quantum error correction",
                "biological_process": "Gene expression",
                "sequencing_challenge": "Low-frequency mutations",
                "dna_sequence": "ATGCATGCATGCATGCATGC",
                "quantum_state": "|ψ⟩ = α|0⟩ + β|1⟩"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system for ultra-fast DNA sequencing and analysis, incorporating the quantum concept of {t['quantum_concept']}, addressing the biological process of {t['biological_process']}, and focusing on the sequencing challenge of {t['sequencing_challenge']}. Use the provided DNA sequence {t['dna_sequence']} and quantum state {t['quantum_state']} in your examples. Your response should include:

1. System Architecture (250-300 words):
   a) Key components of your quantum DNA sequencing system
   b) Interaction between components for sequencing and analysis
   c) Integration of the specified quantum concept
   d) Quantum circuit diagram or schematic representation

2. Quantum-Biological Interface (200-250 words):
   a) Interface mechanism between quantum states and DNA molecules
   b) Novel quantum sensing or measurement techniques
   c) Approach to maintaining quantum coherence in a biological context
   d) Example using the provided DNA sequence and quantum state

3. Sequencing and Analysis Process (250-300 words):
   a) Step-by-step process of DNA sequencing using your quantum system
   b) Approach to addressing the specified sequencing challenge
   c) Analysis of sequenced data, incorporating the biological process
   d) Computational complexity analysis compared to classical methods

4. Advantages and Innovations (200-250 words):
   a) Performance comparison with classical DNA sequencing methods
   b) At least two innovative features of your design
   c) Potential advancements in research for the specified biological process
   d) Quantitative estimates of improvement (e.g., speed, accuracy)

5. Technical Challenges and Solutions (200-250 words):
   a) Three major technical challenges in implementing your system
   b) Proposed solutions or approaches to address each challenge
   c) Trade-offs made in your design decisions
   d) Potential future improvements or research directions

6. Ethical Implications and Safeguards (150-200 words):
   a) Potential ethical concerns related to ultra-fast DNA sequencing and analysis
   b) Proposed safeguards or guidelines for responsible use
   c) Potential societal impacts of widespread access to this technology
   d) Recommendations for policy makers and researchers

Ensure your response demonstrates a deep understanding of both quantum computing and molecular biology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must include a detailed design of a quantum computing system for DNA sequencing and analysis, addressing all specified components and processes.",
            f"The system should clearly incorporate the quantum concept of {t['quantum_concept']} in its design and operation, with a specific example using the provided quantum state {t['quantum_state']}.",
            f"The response must explain how the system addresses the biological process of {t['biological_process']} and the sequencing challenge of {t['sequencing_challenge']}, using the provided DNA sequence {t['dna_sequence']} in an example.",
            "The quantum-biological interface should be clearly explained, including novel quantum sensing or measurement techniques and a specific approach to maintaining quantum coherence.",
            "The response should provide a step-by-step explanation of the DNA sequencing and analysis process, including a computational complexity analysis.",
            "At least two innovative features of the design should be highlighted and explained, with quantitative estimates of improvement over classical methods.",
            "The response must identify and propose solutions for three major technical challenges, including a discussion of trade-offs and future improvements.",
            "Ethical implications of the technology should be discussed, along with proposed safeguards, guidelines for responsible use, and recommendations for policy makers.",
            "The response should demonstrate a deep understanding of both quantum computing and molecular biology throughout, using appropriate terminology from both fields.",
            "The response should adhere to the specified format, including all subsections (a, b, c, d) for each main section, and the overall word count (1250-1550 words)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
