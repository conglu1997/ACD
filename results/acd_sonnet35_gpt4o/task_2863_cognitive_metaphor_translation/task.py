import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'source_language': 'English',
                'target_language': 'Japanese',
                'abstract_concept': 'Time',
                'cultural_context': 'Modern urban society'
            },
            {
                'source_language': 'Spanish',
                'target_language': 'Mandarin Chinese',
                'abstract_concept': 'Power',
                'cultural_context': 'Traditional rural community'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze, translate, and generate conceptual metaphors for the abstract concept of {t['abstract_concept']} in {t['source_language']} and {t['target_language']}, considering the cultural context of {t['cultural_context']}. Your task has four parts:

1. Metaphor Analysis (200-250 words):
   a) Identify and explain three common conceptual metaphors for {t['abstract_concept']} in {t['source_language']}.
   b) Analyze how these metaphors reflect cultural and cognitive aspects of {t['source_language']} speakers.
   c) Discuss any limitations or cultural biases in these metaphors.

2. Cross-linguistic Comparison (250-300 words):
   a) Research and present three conceptual metaphors for {t['abstract_concept']} in {t['target_language']}.
   b) Compare and contrast these metaphors with those in {t['source_language']}.
   c) Explain how differences in language structure and cultural background influence these metaphors.

3. Metaphor Translation (200-250 words):
   a) Translate one metaphor from {t['source_language']} to {t['target_language']}, preserving its conceptual meaning.
   b) Explain your translation process and any challenges encountered.
   c) Discuss how well the translated metaphor fits the cultural context of {t['cultural_context']}.

4. Novel Metaphor Generation (250-300 words):
   a) Create a new conceptual metaphor for {t['abstract_concept']} that is appropriate for {t['target_language']} and {t['cultural_context']}.
   b) Explain the cognitive and cultural basis for your new metaphor.
   c) Provide three example sentences using your new metaphor in {t['target_language']} (with English translations).
   d) Discuss potential implications of introducing this new metaphor into the target culture.

Ensure your response demonstrates a deep understanding of cognitive linguistics, particularly conceptual metaphor theory. Use appropriate terminology and provide clear explanations. Be creative in your metaphor generation while maintaining cultural sensitivity and linguistic plausibility.

Format your response with clear headings for each section. Your total response should be between 900-1100 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of conceptual metaphor theory and cognitive linguistics.",
            "The analysis of source language metaphors is thorough and culturally insightful.",
            "The cross-linguistic comparison shows a nuanced understanding of both languages and cultures.",
            "The metaphor translation is creative and preserves the conceptual meaning while adapting to the target language and culture.",
            "The novel metaphor generation is original, culturally appropriate, and well-explained.",
            "The response shows critical thinking about the implications and limitations of conceptual metaphors across cultures.",
            "The examples and explanations are clear, coherent, and demonstrate linguistic expertise in both languages."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
