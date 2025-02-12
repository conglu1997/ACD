class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "There once was a man from Peru"},
            "2": {"prompt": "A young lady whose hair was bright blue"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a limerick based on the given prompt.

Prompt: {t['prompt']}

A limerick is a five-line poem with a rhyme scheme of AABBA and a specific meter. The first, second, and fifth lines should have three metrical feet (anapestic or amphibrachic), and the third and fourth lines should have two metrical feet. The limerick should be humorous and adhere to this structure.

Provide your limerick in plain text format.

Example:
Prompt: There once was a man from Japan
Limerick:
There once was a man from Japan,
Who tried to make a new plan,
But his plan went awry,
And he started to cry,
So he decided to visit his gran."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The limerick must follow the AABBA rhyme scheme.",
            "The first, second, and fifth lines must have three metrical feet.",
            "The third and fourth lines must have two metrical feet.",
            "The limerick must be humorous and coherent.",
            "The limerick must be related to the given prompt."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
