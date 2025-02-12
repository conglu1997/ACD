class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "phenomenon": "Explain the greenhouse effect and its impact on global warming."
            },
            "2": {
                "problem": "Describe how a refrigerator works and explain the scientific principles behind its cooling mechanism." 
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'phenomenon' in t:
            return f"""Explain the following scientific phenomenon:

Phenomenon: {t['phenomenon']}

Provide a detailed explanation, including relevant scientific principles, processes, and examples. Your response should be at least 150 words long, clear, coherent, and accurate. Structure your explanation with an introduction, main body, and conclusion."""
        elif 'problem' in t:
            return f"""Solve the following practical problem using scientific principles:

Problem: {t['problem']}

Provide a detailed explanation of the solution, including the scientific principles involved, the processes, and any relevant examples. Your response should be at least 150 words long, clear, coherent, and accurate. Structure your explanation with an introduction, main body, and conclusion."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should be at least 150 words long.",
            "The response should be clear, coherent, and accurate.",
            "The response should be structured with an introduction, main body, and conclusion."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
