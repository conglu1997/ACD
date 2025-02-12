class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"protocol": "1. Measure 50 mL of distilled water using a graduated cylinder.\n2. Add 5 grams of sodium chloride to the water and stir until completely dissolved.\n3. Pour the solution into a 100 mL beaker.\n4. Heat the solution to 70°C using a hot plate.\n5. Once the solution reaches 70°C, add 10 mL of 1M hydrochloric acid and stir for 5 minutes.\n6. Record any changes in the appearance of the solution.", "questions": ["What is the purpose of adding sodium chloride to the water?", "Why is the solution heated to 70°C?", "What safety precautions should be taken when adding hydrochloric acid?"]},
            "2": {"goal": "Prepare a buffer solution with a pH of 7.4", "constraints": ["Use only common laboratory reagents.", "The total volume of the solution should be 500 mL.", "Provide detailed steps including measurements and safety precautions."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "protocol" in t:
            return f"""Interpret the following laboratory protocol and answer the questions below:\n\nProtocol:\n{t['protocol']}\n\nQuestions: {', '.join(t['questions'])}\n\nProvide your answers in plain text format."""
        else:
            return f"""Create a detailed laboratory protocol based on the following goal and constraints:\n\nGoal: {t['goal']}\nConstraints: {', '.join(t['constraints'])}\n\nYour protocol should include precise measurements, step-by-step instructions, and necessary safety precautions. Provide your protocol in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "protocol" in t:
            criteria = ["The interpretation should demonstrate understanding of the purpose of each step and address all the questions accurately."]
        else:
            criteria = ["The protocol should be detailed, precise, and include appropriate safety precautions while meeting the given goal and constraints."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
