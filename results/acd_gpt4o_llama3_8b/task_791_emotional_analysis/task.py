class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "John had been working tirelessly for weeks on an important project. He felt a mix of excitement and nervousness as he prepared to present his work to the board. However, during the presentation, the board members seemed uninterested and critical. John left the meeting feeling disheartened and frustrated."},
            "2": {"scenario": "Emily had always been an overachiever, striving to be the best in her class. After receiving a lower grade than expected on a major exam, she felt overwhelmed with disappointment and self-doubt. Her friends tried to console her, but Emily couldn't shake off the feeling of inadequacy."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t['scenario']
        return f"""Read the following scenario and identify the emotional states of the characters involved. Provide a rationale for your analysis based on the details given in the scenario.

Scenario: {scenario}

Ensure that your analysis is well-structured and includes specific references to the scenario. Submit your response as a plain text string in the following format:

Emotional States: [List the emotions identified]

Rationale: [Your rationale for each emotion identified]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The emotional states identified should be appropriate and relevant to the scenario.",
            "The rationale provided should be well-structured and supported by specific references to the scenario."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
