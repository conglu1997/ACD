class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Construct an argument for the existence of free will and critique an argument against it."},
            "2": {"prompt": "Construct an argument against moral relativism and critique an argument in favor of it."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task involves two parts: construction and critique of philosophical arguments.

Part 1: Construction
Construct a well-reasoned argument based on the given prompt.

Prompt: {t['prompt']}

Provide your argument in the following format:
Argument:
- Thesis: [State your thesis]
- Premises: [List your premises]
- Conclusion: [State your conclusion]

Part 2: Critique
Critique the opposing argument based on the given prompt. Identify any logical fallacies, weaknesses, or counterexamples.

Provide your critique in the following format:
Critique:
- Thesis: [State the thesis of the opposing argument]
- Premises: [List the premises of the opposing argument]
- Critique: [Provide your critique of the argument]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The constructed argument should be well-reasoned and logically coherent.",
            "The critique should identify logical fallacies, weaknesses, or counterexamples in the opposing argument.",
            "The submission should cover both parts: construction and critique.",
            "The response should follow the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
