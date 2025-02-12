class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"constraints": "Construct an equilateral triangle inscribed in a circle with a radius of 5 units. Provide the steps in plain text."},
            "2": {"diagram": "A triangle ABC with AB = AC and angle BAC = 60 degrees. Provide a step-by-step construction of this triangle, including any necessary geometric principles."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'constraints' in t:
            return f"Your task is to generate a geometric construction based on the following constraints: {t['constraints']} Ensure your steps are clear and logically correct. Provide your response in the following format:\n\n1. Step-by-step construction instructions\n2. Final geometric construction description"
        elif 'diagram' in t:
            return f"Your task is to analyze and provide a step-by-step construction for the following geometric diagram: {t['diagram']} Ensure your steps are clear and logically correct. Provide your response in the following format:\n\n1. Step-by-step construction instructions\n2. Final geometric construction description"
        else:
            return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The construction steps should be clear and logically correct.", "The construction should meet the specified constraints."] if 'constraints' in t else ["The analysis should be accurate and follow geometric principles.", "The construction steps should be clear and logically correct."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
