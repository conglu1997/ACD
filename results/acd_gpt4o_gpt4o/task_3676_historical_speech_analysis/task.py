class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {"speech": "Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.", "questions": ["What are the main themes of this speech?", "How did this speech impact its audience at the time?"]},
            "2": {"speech": "I have a dream that my four little children will one day live in a nation where they will not be judged by the color of their skin but by the content of their character.", "questions": ["What are the main themes of this speech?", "What historical context does this speech address?"]}
        }
        assert len(tasks) == 2, "There should be exactly two tasks."
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following historical speech:

{t['speech']}

Answer the following questions:
1. {t['questions'][0]}
2. {t['questions'][1]}

Provide detailed answers to each question. Your response should be in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if t['speech'] == "Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.":
            criteria = ["Identify the themes of liberty and equality.", "Discuss the impact of the speech on the audience during the Civil War period."]
        elif t['speech'] == "I have a dream that my four little children will one day live in a nation where they will not be judged by the color of their skin but by the content of their character.":
            criteria = ["Identify the themes of racial equality and justice.", "Discuss the historical context of the Civil Rights Movement."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
