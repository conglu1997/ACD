class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "environment": "You are in a dense forest. To your north, there is a fast-flowing river with a narrow bridge. To your east, there is a steep mountain with a narrow trail. To your south, there is a small village with winding paths. To your west, there is a dark cave. Your task is to reach the village.",
                "destination": "village"
            },
            "2": {
                "environment": "You are in an old house. To your north, there is a dusty kitchen with a locked door. To your east, there is a garden with tall grass and a small gate. To your south, there is a living room with a hidden passage. To your west, there is a bedroom with a creaky floor. Your task is to reach the kitchen.",
                "destination": "kitchen"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        environment = t["environment"]
        destination = t["destination"]
        instructions = f"""Your task is to navigate the following virtual environment and provide clear instructions to reach the specified destination:

{environment}

Your response should include step-by-step navigation instructions, such as 'Go north', 'Turn east', etc. Your goal is to reach the {destination}. Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The navigation instructions should logically lead to the specified destination.",
            "The instructions should be clear and step-by-step.",
            "The response should not contain any unnecessary or incorrect steps."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
