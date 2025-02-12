import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        endangered_languages = [
            'Ayapaneco',
            'Dumi',
            'Njerep',
            'Yaghan'
        ]
        language_aspects = [
            'phonology',
            'morphology',
            'syntax',
            'semantics'
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                'language': random.choice(endangered_languages),
                'aspect': random.choice(language_aspects)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system to assist in the preservation and revitalization of the endangered language {t['language']}, with a specific focus on its {t['aspect']}. Your response should include the following sections:

1. Language Analysis and Documentation (250-300 words):
   a) Describe methods for collecting and analyzing {t['language']} data, focusing on its {t['aspect']}.
   b) Explain how your AI system would process and store this linguistic information.
   c) Discuss challenges specific to working with {t['language']} and how your system addresses them.

2. AI Model Architecture (300-350 words):
   a) Design an AI architecture suitable for low-resource language processing and generation.
   b) Explain how your model handles the unique features of {t['language']}, especially its {t['aspect']}.
   c) Describe techniques for transfer learning or data augmentation to overcome the scarcity of training data.
   d) Include a diagram or pseudocode snippet illustrating a key component of your model.

3. Language Generation and Interactive Learning (250-300 words):
   a) Explain how your AI system generates new content in {t['language']}, focusing on {t['aspect']}.
   b) Describe interactive features that allow language learners to practice and receive feedback.
   c) Discuss how your system ensures the cultural authenticity of generated content.

4. Ethical Considerations and Community Involvement (200-250 words):
   a) Address ethical issues in AI-assisted language revitalization, including data ownership and privacy.
   b) Propose methods for involving the {t['language']} speaking community in the development and use of the AI system.
   c) Discuss how to balance technological intervention with traditional language transmission methods.

5. Evaluation and Impact Assessment (200-250 words):
   a) Propose metrics for evaluating the effectiveness of your AI system in language revitalization.
   b) Describe a methodology for assessing the system's impact on the {t['language']} speaking community.
   c) Discuss potential unintended consequences and how to mitigate them.

6. Future Directions and Scalability (150-200 words):
   a) Suggest how your system could be adapted for other endangered languages.
   b) Propose a research question that arises from this work.
   c) Discuss the potential long-term impact of AI-assisted language revitalization on linguistic diversity.

Ensure your response demonstrates a deep understanding of computational linguistics, endangered language preservation, and ethical AI development. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining cultural sensitivity and scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1700 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['language']} and its {t['aspect']}.",
            "The AI system design is innovative and tailored for low-resource language processing.",
            "Ethical considerations and community involvement are thoroughly addressed.",
            "The evaluation methodology and impact assessment are well-thought-out and comprehensive.",
            "The response shows cultural sensitivity and awareness of the challenges in language revitalization.",
            "The proposed system is technically feasible and scientifically plausible.",
            "The response adheres to the specified format and word count guidelines (1350-1700 words)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
