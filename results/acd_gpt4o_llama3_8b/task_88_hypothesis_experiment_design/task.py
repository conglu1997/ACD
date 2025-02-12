class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"topic": "plant growth under different light conditions"},
            "2": {"topic": "effect of pH on enzyme activity"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        topic = t['topic']
        return f"""Generate a scientific hypothesis based on the following topic: '{topic}'. Then, design an experiment to test this hypothesis. Ensure that your hypothesis is clear and testable. Your experimental design should include the following components:
1. A brief description of the experimental setup, including any necessary equipment and materials.
2. The independent and dependent variables, clearly defined.
3. The control variables, and how they will be managed.
4. A step-by-step procedure to be followed, detailing each phase of the experiment.
5. A description of how the data will be collected, including any specific measurements or observations.
6. An outline of how the data will be analyzed to determine if the hypothesis is supported or refuted.

Submit your response as a plain text string in the following format:
'Hypothesis: [Your hypothesis] Experiment: [Your experimental design]'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The hypothesis should be clear and testable.",
            "The experimental design should include all required components: experimental setup, independent and dependent variables, control variables, procedure, data collection, and data analysis.",
            "The experimental design should be logical, coherent, and feasible."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
