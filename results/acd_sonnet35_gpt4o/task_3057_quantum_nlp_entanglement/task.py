import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "nlp_task": "sentiment analysis",
                "language_pair": "English-Japanese",
                "quantum_principle": "superposition"
            },
            {
                "nlp_task": "machine translation",
                "language_pair": "Spanish-Mandarin",
                "quantum_principle": "entanglement"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system that enhances {t['nlp_task']} for the language pair {t['language_pair']} using the quantum principle of {t['quantum_principle']}. Your response should include:

1. Quantum System Architecture (300-350 words):
   a) Describe the overall structure of your quantum NLP system.
   b) Explain how you incorporate the specified quantum principle into your design.
   c) Detail how your system interfaces with classical NLP components.
   d) Include a high-level diagram or pseudocode to illustrate your architecture.

2. Quantum-Enhanced NLP Process (250-300 words):
   a) Explain step-by-step how your system performs the specified NLP task using quantum principles.
   b) Describe how quantum computation provides an advantage over classical methods for this task.
   c) Discuss any novel quantum algorithms or techniques you've developed for this application.

3. Language-Specific Considerations (200-250 words):
   a) Analyze how the specified language pair influences your quantum NLP system design.
   b) Discuss any challenges or opportunities presented by these languages in a quantum computing context.
   c) Explain how your system addresses language-specific nuances or structures.

4. Performance Analysis (200-250 words):
   a) Propose metrics to evaluate the performance of your quantum NLP system.
   b) Describe how you would compare its performance to state-of-the-art classical NLP systems.
   c) Discuss potential quantum advantages in terms of speed, accuracy, or capabilities.

5. Practical Implementation Challenges (150-200 words):
   a) Identify key technical challenges in implementing your system on current quantum hardware.
   b) Propose solutions or workarounds for these challenges.
   c) Discuss the scalability of your approach as quantum technologies advance.

6. Ethical and Societal Implications (150-200 words):
   a) Analyze potential ethical concerns related to quantum-enhanced NLP systems.
   b) Discuss societal impacts of significantly improved NLP capabilities.
   c) Propose guidelines for responsible development and use of quantum NLP technologies.

Ensure your response demonstrates a deep understanding of both quantum computing principles and natural language processing. Use appropriate technical terminology from both fields and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of both quantum computing principles and natural language processing techniques.",
            "The proposed quantum NLP system design is innovative, logically consistent, and effectively incorporates the specified quantum principle.",
            "The explanation of how quantum computation enhances the NLP task is clear, detailed, and plausible.",
            "The analysis of language-specific considerations is thorough and demonstrates an understanding of linguistic challenges in a quantum computing context.",
            "The performance analysis and practical implementation challenges are well-reasoned and consider current limitations of quantum technologies.",
            "The discussion of ethical and societal implications is insightful and demonstrates an understanding of the broader impacts of advanced NLP technologies."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
