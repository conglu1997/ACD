class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Imagine a future where humans have colonized the oceans. Describe a day in the life of an ocean colonist, including details about their environment, daily activities, and any challenges they face. Include interactions with marine life and the use of advanced underwater technology."},
            "2": {"prompt": "Create a scenario where all animals in the world suddenly gain human-level intelligence. Describe how society adapts to this change, including the impact on politics, economics, and daily life. Detail interactions between humans and animals, and new laws that might be enacted."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given prompt:

{t["prompt"]}

Your scenario should be detailed, imaginative, and coherent. Ensure that you integrate various elements seamlessly to create a plausible and engaging narrative. Submit your response as a plain text string in the following format:

Response: [Your scenario here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The scenario should be detailed and imaginative.", "The narrative should be coherent and integrate various elements seamlessly."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
