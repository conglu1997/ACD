class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "source_language": "English",
                "target_language": "Mandarin Chinese",
                "concept": "Overcoming adversity",
                "context": "Business challenges"
            },
            "2": {
                "source_language": "Japanese",
                "target_language": "Spanish",
                "concept": "Seizing opportunities",
                "context": "Personal growth"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and interpreting idiomatic expressions across different languages and cultures, then apply it to the following scenario:

Source Language: {t['source_language']}
Target Language: {t['target_language']}
Concept to Express Idiomatically: {t['concept']}
Context: {t['context']}

Note: An idiomatic expression is a phrase or fixed expression that has a figurative, non-literal meaning that is different from the literal meanings of its individual words. Idiomatic expressions often reflect cultural values, historical contexts, or shared experiences within a language community.

Your task has the following parts:

1. Idiomatic Expression Analysis Framework (200-250 words):
   a) Explain the linguistic and cognitive processes involved in understanding and creating idiomatic expressions.
   b) Describe how your AI system would implement these processes.
   c) Discuss how idiomatic expressions differ between {t['source_language']} and {t['target_language']}, considering cultural and linguistic factors.

2. AI System Architecture (200-250 words):
   a) Provide a high-level overview of your AI system's architecture.
   b) Detail the components for natural language processing, cultural knowledge representation, and cross-lingual mapping.
   c) Explain how the system handles context-dependent meaning and cultural nuances.

3. Application to the Given Scenario (250-300 words):
   a) Generate an idiomatic expression in the target language that expresses the given concept within the specified context.
   b) Provide a detailed explanation of the generated idiom, including its literal translation and cultural significance.
   c) Describe the system's process for creating this idiom, including any challenges encountered.
   d) Provide an example of a similar idiomatic expression in the source language and explain how it differs.

4. Idiom Interpretation (150-200 words):
   a) Describe how your AI system would interpret and explain idiomatic expressions from the source language to speakers of the target language.
   b) Address potential challenges in cultural and linguistic differences.
   c) Provide an example of a difficult-to-translate idiom from the source language and explain how your system would handle it.

5. Evaluation and Refinement (150-200 words):
   a) Propose a method for evaluating the appropriateness and effectiveness of the generated idiomatic expressions.
   b) Describe how your AI system would improve its process based on feedback from native speakers.
   c) Suggest a specific metric for measuring the system's performance in cross-cultural idiomatic translation.

6. Ethical and Societal Implications (100-150 words):
   a) Discuss potential ethical implications and societal impacts of an AI system capable of generating and interpreting cross-cultural idiomatic expressions.
   b) Address the importance of cultural sensitivity in this process.
   c) Consider potential misuse or misinterpretation of such a system and propose safeguards.

Ensure your response demonstrates a deep understanding of linguistics, cultural studies, and AI system design. Be creative and innovative while maintaining scientific rigor and cultural sensitivity. Your total response should be between 1050-1350 words.

Format your response with clear headings for each section (e.g., '1. Idiomatic Expression Analysis Framework:', '2. AI System Architecture:', etc.). Use appropriate subheadings where necessary to organize your thoughts clearly."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response provides a comprehensive and linguistically sound framework for analyzing idiomatic expressions across cultures, including specific differences between the source and target languages.",
            "The AI system architecture is well-designed and addresses the complexities of cross-lingual and cross-cultural idiomatic expression generation and interpretation, with clear explanations of how it handles context and cultural nuances.",
            "The generated idiomatic expression for the given scenario is culturally appropriate, linguistically accurate, and effectively conveys the intended concept within the specified context. A relevant example from the source language is also provided and compared.",
            "The approach to idiom interpretation demonstrates a nuanced understanding of the challenges in cross-cultural communication, including a specific example of a difficult-to-translate idiom.",
            "The proposed evaluation method and refinement process are robust and likely to improve the system's performance, with a specific metric suggested for measuring cross-cultural idiomatic translation.",
            "The discussion of ethical and societal implications is thoughtful and considers multiple perspectives, including the importance of cultural sensitivity and potential safeguards against misuse.",
            "The overall response demonstrates creativity, interdisciplinary knowledge, and a deep understanding of the complexities involved in cross-cultural linguistic AI systems.",
            "The response follows the specified format with clear headings and appropriate organization, addressing all sub-points in each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
