import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_principle": "Superposition",
                "linguistic_phenomenon": "Polysemy",
                "application_context": "Sentiment analysis in social media posts"
            },
            {
                "quantum_principle": "Entanglement",
                "linguistic_phenomenon": "Semantic relatedness",
                "application_context": "Cross-lingual information retrieval"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired computational model for natural language understanding, applying the quantum principle of {t['quantum_principle']} to represent the linguistic phenomenon of {t['linguistic_phenomenon']}. Then, demonstrate how your model could be applied to {t['application_context']}. Your response should include:

1. Quantum-Linguistic Model (300-350 words):
   a) Describe the key components and structure of your quantum-inspired model for language processing.
   b) Explain how you've incorporated the quantum principle of {t['quantum_principle']} into your model.
   c) Discuss how your model represents the linguistic phenomenon of {t['linguistic_phenomenon']}.
   d) Include at least one mathematical formulation or equation that is central to your model.

2. Cognitive Implications (200-250 words):
   a) Analyze how your model relates to current theories of cognitive processing in language understanding.
   b) Discuss potential implications of your model for our understanding of human language comprehension.
   c) Propose an experiment that could potentially validate or refute your model's cognitive plausibility.

3. Computational Implementation (200-250 words):
   a) Outline the key steps or algorithms needed to implement your model computationally.
   b) Discuss any challenges in translating quantum principles to classical computing systems.
   c) Propose a method for training or optimizing your model using existing linguistic data.

4. Application to {t['application_context']} (250-300 words):
   a) Describe how your quantum-inspired model could be applied to this specific context.
   b) Explain the potential advantages of your approach compared to classical NLP methods.
   c) Discuss any limitations or challenges in applying your model to this context.
   d) Provide a hypothetical example demonstrating your model's performance in this application.

5. Ethical and Philosophical Considerations (150-200 words):
   a) Discuss potential ethical implications of applying quantum-inspired models to language understanding.
   b) Address any philosophical questions raised by your model regarding the nature of meaning or understanding.
   c) Propose guidelines for responsible development and use of quantum-inspired language models.

Ensure your response demonstrates a deep understanding of both quantum mechanics and linguistics. While being creative in your approach, maintain scientific plausibility and rigor. Your model should be innovative but grounded in current scientific understanding. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The model effectively incorporates the quantum principle of {t['quantum_principle']} in a linguistically relevant way.",
            f"The approach to representing {t['linguistic_phenomenon']} is innovative and well-explained.",
            f"The application to {t['application_context']} is clearly described and demonstrates potential advantages.",
            "The response shows a deep understanding of both quantum mechanics and linguistics.",
            "The proposed model is creative while maintaining scientific plausibility.",
            "The mathematical formulation or equation is relevant and correctly applied.",
            "The cognitive implications and experimental proposal are thoughtfully considered.",
            "Ethical and philosophical considerations are addressed comprehensively."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
