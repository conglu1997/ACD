import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'environment': 'Coastal archipelago',
                'technological_level': 'Early industrial',
                'social_structure': 'Matriarchal oligarchy',
                'cultural_focus': 'Maritime trade and exploration'
            },
            {
                'environment': 'Arid mountain plateau',
                'technological_level': 'Post-singularity',
                'social_structure': 'AI-human symbiosis',
                'cultural_focus': 'Sustainable resource management'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that analyzes and synthesizes cultural patterns across diverse societies, then use it to generate a hypothetical culture based on the following parameters:

Environment: {t['environment']}
Technological Level: {t['technological_level']}
Social Structure: {t['social_structure']}
Cultural Focus: {t['cultural_focus']}

Your response should include the following sections:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for cultural analysis and synthesis.
   b) Explain how your system integrates data from various anthropological and sociological sources.
   c) Detail the methods used for identifying and extracting cultural patterns.
   d) Discuss any novel techniques or algorithms used in your design, particularly for cross-cultural synthesis.
   e) Include a brief pseudocode or flowchart description of a key algorithm in your system.

2. Cultural Pattern Analysis (250-300 words):
   a) Explain how your system analyzes cultural patterns across different societies.
   b) Describe the key features or dimensions your system uses to compare cultures.
   c) Discuss how your system accounts for historical context and cultural evolution.
   d) Provide an example of how your system might analyze a specific cultural practice or belief.

3. Hypothetical Culture Generation (300-350 words):
   a) Describe the process your AI system uses to generate a hypothetical culture based on the given parameters.
   b) Explain how each parameter influences the cultural synthesis process.
   c) Present 3-5 key features of the generated culture, explaining how they emerge from the given parameters and your system's analysis.
   d) Provide examples of specific cultural practices, beliefs, or artifacts in this hypothetical culture.

4. Comparative Analysis (200-250 words):
   a) Compare your generated culture to existing or historical cultures with similar parameters.
   b) Discuss any surprising or counterintuitive features that emerged during the generation process.
   c) Analyze how closely the generated culture matches theoretical predictions about cultural development.

5. Ethical Considerations and Limitations (200-250 words):
   a) Discuss potential ethical issues related to using AI for cultural analysis and synthesis.
   b) Address concerns about cultural appropriation, oversimplification, or bias in your system.
   c) Describe limitations of your approach and areas for future improvement.
   d) Propose guidelines for the responsible use of AI in anthropological and cultural studies.

6. Implications and Applications (150-200 words):
   a) Discuss what your system reveals about the nature of culture and cultural development.
   b) Explore potential applications of your system in fields such as anthropology, sociology, or futurism.
   c) Propose a novel research question that could be investigated using your AI cultural synthesis system.

Ensure your response demonstrates a deep understanding of anthropology, sociology, data science, and AI principles. Use appropriate terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific and cultural plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of anthropology, sociology, data science, and AI principles.",
            "The AI system architecture is well-described and includes novel techniques for cultural analysis and synthesis.",
            "The cultural pattern analysis process is logically explained and considers multiple dimensions of culture.",
            "The hypothetical culture generation is creative, coherent, and clearly linked to the given parameters.",
            "The comparative analysis provides insightful comparisons to existing or historical cultures.",
            "Ethical considerations are thoroughly discussed, addressing potential issues and proposing responsible use guidelines.",
            "The implications and applications section offers innovative ideas for future research and use of the system.",
            "The response is well-structured, within the specified word count, and uses appropriate technical terminology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
