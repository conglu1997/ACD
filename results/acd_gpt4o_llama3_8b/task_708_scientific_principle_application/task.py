class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "principle": "Newton's Second Law of Motion",
                "problem": "A car of mass 1500 kg is accelerating at a rate of 2 m/s^2. Calculate the force exerted by the engine."
            },
            "2": {
                "principle": "Ohm's Law",
                "problem": "A resistor in an electrical circuit has a resistance of 10 ohms and the voltage across it is 5 volts. Calculate the current flowing through the resistor."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Apply the given scientific principle to solve the following problem:

Scientific Principle: {t['principle']}
Problem: {t['problem']}

Submit your solution as a plain text string with the following format:

1. A detailed step-by-step explanation of your calculation process.
2. The final answer clearly labeled with appropriate units.

Example Response Format:
Calculation Process: [Your detailed step-by-step explanation]

Final Answer: [Your final answer with units]

Example:
Calculation Process: Using Newton's Second Law, F = ma. Given m = 1500 kg and a = 2 m/s^2, we calculate F as follows:
F = 1500 kg * 2 m/s^2 = 3000 N

Final Answer: 3000 N"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        response_format_criteria = [
            "The response should include a detailed step-by-step explanation of the calculation process.",
            "The final answer should be clearly labeled and correct based on the given scientific principle with appropriate units."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, response_format_criteria) else 0.0
