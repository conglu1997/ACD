import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            '1': {
                'source_period': 'Victorian Era (1837-1901)',
                'target_period': 'Roaring Twenties (1920s)',
                'topic': 'Social etiquette at a dinner party'
            },
            '2': {
                'source_period': 'Renaissance (14th-17th century)',
                'target_period': 'Information Age (late 20th-early 21st century)',
                'topic': 'The concept of human knowledge and learning'
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the linguistic patterns of {t['source_period']} and {t['target_period']}, then complete the following tasks related to the topic of {t['topic']}:

1. Historical Language Analysis (250-300 words):
   a) Describe key linguistic features (vocabulary, grammar, syntax) characteristic of {t['source_period']}. Cite relevant linguistic or historical sources where appropriate.
   b) Explain how these features reflect the cultural and social context of the time.
   c) Provide two example sentences or phrases (10-20 words each) that typify the language of this period.

2. Linguistic Evolution (200-250 words):
   a) Analyze how language changed from {t['source_period']} to {t['target_period']}.
   b) Discuss factors (technological, social, cultural) that influenced this evolution.
   c) Provide examples of words or phrases that emerged or changed meaning between these periods.

3. Text Synthesis (250-300 words):
   a) Write a short paragraph (100-150 words) about {t['topic']} in the style of {t['source_period']}.
   b) Rewrite the same content in the style of {t['target_period']}.
   c) Explain key differences in vocabulary, tone, and structure between the two versions.

4. Cultural Context Analysis (200-250 words):
   a) Discuss how the treatment of {t['topic']} differs between the two periods.
   b) Analyze how these differences reflect broader cultural shifts.
   c) Identify any persistent themes or ideas that remain constant across both periods.

5. Linguistic Pattern Recognition (150-200 words):
   a) Propose an approach for automatically distinguishing texts from these two periods.
   b) Describe key features or patterns a machine learning model might use for this task.
   c) Discuss potential challenges in implementing such a model.

Ensure your response demonstrates a deep understanding of historical linguistics, cultural analysis, and creative writing. Use appropriate terminology and provide clear examples. Your total response should be between 1050-1300 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately describes linguistic features of {t['source_period']} and {t['target_period']}, with appropriate citations.",
            "The analysis of linguistic evolution is thorough and well-supported with examples.",
            f"The synthesized texts convincingly mimic the styles of {t['source_period']} and {t['target_period']}.",
            "The cultural context analysis demonstrates insightful understanding of both periods.",
            "The proposed linguistic pattern recognition approach is technically sound and creative.",
            "The overall response shows a deep understanding of historical linguistics and cultural analysis.",
            "The submission adheres to the specified word count and format requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0