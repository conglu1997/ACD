class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "equipment": "office chair",
                "task_type": "assembly"
            },
            "2": {
                "equipment": "bicycle",
                "task_type": "disassembly"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate detailed step-by-step instructions for {t['task_type']} the following equipment: {t['equipment']}.

Your instructions should include the following sections:
1. Introduction: Briefly describe the equipment and the purpose of the task (assembly or disassembly). For example: 'This office chair is designed to provide ergonomic support. The purpose of this task is to assemble the chair from its individual parts.'
2. Tools Required: List all tools and materials needed. For example: 'Screwdriver, Allen wrench, screws, chair parts.'
3. Step-by-Step Instructions: Provide a detailed, numbered list of steps to complete the process. Each step should be clear and specific. For example:
   1. Attach the wheels to the base.
   2. Insert the gas lift into the base.
   3. Attach the seat to the gas lift.
4. Tips and Warnings: Include any tips for easier assembly/disassembly and warnings about potential issues or hazards. For example: 'Ensure all screws are tightly secured to avoid instability. Be cautious of pinch points when attaching the seat.'

The instructions should be clear, logical, and easy to follow. Use plain text for your submission. Here is an example format for the Step-by-Step Instructions section:

1. Step 1 description
2. Step 2 description
3. Step 3 description
...
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The instructions should be clear and logically ordered.",
            "The list of tools and materials should be complete and accurate.",
            "Each step should be specific and actionable.",
            "Tips and warnings should be relevant and helpful."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
