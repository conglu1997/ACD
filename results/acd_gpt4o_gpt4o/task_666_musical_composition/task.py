class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "A serene morning in the countryside", "constraints": "Use a 4/4 time signature, include at least two different instruments, and the piece should be in the key of C major."},
            "2": {"theme": "A bustling cityscape at night", "constraints": "Use a 3/4 time signature, include at least three different instruments, and the piece should be in the key of G minor."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to compose a short piece of music based on the following theme and constraints:

Theme: {t['theme']}

Constraints:
{t['constraints']}

Provide your composition in the form of a plain text description. Your description should include:
1. The instruments used.
2. The structure of the composition (e.g., verse, chorus, bridge).
3. The tempo of the piece.
4. The key of the piece.
5. A brief explanation of how the music reflects the given theme.
6. Any specific musical elements or motifs that are important to the composition.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The composition should use the specified time signature.",
            "The composition should include the required number of different instruments.",
            "The composition should be in the specified key.",
            "The description should explain how the music reflects the given theme.",
            "The composition should be creative and coherent."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
