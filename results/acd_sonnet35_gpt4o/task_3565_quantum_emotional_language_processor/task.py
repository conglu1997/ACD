import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "emotion": "Ambivalence",
                "context": "A bittersweet farewell party",
                "quantum_concept": "Superposition"
            },
            {
                "emotion": "Nostalgia",
                "context": "Revisiting childhood memories",
                "quantum_concept": "Entanglement"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing framework for emotional language processing and sentiment analysis, then apply it to analyze and generate emotionally nuanced text. Focus on the emotion of {t['emotion']} in the context of {t['context']}, incorporating the quantum concept of {t['quantum_concept']}. Your response should include the following sections:

1. Quantum-Emotional Framework (300-350 words):
   a) Describe the key components of your quantum computing framework for emotional language processing.
   b) Explain how it incorporates the specified quantum concept to model emotional states.
   c) Detail how quantum states or operations represent emotional nuances in language.
   d) Provide a mathematical or formal representation of your framework.

2. Emotional-Linguistic Integration (200-250 words):
   a) Analyze how your framework models the interaction between emotions and language.
   b) Discuss potential insights this integration might offer into human emotional processing.
   c) Explain any novel emergent properties in your quantum-emotional system.

3. Sentiment Analysis Application (250-300 words):
   a) Apply your quantum-emotional framework to analyze the sentiment in a given text sample related to the specified emotion and context.
   b) Provide a step-by-step explanation of how your framework processes and interprets the emotional content.
   c) Compare your approach to traditional sentiment analysis methods, highlighting potential advantages.

4. Emotionally Nuanced Text Generation (200-250 words):
   a) Use your framework to generate a short text (100-150 words) that expresses the specified emotion in the given context.
   b) Explain how your system incorporates emotional nuances in the generated text.
   c) Discuss challenges in generating emotionally authentic text and how your approach addresses them.

5. Ethical Considerations and Future Directions (150-200 words):
   a) Identify potential ethical issues in using quantum computing for emotional language processing.
   b) Propose guidelines for responsible development and use of such systems.
   c) Suggest two future research directions that build on your framework.

Ensure your response demonstrates a deep understanding of quantum computing principles, emotional intelligence, and linguistic analysis. Be creative and innovative while maintaining scientific rigor. Use appropriate terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of quantum computing, particularly related to {t['quantum_concept']}.",
            f"The framework effectively integrates the emotion of {t['emotion']} with linguistic analysis.",
            f"The sentiment analysis application is well-explained and offers clear advantages over traditional methods.",
            f"The generated text convincingly expresses {t['emotion']} in the context of {t['context']}.",
            "The ethical considerations are thoughtfully addressed and future research directions are insightful."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
