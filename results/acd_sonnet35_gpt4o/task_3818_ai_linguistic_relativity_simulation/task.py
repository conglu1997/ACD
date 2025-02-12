import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_features = [
            {
                "feature": "Grammatical Gender",
                "description": "The classification of nouns into masculine, feminine, or neuter categories"
            },
            {
                "feature": "Evidentiality",
                "description": "Grammatical marking of the source of information in a statement"
            }
        ]
        return {str(i+1): feature for i, feature in enumerate(random.sample(linguistic_features, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and implement a simulation that tests the linguistic relativity hypothesis in artificial intelligence systems, focusing on the linguistic feature of {t['feature']}. Then, analyze its implications for AI development and human-AI interaction. Your response should include the following sections:

1. Simulation Design (300-350 words):
   a) Describe the overall architecture of your AI simulation system.
   b) Explain how you model the linguistic feature of {t['feature']} in your AI agents.
   c) Detail the learning process and interaction mechanisms of the AI agents.
   d) Discuss how you will measure the impact of {t['feature']} on the AI agents' cognition and behavior.
   e) Include a high-level pseudocode snippet (10-15 lines) illustrating a key aspect of your simulation.

2. Experiment Setup (250-300 words):
   a) Describe a specific experiment to test the linguistic relativity hypothesis using your simulation.
   b) Explain the variables you will manipulate and measure.
   c) Discuss your hypotheses and expected outcomes.
   d) Propose methods to control for confounding factors.

3. Results Analysis (200-250 words):
   a) Describe potential patterns or outcomes that would support or refute linguistic relativity in AI systems.
   b) Explain how you would interpret different possible results.
   c) Discuss the limitations of your simulation and how they might affect the interpretation of results.

4. Implications for AI Development (250-300 words):
   a) Analyze how your findings might influence the design of future AI systems.
   b) Discuss potential benefits or risks of AI systems with language-influenced cognition.
   c) Explore how this research could impact natural language processing and machine translation.
   d) Consider ethical implications of developing AI systems with language-specific cognitive biases.

5. Human-AI Interaction Analysis (200-250 words):
   a) Discuss how linguistic relativity in AI could affect human-AI communication and collaboration.
   b) Explore potential misunderstandings or biases that could arise in cross-linguistic AI interactions.
   c) Propose strategies to mitigate negative effects and leverage potential benefits in human-AI teams.

6. Future Research Directions (150-200 words):
   a) Suggest two novel experiments or extensions to further explore linguistic relativity in AI.
   b) Discuss how your approach could be adapted to study other aspects of language-cognition interaction in AI systems.
   c) Propose a potential real-world application of your findings.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a well-designed simulation that tests the linguistic relativity hypothesis in AI systems, focusing on {t['feature']}",
            "The response provides a detailed experiment setup with clear hypotheses and methods",
            "The response includes a thoughtful analysis of potential results and their implications",
            "The response discusses implications for AI development and human-AI interaction in depth",
            "The response demonstrates creativity and scientific plausibility in addressing the task",
            "The response is well-structured and adheres to the word count guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
