import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "language_pair": "Mandarin Chinese and Swahili",
                "cultural_context": "Family relationships",
                "cognitive_aspect": "Embodied cognition"
            },
            {
                "language_pair": "Hindi and Finnish",
                "cultural_context": "Concepts of time",
                "cognitive_aspect": "Prototype theory"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates and analyzes semantic networks for different languages and cultures, then use it to explore cross-cultural communication and language acquisition. Focus on the language pair: {t['language_pair']}, the cultural context of {t['cultural_context']}, and incorporate the cognitive aspect of {t['cognitive_aspect']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the overall structure of your AI system for generating and analyzing semantic networks.
   b) Explain how it incorporates principles from computational linguistics and cognitive science.
   c) Detail how the system accounts for cultural differences in semantic representations.
   d) Discuss how {t['cognitive_aspect']} is integrated into your system's design.

2. Semantic Network Generation (250-300 words):
   a) Explain the process your AI uses to generate semantic networks for each language in the pair.
   b) Describe how cultural context influences the network structure, focusing on {t['cultural_context']}.
   c) Provide a specific example of how a concept related to {t['cultural_context']} might be represented differently in each language's semantic network.

3. Cross-lingual Analysis (250-300 words):
   a) Detail how your system compares and analyzes semantic networks across the two languages.
   b) Explain how it identifies and quantifies cultural differences in concept representation.
   c) Describe a hypothetical finding your system might uncover about how {t['cultural_context']} is conceptualized differently in the two cultures.

4. Language Acquisition Application (200-250 words):
   a) Propose how your system could be used to assist in language acquisition for learners of either language in the pair.
   b) Explain how the system's understanding of cultural differences in semantic networks enhances the learning process.
   c) Describe a specific learning activity or tool that could be developed based on your system's analysis.

5. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential biases or limitations in your system's approach to generating and analyzing semantic networks.
   b) Address ethical concerns related to AI systems making inferences about cultural differences.
   c) Propose guidelines for the responsible development and use of such systems in cross-cultural research and education.

6. Future Developments and Implications (150-200 words):
   a) Suggest potential expansions or modifications to your system for other applications in linguistics or cognitive science.
   b) Discuss how this technology might evolve to better incorporate {t['cognitive_aspect']} in its analysis.
   c) Speculate on the long-term implications of such systems for cross-cultural understanding and communication.

Ensure your response demonstrates a deep understanding of computational linguistics, cognitive science, and cultural anthropology. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology and provide clear explanations for complex concepts.

Format your answer with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a deep understanding of computational linguistics, cognitive science, and cultural anthropology, particularly in relation to {t['language_pair']} and {t['cultural_context']}.",
            f"The system architecture should clearly incorporate {t['cognitive_aspect']} and explain how it's integrated into the semantic network generation and analysis.",
            "The cross-lingual analysis section should provide a plausible and insightful hypothetical finding about cultural differences in concept representation.",
            "The language acquisition application should propose a creative and practical use of the system for language learners.",
            "The response should address ethical considerations and limitations thoughtfully, demonstrating awareness of potential biases and responsible AI development."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
