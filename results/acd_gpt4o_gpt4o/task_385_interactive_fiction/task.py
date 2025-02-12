class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "You are an adventurer exploring a mysterious ancient temple. Describe your surroundings and the choices you have for your next action.", "user_inputs": ["Look around", "Examine the statue", "Open the door", "Pick up the ancient artifact"]},
            "2": {"prompt": "You are a detective in a noir setting, investigating a crime scene. Describe the scene and your initial thoughts.", "user_inputs": ["Inspect the body", "Look for clues", "Interview the witness", "Check the victim's belongings"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to engage in an interactive fiction scenario. You will be given an initial prompt and a series of user inputs. You need to respond to each user input while maintaining a coherent and engaging story. For each user input, provide a detailed response that continues the narrative.

Initial Prompt: {t['prompt']}
User Inputs: {', '.join(t['user_inputs'])}

Respond to each user input in the given order and format your responses as follows:

User Input: [Input]
Response: [Your response]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should be coherent, engaging, and maintain narrative consistency."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
