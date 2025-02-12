import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_property": "superposition",
                "nlp_task": "sentiment analysis",
                "language_pair": "English-Mandarin"
            },
            {
                "quantum_property": "entanglement",
                "nlp_task": "machine translation",
                "language_pair": "Spanish-Arabic"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""
        Design a quantum computing-based natural language processing system that leverages the quantum property of {t['quantum_property']} for enhanced {t['nlp_task']}, focusing on the language pair {t['language_pair']}. Then, analyze its potential advantages over classical NLP systems. Your response should include:

        1. Quantum NLP System Architecture (300-350 words):
           a) Describe the key components of your quantum NLP system.
           b) Explain how your system incorporates the specified quantum property.
           c) Detail how your system addresses the given NLP task for the specified language pair.
           d) Provide a high-level diagram or pseudocode to illustrate your architecture.

        2. Quantum Advantage Analysis (250-300 words):
           a) Explain how the quantum property enhances the performance of your NLP system.
           b) Compare your quantum NLP system to state-of-the-art classical systems for the same task.
           c) Quantify the potential improvements in terms of speed, accuracy, or other relevant metrics.

        3. Implementation Challenges (200-250 words):
           a) Discuss the main technical challenges in implementing your quantum NLP system.
           b) Propose solutions or workarounds for these challenges.
           c) Explain any limitations of current quantum hardware that might affect your system's performance.

        4. Linguistic Implications (200-250 words):
           a) Analyze how your quantum NLP system might change our understanding of language processing.
           b) Discuss potential implications for linguistic theory or cognitive science.
           c) Propose an experiment to test a novel hypothesis about language that your system enables.

        5. Ethical Considerations (150-200 words):
           a) Identify potential ethical concerns related to quantum-enhanced NLP systems.
           b) Discuss privacy implications, especially for the specified language pair.
           c) Propose guidelines for responsible development and use of quantum NLP technologies.

        6. Future Applications (150-200 words):
           a) Suggest two potential real-world applications of your quantum NLP system beyond the specified task.
           b) Discuss how these applications might impact society or scientific research.
           c) Propose a roadmap for extending your system to other NLP tasks or language pairs.

        Ensure your response demonstrates a deep understanding of quantum computing, computational linguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

        Format your response with clear headings for each section, numbered as above. Your total response should be between 1250-1550 words.
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately addresses the quantum property of {t['quantum_property']} in the context of {t['nlp_task']}.",
            f"The system design effectively incorporates quantum computing principles for the language pair {t['language_pair']}.",
            "The analysis of quantum advantages over classical systems is thorough and well-reasoned.",
            "The response demonstrates a deep understanding of quantum computing, computational linguistics, and artificial intelligence.",
            "The proposed system is innovative yet scientifically plausible.",
            "The ethical considerations and future applications are thoroughly explored."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
