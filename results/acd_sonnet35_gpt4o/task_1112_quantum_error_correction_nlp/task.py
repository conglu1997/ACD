import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "quantum_principle": "Quantum superposition",
                "error_type": "Semantic drift",
                "nlp_task": "Text generation",
                "domain": "Scientific literature",
                "example_text": "The quantum entanglement of particles can lead to instantaneous communication across vast distances.",
                "context": "This example text contains a common misconception about quantum entanglement, presenting a challenge for error correction in scientific writing."
            },
            "2": {
                "quantum_principle": "Quantum entanglement",
                "error_type": "Contextual misinterpretation",
                "nlp_task": "Machine translation",
                "domain": "Legal documents",
                "example_text": "The parties hereto agree to be bound by the terms and conditions set forth in the quantum state of this agreement.",
                "context": "This example text illustrates the challenge of translating metaphorical language in legal documents, where precision is crucial."
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired error correction system for large language models based on the quantum principle of {t['quantum_principle']}. Your system should address the error type of {t['error_type']} in the NLP task of {t['nlp_task']}, specifically in the domain of {t['domain']}.

This task is relevant to AI development as it explores novel approaches to improving the reliability and accuracy of language models by drawing inspiration from quantum computing principles.

Your response should include the following sections:

1. Conceptual Framework (200-250 words):
   a) Explain the chosen quantum principle and its relevance to error correction in language models.
   b) Describe how the specified error type manifests in the given NLP task and domain.
   c) Propose a novel approach to apply the quantum principle to address the error type.
   d) Discuss potential limitations or challenges of applying quantum principles to NLP tasks.

2. System Design (250-300 words):
   a) Outline the key components of your quantum-inspired error correction system.
   b) Explain how your system integrates with existing language model architectures.
   c) Describe the process of detecting and correcting errors using your system.
   d) Include a high-level pseudocode or diagram illustrating your system's workflow.
   e) Compare your proposed system with existing error correction methods in NLP.

3. Error Correction Mechanism (200-250 words):
   a) Detail the specific techniques your system uses to identify and correct errors.
   b) Explain how these techniques are inspired by or analogous to quantum error correction methods.
   c) Discuss any trade-offs or limitations in your approach.
   d) Provide a specific example of how your system would correct an error in the following text: "{t['example_text']}"
   e) Explain why this example is challenging: {t['context']}

4. Performance Analysis (150-200 words):
   a) Propose metrics to evaluate the effectiveness of your error correction system.
   b) Describe an experimental setup to test your system's performance.
   c) Predict potential improvements in language model output quality.
   d) Discuss how you would validate that your system outperforms classical error correction methods.

5. Broader Implications (150-200 words):
   a) Discuss how your system could impact the field of NLP and language model development.
   b) Explore potential applications of your approach in other domains or AI tasks.
   c) Consider any ethical implications or challenges in implementing your system.
   d) Speculate on how your approach might influence future quantum-classical hybrid AI systems.

Ensure your response demonstrates a deep understanding of both quantum computing principles and natural language processing. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section and number your paragraphs within each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of {t['quantum_principle']} and its application to error correction in language models.",
            f"The proposed system effectively addresses {t['error_type']} in the context of {t['nlp_task']} for {t['domain']}.",
            "The system design is innovative, well-explained, and scientifically plausible.",
            "The error correction mechanism shows a clear connection to quantum error correction principles.",
            f"A specific example of error correction is provided for the given text: '{t['example_text']}', with an explanation of why it's challenging.",
            "The performance analysis includes specific metrics and a detailed experimental setup.",
            "The response compares the proposed system with existing error correction methods in NLP.",
            "The broader implications section discusses potential applications and ethical considerations.",
            "The response is well-structured, using appropriate headings and numbering as requested.",
            "The submission demonstrates creativity and interdisciplinary thinking in applying quantum concepts to NLP."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
