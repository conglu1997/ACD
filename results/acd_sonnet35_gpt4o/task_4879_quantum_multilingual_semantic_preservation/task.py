class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "quantum_principle": "superposition",
                "language_group": "Indo-European",
                "semantic_challenge": "idioms and metaphors",
                "example_phrase": "It's raining cats and dogs"
            },
            "2": {
                "quantum_principle": "entanglement",
                "language_group": "Sino-Tibetan",
                "semantic_challenge": "grammatical structures",
                "example_phrase": "\u6211\u5403\u4e86\u996d (Wo chile fan - I ate)"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-enhanced language model capable of processing and generating text in multiple languages simultaneously while preserving semantic meaning across languages. Focus on incorporating the quantum principle of {t['quantum_principle']}, addressing languages within the {t['language_group']} family, and tackling the semantic challenge of {t['semantic_challenge']}. Use the example phrase "{t['example_phrase']}" as a reference point in your explanation.

Your response should include:

1. Quantum-Enhanced Architecture (300-350 words):
   a) Describe the key components of your quantum-enhanced language model.
   b) Explain how {t['quantum_principle']} is integrated into the language processing system.
   c) Detail how your model leverages quantum computing to handle multiple languages simultaneously.
   d) Include a high-level diagram or pseudocode snippet illustrating a crucial part of your system's architecture.

2. Multilingual Processing (250-300 words):
   a) Explain how your model processes and represents multiple languages from the {t['language_group']} family.
   b) Describe any novel techniques used to maintain language-specific features while allowing cross-lingual interaction.
   c) Discuss how your model handles language-specific nuances and structures.

3. Semantic Preservation (250-300 words):
   a) Detail your approach to preserving semantic meaning across languages, focusing on {t['semantic_challenge']}.
   b) Explain how quantum principles enhance semantic preservation compared to classical methods.
   c) Provide an example of how your model would handle the given example phrase across two languages in the {t['language_group']} family.

4. Training and Optimization (200-250 words):
   a) Describe the training process for your quantum-enhanced multilingual model.
   b) Explain any quantum-inspired optimization techniques used in the training process.
   c) Discuss potential challenges in training such a model and how you would address them.

5. Performance Evaluation (200-250 words):
   a) Propose methods to evaluate the performance of your model in terms of semantic preservation and multilingual capabilities.
   b) Describe quantitative and qualitative metrics for assessing the model's effectiveness.
   c) Compare the theoretical performance of your quantum-enhanced model to state-of-the-art classical multilingual models.

6. Potential Applications and Ethical Considerations (150-200 words):
   a) Discuss potential real-world applications of your quantum-enhanced multilingual model.
   b) Address ethical considerations related to the development and use of such advanced language models.
   c) Propose guidelines for responsible development and deployment of quantum-enhanced language technologies.

Ensure your response demonstrates a deep understanding of quantum computing, linguistics, and natural language processing. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Cite relevant research or theories to support your proposed model design. Include at least 3-5 citations throughout your response, formatted as [Author, Year] in-text citations.

Format your response with clear headings for each section, numbered as above. Begin each section with the heading (e.g., '1. Quantum-Enhanced Architecture:') on a new line, followed by your response for that section. Your total response should be between 1350-1650 words, with each section adhering to the specified word count range.

Include a brief 'References' section at the end of your response, listing the full citations for the sources you cited in your response. This section does not count towards the total word count."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing principles, linguistics, and natural language processing.",
            "The proposed quantum-enhanced language model is innovative and plausible, effectively integrating the specified quantum principle.",
            "The approach to multilingual processing and semantic preservation is well-explained and addresses the given language group and semantic challenge.",
            "The response includes a specific example of how the model would handle the given example phrase across two languages in the specified language group.",
            "The training, optimization, and evaluation methods are appropriate and well-reasoned.",
            "The response includes a clear architectural diagram or pseudocode snippet.",
            "Potential applications and ethical considerations are thoughtfully discussed.",
            "The response is well-structured, adheres to the specified format, and falls within the given word count range of 1350-1650 words.",
            "The response includes at least 3-5 relevant citations to support the proposed model design.",
            "A brief 'References' section is included at the end of the response."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
