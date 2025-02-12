class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"object": "a basic wooden chair", "action": "assemble"},
            "2": {"object": "a desktop computer", "action": "disassemble"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate detailed step-by-step instructions to {t['action']} {t['object']}.

Your response should include:
1. A list of required tools and materials.
2. Clear, logically ordered steps.
3. Safety precautions, if any.
4. Tips or common mistakes to avoid.

Ensure your instructions are thorough, easy to follow, and include all necessary details.

Provide your response in the following format:
Tools and Materials:
- [List of tools and materials]

Steps:
1. [Step 1]
2. [Step 2]
...

Safety Precautions:
- [Precaution 1]
- [Precaution 2]
...

Tips and Common Mistakes:
- [Tip 1]
- [Tip 2]
..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a list of required tools and materials.",
            "The response should provide clear, logically ordered steps.",
            "The response should include safety precautions, if any.",
            "The response should include tips or common mistakes to avoid."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
