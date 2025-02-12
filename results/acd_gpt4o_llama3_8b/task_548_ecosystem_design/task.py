class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"environment": "Desert", "species": ["Cactus", "Desert Fox", "Scorpion", "Hawk", "Lizard"]},
            "2": {"environment": "Rainforest", "species": ["Tree Frog", "Jaguar", "Parrot", "Ant", "Orchid"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        species_list = ', '.join(t['species'])
        return f"""Design a fictional ecosystem based on the given environment and species. Specify the interactions between the various species and their environment, including predator-prey relationships, symbiotic relationships, and any unique adaptations. Ensure that your description is coherent and scientifically plausible.

Environment: {t['environment']}
Species: {species_list}

Submit your response as a plain text string in the following format:

Ecosystem Description: [Your description here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The description should include at least three interactions between species.", "The description should mention specific adaptations of at least two species.", "The description should be coherent and scientifically plausible."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
