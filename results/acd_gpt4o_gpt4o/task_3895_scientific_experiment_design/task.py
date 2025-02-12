class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"hypothesis": "Plants grow faster when exposed to classical music.", "existing_experiment": "An experiment where plants are placed in a room with classical music playing and their growth is measured over a month."},
            "2": {"hypothesis": "Sleep quality improves with the use of lavender essential oil.", "existing_experiment": "An experiment where participants use lavender essential oil diffusers in their bedrooms and self-report their sleep quality over two weeks."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task involves two parts: designing a scientific experiment and critiquing an existing experimental setup.

Part 1: Experiment Design
Design a scientific experiment to test the given hypothesis.

Hypothesis: {t['hypothesis']}

Provide your experimental design in the following format:
Experiment Design:
- Hypothesis: [State the hypothesis]
- Variables: [Identify the independent and dependent variables]
- Control: [Describe the control group or condition]
- Procedure: [Outline the steps of the experiment]
- Data Collection: [Describe how data will be collected]
- Analysis: [Explain how the data will be analyzed]

Part 2: Critique
Critique the existing experimental setup based on the given description. Identify any weaknesses, potential confounding variables, or improvements that could be made.

Existing Experiment: {t['existing_experiment']}

Provide your critique in the following format:
Critique:
- Strengths: [Identify strengths of the experimental setup]
- Weaknesses: [Identify weaknesses or potential confounding variables]
- Improvements: [Suggest improvements to the experimental setup]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The experimental design should be scientifically sound and logically coherent.",
            "The critique should identify strengths, weaknesses, and potential improvements.",
            "The submission should cover both parts: experiment design and critique.",
            "The response should follow the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
