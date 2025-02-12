class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "objective": "Design a city layout for a population of 50,000 people. The city should include residential areas, commercial zones, industrial zones, parks, and roads. The goal is to optimize traffic flow and accessibility to green spaces.",
                "constraints": [
                    "Residential areas should be located away from industrial zones.",
                    "Commercial zones should be easily accessible from residential areas.",
                    "At least 15% of the city area should be dedicated to green spaces.",
                    "Minimize the distance that residents need to travel to reach commercial zones and parks."]
            },
            "2": {
                "objective": "Design a city layout for a population of 100,000 people. The city should include residential areas, commercial zones, industrial zones, parks, schools, and roads. The goal is to optimize traffic flow, access to schools, and distribution of green spaces.",
                "constraints": [
                    "Residential areas should be located away from industrial zones.",
                    "Commercial zones should be easily accessible from residential areas.",
                    "Schools should be evenly distributed throughout the city.",
                    "At least 20% of the city area should be dedicated to green spaces.",
                    "Minimize the distance that residents need to travel to reach schools, commercial zones, and parks."]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        objective = t["objective"]
        constraints = "\n".join(t["constraints"])
        return f"""Design a city layout based on the following objective and constraints:\n
Objective: {objective}\n
Constraints:\n{constraints}\n
Submit your city layout as a detailed text description, including the placement of residential areas, commercial zones, industrial zones, parks, schools (if applicable), and roads. Provide reasoning for your layout decisions to demonstrate how they meet the objective and constraints."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The layout should optimize traffic flow.", "The layout should ensure accessibility to green spaces.", "The layout should adhere to the given constraints.", "The placement of different zones should be logical and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
