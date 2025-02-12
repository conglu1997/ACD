import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "concept": "semantic entanglement",
                "application": "word sense disambiguation"
            },
            {
                "concept": "quantum superposition",
                "application": "multilingual translation"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing-based natural language processing system that represents semantic meaning in a high-dimensional Hilbert space, focusing on the concept of {t['concept']} for {t['application']}. Your response should include:

1. Theoretical Foundation (250-300 words):
   a) Explain the key principles of {t['concept']} in quantum mechanics.
   b) Describe how these principles can be applied to semantic representation in NLP.
   c) Discuss the potential advantages of this approach for {t['application']}.

2. Quantum-NLP Architecture (300-350 words):
   a) Design the main components of your quantum NLP system.
   b) Explain how semantic meaning is encoded in the quantum state space.
   c) Describe the quantum operations used for processing language.
   d) Detail how classical NLP techniques are integrated with quantum processes.

3. Implementation for {t['application']} (250-300 words):
   a) Provide a step-by-step explanation of how your system would perform {t['application']}.
   b) Describe a specific example, showing quantum states and operations involved.
   c) Explain how {t['concept']} enhances the system's capabilities for this task.

4. Advantages and Challenges (200-250 words):
   a) Discuss the potential improvements over classical NLP approaches.
   b) Identify at least three significant challenges in implementing your system.
   c) Propose potential solutions or research directions for these challenges.

5. Evaluation and Benchmarking (150-200 words):
   a) Propose methods to evaluate the performance of your quantum NLP system.
   b) Suggest benchmarks to compare it with state-of-the-art classical NLP systems.
   c) Describe an experiment that could validate the quantum nature of your system.

6. Ethical and Philosophical Implications (150-200 words):
   a) Discuss potential ethical considerations of quantum-enhanced NLP.
   b) Explore how this approach might influence our understanding of language and cognition.
   c) Address any potential risks or misuses of this technology.

Ensure your response demonstrates a deep understanding of both quantum mechanics and computational linguistics. Use appropriate technical terminology and provide clear explanations of complex concepts. Be innovative and technically accurate in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1600 words. Include a word count at the end of your response.

Reminder: Structure your response using the section headings and subheadings provided above. Each section should be clearly delineated and address all points mentioned."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both quantum mechanics and computational linguistics.",
            f"The system design effectively incorporates the concept of {t['concept']} for {t['application']}.",
            "The implementation example is clear, specific, and illustrates the quantum processes involved.",
            "The response addresses potential challenges and proposes plausible solutions or research directions.",
            "The evaluation methods and ethical considerations are thoughtfully discussed.",
            "The response adheres to the required format and word count (1300-1600 words)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
