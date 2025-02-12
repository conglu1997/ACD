class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are an engineer tasked with designing a water tank that can hold exactly 10,000 liters of water. The tank should be cylindrical, and you need to determine the dimensions (radius and height) that minimize the surface area of the tank. Assume the volume of the tank is given by \(V = \pi r^2 h\) and the surface area is given by \(A = 2\pi r (r + h)\)."},
            "2": {"scenario": "A car travels from City A to City B, a distance of 300 kilometers, at a varying speed. The car travels the first 100 kilometers at 60 km/h, the next 100 kilometers at 80 km/h, and the last 100 kilometers at 100 km/h. Determine the average speed of the car for the entire journey by considering the total distance and total time taken."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following mathematical problem based on the given scenario:

Scenario: {t["scenario"]}

Provide a detailed solution including any necessary calculations and explanations. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The solution should be mathematically correct and include all necessary calculations and explanations."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
