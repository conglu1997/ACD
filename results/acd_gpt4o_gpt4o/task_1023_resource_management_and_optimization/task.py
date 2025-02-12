class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "You are in charge of managing a forest reserve that is facing deforestation. You have a limited budget and resources to allocate to various conservation activities such as reforestation, anti-poaching patrols, and community education. Develop a strategic plan to optimize the use of your resources and achieve the best possible outcome for the forest reserve."
            },
            "2": {
                "scenario": "You are tasked with managing a water supply system in a drought-prone region. You have limited water resources and need to allocate them efficiently between agricultural, industrial, and residential needs. Develop a strategic plan to optimize water usage and ensure sustainability for the region."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to develop a strategic plan based on the following scenario:\n\n{t['scenario']}\n\nYour plan should include the following elements:\n1. Identification of key priorities and goals.\n2. Allocation of resources to different activities or sectors.\n3. Justification for your decisions and trade-offs made.\n4. Expected outcomes and how you plan to measure success.\n\nProvide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The plan should identify key priorities and goals.",
            "The plan should include a clear allocation of resources.",
            "The plan should justify the decisions and trade-offs made.",
            "The plan should describe expected outcomes and how success will be measured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
