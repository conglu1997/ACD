class TaskFamily:
    import json
    from typing import List, Optional

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "initial_conditions": "A garden with 3 plants: a rose (initial height: 10 cm), a tulip (initial height: 8 cm), and a sunflower (initial height: 15 cm). The garden receives 6 hours of sunlight and is watered once a day.",
                "rules": [
                    "If a plant receives more than 5 hours of sunlight, it grows 1 cm per day.",
                    "If a plant receives 3-5 hours of sunlight, it grows 0.5 cm per day.",
                    "If a plant receives less than 3 hours of sunlight, it wilts 1 cm per day.",
                    "If a plant is watered once a day, it stays healthy. If not watered, it wilts 2 cm per day.",
                    "If a plant is watered twice a day, it grows an additional 0.5 cm per day.",
                    "If a plant is not watered for more than 3 consecutive days, it dies."
                ],
                "task": "Predict the height and health status of each plant after 7 days."
            },
            "2": {
                "initial_conditions": "A virtual ecosystem with 2 predators (wolves) and 5 prey (rabbits). The ecosystem has a forest and a meadow. The initial rabbit population is distributed with 3 in the forest and 2 in the meadow.",
                "rules": [
                    "Wolves eat 1 rabbit every 3 days. If no rabbits are available, wolves starve and lose 1 health point per day (starting health: 5 points).",
                    "Rabbits reproduce every 4 days, doubling their population.",
                    "If the number of rabbits exceeds 10, they move to the meadow. If below 5, they stay in the forest.",
                    "If the wolf population falls to 1, the remaining wolf moves to the meadow in search of food.",
                    "Rabbits in the meadow reproduce at double the rate of those in the forest."
                ],
                "task": "Describe the population dynamics of wolves and rabbits after 12 days, including their locations and health status."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = """Your task is to interpret and respond to changes in a simulated environment based on the following initial conditions and rules:\n\n"""
        instructions += f"Initial Conditions: {t['initial_conditions']}\n\n"
        instructions += "Rules:\n"
        for rule in t['rules']:
            instructions += f"- {rule}\n"
        instructions += f"\nTask: {t['task']}\n"
        instructions += """\nEnsure that your response is logical, coherent, and follows the given rules. Provide your predictions and descriptions in plain text format. Structure your response as follows:\n\n[Predictions and Descriptions]\n1. Plant/Rabbit/Wolf Descriptions: [Describe each plant/rabbit/wolf with its height/health/status]\n2. Rule Application: [Explain how each rule was applied to reach your predictions]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should accurately apply the given rules.",
            "The predictions should be logical and based on the initial conditions.",
            "The description should be coherent and well-structured.",
            "The response should include detailed explanations of rule application."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0