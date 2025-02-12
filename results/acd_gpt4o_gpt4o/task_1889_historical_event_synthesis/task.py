class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"events": ["The signing of the Magna Carta in 1215", "The invention of the printing press by Gutenberg in 1440", "The discovery of the New World by Columbus in 1492"]},
            "2": {"events": ["The fall of the Berlin Wall in 1989", "The invention of the internet in the late 20th century", "The 9/11 terrorist attacks in 2001"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a coherent and plausible narrative that connects the following historical events:

Events: {', '.join(t['events'])}

Instructions:
1. Provide an introduction (at least 100 words) that sets the historical context for the events.
2. Explain how these events are connected through causality or influence (at least 200 words).
3. Incorporate creative elements to fill gaps and make the narrative engaging while remaining plausible (at least 200 words).
4. Conclude with a summary that highlights the significance of the events and their interconnections (at least 100 words).

Your response should be structured as follows:
Introduction: [Your introduction]
Connections: [Your explanation of connections]
Creative Elements: [Your creative narrative]
Conclusion: [Your conclusion]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The introduction should set the historical context and be at least 100 words.", "The explanation of connections should demonstrate causality or influence and be at least 200 words.", "The narrative should incorporate creative elements while remaining plausible and be at least 200 words.", "The conclusion should summarize the significance and interconnections of the events and be at least 100 words."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
