class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "nlp_task": "Text classification",
                "quantum_concept": "Superposition",
                "linguistic_feature": "Semantic ambiguity"
            },
            "2": {
                "nlp_task": "Machine translation",
                "quantum_concept": "Entanglement",
                "linguistic_feature": "Syntactic dependencies"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hybrid quantum-classical algorithm for the NLP task of {t['nlp_task']}, incorporating the quantum concept of {t['quantum_concept']} and addressing the linguistic feature of {t['linguistic_feature']}. Your response should include:

1. Algorithm Design (300-350 words):
   a) Describe the overall structure of your hybrid quantum-classical algorithm.
   b) Explain how you incorporate the specified quantum concept into your algorithm.
   c) Detail how your algorithm addresses the given linguistic feature.
   d) Provide a high-level pseudocode or flow diagram of your algorithm.

2. Quantum Component Analysis (200-250 words):
   a) Explain the theoretical advantage of using the specified quantum concept in this NLP task.
   b) Describe potential quantum circuits or operations used in your algorithm.
   c) Discuss how the quantum and classical components of your algorithm interact.

3. Linguistic Integration (200-250 words):
   a) Analyze how your algorithm specifically addresses the given linguistic feature.
   b) Explain any novel insights or approaches your quantum-inspired method brings to this linguistic challenge.
   c) Discuss potential limitations or challenges in applying quantum concepts to this linguistic feature.

4. Performance Prediction (150-200 words):
   a) Hypothesize about the expected performance of your algorithm compared to classical NLP approaches.
   b) Identify key metrics for evaluating your algorithm's success.
   c) Describe potential challenges in implementing and scaling your algorithm.

5. Quantum NLP Implications (200-250 words):
   a) Discuss the broader implications of quantum-inspired approaches in NLP.
   b) Propose two other NLP tasks that might benefit from quantum computing concepts.
   c) Speculate on how quantum NLP might evolve in the next decade.

6. Ethical Considerations (100-150 words):
   a) Identify potential ethical issues in developing quantum NLP technologies.
   b) Propose guidelines for responsible research and application in this field.

Ensure your response demonstrates a deep understanding of both quantum computing and computational linguistics. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both quantum computing concepts and computational linguistics.",
            "The proposed algorithm creatively and plausibly incorporates the specified quantum concept and addresses the given linguistic feature.",
            "The analysis of quantum components and linguistic integration is thorough and insightful.",
            "The performance prediction and discussion of implications show critical thinking and awareness of the field's challenges and potential.",
            "The response includes creative yet scientifically grounded ideas for future applications and ethical considerations.",
            "The submission adheres to the specified format and word limits."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
