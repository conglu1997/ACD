import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_features = [
            "semantic ambiguity",
            "syntactic complexity",
            "phonological patterns",
            "pragmatic inference"
        ]
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum fourier transform"
        ]
        return {
            str(i+1): {
                'linguistic_feature': random.choice(linguistic_features),
                'quantum_principle': random.choice(quantum_principles),
                'sample_text': TaskFamily.generate_sample_text()
            } for i in range(2)
        }

    @staticmethod
    def generate_sample_text() -> str:
        texts = [
            "The old man the boat.",
            "Time flies like an arrow; fruit flies like a banana.",
            "The complex houses married and single soldiers and their families.",
            "The horse raced past the barn fell."
        ]
        return random.choice(texts)

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing algorithm for advanced linguistic analysis and natural language processing, focusing on the linguistic feature of {t['linguistic_feature']} and utilizing the quantum principle of {t['quantum_principle']}. Then, analyze its potential impact on cryptography and secure communication. Use the following sample text in your analysis: "{t['sample_text']}"

Your response should include the following sections:

1. Quantum Algorithm Design (300-350 words):
   a) Describe the key components and steps of your quantum algorithm for linguistic analysis.
   b) Explain how your algorithm leverages {t['quantum_principle']} to analyze {t['linguistic_feature']}.
   c) Provide a high-level quantum circuit diagram or pseudocode for a crucial part of your algorithm.
   d) Discuss the theoretical advantages of your quantum approach over classical methods.

2. Linguistic Application (250-300 words):
   a) Explain how your algorithm processes and analyzes {t['linguistic_feature']} in the given sample text.
   b) Provide a specific example of how it would handle a complex linguistic structure in the text.
   c) Discuss potential challenges in applying quantum principles to linguistic analysis and how you address them.

3. Cryptographic Implications (250-300 words):
   a) Analyze how your quantum linguistic algorithm could impact current cryptographic methods.
   b) Propose a novel approach to secure communication based on your algorithm, using the linguistic features it analyzes.
   c) Discuss potential vulnerabilities and how they might be addressed.

4. Performance Analysis (200-250 words):
   a) Estimate the theoretical performance of your algorithm in terms of speed and accuracy.
   b) Compare your quantum approach to state-of-the-art classical NLP methods for analyzing {t['linguistic_feature']}.
   c) Discuss scalability and potential limitations of your approach.

5. Ethical and Societal Implications (150-200 words):
   a) Identify potential ethical concerns related to the use of quantum computing in linguistic analysis and cryptography.
   b) Discuss the societal impact of advanced quantum NLP technologies, particularly in the context of privacy and security.
   c) Propose guidelines for responsible development and use of such systems.

6. Future Research Directions (150-200 words):
   a) Suggest two potential extensions or improvements to your quantum linguistic algorithm.
   b) Discuss how this approach could be adapted for other areas of computational linguistics or cryptography.
   c) Speculate on the long-term implications of quantum NLP for artificial intelligence and human-computer interaction.

Ensure your response demonstrates a deep understanding of both quantum computing principles and linguistics. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and technological plausibility.

Format your response with clear headings for each section. Adhere strictly to the word limits provided for each section. Your total response should be between 1300-1600 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of both quantum computing principles (especially {t['quantum_principle']}) and linguistics (focusing on {t['linguistic_feature']})",
            "The quantum algorithm design is innovative and plausibly leverages the specified quantum principle",
            f"The linguistic application effectively addresses the specified linguistic feature and analyzes the given sample text: \"{t['sample_text']}\"",
            "The cryptographic implications are thoroughly analyzed and a novel secure communication approach is proposed based on the linguistic analysis",
            "The performance analysis and comparison to classical methods are well-reasoned and specific to the given linguistic feature",
            "Ethical and societal implications are thoughtfully considered, especially in the context of privacy and security",
            "Future research directions are creative and build upon the proposed algorithm",
            "The response adheres to the specified word limits for each section and the overall word count is between 1300-1600 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
