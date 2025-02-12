class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Interpret the surrealist art piece described as follows: 'A clock melting over a tree branch in a desert under a sky filled with floating fish'."},
            "2": {"prompt": "Create a description for a surrealist art piece that includes the following elements: 'a giant snail with a cityscape on its shell, floating above an ocean with pink waves'."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret or create a description for a surrealist art piece based on the given prompt:\n\n{t['prompt']}\n\nEnsure that your response is imaginative, coherent, and captures the essence of surrealist art. Provide your response in plain text format. Structure your response as follows:\n1. Introduction: [Your introduction]\n2. Main Body: [Your main body]\n3. Conclusion: [Your conclusion]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should be imaginative and coherent.", "The response should capture the essence of surrealist art."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
