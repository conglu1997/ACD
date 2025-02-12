class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "biological_structure": "Microtubules",
                "quantum_effect": "Quantum coherence",
                "computational_task": "Pattern recognition"
            },
            "2": {
                "biological_structure": "DNA",
                "quantum_effect": "Quantum tunneling",
                "computational_task": "Optimization problems"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum-biological computing system that leverages quantum effects in biological structures to perform complex computations. Your system should utilize {t['biological_structure']} as the primary biological component, incorporate {t['quantum_effect']} as the key quantum effect, and be optimized for {t['computational_task']}. Your response should include:

        1. System Architecture (300-350 words):
           a) Describe the key components of your quantum-biological computing system.
           b) Explain how your system integrates the specified biological structure and quantum effect.
           c) Detail how these components work together to perform the given computational task.
           d) Provide a diagram or detailed description of your system's structure (use ASCII characters or simple text formatting).

        2. Quantum-Biological Interface (250-300 words):
           a) Explain the mechanisms by which quantum effects are harnessed in the biological component.
           b) Describe how information is encoded, processed, and read out from the system.
           c) Address potential issues of decoherence and propose solutions.

        3. Computational Paradigm (250-300 words):
           a) Describe the computational model of your system (e.g., how it represents and manipulates data).
           b) Explain how your system performs the specified computational task.
           c) Compare the theoretical performance of your system to classical computing approaches for this task.

        4. Fabrication and Operation (200-250 words):
           a) Propose a theoretical method for fabricating or growing your quantum-biological computing system.
           b) Describe the operating conditions required (e.g., temperature, environment).
           c) Discuss any challenges in maintaining and scaling up such a system.

        5. Potential Applications (150-200 words):
           a) Suggest three potential applications of your quantum-biological computing system beyond the specified task.
           b) Briefly explain how each application could benefit from this novel computing paradigm.

        6. Ethical and Societal Implications (150-200 words):
           a) Discuss potential ethical concerns or societal impacts of developing such technology.
           b) Propose guidelines for responsible research and development in this field.

        7. Future Research Directions (200-250 words):
           a) Identify key challenges that need to be overcome to realize such a system.
           b) Propose two specific research questions that arise from your design.
           c) Speculate on how this technology might evolve in the next 20-30 years.

        Ensure your response demonstrates a deep understanding of quantum mechanics, biology, and computer science. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

        Format your response with clear headings for each section, numbered as above. Your total response should be between 1500-1850 words.
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all seven required sections with appropriate content and adheres to the specified word counts.",
            f"The system architecture clearly integrates {t['biological_structure']} and {t['quantum_effect']} in a plausible manner.",
            f"The computational paradigm effectively addresses how the system performs {t['computational_task']}.",
            "The quantum-biological interface is well-explained, addressing issues like decoherence.",
            "The fabrication and operation section provides plausible theoretical methods and discusses challenges.",
            "Potential applications, ethical implications, and future research directions are thoughtfully explored.",
            "The response demonstrates a deep understanding of quantum mechanics, biology, and computer science, using appropriate terminology.",
            "The proposed system is innovative while maintaining scientific plausibility.",
            "The response stays within the overall word limit of 1500-1850 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
