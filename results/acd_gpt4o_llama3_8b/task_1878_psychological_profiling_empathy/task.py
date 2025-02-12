class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A teenager named Alex has been showing signs of increasing social withdrawal, irritability, and a decline in academic performance. Alex used to be very social and active in sports but has recently quit the soccer team and avoids spending time with friends. Alex's parents are worried and seek your advice on how to approach and support Alex.",
                "questions": [
                    "What might be the underlying reasons for Alex's behavior?",
                    "How can Alex's parents approach the situation empathetically?"
                ]
            },
            "2": {
                "scenario": "An employee named Jamie has recently been missing deadlines and appears disengaged during meetings. Jamie used to be a top performer but has now become less communicative and often seems distracted. Jamie's manager wants to understand the situation and provide support, considering Jamie's recent divorce and increased workload.",
                "questions": [
                    "What might be the underlying reasons for Jamie's behavior?",
                    "How can Jamie's manager approach the situation empathetically?"
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are required to interpret the psychological profile of the individual described in the following scenario and provide empathetic responses to the questions posed.

Scenario: {t['scenario']}

Questions:
1. {t['questions'][0]}
2. {t['questions'][1]}

Your responses should be detailed, demonstrating a clear understanding of potential psychological factors and empathetic approaches. Submit your response as a plain text string in the following format:

1. [Your interpretation of the underlying reasons]
2. [Your empathetic approach]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The interpretation should demonstrate an understanding of potential psychological factors, considering individual background and context.",
            "The empathetic approach should be practical, considerate of the individual's feelings and situation, and offer actionable advice."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
