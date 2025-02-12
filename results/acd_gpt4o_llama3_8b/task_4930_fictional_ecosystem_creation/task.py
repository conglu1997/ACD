class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "data": {
                    "biome": "rainforest",
                    "unique_element": "bioluminescent plants"
                }
            },
            "2": {
                "data": {
                    "biome": "desert",
                    "unique_element": "underground rivers"
                }
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        biome = t['data']['biome']
        unique_element = t['data']['unique_element']
        return f"""Create a detailed description of a fictional natural ecosystem set in a {biome} biome. Include the unique element of {unique_element} in your ecosystem. Describe the flora, fauna, and other components of this ecosystem, and explain how they interact with each other and their environment. Ensure that the ecosystem is scientifically plausible and integrates relevant ecological principles.

Submit your response as a plain text string in the following format:

Ecosystem Description: [Your description]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The ecosystem should be scientifically plausible.",
            "The description should integrate relevant ecological principles.",
            "The interactions among components should be detailed and logical."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
