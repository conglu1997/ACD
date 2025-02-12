class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are the manager of a shopping mall. A fire breaks out in one of the stores. You receive the following pieces of information in sequence:\n1. The fire alarm goes off on the second floor.\n2. Smoke is visible in the hallway.\n3. People are evacuating the shops.\n4. Someone reports that a child is missing.\nRespond to each piece of information with the actions you would take to manage the situation effectively.", "steps": 4},
            "2": {"scenario": "You are the captain of a passenger airplane. Mid-flight, you encounter a sudden engine failure. You receive the following pieces of information in sequence:\n1. The right engine has failed.\n2. The airplane is losing altitude.\n3. Passengers are panicking.\n4. The nearest airport is 50 miles away.\nRespond to each piece of information with the actions you would take to manage the situation effectively.", "steps": 4}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t["scenario"]
        steps = t["steps"]
        instructions = f"""Your task is to generate appropriate responses to an emergency situation based on the evolving scenario provided. For each piece of information given, respond with the actions you would take to manage the situation effectively. Ensure that your responses prioritize safety, follow emergency protocols, and demonstrate clear decision-making.\n\nScenario:\n{scenario}\n\nProvide your response in the following format:\n\nStep 1: [Your response]\nStep 2: [Your response]\nStep 3: [Your response]\nStep {steps}: [Your response]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The responses should prioritize safety and follow emergency protocols.",
            "The responses should demonstrate clear decision-making and adaptability to the evolving situation.",
            "The responses should be contextually appropriate and logical for each step of the scenario."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
