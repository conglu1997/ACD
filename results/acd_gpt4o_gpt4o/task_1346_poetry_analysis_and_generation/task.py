class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"format": "haiku", "example": "An old silent pond... \nA frog jumps into the pond, \nsplash! Silence again."},
            "2": {"format": "sonnet", "example": "Shall I compare thee to a summer's day? \nThou art more lovely and more temperate..."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        format = t["format"]
        example = t["example"]
        instructions = f"""Your task is to analyze the following {format} and generate a new {format} following the same structure and rules.

Example {format}:
{example}

For a haiku:
- A haiku must have three lines.
- The first line should have 5 syllables.
- The second line should have 7 syllables.
- The third line should have 5 syllables.

For a sonnet:
- A sonnet must have 14 lines.
- Each line should be written in iambic pentameter.
- The rhyme scheme should follow the pattern ABABCDCDEFEFGG.

1. Analyze the given {format} and explain its meaning, structure, and any notable literary techniques used.
2. Generate a new {format} following the same structure and rules.

Provide your response in the following format:

Analysis: [Your analysis]
New {format}: [Your new {format}]

Ensure your analysis is detailed and your generated {format} adheres to the structural rules of the given format.
Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should be detailed and accurate, covering the meaning, structure, and literary techniques of the given poem.",
            "The generated poem should adhere to the specific structural rules of the given format.",
            "The generated poem should be creative and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
