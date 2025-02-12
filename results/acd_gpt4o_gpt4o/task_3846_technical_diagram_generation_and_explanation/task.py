class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Generate a simple circuit diagram for a series circuit consisting of a battery, a resistor, and a light bulb. Explain the function of each component in the circuit."},
            "2": {"description": "Generate a flowchart that describes the process of a user logging into a web application. The flowchart should include steps like user input, authentication, and successful login. Explain each step in the flowchart."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a technical diagram based on the following description and explain it clearly:

Description: {t['description']}

Ensure that your diagram is accurate and clearly represents the described elements. Use text-based characters to represent the diagram (e.g., ASCII art). Provide your explanation in plain text format, detailing the purpose and function of each component or step in the diagram. Your response should be in the following format:

Diagram:
[Your diagram]

Explanation:
[Your explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The diagram should accurately represent the described elements using text-based characters.", "The explanation should clearly detail the purpose and function of each component or step."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
