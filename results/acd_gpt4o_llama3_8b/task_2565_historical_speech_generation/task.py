class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"figure": "Martin Luther King Jr.", "event": "Civil Rights Movement", "context": "March on Washington"},
            "2": {"figure": "Winston Churchill", "event": "World War II", "context": "Battle of Britain"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        figure = t["figure"]
        event = t["event"]
        context = t["context"]
        return f"""Generate a speech as if you are {figure} during the {event}, specifically addressing the {context}. Ensure that the speech reflects the historical context, style, and tone of {figure}. Submit your speech as a plain text string.\n\nExample for figure 'Abraham Lincoln' and event 'American Civil War' with context 'Gettysburg Address':\nFour score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.\n\nNow we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure.\nThis speech reflects the historical context, tone, and style of Abraham Lincoln during the American Civil War."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The speech should accurately reflect the historical context.", "The speech should maintain the stylistic consistency of the historical figure.", "The speech should be coherent and relevant to the event and context."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
