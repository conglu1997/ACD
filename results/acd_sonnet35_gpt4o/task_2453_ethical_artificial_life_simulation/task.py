import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            "resource-scarce", "predator-prey", "cooperative", "competitive"
        ]
        ethical_dilemmas = [
            "altruism vs selfishness", "individual vs group benefit",
            "short-term vs long-term survival", "truth-telling vs deception"
        ]
        evolutionary_mechanisms = [
            "natural selection", "genetic drift", "mutation", "gene flow"
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "environment": random.choice(environments),
                "ethical_dilemma": random.choice(ethical_dilemmas),
                "evolutionary_mechanism": random.choice(evolutionary_mechanisms)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze an artificial life simulation that incorporates ethical decision-making, exploring the emergence of moral behavior in evolving digital organisms. Your simulation should focus on a {t['environment']} environment, address the ethical dilemma of {t['ethical_dilemma']}, and emphasize the evolutionary mechanism of {t['evolutionary_mechanism']}. Your response should include the following sections:

1. Simulation Design (300-350 words):
   a) Describe the key components of your artificial life simulation, including the digital organisms and their environment.
   b) Explain how you model ethical decision-making in your digital organisms.
   c) Detail how the {t['evolutionary_mechanism']} mechanism is implemented in your simulation.
   d) Discuss how the {t['environment']} environment influences organism behavior and evolution.
   e) Provide a simple diagram or flowchart representing the structure of your simulation (described in text).

2. Ethical Framework (250-300 words):
   a) Explain how you represent and evaluate ethical behavior in your simulation.
   b) Describe how the {t['ethical_dilemma']} dilemma is implemented and how it affects organism fitness.
   c) Discuss any assumptions or simplifications you've made in modeling ethics in artificial life.
   d) Propose at least two quantifiable metrics for measuring ethical behavior in your simulation.

3. Simulation Process (200-250 words):
   a) Provide a step-by-step explanation of how your simulation runs, from initialization to multiple generations.
   b) Explain how ethical behaviors are passed on or modified through generations.
   c) Describe how you measure and track the emergence of moral behavior over time.
   d) Discuss any mechanisms for handling edge cases or unexpected behaviors in your simulation.

4. Predicted Outcomes (250-300 words):
   a) Describe the expected results of running your simulation over many generations.
   b) Explain how the {t['evolutionary_mechanism']} mechanism might influence the development of ethical behavior.
   c) Discuss any potential emergent phenomena or unexpected outcomes you anticipate.
   d) Provide a hypothetical dataset or graph illustrating the evolution of ethical behavior over time.

5. Analysis and Implications (200-250 words):
   a) Analyze the factors that most significantly impact the evolution of ethical behavior in your simulation.
   b) Discuss the philosophical and practical implications of your simulation for understanding the evolution of morality.
   c) Compare your simulation's predictions with real-world observations of moral behavior in biological systems.
   d) Propose at least two potential real-world applications of your simulation findings.

6. Ethical Considerations and Limitations (150-200 words):
   a) Discuss the ethical implications of creating simulations that model the evolution of morality.
   b) Address potential misuses or misinterpretations of your simulation results.
   c) Identify limitations of your approach and suggest ways to address them in future work.
   d) Propose guidelines for the responsible development and use of artificial life simulations in ethics research.

Ensure your response demonstrates a deep understanding of artificial life, evolutionary biology, ethics, and complex systems modeling. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility and ethical responsibility.

Format your answer with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately addresses the {t['environment']} environment, the ethical dilemma of {t['ethical_dilemma']}, and the evolutionary mechanism of {t['evolutionary_mechanism']}.",
            "The proposed simulation demonstrates a plausible approach to modeling ethical behavior in artificial life.",
            "The response shows a deep understanding of artificial life, evolutionary biology, ethics, and complex systems modeling.",
            "The ethical considerations and limitations are thoroughly discussed.",
            "The response is creative while maintaining scientific plausibility and ethical responsibility.",
            "The response includes a diagram or flowchart of the simulation structure and a hypothetical dataset or graph.",
            "The response proposes real-world applications of the simulation findings."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
