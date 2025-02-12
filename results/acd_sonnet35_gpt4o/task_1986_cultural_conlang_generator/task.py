import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            {
                "name": "Aquatic Nomads",
                "environment": "Deep ocean with bioluminescent flora",
                "social_structure": "Matriarchal pods",
                "primary_values": "Harmony with nature, collective knowledge"
            },
            {
                "name": "Sky Dwellers",
                "environment": "Floating cities in gas giant atmosphere",
                "social_structure": "Meritocratic guilds",
                "primary_values": "Innovation, resource efficiency"
            },
            {
                "name": "Subterranean Hive",
                "environment": "Vast underground network of tunnels and caverns",
                "social_structure": "Eusocial hierarchy",
                "primary_values": "Order, community, expansion"
            }
        ]
        return {str(i+1): culture for i, culture in enumerate(random.sample(cultures, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates and analyzes a constructed language (conlang) for the {t['name']} culture. Your system should create a language that reflects the culture's environment, social structure, and values.

Culture characteristics:
- Environment: {t['environment']}
- Social Structure: {t['social_structure']}
- Primary Values: {t['primary_values']}

Your response should include the following sections:

1. AI System Architecture (250-300 words):
   a) Describe the key components of your AI system for conlang generation and analysis.
   b) Explain how the system incorporates the given cultural parameters into the language design.
   c) Discuss any machine learning techniques or linguistic models used in your system.

2. Conlang Features (300-350 words):
   a) Describe the phonology of the generated language, explaining how it reflects the culture's environment.
   b) Explain the morphological and syntactic structures, relating them to the social structure.
   c) Describe the semantic and pragmatic aspects of the language, connecting them to the culture's primary values.
   d) Provide at least three example words or phrases in the conlang, with translations and cultural significance.

3. Cultural-Linguistic Analysis (200-250 words):
   a) Explain how your AI system analyzes the relationships between the generated language and the culture.
   b) Describe any metrics or methods used to evaluate the conlang's cultural authenticity and expressiveness.
   c) Discuss how the system might identify potential areas of language change or evolution based on cultural factors.

4. Comparative Linguistics Module (150-200 words):
   a) Describe how your system could compare the generated conlang with existing human languages.
   b) Explain how this comparison could provide insights into the relationship between language and culture.
   c) Discuss any potential applications of this comparative analysis in linguistics or anthropology.

5. Ethical Considerations and Limitations (150-200 words):
   a) Discuss the ethical implications of using AI to generate and analyze languages for hypothetical cultures.
   b) Address potential biases in the AI system and how they might be mitigated.
   c) Explain the limitations of your approach and areas for future improvement.

Ensure your response demonstrates a deep understanding of linguistics, cultural anthropology, and AI. Use appropriate terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Your total response should be between 1050-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The AI system design must be tailored to the {t['name']} culture, considering their environment, social structure, and primary values",
            "The conlang features should be logically consistent and reflect the given cultural parameters",
            "The response should provide specific examples of words or phrases in the conlang",
            "The cultural-linguistic analysis should demonstrate a deep understanding of the relationship between language and culture",
            "The comparative linguistics module should propose plausible methods for comparing the conlang with human languages",
            "The response should address ethical considerations and limitations of the approach",
            "The response should be well-organized and within the specified word count"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
