import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_concept": "superposition",
                "biological_mechanism": "DNA replication",
                "information_theory_principle": "error correction"
            },
            {
                "quantum_concept": "entanglement",
                "biological_mechanism": "protein folding",
                "information_theory_principle": "data compression"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum-biological nanocomputer that uses DNA-based quantum gates for information processing. A quantum-biological nanocomputer is a hypothetical device that combines principles from quantum computing and molecular biology to perform computations at the nanoscale using biological molecules.

Your design should incorporate the quantum concept of {t['quantum_concept']}, the biological mechanism of {t['biological_mechanism']}, and the information theory principle of {t['information_theory_principle']}. Additionally, you must address the challenge of quantum decoherence in biological systems. Provide your response in the following format:

1. Conceptual Framework (250-300 words):
   a) Explain the key principles of {t['quantum_concept']}, {t['biological_mechanism']}, and {t['information_theory_principle']}.
   b) Discuss how these concepts could theoretically be integrated in a nanocomputer design.
   c) Describe any existing research or theories that support the possibility of such integration.

2. Nanocomputer Architecture (300-350 words):
   a) Outline the core components of your quantum-biological nanocomputer.
   b) Explain how DNA-based quantum gates would function in your design at the molecular level.
   c) Describe how {t['quantum_concept']} is implemented and maintained in a biological context.
   d) Discuss how {t['biological_mechanism']} is harnessed for computation.
   e) Explain how {t['information_theory_principle']} is incorporated into the system.

3. Quantum Decoherence Solution (200-250 words):
   a) Explain the challenge of quantum decoherence in biological systems.
   b) Propose a detailed, scientifically plausible solution to maintain quantum coherence in your nanocomputer.
   c) Discuss any trade-offs or limitations of your proposed solution.

4. Information Processing Mechanism (250-300 words):
   a) Detail the step-by-step process of how information would be input, processed, and output in your nanocomputer.
   b) Explain how quantum and biological processes work together in this information flow.
   c) Discuss any novel algorithms or computational paradigms enabled by this design.

5. Potential Applications (200-250 words):
   a) Propose three potential applications for your quantum-biological nanocomputer.
   b) Explain how each application leverages the unique capabilities of your design.
   c) Discuss potential advantages over classical and current quantum computing approaches.

6. Challenges and Limitations (200-250 words):
   a) Identify key technical or scientific challenges in implementing your design.
   b) Discuss any theoretical limitations of your quantum-biological approach.
   c) Propose potential solutions or areas for future research to address these challenges.

7. Ethical and Societal Implications (150-200 words):
   a) Analyze potential ethical concerns related to the development and use of such technology.
   b) Discuss possible societal impacts, both positive and negative.
   c) Propose guidelines for responsible development and application of quantum-biological computing.

8. Comparative Analysis (150-200 words):
   a) Compare your quantum-biological nanocomputer design to current quantum computing approaches.
   b) Discuss potential advantages and disadvantages of your approach.
   c) Speculate on how this technology might evolve in the next 50 years.

Ensure your response demonstrates a deep understanding of quantum physics, molecular biology, and information theory. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be creative and speculative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1700-2100 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately explains and integrates the concepts of {t['quantum_concept']}, {t['biological_mechanism']}, and {t['information_theory_principle']}.",
            "The nanocomputer design is highly creative, scientifically plausible, and explained in detail at the molecular level.",
            "The proposed solution for quantum decoherence in biological systems is innovative and well-reasoned.",
            "The response demonstrates an exceptional understanding of quantum physics, molecular biology, and information theory.",
            "The potential applications, challenges, and ethical implications are analyzed with depth and insight.",
            "The response is well-structured, following the specified format and word count guidelines.",
            "The proposed design and solutions show a high level of originality and potential for advancing the field of quantum-biological computing."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
