import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "period": "Victorian England",
                "year": 1850,
                "location": "London",
                "theme": "Social inequality"
            },
            {
                "period": "American Roaring Twenties",
                "year": 1925,
                "location": "New York City",
                "theme": "Technological progress"
            },
            {
                "period": "Tang Dynasty China",
                "year": 750,
                "location": "Chang'an (modern-day Xi'an)",
                "theme": "Cultural exchange"
            },
            {
                "period": "Renaissance Italy",
                "year": 1505,
                "location": "Florence",
                "theme": "Artistic innovation"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Create a short story (450-500 words) set in {t['period']} (specifically the year {t['year']}) in {t['location']}. Your story should explore the theme of {t['theme']}. Adhere to the following requirements:\n\n" \
               f"1. Provide a title for your story that reflects the historical setting and theme.\n" \
               f"2. Use the appropriate dialect, slang, and idioms of the time and place.\n" \
               f"3. Include at least three historically accurate cultural references or customs.\n" \
               f"4. Mention at least two real historical figures from that period, but they don't need to be main characters.\n" \
               f"5. Describe one technological or social aspect that was innovative or controversial at the time.\n" \
               f"6. Incorporate at least one historically accurate quotation or proverb from the time period.\n" \
               f"7. Provide vivid sensory details that bring the historical setting to life (sights, sounds, smells, etc.).\n" \
               f"8. Include a minor conflict or tension related to the theme.\n" \
               f"9. Incorporate a brief dialogue exchange (2-3 lines) that reflects the speaking style of the time period.\n" \
               f"10. Mention a significant historical event that occurred within 5 years of your story's setting.\n" \
               f"11. Ensure your story has a clear beginning, middle, and end.\n\n" \
               f"After your story, provide a brief explanation (250-300 words) of how your story reflects the historical period, including references to the dialect used, cultural elements incorporated, historical events mentioned, and the accuracy of the sensory details and dialogue. Also, briefly discuss any creative liberties you may have taken and justify them."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The story is set in {t['period']} (year {t['year']}) in {t['location']} and explores the theme of {t['theme']}.",
            "The story has an appropriate title reflecting the historical setting and theme.",
            "The story uses appropriate dialect, slang, and idioms for the time and place.",
            "The story includes at least three historically accurate cultural references or customs.",
            "The story mentions at least two real historical figures from the period.",
            "The story describes one technological or social aspect that was innovative or controversial at the time.",
            "The story incorporates at least one historically accurate quotation or proverb from the time period.",
            "The story provides vivid sensory details that bring the historical setting to life.",
            "The story includes a minor conflict or tension related to the theme.",
            "The story incorporates a brief dialogue exchange that reflects the speaking style of the time period.",
            "The story mentions a significant historical event that occurred within 5 years of the story's setting.",
            "The story has a clear beginning, middle, and end.",
            "The story is between 450-500 words.",
            "The explanation accurately reflects how the story represents the historical period, including references to dialect, cultural elements, historical events, sensory details, and dialogue.",
            "The explanation discusses any creative liberties taken and provides justification."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
