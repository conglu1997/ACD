class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "It's Friday evening, and your restaurant is fully booked. You receive a call that three of your waitstaff are sick and won't be able to make it. You need to decide how to manage the situation, including reassigning tasks, managing customer expectations, and ensuring smooth operations. Additionally, a large order for a birthday party needs special attention."
            },
            "2": {
                "scenario": "A large group of customers arrives unexpectedly, and there are no available tables. You need to decide how to accommodate them, manage current reservations, and maintain customer satisfaction. Additionally, one of your chefs informs you that there is a shortage of key ingredients for the night's special menu."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to manage a restaurant during a dynamic scenario. Read the scenario carefully and make quick decisions to handle the situation. Provide a detailed plan of action, including how you will prioritize tasks, manage staff, and ensure customer satisfaction. Your response should be clear, logical, and demonstrate your ability to adapt to the changing situation.\n\nScenario: {t['scenario']}\n\nProvide your plan of action in plain text format. Ensure your response includes: 1. Task prioritization, 2. Staff management, 3. Customer satisfaction strategies, and 4. Contingency plans."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should include a clear and logical plan of action.", "The plan should demonstrate adaptability and prioritization.", "The plan should address customer satisfaction and staff management.", "The plan should include contingency strategies."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
