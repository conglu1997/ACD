import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scientific_concepts = [
            'Quantum Entanglement',
            'Cellular Respiration',
            'Plate Tectonics',
            'General Relativity',
            'Natural Selection'
        ]
        cognitive_linguistic_principles = [
            'Conceptual Metaphor Theory',
            'Frame Semantics',
            'Cognitive Grammar',
            'Mental Spaces Theory',
            'Construction Grammar'
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                'scientific_concept': random.choice(scientific_concepts),
                'cognitive_linguistic_principle': random.choice(cognitive_linguistic_principles)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that interfaces between human language and artificial neural networks using principles from cognitive linguistics, then apply it to translate the complex scientific concept of {t['scientific_concept']} into a neural network architecture. Your system should incorporate the cognitive linguistic principle of {t['cognitive_linguistic_principle']}. Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system and how they interact.
   b) Explain how your system incorporates the specified cognitive linguistic principle.
   c) Detail how your system processes natural language input and converts it into neural network structures.
   d) Propose a novel feature that enhances the system's ability to capture complex scientific concepts.

2. Cognitive Linguistic Analysis (200-250 words):
   a) Analyze the given scientific concept using the specified cognitive linguistic principle.
   b) Explain how this analysis informs the translation process into neural network architecture.
   c) Discuss any challenges in applying this linguistic principle to the scientific concept.

3. Neural Network Translation (250-300 words):
   a) Describe the neural network architecture that results from translating the scientific concept.
   b) Explain how specific aspects of the scientific concept are represented in the network structure.
   c) Discuss any novel or unconventional neural network components or connections necessitated by the translation.
   d) Include a simple ASCII art diagram illustrating the key features of your neural network architecture.

4. Evaluation and Validation (200-250 words):
   a) Propose a method to evaluate the accuracy and effectiveness of your translation system.
   b) Discuss potential benchmarks or comparisons with existing methods.
   c) Analyze potential biases or limitations in your approach.

5. Interdisciplinary Implications (150-200 words):
   a) Discuss how your system might contribute to advancements in cognitive science or neuroscience.
   b) Explore potential applications of your system in scientific research or education.
   c) Propose a research question that could be investigated using your system.

6. Ethical Considerations (100-150 words):
   a) Identify potential ethical issues related to your system's development or application.
   b) Propose guidelines for responsible use and development of such cognitive-linguistic AI interfaces.

Ensure your response demonstrates a deep understanding of cognitive linguistics, neural network architectures, and the specified scientific concept. Be creative in your system design while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive linguistics, neural network architectures, and the specified scientific concept.",
            f"The system effectively incorporates the cognitive linguistic principle of {t['cognitive_linguistic_principle']}.",
            f"The neural network architecture adequately represents the scientific concept of {t['scientific_concept']}.",
            "The proposed evaluation method is sound and well-explained.",
            "The response includes creative and plausible ideas for system design and application.",
            "The ethical considerations are thoughtfully addressed.",
            "The response is well-structured, clear, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
