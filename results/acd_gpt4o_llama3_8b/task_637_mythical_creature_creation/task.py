class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "criteria": "Create a mythical creature that lives in a forest. The creature should have features of both a bird and a mammal. Provide a detailed description including its physical appearance, habitat, behaviors, and any special abilities it possesses.",
                "instructions": "Based on the given criteria, create and describe a mythical creature. Ensure your description is detailed and logically consistent. Submit your response as a plain text string with the following sections: Physical Appearance, Habitat, Behaviors, Special Abilities."
            },
            "2": {
                "criteria": "Create a mythical creature that lives in the ocean. The creature should have features of both a reptile and a fish. Provide a detailed description including its physical appearance, habitat, behaviors, and any special abilities it possesses.",
                "instructions": "Based on the given criteria, create and describe a mythical creature. Ensure your description is detailed and logically consistent. Submit your response as a plain text string with the following sections: Physical Appearance, Habitat, Behaviors, Special Abilities."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Based on the following criteria, create and describe a mythical creature. Ensure your description is detailed and logically consistent. Submit your response as a plain text string with the following sections: Physical Appearance, Habitat, Behaviors, Special Abilities. Here are the criteria:

{t["criteria"]}

"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should include a detailed description of the creature's physical appearance.",
            "The response should describe the creature's habitat.",
            "The response should explain the creature's behaviors.",
            "The response should include any special abilities the creature possesses.",
            "The description should be logically consistent and culturally rich."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
