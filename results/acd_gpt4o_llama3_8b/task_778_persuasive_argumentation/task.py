class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Generate a persuasive argument in favor of implementing a four-day workweek."
            },
            "2": {
                "prompt": "Critique the following argument against universal basic income: 'Universal basic income will make people lazy and unwilling to work, leading to a decline in productivity and economic growth.'"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Perform the following task:

{t["prompt"]}

For task 1, your response should include a coherent and convincing argument with supporting evidence. Elements of a strong argument include a clear thesis, logical structure, relevant examples, and compelling reasoning. Ensure your argument is detailed and thorough.

For task 2, your critique should address the strengths and weaknesses of the argument, providing counterarguments and evidence where appropriate. Elements of a strong critique include identifying logical fallacies, providing counterexamples, and discussing potential implications. Ensure your critique is detailed and thorough.

Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["prompt"].startswith("Generate"):
            validation_criteria = [
                "The argument should be coherent and convincing.",
                "The argument should include supporting evidence.",
                "The argument should have a clear thesis and logical structure.",
                "The argument should use relevant examples and compelling reasoning.",
                "The argument should be detailed and thorough."]
        else:
            validation_criteria = [
                "The critique should address the strengths and weaknesses of the argument.",
                "The critique should provide counterarguments and evidence where appropriate.",
                "The critique should identify logical fallacies.",
                "The critique should discuss potential implications.",
                "The critique should be detailed and thorough."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
