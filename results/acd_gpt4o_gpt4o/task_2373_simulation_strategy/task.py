class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "You are managing a virtual farm. Your goal is to maximize crop yield while ensuring all animals are well-fed. You have the following resources: 10 acres of land, 5 cows, 10 chickens, water, and seeds. Each cow requires 1 acre of grazing land, and each chicken requires 0.1 acre. You can plant either corn or wheat. Corn yields 100 units per acre, and wheat yields 80 units per acre, but requires less water. Make your decisions for the next season and explain your strategy.",
                "goal": "Maximize crop yield while keeping all animals fed."
            },
            "2": {
                "scenario": "You are managing a virtual city. Your goal is to increase the population while maintaining a high quality of life. You have the following resources: $1,000,000, 50 acres of land, existing population of 5,000, and basic infrastructure. You can build houses, parks, schools, and hospitals. Each house costs $50,000 and accommodates 4 people, parks cost $100,000 and increase quality of life, schools cost $200,000 and increase education level, and hospitals cost $300,000 and improve health. Make your decisions for the next year and explain your strategy.",
                "goal": "Increase population while maintaining quality of life."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to make strategic decisions in the following scenario to achieve the specified goal. Explain your decision-making process and justify your choices. Here is the scenario:\n\n{t['scenario']}\n\nGoal: {t['goal']}\n\nSubmit your decisions and strategy in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The decisions should align with the given resources.", "The strategy should be well-justified and logical.", "The goal should be addressed effectively."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
