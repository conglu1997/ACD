class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A job interview where the interviewer asks the candidate about their previous work experience and skills.",
                "characters": ["Interviewer", "Candidate"]
            },
            "2": {
                "scenario": "A parent-teacher meeting where the teacher discusses the student's progress and areas for improvement with the parent.",
                "characters": ["Teacher", "Parent"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t["scenario"]
        characters = ", ".join(t["characters"])
        return f"""Simulate a dialogue between the characters based on the given social scenario.

Scenario: {scenario}

Characters: {characters}

Submit the dialogue as a plain text string in the following format:

[Character 1]: [Dialogue]
[Character 2]: [Dialogue]

Ensure that the dialogue consists of at least 6 exchanges (3 from each character) and maintains the context of the scenario."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The dialogue should be contextually appropriate.", "The responses should be coherent and relevant to the scenario.", "The dialogue should consist of at least 6 exchanges (3 from each character)."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
