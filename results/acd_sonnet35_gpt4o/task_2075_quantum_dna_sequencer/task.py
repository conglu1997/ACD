import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_techniques = [
            {
                "technique": "Quantum Fourier Transform",
                "description": "Efficiently performs Fourier transforms on quantum states",
                "application": "Analyzing repetitive DNA sequences"
            },
            {
                "technique": "Grover's Algorithm",
                "description": "Provides quadratic speedup for searching unsorted databases",
                "application": "Identifying specific genetic markers"
            },
            {
                "technique": "Quantum Phase Estimation",
                "description": "Estimates the phase of an eigenstate of a unitary operator",
                "application": "Determining DNA strand lengths"
            },
            {
                "technique": "Quantum Error Correction",
                "description": "Protects quantum information from decoherence and other errors",
                "application": "Ensuring accuracy in DNA base pair identification"
            }
        ]
        return {str(i+1): technique for i, technique in enumerate(random.sample(quantum_techniques, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a theoretical quantum computing algorithm for ultra-fast DNA sequencing and analysis, incorporating the quantum technique of {t['technique']}. Then, analyze its potential impact on genomics and personalized medicine. Your response should include the following sections:\n\n1. Quantum Algorithm Design (300-350 words):\n   a) Explain how you would use {t['technique']} in your DNA sequencing algorithm.\n   b) Describe the overall structure and steps of your quantum algorithm.\n   c) Discuss how your algorithm interfaces with classical DNA sequencing techniques.\n   d) Explain how your algorithm addresses the challenge of {t['application']}.\n   e) Include a high-level quantum circuit diagram or pseudocode for a key part of your algorithm.\n\n2. Performance Analysis (200-250 words):\n   a) Estimate the theoretical speed-up of your quantum algorithm compared to classical methods.\n   b) Analyze the potential accuracy improvements offered by your quantum approach.\n   c) Discuss any limitations or challenges in implementing your algorithm on current or near-term quantum hardware.\n\n3. Genomic Applications (200-250 words):\n   a) Describe how your quantum DNA sequencing algorithm could advance the field of genomics.\n   b) Propose a novel application of your algorithm in genetic research or clinical diagnostics.\n   c) Discuss how the improved speed and accuracy could impact large-scale genomic studies.\n\n4. Personalized Medicine Implications (200-250 words):\n   a) Analyze how your quantum algorithm could enhance personalized medicine approaches.\n   b) Describe a specific scenario where your algorithm could improve patient outcomes.\n   c) Discuss ethical considerations related to the increased speed and scale of genetic analysis.\n\n5. Future Directions and Challenges (150-200 words):\n   a) Propose potential improvements or extensions to your quantum DNA sequencing algorithm.\n   b) Discuss how your approach could be combined with other quantum or classical techniques for enhanced performance.\n   c) Identify key technological advances needed to fully realize the potential of your algorithm.\n\nEnsure your response demonstrates a deep understanding of quantum computing, genomics, and information theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.\n\nYour total response should be between 1050-1300 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The quantum algorithm design effectively incorporates {t['technique']} for DNA sequencing and addresses {t['application']}.",
            "The response includes a clear quantum circuit diagram or pseudocode for a key part of the algorithm.",
            "The performance analysis provides a reasonable estimate of speed-up and accuracy improvements.",
            "The genomic applications and personalized medicine implications are well-reasoned and innovative.",
            "The response demonstrates a deep understanding of quantum computing, genomics, and information theory.",
            "The proposed future directions and challenges are insightful and scientifically plausible.",
            "The response is well-structured, following the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
