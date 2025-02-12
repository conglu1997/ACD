class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Describe a simple electrical circuit with a battery connected to a light bulb and a switch in between that can turn the light on and off."},
            "2": {"description": "Illustrate a process flow where a customer places an order, the order is processed by the system, then the items are picked from the warehouse, and finally shipped to the customer."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return "Your task is to convert the following textual description into a visual diagram: " + t["description"] + " Ensure your diagram is clear, accurate, and includes all described components. Provide your solution as a plain text description of the diagram's elements and their relationships. Use the format: 'Component1 -> Component2 -> ...' for connections."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The diagram should accurately represent the described scenario.",
            "The diagram should be clear and include all described components.",
            "The relationships between components should be correctly depicted."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
