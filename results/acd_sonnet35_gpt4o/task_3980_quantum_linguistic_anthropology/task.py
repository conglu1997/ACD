import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_principle": "Superposition",
                "linguistic_feature": "Semantic change",
                "cultural_domain": "Rituals and ceremonies",
                "time_span": "500 years"
            },
            {
                "quantum_principle": "Entanglement",
                "linguistic_feature": "Syntactic drift",
                "cultural_domain": "Kinship systems",
                "time_span": "1000 years"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system that models and analyzes the co-evolution of language and cultural practices across multiple societies. Your system should incorporate the quantum principle of {t['quantum_principle']}, focus on the linguistic feature of {t['linguistic_feature']}, and apply it to the cultural domain of {t['cultural_domain']} over a time span of {t['time_span']}. Your response should include the following sections:

1. Quantum-Linguistic-Anthropological Integration (300-350 words):
   a) Explain how you integrate {t['quantum_principle']} with {t['linguistic_feature']} and {t['cultural_domain']}.
   b) Describe the novel quantum algorithms or techniques used in your system.
   c) Discuss how quantum principles enhance the modeling of linguistic and cultural evolution.
   d) Include a high-level diagram of your system architecture (describe it textually).

2. Quantum Modeling of Language and Culture (250-300 words):
   a) Detail how your system represents linguistic features and cultural practices as quantum states.
   b) Explain how quantum operations model changes in language and culture over time.
   c) Describe how your system handles the interaction between multiple societies.
   d) Discuss how you address the challenge of maintaining coherence in your quantum system over the specified time span.

3. Data Integration and Analysis (200-250 words):
   a) Explain how your system integrates linguistic and anthropological data into the quantum model.
   b) Describe the types of insights your system can generate about the co-evolution of language and culture.
   c) Provide an example of a specific analysis your system might perform.

4. Comparative Analysis (200-250 words):
   a) Compare your quantum approach to traditional computational methods in linguistics and anthropology.
   b) Discuss the advantages and potential limitations of using quantum computing in this context.
   c) Analyze how your system might perform differently from classical AI approaches.

5. Ethical Considerations and Societal Impact (150-200 words):
   a) Identify potential ethical concerns in using quantum computing to model cultural evolution.
   b) Discuss the implications of quantum-enhanced predictions of linguistic and cultural change.
   c) Propose guidelines for the responsible use of your system in academic and policy contexts.

6. Future Directions and Implications (150-200 words):
   a) Suggest two potential extensions or applications of your quantum linguistic-anthropological system.
   b) Discuss how this research might influence our understanding of language, culture, and quantum systems.
   c) Speculate on the long-term implications of quantum computing in social sciences.

Ensure your response demonstrates a deep understanding of quantum computing, linguistics, and cultural anthropology. Use appropriate technical terminology from all three fields and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, and number your paragraphs within each section for clarity. Your total response should be between 1250-1550 words.

Important: Include at least three specific quantum computing terms or concepts (beyond those already mentioned in the instructions) in your explanation.

Remember to provide a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must address all six required sections with appropriate content and word count for each.",
            "The integration of quantum principles, linguistic features, and cultural domains should be innovative and clearly explained.",
            "The quantum modeling approach should be scientifically plausible and demonstrate a deep understanding of quantum computing concepts.",
            "The system's ability to analyze the co-evolution of language and culture should be clearly described with specific examples.",
            "The comparative analysis should provide meaningful insights into the advantages and limitations of the quantum approach.",
            "Ethical considerations and future implications should be thoughtfully addressed.",
            "The overall response should demonstrate a clear integration of knowledge from quantum computing, linguistics, and cultural anthropology, while being innovative and scientifically sound.",
            "The response must include at least three specific quantum computing terms or concepts beyond those mentioned in the instructions.",
            "The response should be properly formatted with numbered sections and paragraphs, and include a word count at the end."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
