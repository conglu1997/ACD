class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"circuit": "A simple series circuit with a battery, a switch, and a light bulb. The light bulb does not light up when the switch is closed."},
            "2": {"circuit": "A parallel circuit with two resistors and a battery. One of the resistors is not functioning, causing an imbalance in the circuit."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return "Diagnose and troubleshoot the following electrical circuit problem. Provide a step-by-step explanation of your diagnostic process and the solution. Here is the circuit description: '" + t["circuit"] + "'. Ensure your response includes checking all possible components and connections that might be causing the issue."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        task_id = None
        for key, value in TaskFamily.get_tasks().items():
            if value["circuit"] == t["circuit"]:
                task_id = key
                break
        correct_diagnoses = {
            "1": "Check the battery, switch, and light bulb connections. Ensure the battery is charged and the switch is functional. If all components are working, check for loose connections.",
            "2": "Identify the non-functioning resistor and replace it. Check the connections and ensure both resistors are properly connected to the battery."
        }
        criteria = [f"The response should correctly diagnose and provide a solution for the circuit problem, which is: {correct_diagnoses[task_id]}."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
