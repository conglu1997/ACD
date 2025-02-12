class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "You are the CEO of a mid-sized tech company facing financial difficulties. You must decide whether to cut staff by 20% to reduce costs or to seek a large investment that could potentially dilute current shareholders' stakes."
            },
            "2": {
                "scenario": "You are the mayor of a city facing an unprecedented drought. You must decide whether to impose strict water rationing, which could hurt local businesses, or invest in expensive desalination plants that would increase taxes."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t['scenario']
        return f"""Consider the following scenario:\n\nScenario: {scenario}\n\nYour task is to make a well-reasoned decision. Consider the following factors in your decision-making process:\n1. Short-term vs. long-term impacts\n2. Economic implications\n3. Social implications\n4. Ethical considerations\n\nProvide a clear decision and a detailed justification for your choice. Your response should be structured as follows:\n\nDecision: [Your decision]\n\nJustification: [Your detailed justification]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The decision should be clearly stated.",
            "The justification should consider short-term and long-term impacts.",
            "The justification should address economic, social, and ethical implications.",
            "The justification should be logical, coherent, and well-structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
