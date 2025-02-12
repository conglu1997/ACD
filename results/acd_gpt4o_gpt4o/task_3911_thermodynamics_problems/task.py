class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "A gas undergoes an isothermal expansion at a temperature of 300 K from a volume of 1 m³ to 3 m³. Calculate the work done by the gas and explain the process in terms of the first law of thermodynamics.",
                "explanation_task": "Provide a detailed explanation of the isothermal expansion process and how it relates to the first law of thermodynamics."
            },
            "2": {
                "problem": "A heat engine operates between two reservoirs at temperatures 500 K and 300 K. If the engine absorbs 600 J of heat from the hot reservoir, calculate the maximum possible work output and the efficiency of the engine. Explain the process in terms of the second law of thermodynamics.",
                "explanation_task": "Provide a detailed explanation of the heat engine's operation and how it relates to the second law of thermodynamics."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        problem = t["problem"]
        explanation_task = t["explanation_task"]
        instructions = f"""Your task is to solve the following thermodynamics problem and explain the physical phenomena involved:

Problem: {problem}

After solving the problem, provide a detailed explanation of the physical process involved. Your explanation should include relevant principles and laws of thermodynamics, and how they apply to the problem. Ensure your explanation is clear and coherent, and accurately reflects the scientific concepts.

Response format:
1. Solution to the problem
2. Explanation of the physical phenomena involved"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The submission should include a correct solution to the thermodynamics problem.", "The explanation should accurately reflect the physical phenomena and be clearly described."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
