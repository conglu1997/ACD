class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "diagram_description": "A lever system where a 2-meter-long rod is balanced on a fulcrum positioned 0.5 meters from one end. A weight of 10 kg is placed on the shorter end. Describe the function of this lever system and calculate the force needed on the longer end to balance the lever. Assume standard gravity."
            },
            "2": {
                "diagram_description": "A pulley system consisting of a fixed pulley and a movable pulley is used to lift a heavy object. The fixed pulley is attached to the ceiling, and the rope passes through both pulleys. One end of the rope is attached to the object, and the other end is free to be pulled. Calculate the mechanical advantage provided by this pulley system."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to solve the following problem related to a mechanical diagram:\n\n{t['diagram_description']}\n\nProvide your solution in plain text format, including the steps taken to explain the function or calculate the mechanical advantage and the final result. Ensure that your explanation is clear and logically structured. Avoid any assumptions not stated in the problem."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should accurately explain the function of the mechanical system described.",
            "The solution should include the steps taken to arrive at the result.",
            "The explanation should be clear and logically structured.",
            "The final result should be correct and match the given diagram description." 
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
