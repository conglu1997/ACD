class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "objective": "Design a pulley system to lift a 100 kg weight with minimal effort. Optimize the system for the least amount of force required to lift the weight.",
                "constraints": "The system should use no more than 3 pulleys, and the total length of rope must not exceed 20 meters. The lifting height is 5 meters. Assume the pulleys are ideal (no friction). Include a safety factor of 1.5 in your calculations."
            },
            "2": {
                "objective": "Design a gear system to increase the speed of a rotating shaft from 100 RPM to 500 RPM. Optimize the system to minimize the number of gears used.",
                "constraints": "The system should fit within a 1 cubic meter space and use standard gear sizes available in the market. The input torque is 50 Nm, and the output torque should be at least 10 Nm. Assume gears are ideal (no friction). Include a safety factor of 1.2 in your calculations."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a mechanical system to achieve the following objective:

Objective: {t['objective']}

Constraints: {t['constraints']}

Tasks:
1. Describe the design of your system in detail, including a diagram if necessary. Use ASCII art or describe the diagram in words if needed.
2. Explain how your design meets the objective and constraints specified.
3. Provide calculations to show the efficiency or performance of your design, such as force required, gear ratios, etc. Ensure to include the safety factor in your calculations.
4. Suggest any potential improvements or optimizations for your design.

Submit your response as a plain text string with the following sections:
- Design Description: [Your design description]
- Objective and Constraints: [Your explanation of how the design meets the objectives and constraints]
- Calculations: [Your performance or efficiency calculations]
- Optimizations: [Your suggested improvements or optimizations]

Ensure your response is thorough and well-structured to cover all aspects of the task. Provide clear and detailed calculations to support your design choices."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The design description should be clear, detailed, and include a diagram if necessary.",
            "The explanation should clearly show how the design meets the objective and constraints.",
            "The calculations should demonstrate the efficiency or performance of the design, including the safety factor.",
            "The suggested improvements or optimizations should be logical and feasible."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
