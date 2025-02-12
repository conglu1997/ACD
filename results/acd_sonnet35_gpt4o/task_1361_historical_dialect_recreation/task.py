import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "dialect": "Shakespearean English",
                "period": "Late 16th to early 17th century",
                "region": "England",
                "modern_text": "I'm really excited about this new project. It's going to be amazing!"
            },
            {
                "dialect": "American Southern Antebellum",
                "period": "Early to mid-19th century",
                "region": "Southern United States",
                "modern_text": "The weather is terrible today. I think I'll stay inside and read a book."
            },
            {
                "dialect": "Victorian Cockney",
                "period": "Mid to late 19th century",
                "region": "East End of London",
                "modern_text": "I can't believe how expensive everything is getting. It's hard to make ends meet."
            },
            {
                "dialect": "1920s American Flapper Slang",
                "period": "1920s",
                "region": "Urban United States",
                "modern_text": "That party last night was so much fun. Everyone looked great and the music was fantastic."
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze and recreate the historical dialect of {t['dialect']} from the {t['period']} in the {t['region']}. Then, use this dialect to translate a piece of modern text. Follow these steps:

1. Dialect Analysis (200-250 words):
   a) Describe the key linguistic features of the {t['dialect']} dialect, including aspects of pronunciation, grammar, vocabulary, and syntax.
   b) Explain how historical and cultural factors of the {t['period']} and {t['region']} influenced this dialect.
   c) Provide at least three specific examples of words or phrases unique to this dialect.

2. Dialect Recreation (100-150 words):
   a) Create a short original passage (3-4 sentences) in the {t['dialect']} dialect.
   b) Explain how your passage incorporates the key features you described in the analysis.

3. Modern Text Translation (100-150 words):
   a) Translate the following modern text into the {t['dialect']} dialect:
      "{t['modern_text']}"
   b) Explain your translation choices, highlighting how they reflect the dialect's features.

4. Reflection (100-150 words):
   a) Discuss the challenges you encountered in recreating and using this historical dialect.
   b) Reflect on how this exercise contributes to our understanding of language evolution and cultural history.

Ensure your response demonstrates a deep understanding of historical linguistics, cultural context, and creative language use. Use appropriate terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 500-700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately describes key linguistic features of the {t['dialect']} dialect",
            "The dialect analysis includes relevant historical and cultural context",
            "The recreated passage and translated text convincingly mimic the specified dialect",
            "The explanation of translation choices demonstrates understanding of the dialect's features",
            "The reflection shows insight into the challenges and significance of historical dialect recreation",
            "The overall response demonstrates creativity and deep linguistic understanding"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
