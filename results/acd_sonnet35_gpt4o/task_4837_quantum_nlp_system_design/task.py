class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "quantum_principle": "Quantum superposition",
                "nlp_task": "Semantic analysis",
                "target_language": "English",
                "scenario": "Analyzing sentiment in social media posts"
            },
            "2": {
                "quantum_principle": "Quantum entanglement",
                "nlp_task": "Machine translation",
                "target_language": "Mandarin Chinese",
                "scenario": "Translating technical medical documents"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum-enhanced natural language processing system that leverages the quantum principle of {t['quantum_principle']} to improve {t['nlp_task']} for {t['target_language']}, specifically addressing the scenario of {t['scenario']}. 

Brief explanation of the quantum principle:
- Quantum superposition: The ability of a quantum system to exist in multiple states simultaneously until measured.
- Quantum entanglement: A phenomenon where two or more quantum particles are correlated in such a way that the quantum state of each particle cannot be described independently.

Your response should include the following sections:

1. Quantum-NLP Integration (200-250 words):
   a) Explain how {t['quantum_principle']} can be applied to enhance {t['nlp_task']}.
   b) Describe the potential advantages of using quantum computing for this NLP task.
   c) Discuss any challenges in integrating quantum principles with classical NLP techniques.

2. System Architecture (200-250 words):
   a) Provide a high-level overview of your quantum-enhanced NLP system's architecture.
   b) Explain how classical and quantum components interact within your system.
   c) Describe any novel quantum algorithms or data structures used in your design.

3. Language-Specific Considerations (150-200 words):
   a) Discuss how your system addresses specific challenges or features of {t['target_language']}.
   b) Explain any modifications to your quantum approach necessary for this language.

4. Comparative Analysis (200-250 words):
   a) Compare your quantum-enhanced approach to a state-of-the-art classical approach for {t['nlp_task']}.
   b) Analyze the strengths and weaknesses of both approaches.
   c) Discuss scenarios where your quantum approach would outperform classical methods.

5. Performance and Limitations (150-200 words):
   a) Propose a method for evaluating the performance of your quantum-enhanced NLP system.
   b) Discuss any potential limitations or trade-offs in your approach.
   c) Suggest ways to mitigate these limitations.

6. Ethical and Societal Implications (150-200 words):
   a) Analyze potential ethical concerns related to quantum-enhanced NLP systems.
   b) Discuss societal impacts of deploying such systems for {t['nlp_task']}.
   c) Propose guidelines for responsible development and use of quantum NLP technologies.

Ensure your response demonstrates creative integration of quantum computing principles with NLP concepts. Use appropriate terminology and provide clear explanations for complex ideas. Maintain scientific plausibility throughout your design.

Format your response with clear headings for each section. Your total response should be between 1050-1350 words.

Example approach (for inspiration only, do not copy directly):
For quantum superposition in semantic analysis, you might consider representing words as quantum states, allowing for multiple meanings to be superposed until context 'measures' the intended meaning."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates creative integration of quantum computing and natural language processing concepts.",
            f"The proposed system effectively applies {t['quantum_principle']} to {t['nlp_task']} for the given scenario.",
            f"The design addresses specific challenges or features of {t['target_language']}.",
            "The comparative analysis between quantum and classical approaches is insightful.",
            "The response includes a thoughtful analysis of performance, limitations, and ethical implications.",
            "The proposed system maintains scientific plausibility throughout the design."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
