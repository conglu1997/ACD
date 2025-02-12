class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Once upon a time in a small village nestled between two mountains, there lived a young girl named Elara who possessed a mysterious power. She could communicate with animals and had a special bond with a majestic white wolf named Luna. One day, a dark cloud appeared over the village, and Elara knew that something terrible was about to happen. She decided to ...",
                "constraints": "The continuation should introduce a new character who helps Elara in her quest. The new character must have a unique ability that complements Elara's powers. The story should include at least one dialogue between Elara and the new character."
            },
            "2": {
                "prompt": "In the bustling city of Metropia, a brilliant scientist named Dr. Aiden was on the verge of a groundbreaking discovery. He had developed a device that could manipulate time, but he knew that such power came with great responsibility. As he pondered the potential consequences, an unexpected visitor arrived at his laboratory. It was ...",
                "constraints": "The continuation should introduce a conflict that challenges Dr. Aiden's moral values. The visitor must have a hidden agenda related to the time-manipulation device. The story should include a moral dilemma that Dr. Aiden faces."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Continue the following story prompt while adhering to the specified constraints:

Prompt: {t['prompt']}

Constraints: {t['constraints']}

Your response should include a continuation of the story that follows the given constraints. Ensure that the story remains coherent and maintains narrative consistency. Submit your continuation as a plain text string in the following format:

[Your story continuation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The continuation should introduce a new character (Task 1) or a conflict (Task 2) as specified.",
            "The continuation should include the required dialogue or moral dilemma.",
            "The story should remain coherent and maintain narrative consistency."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
