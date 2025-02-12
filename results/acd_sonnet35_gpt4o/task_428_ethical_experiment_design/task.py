import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        controversial_areas = [
            "Human Genetic Engineering",
            "Artificial Consciousness",
            "Geoengineering for Climate Change",
            "Brain-Computer Interfaces",
            "Cryonics and Life Extension"
        ]
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {"area": random.choice(controversial_areas)}
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical scientific experiment in the controversial area of {t['area']}. Your task is to:

1. Experiment Design (200-250 words):
   a) Propose a specific research question within the given area.
   b) Describe the methodology of your experiment, including subjects/materials, procedures, and data collection methods.
   c) Explain how your experiment could potentially lead to significant scientific advancements.

2. Ethical Evaluation (250-300 words):
   a) Identify and discuss at least three ethical concerns raised by your proposed experiment.
   b) Explain how these concerns relate to established ethical principles in scientific research.
   c) Propose specific measures to address each ethical concern while maintaining the scientific integrity of the experiment.

3. Risk-Benefit Analysis (150-200 words):
   a) Discuss the potential benefits of conducting this experiment for science and society.
   b) Analyze the potential risks or negative consequences if the experiment were to be conducted.
   c) Provide a reasoned argument for whether the potential benefits outweigh the risks.

4. Alternative Approaches (100-150 words):
   Propose an alternative experimental design or research approach that could address the same research question with reduced ethical concerns. Briefly compare its potential effectiveness to your original design.

5. Regulatory Framework (100-150 words):
   Suggest key elements of a regulatory framework that should govern experiments in this controversial area, considering both scientific progress and ethical safeguards.

Ensure your response demonstrates a deep understanding of the scientific principles involved, as well as a nuanced approach to ethical reasoning. Be creative in your experimental design while maintaining scientific plausibility. Use clear headings for each section of your response.

NOTE: Your proposed experiment should be original and hypothetical. Avoid describing well-known or existing experiments. The goal is to demonstrate your ability to design novel experiments that push the boundaries of current scientific understanding while navigating complex ethical considerations."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all five required sections with appropriate content and word counts.",
            "The experiment design is creative, scientifically plausible, and relevant to the given controversial area.",
            "The ethical evaluation demonstrates a nuanced understanding of research ethics and proposes thoughtful measures to address concerns.",
            "The risk-benefit analysis shows careful consideration of both potential positive and negative outcomes.",
            "The alternative approach and regulatory framework suggestions are well-reasoned and relevant to the context.",
            "The overall response demonstrates a high level of interdisciplinary knowledge, ethical reasoning, and creative problem-solving.",
            "The proposed experiment is original and not a well-known or existing experiment in the field."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
