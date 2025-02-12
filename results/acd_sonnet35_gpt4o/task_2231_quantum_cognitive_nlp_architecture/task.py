import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Quantum Tunneling",
            "Quantum Interference"
        ]
        nlp_tasks = [
            "Sentiment Analysis",
            "Named Entity Recognition",
            "Text Summarization",
            "Question Answering"
        ]
        return {
            "1": {"principle": random.choice(quantum_principles), "task": random.choice(nlp_tasks)},
            "2": {"principle": random.choice(quantum_principles), "task": random.choice(nlp_tasks)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired cognitive architecture for natural language understanding, focusing on the quantum principle of {t['principle']} and its application to the NLP task of {t['task']}. Then, analyze its potential advantages and limitations compared to classical approaches. Your response should include:

1. Quantum-Inspired Cognitive Architecture (300-350 words):
   a) Describe the key components of your quantum-inspired cognitive architecture for NLP.
   b) Explain how you incorporate the quantum principle of {t['principle']} into your architecture.
   c) Discuss how this architecture is specifically tailored for the NLP task of {t['task']}.
   d) Include a simple diagram or schematic representation of your architecture (using ASCII art or a clear textual description).

2. Quantum Principle Application (250-300 words):
   a) Explain in detail how the quantum principle of {t['principle']} is used to enhance natural language understanding.
   b) Describe the theoretical advantages this quantum-inspired approach might offer over classical methods for {t['task']}.
   c) Discuss any challenges in implementing this quantum principle in a cognitive architecture.

3. NLP Task Implementation (200-250 words):
   a) Provide a step-by-step explanation of how your architecture would process and solve the {t['task']} task.
   b) Describe the data inputs, processing steps, and expected outputs of your system.
   c) Explain how the quantum-inspired elements contribute to each stage of the NLP process.

4. Comparative Analysis (200-250 words):
   a) Compare your quantum-inspired approach to a state-of-the-art classical method for {t['task']}.
   b) Analyze potential performance improvements, efficiency gains, or novel capabilities of your approach.
   c) Discuss any limitations or drawbacks of your quantum-inspired architecture.

5. Cognitive Science Implications (150-200 words):
   a) Discuss how your quantum-inspired architecture might relate to or inform our understanding of human cognition and language processing.
   b) Propose a hypothesis about how quantum effects might play a role in biological cognitive systems.

6. Ethical and Practical Considerations (150-200 words):
   a) Identify potential ethical implications of using quantum-inspired cognitive architectures for NLP tasks.
   b) Discuss practical challenges in implementing and scaling such systems.
   c) Propose guidelines for responsible development and use of quantum-inspired NLP technologies.

7. Future Research Directions (100-150 words):
   a) Suggest two potential areas for further research based on your quantum-inspired cognitive architecture.
   b) Explain how these research directions could advance the fields of quantum computing, cognitive science, or NLP.

8. Case Study (200-250 words):
   Provide a specific case study or example that demonstrates how your quantum-inspired cognitive architecture would process and analyze a given text input for the {t['task']} task. Include sample input, intermediate processing steps, and final output.

Ensure your response demonstrates a deep understanding of quantum computing principles, cognitive science, and natural language processing. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Adhere to the word count guidelines provided for each section. Your total response should be between 1550-1950 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed and scientifically plausible design for a quantum-inspired cognitive architecture that effectively incorporates the quantum principle of {t['principle']} for the NLP task of {t['task']}.",
            "The explanation of how the quantum principle is applied to natural language understanding is clear, innovative, and demonstrates a deep understanding of both quantum concepts and NLP.",
            f"The implementation description for the {t['task']} task is comprehensive and logically connects the quantum-inspired architecture to practical NLP processing steps.",
            "The comparative analysis provides insightful comparisons between the quantum-inspired approach and classical methods, including realistic advantages and limitations.",
            "The discussion of cognitive science implications shows creative thinking about the potential connections between quantum processes and biological cognition.",
            "The ethical and practical considerations demonstrate a nuanced understanding of the broader implications of this technology.",
            "The proposed future research directions are innovative and have the potential to significantly advance the relevant fields.",
            "The case study provides a concrete example of how the architecture would process a specific input, demonstrating the practical application of the proposed system.",
            "The overall response shows a strong grasp of quantum computing, cognitive science, and NLP, with appropriate use of technical terminology and clear explanations of complex concepts.",
            "The response adheres to the specified format and word count guidelines for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
