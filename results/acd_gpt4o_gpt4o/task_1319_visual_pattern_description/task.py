class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"pattern": "#1#2#3\n#4#5#6\n#7#8#9\n#10#11#12", "description": "Describe the pattern in the given 4x3 grid of symbols."},
            "2": {"pattern": "A - B - C - D\n|   |   |   |\nE - F - G - H\n|   |   |   |\nI - J - K - L", "description": "Interpret and describe the connections and layout in the given 4x3 diagram."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        pattern = t["pattern"]
        description = t["description"]
        instructions = f"""Your task is to interpret and describe the following visual pattern or diagram in detail:

Pattern:
{pattern}

{description}

Your response should include:
1. A comprehensive description of the pattern or diagram.
2. Any symmetries, repetitions, or notable features observed.
3. An explanation of how you interpreted the pattern or layout.

Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should be comprehensive and accurately reflect the given pattern or diagram.",
            "The response should identify any symmetries, repetitions, or notable features.",
            "The explanation should logically interpret the pattern or layout."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
