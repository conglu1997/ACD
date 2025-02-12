class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Describe the sound of a thunderstorm in vivid detail. Include the different elements of the storm such as thunder, lightning, rain, and wind."
            },
            "2": {
                "prompt": "Imagine and describe the sound of a futuristic city. Consider elements like transportation, communication devices, and the general ambiance."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to generate a detailed textual description of the following sound scenario:\n\n{t['prompt']}\n\nEnsure that your description is vivid, includes various elements of the sound, and creates a clear auditory image for the reader. Provide your response in plain text format using the following structure:\n\nDescription: [Your detailed description]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should be vivid and detailed.",
            "The description should include various elements of the sound scenario.",
            "The description should create a clear auditory image for the reader."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
