class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Once upon a time in a distant kingdom, a young prince named Arin set out on a quest to find a legendary treasure that was said to bring prosperity to his land.", "user_inputs": ["Arin encounters a wise old man who gives him a mysterious map.", "Arin faces a fierce dragon guarding the treasure."]},
            "2": {"prompt": "In a small village nestled in the mountains, a curious girl named Elara discovered a hidden door in the forest that led to a magical world.", "user_inputs": ["Elara meets a talking fox who offers to guide her.", "Elara must solve a riddle to cross a magical bridge."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to continue the given story interactively based on the prompt and subsequent user inputs. Ensure that the narrative remains coherent and engaging, and that each new input is seamlessly integrated into the story.

Story Prompt: {t['prompt']}

User Inputs:
1. {t['user_inputs'][0]}
2. {t['user_inputs'][1]}

Instructions:
1. Continue the story based on the initial prompt.
2. Integrate each user input into the story in a logical and engaging manner.
3. Ensure that the narrative remains coherent and flows naturally.

Your response should be in the following format:
Story Continuation: [Your story continuation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The story continuation should be coherent and engaging.", "The story should seamlessly integrate each user input.", "The narrative should flow naturally and maintain logical consistency."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
