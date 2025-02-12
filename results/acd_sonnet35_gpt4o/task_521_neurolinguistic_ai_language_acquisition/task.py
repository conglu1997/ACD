import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_aspects = [
            "Syntax",
            "Semantics",
            "Pragmatics",
            "Phonology"
        ]
        brain_regions = [
            "Broca's area",
            "Wernicke's area",
            "Angular gyrus",
            "Arcuate fasciculus"
        ]
        learning_theories = [
            "Statistical learning",
            "Rule-based learning",
            "Connectionist models",
            "Usage-based theory"
        ]
        
        tasks = [
            {
                "language_aspect": aspect,
                "brain_region": region,
                "learning_theory": theory
            }
            for aspect in language_aspects
            for region in brain_regions
            for theory in learning_theories
        ]
        
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI language acquisition system inspired by neurolinguistic theories of how the human brain processes and learns language. Focus on the language aspect of {t['language_aspect']}, incorporate the function of {t['brain_region']}, and apply the learning theory of {t['learning_theory']}. It is crucial to integrate all three of these elements throughout your response.

Your response should include the following sections:

1. Theoretical Foundation (200-250 words):
   a) Explain the chosen language aspect and its role in language acquisition.
   b) Describe the function of the specified brain region in language processing.
   c) Outline the key principles of the given learning theory.
   d) Discuss how these three elements interact in human language acquisition.

2. AI System Design (250-300 words):
   a) Propose an AI architecture that mimics the brain's language processing mechanisms.
   b) Explain how your system incorporates the specified brain region's function.
   c) Describe how your AI model implements the chosen learning theory.
   d) Detail the specific mechanisms for acquiring the focused language aspect.
   e) Include a simple diagram or flowchart of your system architecture.

3. Learning Process Simulation (200-250 words):
   a) Outline a step-by-step process of how your AI system would acquire a new language feature.
   b) Provide a concrete example related to the specified language aspect.
   c) Explain how this process reflects both neurolinguistic principles and AI learning mechanisms.

4. Evaluation Metrics (150-200 words):
   a) Propose methods to measure the effectiveness of your AI system in acquiring the language aspect.
   b) Describe how you would compare its performance to human language acquisition.
   c) Suggest experiments to test the system's generalization abilities to new linguistic inputs.

5. Limitations and Ethical Considerations (150-200 words):
   a) Discuss potential limitations of your AI language acquisition system.
   b) Address ethical implications of developing AI systems that mimic human cognitive processes.
   c) Propose guidelines for responsible development and use of such systems in research or applications.

6. Future Directions (100-150 words):
   a) Suggest two potential improvements or extensions to your AI language acquisition system.
   b) Briefly describe how these developments could enhance the system's capabilities or address current limitations.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility.

Format your response using clear headings for each section. Your total response should be between 1050-1350 words, not including the diagram. Include the diagram as a text-based representation (e.g., ASCII art or a structured text description) within your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of the specified language aspect, brain region, and learning theory.",
            "The AI system design effectively incorporates neurolinguistic principles and mimics brain functions.",
            "The learning process simulation provides a concrete, step-by-step example of language acquisition.",
            "The evaluation metrics are appropriate and well-explained.",
            "Limitations and ethical considerations are thoughtfully addressed.",
            "Future directions are innovative and relevant.",
            "The response includes a diagram or flowchart of the system architecture.",
            "The writing is clear, well-structured, and uses appropriate technical terminology.",
            "The response is creative while maintaining scientific plausibility.",
            "The total word count is between 1050-1350 words (excluding the diagram).",
            "All three elements (language aspect, brain region, and learning theory) are consistently integrated throughout the response."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0