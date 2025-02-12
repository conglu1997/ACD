class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A company wants to optimize the production of two products, A and B, given that each product requires different amounts of resources (labor and materials). The company has a limited amount of these resources and wants to maximize its profit. The profit per unit of product A is $40 and for product B is $30. The company has 300 hours of labor and 200 kg of materials available. Product A requires 2 hours of labor and 1 kg of materials per unit, while product B requires 1 hour of labor and 2 kg of materials per unit.", "question": "Construct a linear programming model to determine the optimal number of units of products A and B that the company should produce to maximize profit. Provide the solution and interpret the results."},
            "2": {"scenario": "A city is planning to build a new park and wants to decide the best location based on minimizing the average distance for residents to travel to the park. The city has three potential locations (L1, L2, and L3) and the population distribution across different neighborhoods. The coordinates of the neighborhoods and the potential park locations are provided. Neighborhoods: N1(1,3), N2(4,5), N3(3,7), N4(6,2). Potential Park Locations: L1(2,4), L2(5,6), L3(4,3).", "question": "Construct a mathematical model to determine the optimal location for the park that minimizes the average distance for residents to travel. Provide the solution and interpret the results."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to construct and interpret a mathematical model based on the following real-world scenario:

{t['scenario']}

Your response should include:
1. A clear formulation of the mathematical model, including any necessary equations or constraints.
2. The solution to the model, showing all necessary calculations.
3. An interpretation of the results, explaining the practical implications and any recommendations based on the solution.

Ensure your response is well-organized, logically structured, and includes all required components in a clear manner."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a clear formulation of the mathematical model, including any necessary equations or constraints.",
            "The response should include the solution to the model, showing all necessary calculations.",
            "The response should provide an interpretation of the results, explaining the practical implications and any recommendations based on the solution.",
            "The response should be well-organized and logically structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
