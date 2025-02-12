import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling"
        ]
        brain_regions = [
            "Broca's area",
            "Wernicke's area",
            "Anterior cingulate cortex"
        ]
        nlp_tasks = [
            "Sentiment analysis",
            "Machine translation",
            "Text summarization"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "brain_region": random.choice(brain_regions),
                "nlp_task": random.choice(nlp_tasks)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "brain_region": random.choice(brain_regions),
                "nlp_task": random.choice(nlp_tasks)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a quantum-inspired cognitive architecture for natural language processing that leverages principles from quantum computing and neuroscience to enhance language understanding and generation. Your task is to create a system that incorporates the following elements:\n\n1. Quantum Principle: {t['quantum_principle']}\n2. Brain Region: {t['brain_region']}\n3. NLP Task: {t['nlp_task']}\n\nYour response should include the following sections:\n\n1. Theoretical Framework (250-300 words):\n   a) Explain how the specified quantum principle can be applied to cognitive processing and language.\n   b) Describe the function of the given brain region and its role in language processing.\n   c) Discuss how these concepts can be integrated to enhance the specified NLP task.\n\n2. System Architecture (300-350 words):\n   a) Propose a detailed architecture for your quantum-inspired cognitive NLP system.\n   b) Explain how your system incorporates the quantum principle and mimics the function of the specified brain region.\n   c) Describe the key components and their interactions within your system.\n   d) Include a simple diagram or flowchart of your system architecture using ASCII art or Unicode characters.\n\n3. Information Processing (250-300 words):\n   a) Detail how information flows through your system, from input to output.\n   b) Explain how your system applies quantum-inspired processing to language data.\n   c) Describe how your architecture enhances the specified NLP task compared to classical approaches.\n\n4. Learning and Adaptation (200-250 words):\n   a) Propose a method for training your quantum-inspired cognitive NLP system.\n   b) Explain how your system could adapt to new linguistic inputs or tasks.\n   c) Discuss any potential advantages in learning efficiency or adaptability compared to classical NLP systems.\n\n5. Performance Analysis (200-250 words):\n   a) Suggest metrics to evaluate the performance of your system on the specified NLP task.\n   b) Hypothesize potential improvements in accuracy, efficiency, or novel capabilities of your system.\n   c) Discuss any trade-offs or limitations inherent in your approach.\n\n6. Ethical Considerations and Future Directions (150-200 words):\n   a) Address potential ethical implications of using quantum-inspired cognitive systems for language processing.\n   b) Propose guidelines for responsible development and use of such systems.\n   c) Suggest two potential future research directions to further enhance your system.\n\nEnsure your response demonstrates a deep understanding of quantum computing principles, cognitive neuroscience, and natural language processing. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1350-1650 words. Include a word count at the end of each section and a total word count at the end of your response."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified quantum principle, brain region, and NLP task, and creatively integrates them into a coherent system design.",
            "The proposed architecture is innovative, scientifically plausible, and clearly explained, with a logical flow from theoretical framework to practical implementation.",
            "The submission addresses all required sections comprehensively, providing insightful analysis of the system's potential performance, learning capabilities, and ethical implications.",
            "The response shows strong interdisciplinary knowledge integration, combining concepts from quantum computing, cognitive neuroscience, and natural language processing effectively.",
            "The writing is clear, well-structured, and uses appropriate technical terminology throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
