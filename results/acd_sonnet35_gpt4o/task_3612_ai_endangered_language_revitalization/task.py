import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = [
            {
                'language': 'Ainu',
                'region': 'Japan',
                'speakers': 'Less than 100 native speakers',
                'unique_feature': 'Complex system of evidentiality markers'
            },
            {
                'language': 'Sami',
                'region': 'Northern Scandinavia',
                'speakers': 'Approximately 30,000 speakers across several varieties',
                'unique_feature': 'Extensive case system with up to 9 cases'
            },
            {
                'language': 'Quechua',
                'region': 'Andean regions of South America',
                'speakers': 'Several million speakers, but many varieties endangered',
                'unique_feature': 'Evidential suffixes indicating source of information'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(languages, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system for preserving and revitalizing the endangered language {t['language']} from {t['region']}. The language has {t['speakers']} and features a {t['unique_feature']}. Then, analyze the system's potential impact on linguistic diversity and cultural preservation. Your response should include the following sections:

1. AI System Architecture (300-350 words):
   a) Describe the overall structure and key components of your AI system for language preservation and revitalization.
   b) Explain how your system incorporates natural language processing, machine learning, and other relevant AI technologies.
   c) Detail how the AI system captures and preserves the unique linguistic features of {t['language']}, particularly its {t['unique_feature']}.
   d) Discuss any novel AI techniques or approaches you've incorporated to address the specific challenges of this endangered language.

2. Data Collection and Processing (250-300 words):
   a) Outline your strategy for collecting linguistic data on {t['language']}, considering the limited number of speakers.
   b) Explain how your AI system processes and analyzes this data to create a comprehensive language model.
   c) Describe any ethical considerations in data collection and how you address them.
   d) Discuss how your system ensures data quality and handles potential biases or gaps in the available linguistic information.

3. Language Learning and Generation (250-300 words):
   a) Explain how your AI system facilitates language learning for new speakers of {t['language']}.
   b) Describe the AI's capability to generate new, culturally appropriate content in the language.
   c) Discuss how the system adapts to different learning styles and proficiency levels.
   d) Explain how your AI maintains the authenticity of the language while making it accessible to learners.

4. Cultural Context Integration (200-250 words):
   a) Describe how your AI system incorporates the cultural context and traditional knowledge associated with {t['language']}.
   b) Explain how the system preserves and transmits cultural practices, stories, and traditions alongside the language.
   c) Discuss any potential challenges in representing cultural nuances through AI and how you address them.

5. Community Engagement and Empowerment (200-250 words):
   a) Outline your strategy for involving the {t['language']} speaking community in the development and use of the AI system.
   b) Explain how the AI empowers the community to take ownership of their language revitalization efforts.
   c) Describe any features that allow community members to contribute to and improve the AI's language model over time.

6. Impact Analysis (250-300 words):
   a) Analyze the potential impact of your AI system on the preservation and revitalization of {t['language']}.
   b) Discuss how this technology might influence linguistic diversity on a broader scale.
   c) Consider both positive outcomes and potential risks or unintended consequences of using AI for language revitalization.
   d) Propose metrics or methods for evaluating the long-term success of your AI system in preserving and revitalizing {t['language']}.

7. Ethical Considerations and Future Directions (200-250 words):
   a) Identify and discuss ethical issues related to using AI for language preservation and revitalization.
   b) Propose guidelines for responsible development and use of AI in endangered language contexts.
   c) Suggest potential improvements or extensions to your system for future development.
   d) Discuss how your approach could be adapted for other endangered languages or linguistic preservation efforts.

Ensure your response demonstrates a deep understanding of linguistics, artificial intelligence, and cultural anthropology. Use technical terminology appropriately and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and practical plausibility.

Format your response with clear headings for each section. Use numbered subsections (e.g., 1a, 1b, 1c) to organize your thoughts within each main section. Your total response should be between 1650-2000 words. Responses significantly shorter or longer than this range may be penalized in scoring."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, artificial intelligence, and cultural anthropology.",
            f"The AI system architecture effectively addresses the preservation and revitalization of {t['language']}, incorporating its unique features, especially the {t['unique_feature']}.",
            "The data collection and processing approach is comprehensive, ethically sound, and addresses the challenges of working with a language that has {t['speakers']}.",
            "The language learning and generation methods are well-explained, culturally appropriate, and cater to different learning styles and proficiency levels.",
            "The system effectively integrates cultural context and involves the {t['language']} speaking community in the revitalization process.",
            "The impact analysis is thorough, considering both positive outcomes and potential risks, with clear metrics for evaluating long-term success.",
            "Ethical considerations are thoughtfully addressed, with clear guidelines for responsible use of AI in endangered language contexts.",
            "The response uses technical terminology appropriately and provides clear explanations for complex concepts.",
            "The overall response demonstrates strong interdisciplinary knowledge integration, cultural sensitivity, and creative problem-solving.",
            "The response follows the required format with clear headings, numbered subsections, and falls within the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
