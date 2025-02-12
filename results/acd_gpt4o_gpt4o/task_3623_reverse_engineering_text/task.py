class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"final_output": "The cake was half-baked and the frosting was melting."},
            "2": {"final_output": "The treasure map was found inside an old, dusty book."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Your task is to deduce the original sequence of transformations or steps that led to the given final output. Here is the final output:\n\n{t['final_output']}\n\nProvide a detailed step-by-step reconstruction in the following format:\nStep 1: [Description]\nStep 2: [Description]\n...\nStep N: [Description]\n"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The reconstructed steps should logically and accurately lead to the final output."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
