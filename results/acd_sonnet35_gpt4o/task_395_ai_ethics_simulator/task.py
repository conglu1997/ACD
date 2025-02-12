class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "technology": "Brain-Computer Interfaces for Dream Recording",
                "context": "A society with strict privacy laws but high technological adoption"
            },
            "2": {
                "technology": "Artificial Wombs for Human Gestation",
                "context": "A society with declining birth rates and traditional family values"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI Ethics Simulator to predict and analyze the ethical implications of {t['technology']} in {t['context']}. Your response should include:

1. System Architecture (200-250 words):
   a) Outline the key components of your AI Ethics Simulator.
   b) Explain how it integrates ethical frameworks, societal data, and technological parameters.
   c) Describe the simulation process and output format.

2. Ethical Considerations (250-300 words):
   a) Identify at least three potential ethical issues related to the given technology and context.
   b) Explain how your system would model and predict the impact of these issues.
   c) Discuss any limitations or biases in your system's ethical reasoning capabilities.

3. Scenario Analysis (200-250 words):
   a) Present a specific ethical dilemma that your system predicts for the given technology and context.
   b) Describe the factors contributing to this dilemma and potential outcomes.
   c) Explain how your system would assist in decision-making for this scenario.

4. Adaptive Learning (150-200 words):
   a) Propose a method for your system to learn and adapt its ethical reasoning based on real-world outcomes.
   b) Discuss potential risks and safeguards in allowing the system to evolve its ethical framework.

5. Interdisciplinary Integration (150-200 words):
   a) Explain how your system incorporates knowledge from at least three relevant disciplines (e.g., philosophy, sociology, law, psychology).
   b) Discuss any challenges in integrating these diverse fields and how you address them.

Ensure your response demonstrates a deep understanding of AI ethics, the given technology, and the societal context. Be creative in your design while maintaining scientific plausibility and ethical rigor."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all five required sections comprehensively.",
            "The AI Ethics Simulator design is innovative, plausible, and well-explained.",
            "The ethical analysis is nuanced, considering multiple perspectives and potential consequences.",
            "The response demonstrates a deep understanding of AI ethics, the given technology, and the societal context.",
            "The proposed system integrates knowledge from multiple disciplines effectively.",
            "The response shows creativity in addressing complex ethical challenges while maintaining scientific and ethical rigor."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
