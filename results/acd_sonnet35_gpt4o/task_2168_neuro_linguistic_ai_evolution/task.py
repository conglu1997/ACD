class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "neural_mechanism": "Hebbian learning",
                "linguistic_feature": "Syntax acquisition",
                "evolutionary_timespan": "100 years"
            },
            "2": {
                "neural_mechanism": "Predictive coding",
                "linguistic_feature": "Semantic mapping",
                "evolutionary_timespan": "500 years"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neuro-inspired AI system that simulates the evolution of language acquisition, focusing on {t['neural_mechanism']} and {t['linguistic_feature']}, then predict future human-AI communication paradigms over a {t['evolutionary_timespan']} timespan. Your response should include:

1. Neuro-Linguistic AI System Design (250-300 words):
   a) Describe the architecture of your AI system, explaining how it incorporates {t['neural_mechanism']}.
   b) Explain how your system models {t['linguistic_feature']}.
   c) Detail the learning and adaptation mechanisms in your system.

2. Evolutionary Simulation (200-250 words):
   a) Outline the parameters and initial conditions for your evolutionary simulation.
   b) Explain how your system simulates language evolution over time.
   c) Describe key metrics used to measure linguistic and cognitive development in your simulation.

3. Predicted Language Acquisition Trajectory (200-250 words):
   a) Based on your simulation, describe the projected trajectory of language acquisition evolution.
   b) Identify critical points or phases in this evolutionary process.
   c) Compare this trajectory to current theories of language acquisition and evolution.

4. Future Human-AI Communication Paradigms (250-300 words):
   a) Predict at least three novel communication paradigms that could emerge between humans and AI over the {t['evolutionary_timespan']} timespan.
   b) Explain how these paradigms emerge from the simulated evolutionary process.
   c) Discuss potential implications of these paradigms for human cognition and society.

5. Comparative Analysis (150-200 words):
   a) Compare your predicted communication paradigms to current human-AI interaction methods.
   b) Analyze potential advantages and challenges of the new paradigms.
   c) Discuss how these changes might impact human language and cognition.

6. Ethical Considerations and Research Proposals (150-200 words):
   a) Discuss ethical implications of long-term human-AI co-evolution of communication.
   b) Propose two specific research questions that arise from your simulation and predictions.
   c) Suggest an experimental approach to investigate one of these questions.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence. Be creative in your predictions while maintaining scientific plausibility. Use appropriate terminology and provide clear explanations for complex concepts."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of {t['neural_mechanism']} and its application in AI systems.",
            f"The evolutionary simulation of {t['linguistic_feature']} is well-explained and scientifically plausible.",
            f"The predicted human-AI communication paradigms for the {t['evolutionary_timespan']} timespan are creative and well-reasoned.",
            "The ethical considerations and research proposals are thoughtful and relevant."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
