class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "Ancient Roman Empire",
                "length": 300
            },
            "2": {
                "theme": "Medieval Japan",
                "length": 300
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        theme = t["theme"]
        length = t["length"]
        instructions = f"""Your task is to create a fictional holiday tradition based on the cultural or historical theme: {theme}. 

The description should be at least {length} words long and include the following elements:
1. The name of the holiday.
2. The historical or cultural significance of the holiday.
3. The main activities or rituals associated with the holiday.
4. Any special foods, decorations, or symbols used during the holiday.
5. How the holiday is celebrated by different groups or communities within the culture.

Ensure that your description is coherent, creative, and contextually appropriate for the given theme. Provide your response in plain text format.

Example Response Format:
Name of the Holiday: [Your holiday name]
Historical or Cultural Significance: [Significance]
Main Activities or Rituals: [Activities or rituals]
Special Foods, Decorations, or Symbols: [Foods, decorations, symbols]
Celebration by Different Groups: [How different groups celebrate]

Remember, it is crucial to include all the required elements and ensure your description is at least {length} words long."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The holiday tradition must include all the required elements.",
            "The description must be coherent and contextually appropriate for the given theme.",
            "The description must be at least the specified length.",
            "The holiday tradition must be creative and culturally informed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
