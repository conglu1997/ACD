class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Create a mystery scenario involving a stolen artifact from a museum. Include at least 3 characters and 5 clues. Provide a logical solution to the mystery explaining how the artifact was stolen and who the culprit is.",
                "instructions": "Create a detailed mystery scenario based on the following prompt: 'A valuable artifact has been stolen from a museum. Include at least 3 characters and 5 clues in your scenario. Then provide a logical solution to the mystery explaining how the artifact was stolen and who the culprit is.' Ensure that your scenario is engaging, coherent, and logically consistent. The total word count for the scenario and solution should be between 500 to 800 words. Submit your response as a plain text string."
            },
            "2": {
                "prompt": "Create a mystery scenario involving a disappearance at a remote cabin. Include at least 4 characters and 6 clues. Provide a logical solution to the mystery explaining what happened to the missing person and who is responsible.",
                "instructions": "Create a detailed mystery scenario based on the following prompt: 'A person has disappeared from a remote cabin. Include at least 4 characters and 6 clues in your scenario. Then provide a logical solution to the mystery explaining what happened to the missing person and who is responsible.' Ensure that your scenario is engaging, coherent, and logically consistent. The total word count for the scenario and solution should be between 500 to 800 words. Submit your response as a plain text string."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a detailed mystery scenario based on the following prompt: '{t['prompt']}'. Ensure that your scenario is engaging, coherent, and logically consistent. Include the required number of characters and clues as specified in the prompt. The total word count for the scenario and solution should be between 500 to 800 words. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The scenario should be engaging and coherent.",
            "The scenario should include the required number of characters and clues.",
            "The solution should be logically consistent and explain the mystery.",
            "The total word count should be between 500 to 800 words."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
