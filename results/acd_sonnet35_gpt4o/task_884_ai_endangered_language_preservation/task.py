import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        endangered_languages = [
            {
                'language': 'Ayapaneco',
                'location': 'Mexico',
                'speakers': 'Less than 10',
                'unique_feature': 'Complex tonal system'
            },
            {
                'language': 'Njerep',
                'location': 'Cameroon',
                'speakers': '4',
                'unique_feature': 'Extensive use of ideophones'
            },
            {
                'language': 'Dumi',
                'location': 'Nepal',
                'speakers': 'Around 8',
                'unique_feature': 'Unique system of verb agreement'
            },
            {
                'language': 'Kaixana',
                'location': 'Brazil',
                'speakers': '1',
                'unique_feature': 'Complex evidentiality system'
            }
        ]
        
        return {str(i+1): random.choice(endangered_languages) for i in range(2)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system to preserve and revitalize the endangered language {t['language']} from {t['location']}, which currently has {t['speakers']} speakers and features a {t['unique_feature']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for language preservation and revitalization.
   b) Explain how your system incorporates computational linguistics techniques.
   c) Detail how the system will capture and represent the unique features of {t['language']}, especially its {t['unique_feature']}.
   d) Discuss how your system ensures cultural sensitivity and ethical data collection.

2. Data Collection and Processing (200-250 words):
   a) Propose innovative methods for collecting language data from the remaining speakers.
   b) Describe how your system will process and analyze this data.
   c) Explain how you'll address challenges related to limited data availability.
   d) Discuss how you'll incorporate cultural context and non-linguistic information.

3. Language Revitalization Strategies (200-250 words):
   a) Propose AI-driven strategies for teaching {t['language']} to new learners.
   b) Describe how your system will generate new content in {t['language']}.
   c) Explain how you'll balance language evolution with preservation of traditional forms.
   d) Discuss how your system will foster a community of speakers and support ongoing use.

4. Ethical Considerations and Cultural Preservation (200-250 words):
   a) Identify potential ethical challenges in using AI for language preservation.
   b) Propose guidelines to ensure respectful and culturally appropriate language documentation.
   c) Discuss how to balance technological intervention with community autonomy.
   d) Explain how your system will preserve cultural knowledge associated with the language.

5. Evaluation and Long-term Impact (150-200 words):
   a) Propose metrics to evaluate the effectiveness of your AI system in language preservation and revitalization.
   b) Describe potential long-term impacts of your system on the {t['language']} community.
   c) Discuss how your approach could be adapted for other endangered languages.

Ensure your response demonstrates a deep understanding of computational linguistics, cultural anthropology, and AI ethics. Use appropriate terminology and provide clear explanations for complex ideas. Be innovative in your approach while maintaining cultural sensitivity and scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1000-1250 words. Include specific examples and techniques that address the unique features of {t['language']}, particularly its {t['unique_feature']}."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of computational linguistics, cultural anthropology, and AI ethics in the context of language preservation.",
            f"The proposed AI system effectively addresses the unique challenges of preserving and revitalizing {t['language']}, including specific techniques for handling its {t['unique_feature']}.",
            f"The data collection and processing methods are innovative and sensitive to the challenges of working with a language with only {t['speakers']} speakers.",
            "The language revitalization strategies are creative, leverage AI capabilities, and respect cultural context.",
            "Ethical considerations are thoroughly addressed, demonstrating a strong awareness of the potential impacts on the language community.",
            "The evaluation metrics and long-term impact analysis show a deep understanding of the complexities involved in language preservation efforts.",
            "The response follows the required format and word count guidelines, and includes specific examples and techniques for the given language."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
