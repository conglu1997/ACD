import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "language_type": "tonal",
                "cultural_focus": "nomadic society",
                "time_span": "1000 years"
            },
            {
                "language_type": "polysynthetic",
                "cultural_focus": "technologically advanced underwater civilization",
                "time_span": "500 years"
            },
            {
                "language_type": "logographic",
                "cultural_focus": "interstellar trading culture",
                "time_span": "2000 years"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a constructed language ({t['language_type']}) and simulate its evolution within a hypothetical {t['cultural_focus']} over a span of {t['time_span']}. Your response should include:

1. Initial Language Design (300-350 words):
   a) Describe the key features of your constructed language, including phonology, morphology, and syntax.
   b) Explain how the language reflects the initial culture and environment of its speakers.
   c) Provide a sample sentence in your conlang with a word-for-word gloss and English translation.

2. Cultural Context (200-250 words):
   a) Describe the initial state of the culture, including social structure, technology, and belief systems.
   b) Explain how the language and culture are interconnected at this starting point.

3. Linguistic Evolution (300-350 words):
   a) Describe 3-4 major linguistic changes that occur over the specified time span.
   b) Explain the cultural or environmental factors that drive each change.
   c) Provide examples of how these changes manifest in the language's structure or vocabulary.

4. Cultural Evolution (250-300 words):
   a) Describe how the culture changes over the specified time span.
   b) Explain how linguistic changes both reflect and influence cultural developments.
   c) Discuss any significant events or innovations that impact both language and culture.

5. Final Language State (250-300 words):
   a) Describe the key features of the language at the end of the specified time span.
   b) Explain how these features differ from the initial state and why.
   c) Provide a sample sentence (the same meaning as in section 1) in the evolved conlang with a word-for-word gloss and English translation.

6. Comparative Analysis (150-200 words):
   a) Compare the evolution of your conlang to known historical language changes.
   b) Discuss any unique or surprising developments in your language-culture simulation.

Ensure your response demonstrates a deep understanding of linguistic principles, cultural anthropology, and the complex interplay between language and culture. Be creative and internally consistent in your speculative worldbuilding. Use appropriate linguistic terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1450-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistic principles and cultural anthropology.",
            "The constructed language is well-designed and consistent with the specified language type.",
            "The linguistic and cultural evolutions are plausible and well-explained.",
            "The response shows creativity and internal consistency in speculative worldbuilding.",
            "The comparative analysis draws meaningful connections to real-world linguistic phenomena.",
            "The response adheres to the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
