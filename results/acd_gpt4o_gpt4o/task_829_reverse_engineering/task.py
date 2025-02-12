class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "reverse_engineer", "system": "simple_machine", "description": "A lever with a fulcrum positioned one-third of the way along its length. The lever is used to lift a weight by applying force at the longer end."},
            "2": {"task": "reverse_engineer", "system": "computer_algorithm", "description": "A sorting algorithm that repeatedly steps through a list, compares adjacent elements and swaps them if they are in the wrong order. The process is repeated until the list is sorted."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Your task is to reverse engineer the following {t['system']} based on its description: '{t['description']}'. Provide your response as a detailed explanation or representation of the system or process in plain text format. Ensure your response accurately captures the key components and functioning of the original system."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should accurately capture the key components of the system.",
            "The response should accurately describe the functioning of the system.",
            "The response should be clear and detailed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
