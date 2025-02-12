class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "object": "a simple bookshelf",
                "parts": [
                    "2 side panels",
                    "3 shelves",
                    "1 back panel",
                    "12 screws",
                    "1 screwdriver"
                ]
            },
            "2": {
                "object": "a basic table",
                "parts": [
                    "1 tabletop",
                    "4 legs",
                    "8 bolts",
                    "1 wrench"
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are given a list of parts and the name of an object. Generate step-by-step assembly instructions to assemble the object using the given parts.

Object: {t['object']}
Parts: {', '.join(t['parts'])}

Submit your instructions as a plain text string in the following format:
Step 1: [Instruction]
Step 2: [Instruction]
Step 3: [Instruction]
...

Ensure that each step is clear, detailed, and necessary for the assembly of the object. The steps should be in a logical sequence and sufficient to complete the assembly."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The instructions should be clear and logically ordered.",
            "The instructions should correctly use all the listed parts to assemble the object.",
            "The instructions should follow a logical sequence and be easy to follow.",
            "All steps should be necessary and sufficient to complete the assembly.",
            "Each step should be clear and detailed."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
