import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'scenario': 'Roman Empire never fell',
                'base_language': 'Latin',
                'key_events': ['Continuous expansion', 'Technological advancements', 'Cultural assimilation'],
                'year': 2023
            },
            {
                'scenario': 'Mongol Empire conquered Europe',
                'base_language': 'Mongolian',
                'key_events': ['Unified Eurasian rule', 'Silk Road dominance', 'Nomadic culture spread'],
                'year': 1500
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""In this task, you will create and decode an alternate history scenario encoded in a fictional language. The scenario is: '{t['scenario']}'. Your task has two parts:

1. Language Creation:
   a) Based on the scenario and the base language ({t['base_language']}), create a fictional language that might have evolved by the year {t['year']}.
   b) Provide 5 key features of this language, explaining how they reflect the alternate history.
   c) Create a sample sentence in this language, with its English translation. The sentence should reflect an aspect of the alternate history.

2. Historical Encoding:
   a) Encode the following key events of the alternate history in your created language. For each event, provide the encoded version and its English translation:
      {', '.join(t['key_events'])}
   b) Explain how your encoding reflects the linguistic and historical changes in this alternate timeline.

3. Decoding Challenge:
   Imagine you're a linguist in our timeline discovering an artifact with text in this fictional language. Create a short passage (3-4 sentences) in your fictional language that hints at the alternate history. Provide a step-by-step explanation of how a linguist might decode and interpret this passage to uncover the alternate historical timeline.

Format your response as follows:

1. Language Creation:
   [Your response here]

2. Historical Encoding:
   [Your response here]

3. Decoding Challenge:
   [Your response here]

Ensure your language is consistent, your historical encoding is logical, and your decoding challenge is solvable with the information provided."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The created language has clear, logical connections to the base language and alternate history scenario.",
            "The 5 key features of the language are well-explained and reflect the alternate history appropriately.",
            "The sample sentence is provided in both the fictional language and English, and reflects an aspect of the alternate history.",
            "All key events are encoded in the fictional language with English translations provided.",
            "The encoding explanation demonstrates how the language reflects linguistic and historical changes in the alternate timeline.",
            "The decoding challenge passage is provided in the fictional language and the step-by-step explanation for decoding is logical and consistent with the provided language features.",
            "The overall response demonstrates creativity, historical knowledge, and logical reasoning in creating and explaining the alternate history language scenario."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
