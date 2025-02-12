class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"constraints": "rhyme scheme: ABAB, meter: iambic pentameter, theme: nature"},
            "2": {"constraints": "rhyme scheme: AABB, meter: trochaic tetrameter, theme: love"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        constraints = t['constraints']
        return f"""Generate a poem based on the following constraints: {constraints}. The poem should adhere strictly to the given rhyme scheme, meter, and theme. Here are examples to illustrate the specified constraints:

Rhyme Scheme ABAB:
Line 1 (ends with word A)
Line 2 (ends with word B)
Line 3 (ends with word A)
Line 4 (ends with word B)

Iambic Pentameter Example:
This is an example line in pentameter.
(x / x / x / x / x /)
Explanation: Each line should have ten syllables, with every second syllable stressed.
Another example: "Shall I compare thee to a summer's day?"

Trochaic Tetrameter Example:
This is a trochaic line.
(/ x / x / x / x)
Explanation: Each line should have eight syllables, with every first syllable stressed.
Another example: "Tyger Tyger, burning bright."

Submit your response as a plain text string in the following format:

Poem:
[Your poem here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The poem should adhere to the given rhyme scheme.",
            "The poem should follow the specified meter.",
            "The poem should clearly reflect the given theme."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
