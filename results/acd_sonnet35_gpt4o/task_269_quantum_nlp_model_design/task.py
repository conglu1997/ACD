import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            {
                "principle": "Superposition",
                "linguistic_application": "word sense disambiguation"
            },
            {
                "principle": "Entanglement",
                "linguistic_application": "semantic relationships"
            }
        ]
        return {
            "1": random.choice(quantum_principles),
            "2": random.choice(quantum_principles)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired natural language processing model that incorporates the quantum mechanical principle of {t['principle']} to handle {t['linguistic_application']}. Your task has five parts:

1. Quantum-Linguistic Analogy (200-250 words):
   a) Explain the chosen quantum principle of {t['principle']} in simple terms.
   b) Draw a detailed analogy between this principle and the linguistic phenomenon of {t['linguistic_application']}.
   c) Discuss how this analogy can be leveraged in natural language processing.

2. Model Architecture (250-300 words):
   a) Describe the overall structure of your quantum-inspired NLP model.
   b) Explain how it incorporates the {t['principle']} principle in its design.
   c) Detail how the model will handle {t['linguistic_application']} using this quantum-inspired approach.

3. Mathematical Formulation (200-250 words):
   a) Provide a mathematical representation of your model, using quantum mechanical notation where appropriate.
   b) Explain each component of your formulation and how it relates to both quantum mechanics and linguistics.
   c) Discuss any simplifications or assumptions made in your mathematical model.

4. Potential Advantages and Challenges (200-250 words):
   a) Explain potential advantages of your quantum-inspired approach over classical NLP methods for {t['linguistic_application']}.
   b) Discuss challenges in implementing and scaling your model.
   c) Propose potential solutions or areas for future research to address these challenges.

5. Ethical Implications and Societal Impact (150-200 words):
   a) Discuss potential ethical considerations in developing and deploying quantum-inspired NLP models.
   b) Explore possible societal impacts, both positive and negative, of applying quantum principles to language processing.
   c) Suggest guidelines or safeguards for responsible development of such technologies.

Ensure your response demonstrates a deep understanding of both quantum mechanics and computational linguistics. Be creative in your approach while maintaining scientific plausibility. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of the quantum principle of {t['principle']} and its application to {t['linguistic_application']}",
            "The model architecture is well-described and incorporates quantum principles in a plausible manner",
            "The mathematical formulation is provided and explained, using appropriate quantum mechanical notation",
            "Potential advantages and challenges of the approach are thoughtfully discussed",
            "Ethical implications and societal impacts are considered",
            "The response is creative while maintaining scientific plausibility",
            "The total response is between 1000-1250 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
