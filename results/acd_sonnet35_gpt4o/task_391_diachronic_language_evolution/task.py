import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'start_period': 'Middle English (1100-1500)',
                'end_period': 'Modern English (1800-present)',
                'text': 'The knight rode his horse through the forest, seeking adventure.',
                'focus': 'Vocabulary and spelling changes'
            },
            {
                'start_period': 'Old English (450-1100)',
                'end_period': 'Early Modern English (1500-1800)',
                'text': 'The wise king ruled his land with justice and mercy.',
                'focus': 'Grammatical structure and word order'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Simulate the evolution of the given text from the start period to the end period, applying appropriate linguistic changes. Your task has the following parts:

1. Original Text Analysis (100-150 words):
   Analyze the given text in its original form, considering its linguistic features relevant to the {t['start_period']}.

2. Language Evolution Simulation (200-250 words):
   Transform the text to reflect how it might appear in the {t['end_period']}. Focus particularly on {t['focus']}.
   Provide the evolved text and explain the changes you made, citing specific linguistic principles or historical events that justify these modifications.

3. Comparative Analysis (150-200 words):
   Compare and contrast the original and evolved versions of the text. Discuss how the changes reflect broader trends in the evolution of the English language during this period.

4. Linguistic Principles (100-150 words):
   Identify and explain at least two key linguistic principles or mechanisms of language change demonstrated in your simulation (e.g., semantic shift, phonological changes, syntactic restructuring).

5. Historical Context (100-150 words):
   Briefly discuss how historical events or sociocultural factors during this period might have influenced the linguistic changes you've simulated.

Original text: "{t['text']}"

Ensure your response demonstrates a deep understanding of historical linguistics and language evolution. Use appropriate linguistic terminology and provide clear explanations for the changes you implement.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of historical linguistics and language evolution principles.",
            f"The simulated text evolution accurately reflects changes typical of the transition from {t['start_period']} to {t['end_period']}.",
            f"The analysis focuses on {t['focus']} as specified in the task.",
            "The explanation of linguistic changes is clear, detailed, and supported by relevant linguistic principles or historical events.",
            "The comparative analysis effectively highlights significant differences between the original and evolved texts.",
            "At least two key linguistic principles or mechanisms of language change are correctly identified and explained.",
            "The discussion of historical context provides plausible connections between sociocultural factors and linguistic changes.",
            "Appropriate linguistic terminology is used throughout the response."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
