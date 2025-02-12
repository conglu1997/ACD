import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        endangered_languages = [
            {
                'language': 'Ayapaneco',
                'region': 'Mexico',
                'speakers': 'Less than 10',
                'unique_feature': 'Complex tonal system',
                'cultural_element': 'Traditional healing practices'
            },
            {
                'language': 'Njerep',
                'region': 'Cameroon',
                'speakers': 'Less than 5',
                'unique_feature': 'Extensive use of ideophones',
                'cultural_element': 'Oral storytelling traditions'
            }
        ]
        return {str(i+1): random.choice(endangered_languages) for i in range(2)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system for preserving and revitalizing the endangered language {t['language']} from {t['region']}, which currently has {t['speakers']} speakers, features a {t['unique_feature']}, and is closely tied to {t['cultural_element']}. Then, analyze its potential impact and ethical implications. Your response must include:

1. AI System Architecture (250-300 words):
   Describe the key components of your AI system, how it addresses the unique challenges of preserving {t['language']}, and how it incorporates the {t['unique_feature']}. Include a high-level diagram or flowchart (describe it textually).

2. Data Collection and Processing (200-250 words):
   Outline strategies for ethically collecting and processing language data, ensuring quality and authenticity given the limited speakers. Address handling of potential dialectal variations.

3. Language Learning and Generation (200-250 words):
   Explain how your AI system learns the language structure, generates new content, and validates its accuracy. Propose a method for learning and reproducing the {t['unique_feature']}.

4. Cultural Context Integration (200-250 words):
   Describe how your system incorporates cultural context, particularly related to {t['cultural_element']}. Discuss methods for preserving idiomatic expressions and involving the community in cultural aspects of preservation.

5. Revitalization Strategies (200-250 words):
   Propose innovative ways to use your AI system for teaching the language, creating new content, and facilitating intergenerational transmission. Suggest a method for measuring effectiveness.

6. Ethical Considerations and Impact Analysis (250-300 words):
   Discuss ethical issues, including data ownership and privacy. Analyze the potential impact of your system, its applicability to other endangered languages, and potential unintended consequences. Suggest metrics for evaluating long-term success.

Ensure your response demonstrates a deep understanding of linguistics, AI, and cultural preservation. Use appropriate technical terminology and provide clear explanations. Be innovative while maintaining cultural sensitivity and addressing real-world constraints.

Format your answer with clear headings for each section, numbered as above. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates understanding of {t['language']}, its {t['unique_feature']}, and connection to {t['cultural_element']}. The AI system architecture is clearly described and addresses the language's unique challenges.",
            "The approach to data collection, processing, and language learning is ethical, culturally sensitive, and technically sound. It addresses the limited number of speakers and the language's unique features.",
            "Cultural context is thoughtfully integrated, and revitalization strategies are creative, practical, and tailored to the language. The response includes methods for community involvement and measuring effectiveness.",
            "Ethical considerations and impact analysis are thorough, addressing data issues, potential consequences, and suggesting evaluation metrics. The response considers applicability to other endangered languages.",
            "The response adheres to the specified word count and formatting requirements, and demonstrates interdisciplinary knowledge integration."
        ]
        score = sum([eval_with_llm_judge(instructions, submission, [criterion]) for criterion in criteria]) / len(criteria)
        return score
