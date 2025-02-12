import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'biochemical_process': 'protein synthesis',
                'phenomenon_to_describe': 'climate change'
            },
            {
                'biochemical_process': 'cellular respiration',
                'phenomenon_to_describe': 'economic inflation'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical language based on the biochemical process of {t['biochemical_process']}, and use it to describe the complex phenomenon of {t['phenomenon_to_describe']}. Your response should include:

1. Language Design (300-350 words):
   a) Explain how your language incorporates key elements of {t['biochemical_process']}.
   b) Define at least 5 fundamental 'parts of speech' in your language, relating each to a specific aspect of the biochemical process.
   c) Describe the basic grammar and syntax rules, drawing parallels to biochemical mechanisms.
   d) Provide examples of how common concepts (e.g., action, description, time) are expressed in your language.

2. Vocabulary Generation (200-250 words):
   a) Create a mini-lexicon of at least 10 words or phrases in your language, with their English translations.
   b) Explain the biochemical basis for each word or phrase.
   c) Demonstrate how these words can be combined to form more complex expressions.

3. Phenomenon Description (250-300 words):
   a) Use your biochemical language to describe the phenomenon of {t['phenomenon_to_describe']}.
   b) Provide both the description in your invented language and an English translation.
   c) Explain how specific features of your language allow for unique or insightful ways of describing this phenomenon.

4. Linguistic Analysis (200-250 words):
   a) Analyze how your language might shape thinking about {t['phenomenon_to_describe']}.
   b) Compare your language's approach to describing this phenomenon with that of natural languages.
   c) Discuss any limitations or advantages of your language for scientific or abstract thinking.

5. Interdisciplinary Connections (150-200 words):
   a) Explore potential applications of your biochemical language in scientific research or education.
   b) Propose an experiment to test whether thinking in your language affects problem-solving in biochemistry or related fields.

Ensure your response demonstrates a deep understanding of both {t['biochemical_process']} and linguistic principles. Be creative in your language design while maintaining scientific plausibility. Use appropriate terminology from biochemistry and linguistics throughout your answer."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed design of a language based on {t['biochemical_process']} with at least 5 parts of speech and clear grammar rules.",
            "A mini-lexicon of at least 10 words or phrases is provided with explanations of their biochemical basis.",
            f"The phenomenon of {t['phenomenon_to_describe']} is described using the invented language, with an English translation and explanation.",
            "The response includes an analysis of how the language might shape thinking and compares it to natural languages.",
            "Potential applications and an experiment to test the language's effects on problem-solving are proposed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
