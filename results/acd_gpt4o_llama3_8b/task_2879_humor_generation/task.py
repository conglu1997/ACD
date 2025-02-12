class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Write a short, humorous story about a day in the life of a talking cat who works as a barista. Include interactions with at least three different customers and a funny mishap that occurs."},
            "2": {"prompt": "Create a funny dialogue between two aliens who are trying to understand human customs. Include at least one misunderstanding about a common human activity and a humorous resolution to the conversation."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        prompt = t['prompt']
        return f"""You are tasked with generating humorous content based on the provided prompt. Ensure that your response is engaging, coherent, and funny. Use creativity and wit to make the content entertaining.

Prompt: {prompt}

Submit your response as a plain text string in the following format:

Response: [Your humorous content here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The content should be coherent and logically consistent.",
            "The content should be humorous and entertaining.",
            "The content should align with the given prompt."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
