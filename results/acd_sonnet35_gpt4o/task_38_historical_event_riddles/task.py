import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        historical_events = [
            {
                "event": "French Revolution",
                "year": 1789,
                "key_figure": "Marie Antoinette"
            },
            {
                "event": "Moon Landing",
                "year": 1969,
                "key_figure": "Neil Armstrong"
            },
            {
                "event": "Fall of the Berlin Wall",
                "year": 1989,
                "key_figure": "Mikhail Gorbachev"
            },
            {
                "event": "Signing of the Magna Carta",
                "year": 1215,
                "key_figure": "King John of England"
            }
        ]
        return {
            "1": random.choice(historical_events),
            "2": random.choice(historical_events)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Create a riddle based on the historical event: {t['event']} ({t['year']}). Your riddle should:\n\n1. Be 4-6 lines long.\n2. Include a clever play on words related to the event or the key figure {t['key_figure']}.\n3. Reference at least two historical facts about the event without explicitly naming it.\n4. End with a question asking to identify the event or key figure.\n\nAfter creating the riddle, provide the solution and explain the wordplay and historical references used.\n\nFormat your response as follows:\n\nRiddle:\n[Your riddle here]\n\nSolution:\n[Event or key figure name]\n\nExplanation:\n[Explain the wordplay and historical references]\n"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The riddle accurately references the historical event: {t['event']} ({t['year']}).",
            f"The riddle includes a clever play on words related to the event or {t['key_figure']}.",
            "The riddle contains at least two accurate historical facts without explicitly naming the event.",
            "The riddle ends with a question asking to identify the event or key figure.",
            "The solution correctly identifies the event or key figure.",
            "The explanation clearly outlines the wordplay and historical references used in the riddle."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
