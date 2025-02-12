class TaskFamily:
    
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Discuss the implications of free will versus determinism. Construct a coherent argument in favor of one position and address potential counterarguments."
            },
            "2": {
                "prompt": "Analyze the ethical implications of artificial intelligence. Construct an argument considering both the potential benefits and risks, and address counterarguments."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to construct and analyze a philosophical argument based on the following prompt:\n\nPrompt: {t['prompt']}\n\nEnsure that your argument is coherent, well-structured, and considers potential counterarguments. Provide your response in plain text format. Structure your response as follows:\n\n1. Argument: [Your main argument]\n2. Counterarguments: [Address potential counterarguments]\n\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The argument should be coherent and well-structured.",
            "The argument should address potential counterarguments.",
            "The response should demonstrate an understanding of the philosophical concepts involved."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
