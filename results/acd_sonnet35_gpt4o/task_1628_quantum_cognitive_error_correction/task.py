class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        import random
        tasks = [
            {
                'quantum_concept': 'superposition',
                'cognitive_process': 'working memory',
                'error_type': 'information degradation',
                'constraint': 'must incorporate at least one quantum gate operation'
            },
            {
                'quantum_concept': 'entanglement',
                'cognitive_process': 'long-term potentiation',
                'error_type': 'false memory formation',
                'constraint': 'must use a minimum of three qubits in the system design'
            }
        ]
        return {"1": tasks[0], "2": tasks[1]}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum error correction system for human memory, focusing on the quantum concept of {t['quantum_concept']}, the cognitive process of {t['cognitive_process']}, and addressing the error type of {t['error_type']}. Your system {t['constraint']}. Your response should include:

        1. Conceptual Framework (300-350 words):
           a) Explain how the specified quantum concept can be applied to the given cognitive process.
           b) Describe how this framework could potentially address the given error type in human memory.
           c) Discuss any novel insights or approaches your quantum-inspired method brings to cognitive error correction.
           d) Explain how your system satisfies the given constraint.

        2. System Architecture (250-300 words):
           a) Outline the key components of your quantum cognitive error correction system.
           b) Explain how these components interact to implement the error correction process.
           c) Describe any hypothetical quantum-biological interfaces necessary for your system.
           d) Include a simple diagram or flowchart illustrating the system architecture.

        3. Error Correction Mechanism (250-300 words):
           a) Detail the specific mechanism by which your system would correct or prevent the given error type.
           b) Explain how this mechanism incorporates both quantum and cognitive principles.
           c) Provide a step-by-step description of the error correction process.
           d) Include a mathematical representation or pseudo-code of a key part of your error correction algorithm.

        4. Theoretical Predictions and Validation (200-250 words):
           a) Hypothesize about the expected effects of your system on human memory and cognition.
           b) Identify potential side effects or unintended consequences of the error correction process.
           c) Propose a detailed experiment to test the efficacy and safety of your system, including methodology and expected results.
           d) Discuss how you would measure and quantify the success of your system.

        5. Ethical and Philosophical Implications (200-250 words):
           a) Discuss the ethical considerations of enhancing human memory through quantum methods.
           b) Explore the philosophical implications of quantum-assisted cognition for concepts of consciousness and free will.
           c) Propose guidelines for responsible development and use of quantum cognitive technologies.
           d) Address potential societal impacts if this technology becomes widely available.

        Ensure your response demonstrates a deep understanding of both quantum physics and cognitive neuroscience. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

        Format your response with clear headings for each section and subsections labeled a, b, c, d. Your total response should be between 1200-1450 words.
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding and creative application of {t['quantum_concept']} to {t['cognitive_process']}.",
            f"The proposed system effectively addresses {t['error_type']} and satisfies the constraint: {t['constraint']}.",
            "The system architecture and error correction mechanism are logically consistent and incorporate both quantum and cognitive principles.",
            "The theoretical predictions are well-reasoned, and the proposed experiment is detailed and scientifically plausible.",
            "The discussion of ethical and philosophical implications is thoughtful and comprehensive.",
            "The response includes all required elements: conceptual framework, system architecture, error correction mechanism, theoretical predictions, and ethical implications.",
            "The overall response is well-structured, coherent, and adheres to the word count guidelines for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
