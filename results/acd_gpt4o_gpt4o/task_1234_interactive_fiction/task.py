class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A lost traveler in a mysterious forest",
                "initial_choice": "The traveler comes across a fork in the path. Does he go left or right?"
            },
            "2": {
                "scenario": "A detective in a haunted mansion",
                "initial_choice": "The detective hears a noise upstairs and downstairs. Where does she investigate first?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to design a branching storyline for an interactive fiction scenario based on the given context. Start with the initial choice and create two distinct paths from that choice. Each path should lead to at least two more choices, forming a small branching narrative. Ensure that each choice and resulting storyline is coherent, engaging, and logically consistent with the scenario.\n\nScenario: {t['scenario']}\nInitial Choice: {t['initial_choice']}\n\nGuidelines:\n1. Create an engaging and coherent narrative for each branch.\n2. Ensure logical consistency and cause-effect relationships in each storyline.\n3. Provide your response in plain text format, with each path clearly delineated.\n\nExample Response:\nPath 1 - Left:\n  - The traveler finds an abandoned cabin. Does he enter or continue on the path?\n    - Enter: The cabin is occupied by a mysterious figure who offers help.\n    - Continue: The traveler encounters a wild animal.\nPath 2 - Right:\n  - The traveler discovers a river. Does he follow the river or build a raft?\n    - Follow: The river leads to a village.\n    - Build: The raft leads to a waterfall.\n"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The narrative is engaging and coherent.",
            "Each choice leads to a logically consistent outcome.",
            "The storylines are creative and maintain interest.",
            "The branching paths are clearly delineated."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
