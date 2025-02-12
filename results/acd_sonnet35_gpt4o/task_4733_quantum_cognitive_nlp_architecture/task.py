import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_principle": "Superposition",
                "cognitive_process": "Semantic memory retrieval",
                "nlp_task": "Word sense disambiguation",
                "example_scenario": "Disambiguating the word 'bank' in the sentence 'I went to the bank.'"
            },
            {
                "quantum_principle": "Entanglement",
                "cognitive_process": "Analogical reasoning",
                "nlp_task": "Metaphor comprehension",
                "example_scenario": "Understanding the metaphor 'Time is a thief' in context."
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired cognitive architecture for natural language understanding and generation, focusing on the quantum principle of {t['quantum_principle']}, the cognitive process of {t['cognitive_process']}, and the NLP task of {t['nlp_task']}. Consider the example scenario: {t['example_scenario']}

Your response should include:

1. Architectural Design (300-350 words):
   a) Describe the key components of your quantum-inspired cognitive architecture.
   b) Explain how you incorporate the specified quantum principle into your design.
   c) Detail how your architecture models the given cognitive process.
   d) Discuss how your system approaches the specified NLP task, using the example scenario.
   e) Provide a conceptual diagram or detailed description of your architecture.

2. Quantum-Classical Integration (250-300 words):
   a) Explain the theoretical basis for using quantum principles in cognitive modeling and NLP.
   b) Describe how quantum and classical computations interact in your architecture.
   c) Discuss any novel mathematical formulations or algorithms you've developed for this integration.

3. Implementation and Challenges (200-250 words):
   a) Outline the key steps required to implement your architecture.
   b) Discuss potential challenges in realizing this system and propose solutions.
   c) Explain how you would validate the quantum aspects of your model.

4. Performance Analysis (200-250 words):
   a) Predict how your architecture might perform compared to classical NLP systems on the specified task.
   b) Describe potential advantages and limitations of your quantum-inspired approach.
   c) Propose a method for empirically comparing your system to state-of-the-art classical NLP models.

5. Cognitive Science Implications (150-200 words):
   a) Discuss how your architecture might inform or challenge current theories in cognitive science.
   b) Propose an experiment to test whether human cognition exhibits quantum-like properties in the specified cognitive process.

6. Ethical Considerations and Societal Impact (150-200 words):
   a) Analyze potential ethical implications of developing quantum-inspired AI systems for language processing.
   b) Discuss possible societal impacts, both positive and negative, of this technology.
   c) Propose guidelines for responsible development and use of quantum-cognitive AI systems.

7. Future Research Directions (100-150 words):
   a) Suggest two potential extensions or applications of your architecture in other areas of AI or cognitive science.
   b) Briefly explain how these could contribute to advancing our understanding of mind and machine intelligence.

Ensure your response demonstrates a deep understanding of quantum mechanics, cognitive science, and natural language processing. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1700 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a comprehensive understanding of the quantum principle of {t['quantum_principle']}, the cognitive process of {t['cognitive_process']}, and the NLP task of {t['nlp_task']}, with clear integration of these concepts in the architectural design.",
            "The quantum-inspired cognitive architecture is innovative, coherent, and scientifically plausible, with a clear explanation of how quantum and classical computations interact.",
            "The implementation challenges, performance analysis, and validation methods are thoroughly discussed, showing a realistic understanding of the technical difficulties involved.",
            "The response addresses the cognitive science implications, ethical considerations, and future research directions comprehensively, demonstrating broad interdisciplinary thinking.",
            "The overall response is well-structured, uses appropriate technical terminology, and provides clear explanations for complex concepts across quantum mechanics, cognitive science, and NLP.",
            f"The example scenario of {t['example_scenario']} is effectively incorporated into the architectural design and discussion.",
            "The response falls within the specified word count range of 1350-1700 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
