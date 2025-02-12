import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            {
                'concept': 'time',
                'language': 'Japanese',
                'synesthesia_type': 'chromesthesia (sound-to-color)',
                'target_words': ['jikan (時間) - time', 'kako (過去) - past', 'mirai (未来) - future']
            },
            {
                'concept': 'emotions',
                'language': 'Arabic',
                'synesthesia_type': 'lexical-gustatory (word-to-taste)',
                'target_words': ['sa\'ada - happiness', 'huzn - sadness', 'ghadab - anger']
            }
        ]
        return {str(i+1): concept for i, concept in enumerate(concepts)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a language learning method based on synesthesia principles to teach the concept of '{t['concept']}' in {t['language']}, using {t['synesthesia_type']} associations. Your task has four parts:

1. Synesthetic Learning Method (200-250 words):
   a) Describe your synesthesia-based method for teaching the concept.
   b) Explain how it leverages {t['synesthesia_type']} to enhance language acquisition.
   c) Discuss potential cognitive benefits and challenges of this approach.

2. Concept Application (150-200 words):
   Apply your method to teach the following {t['language']} words related to {t['concept']}:
   {', '.join(t['target_words'])}
   Provide specific examples of the synesthetic associations you would use for each word.

3. Learning Activity (100-150 words):
   Design a practical learning activity that employs your synesthetic method to teach these words. Describe the activity's steps and materials needed.

4. Critical Analysis (200-250 words):
   a) Discuss potential advantages and limitations of your synesthetic language learning method compared to traditional approaches.
   b) Explain how this method might be adapted for learners who don't experience synesthesia.
   c) Propose a way to empirically test the effectiveness of your method.

Ensure your response demonstrates a deep understanding of both synesthesia and language acquisition principles. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section (e.g., '1. Synesthetic Learning Method', '2. Concept Application', etc.) and adhere to the specified word limits."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all four required sections with appropriate headings and adheres to the specified word limits.",
            "The synesthetic learning method is clearly described, innovative, and demonstrates a sound understanding of both synesthesia and language acquisition principles.",
            "Specific and appropriate synesthetic associations are provided for each of the target words in the concept application section.",
            "The learning activity is practical, engaging, and directly applies the proposed synesthetic method.",
            "The critical analysis includes a balanced discussion of advantages and limitations, a plausible adaptation for non-synesthetes, and a concrete proposal for empirical testing."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
