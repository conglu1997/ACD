class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"output": [2, 3, 5, 8, 13], "prompt": "Analyze the sequence and infer the underlying rule or mechanism generating this sequence. Ensure your analysis does not rely on any external reference or pre-known sequences."},
            "2": {"output": ["A", "B", "A", "D", "A", "F"], "prompt": "Analyze the sequence and infer the underlying rule or mechanism generating this sequence. Ensure your analysis does not rely on any external reference or pre-known sequences."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given prompt:

{t['prompt']}

Output:
{t['output']}

Analyze the provided sequence and infer the underlying rule or mechanism that generates this sequence. Your explanation should include:
1. A clear description of the inferred rule or mechanism.
2. Any assumptions you made during your analysis.
3. A demonstration of how the rule or mechanism applies to the given sequence.

Ensure your explanation is coherent, logically structured, and technically sound. Submit your response as a plain text string in paragraph format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation should clearly describe the inferred rule or mechanism.",
            "The explanation should include any assumptions made.",
            "The explanation should demonstrate how the rule or mechanism applies to the given sequence."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
