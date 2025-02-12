import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_concept": "superposition",
                "linguistic_application": "semantic ambiguity"
            },
            {
                "quantum_concept": "quantum tunneling",
                "linguistic_application": "language acquisition"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum-based linguistic system that applies the quantum concept of {t['quantum_concept']} to {t['linguistic_application']} in language. Your response should include:

1. Conceptual Framework (200-250 words):
   a) Explain the quantum concept of {t['quantum_concept']} and its key principles.
   b) Describe how {t['linguistic_application']} works in conventional linguistics.
   c) Propose a novel way to integrate {t['quantum_concept']} into {t['linguistic_application']}.

2. System Design (250-300 words):
   a) Outline the architecture of your quantum linguistic system.
   b) Explain how it incorporates {t['quantum_concept']} to enhance or alter {t['linguistic_application']}.
   c) Provide at least one mathematical formulation or diagram to illustrate your system's operation.
   d) Describe how information would be encoded, transmitted, and decoded in your system.

3. Implications and Applications (200-250 words):
   a) Analyze potential advantages of your system over classical linguistic models.
   b) Discuss challenges or limitations of implementing this system.
   c) Propose two practical applications of your quantum linguistic system in fields such as communication, cryptography, or artificial intelligence.

4. Thought Experiment (150-200 words):
   a) Design a thought experiment to test a key feature of your quantum linguistic system.
   b) Describe the setup, procedure, and expected outcomes of your experiment.
   c) Explain how the results would validate or challenge your system's principles.

5. Ethical and Philosophical Considerations (150-200 words):
   a) Discuss potential ethical implications of a quantum-based linguistic system.
   b) Explore how this system might influence our understanding of consciousness or reality.
   c) Consider potential societal impacts if this system were to be implemented globally.

Ensure your response demonstrates a deep understanding of both quantum mechanics and linguistics. Use appropriate terminology and provide clear explanations for complex concepts. Be creative and original in your approach while maintaining scientific plausibility. Your total response should be between 950-1200 words.

Format your response with clear headings for each section and subheadings where appropriate. Use concise, clear language and provide specific examples to illustrate your points.

Example level of detail (for a different concept):
Quantum Concept: Quantum Entanglement
Linguistic Application: Syntactic Dependencies

In this system, words in a sentence could be 'entangled' such that the syntactic role of one word instantaneously influences the role of its entangled partner, regardless of their distance in the sentence. This could lead to novel sentence structures where long-distance dependencies are more easily formed and processed.

Mathematical formulation: Let W1 and W2 be entangled words in a sentence S. Their syntactic roles R1 and R2 could be represented as:
|ψ⟩ = α|R1⟩|R2⟩ + β|R1'⟩|R2'⟩
where α and β are complex numbers representing the probability amplitudes of the respective syntactic role pairs.

Note: This is just an example to illustrate the expected level of detail and creativity. Your response should focus on the quantum concept and linguistic application provided in the task.

Note: Do not provide direct answers or solutions in your response. The task is designed to challenge your ability to integrate complex concepts from different fields."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must include a clear and accurate explanation of {t['quantum_concept']} and how it relates to {t['linguistic_application']}.",
            "The system design should be novel, coherent, and scientifically plausible, with a clear description of its architecture and operation.",
            "The response must include at least one relevant and well-explained mathematical formulation or diagram.",
            "The thought experiment should be well-designed, relevant to the proposed system, and include clear setup, procedure, and expected outcomes.",
            "The response should demonstrate interdisciplinary knowledge, creative problem-solving, and consider ethical and philosophical implications.",
            "The response should adhere to the specified word count (950-1200 words) and formatting guidelines.",
            "The proposed applications should be innovative and demonstrate a clear understanding of the potential impact of the quantum linguistic system."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
