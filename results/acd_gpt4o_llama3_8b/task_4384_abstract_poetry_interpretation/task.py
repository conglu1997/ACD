class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "poem": "The wind whispers secrets of the past,\nThrough leaves that dance in twilight's cast.\nStars murmur tales of distant dreams,\nIn the river's flow, the moonlight gleams.",
                "theme": "Nature and Time"
            },
            "2": {
                "poem": "Echoes of laughter in empty halls,\nShadows of memories on silent walls.\nA melody lost in the whispering breeze,\nFragments of moments, time's gentle tease.",
                "theme": "Memory and Loss"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Read the following abstract poem carefully and interpret its meaning based on the given theme. Then, create an analogous poem that explores the same theme, using similar abstract language and imagery. \n\nPoem:\n{t['poem']}\n\nTheme: {t['theme']}\n\nYour response should include: \n1. Interpretation: A brief paragraph explaining your interpretation of the given poem.\n2. Analogous Poem: A new poem that explores the same theme with similar abstract language and imagery. \n\nSubmit your response as a plain text string in the following format:\n\nInterpretation: [Your interpretation here]\nAnalogous Poem: [Your analogous poem here]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The interpretation should be relevant to the given theme.",
            "The analogous poem should explore the same theme and use abstract language and imagery similar to the original poem."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
