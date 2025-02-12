class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"issue": "A user's computer is running very slowly. They have tried restarting, but it hasn't helped. Provide a detailed set of steps to diagnose and resolve the issue, considering possible causes such as insufficient RAM, malware, or excessive background processes."},
            "2": {"issue": "A user is unable to connect to the WiFi network on their laptop. They have checked that the WiFi is turned on. Provide a detailed set of steps to diagnose and resolve the issue, considering possible causes such as incorrect network settings, driver issues, or router problems."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to provide technical support for the following software issue. Explain the steps clearly and effectively to resolve the problem. Here is the issue:\n\n{t['issue']}\n\nSubmit your solution in plain text format. Your response should include:\n1. Restatement of the problem.\n2. Step-by-step instructions to diagnose the issue, considering various potential causes.\n3. Step-by-step instructions to resolve the issue.\n4. A brief explanation of why the solution should work.\n5. Any additional tips or preventive measures to avoid similar issues in the future."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The steps should be clear and logically ordered.", "The solution should be feasible and effective.", "The explanation should be concise and accurate.", "The response should consider multiple potential causes of the issue.", "Any additional tips or preventive measures should be relevant and useful."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
