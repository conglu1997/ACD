class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"historical_figure": "Marie Curie", "historical_event": "Discovery of Radium", "date": "December 21, 1898", "context": "On this date, Marie Curie and her husband Pierre announced the discovery of Radium, a new radioactive element. This discovery was significant in the field of chemistry and physics, leading to advancements in medical treatments and scientific understanding of radioactivity."},
            "2": {"historical_figure": "Leonardo da Vinci", "historical_event": "Completion of the Mona Lisa", "date": "1519", "context": "Leonardo da Vinci, the renowned Renaissance artist and polymath, is believed to have completed his famous painting, the Mona Lisa, around 1519. The painting is celebrated for its exquisite detail, the enigmatic expression of the subject, and its innovative use of sfumato technique."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to write a fictional diary entry as if you are the historical figure {t['historical_figure']} on the date of {t['date']}, based on the historical event: {t['historical_event']}. Ensure that the diary entry is creative, historically accurate, and reflects the personality and experiences of the historical figure. Provide specific details and context, and aim for a length of at least 150 words. Here is some context to help you: {t['context']}. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The diary entry should be historically accurate.", "The diary entry should reflect the personality and experiences of the historical figure.", "The diary entry should be creatively written and engaging.", "The diary entry should be at least 150 words long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
