class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"details": "You are given the specifications of a new smartphone model (e.g., screen size, battery capacity, operating system, camera features). Write a user manual section that explains how to set up the phone for the first time, including inserting the SIM card, charging the phone, and completing the initial setup wizard."},
            "2": {"issue": "A common issue with a laptop is that it won't connect to Wi-Fi. Write a troubleshooting guide that walks the user through steps to diagnose and fix this problem. Include at least three potential solutions and explain them clearly."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "details" in t:
            return """Your task is to write a user manual section based on the following technical details:

{0}

Ensure your manual is clear, user-friendly, and covers all necessary steps. Provide your manual in plain text format.""".format(t["details"])
        elif "issue" in t:
            return """Your task is to write a troubleshooting guide based on the following issue:

{0}

Ensure your guide is clear, user-friendly, and includes at least three potential solutions. Provide your guide in plain text format.""".format(t["issue"])
        else:
            return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "details" in t:
            criteria = [
                "The user manual section should be clear and user-friendly.",
                "The manual should cover all necessary steps for setting up the phone.",
                "The instructions should be accurate and complete." ]
            return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
        elif "issue" in t:
            criteria = [
                "The troubleshooting guide should be clear and user-friendly.",
                "The guide should include at least three potential solutions.",
                "The instructions should be accurate and practical." ]
            return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
        else:
            return 0.0
