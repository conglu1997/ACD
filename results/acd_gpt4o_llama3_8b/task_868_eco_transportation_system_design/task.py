class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "city_name": "EcoCity",
                "population": "1 million",
                "area": "500 square km",
                "current_transport": "buses, cars, bicycles",
                "goals": "reduce carbon emissions, improve public health, ensure affordability"
            },
            "2": {
                "city_name": "GreenTown",
                "population": "500,000",
                "area": "200 square km",
                "current_transport": "trams, cars, walking paths",
                "goals": "minimize traffic congestion, increase green spaces, enhance accessibility"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are tasked with designing an eco-friendly transportation system for a fictional city. Consider the following information about the city:

City Name: {t['city_name']}
Population: {t['population']}
Area: {t['area']}
Current Modes of Transport: {t['current_transport']}
Goals: {t['goals']}

Your design should include the following components:
1. Description of the transportation modes and infrastructure.
2. Explanation of how the system meets the city's goals.
3. Consideration of sustainability, efficiency, feasibility, and technological innovations.

Submit your response in the following format:
1. Transportation Modes and Infrastructure: [Detailed description]
2. Meeting the Goals: [Explanation of how the system meets the goals]
3. Sustainability, Feasibility, and Technological Innovations: [Consideration of sustainability, efficiency, feasibility, and technological innovations]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The transportation system should be eco-friendly and align with the city's goals.",
            "The description should include detailed modes of transportation and infrastructure.",
            "The explanation should consider sustainability, efficiency, feasibility, and technological innovations.",
            "The response should follow the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
