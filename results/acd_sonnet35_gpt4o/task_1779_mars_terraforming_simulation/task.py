class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "focus": "atmospheric modification",
                "ethical_concern": "potential impact on indigenous microbial life"
            },
            "2": {
                "focus": "water cycle establishment",
                "ethical_concern": "resource allocation between Earth and Mars"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        base_instructions = """Design a comprehensive simulation system for Mars terraforming, focusing on {focus}. Your task is to create a detailed plan for a simulation that models the long-term effects of terraforming efforts on Mars, incorporating various scientific disciplines and addressing ethical considerations. Your response should include the following sections:

1. Simulation System Architecture (300-350 words):
   a) Describe the overall structure of your simulation system, including key components and their interactions.
   b) Explain how your system integrates knowledge from relevant scientific fields (e.g., astrophysics, geology, climate science, biology).
   c) Detail the main variables and parameters your simulation will track and model.
   d) Discuss how your system handles different timescales, from immediate effects to long-term consequences.

2. Terraforming Strategies and Modeling (250-300 words):
   a) Propose specific terraforming strategies related to {focus}.
   b) Explain how your simulation models these strategies and their effects on the Martian environment.
   c) Describe any novel approaches or technologies your simulation incorporates.
   d) Discuss how your system accounts for potential feedback loops and unintended consequences.

3. Data Integration and Analysis (200-250 words):
   a) Explain how your simulation integrates data from various sources (e.g., satellite observations, rover data, theoretical models).
   b) Describe the data processing and analysis techniques used in your system.
   c) Discuss how your simulation handles uncertainties and gaps in current scientific knowledge.

4. Visualization and Interaction (150-200 words):
   a) Describe how your simulation presents results and allows for user interaction.
   b) Explain any novel visualization techniques you've incorporated to represent complex data and long-term trends.
   c) Discuss how your system could be used as a tool for scientific exploration and decision-making.

5. Ethical Considerations (200-250 words):
   a) Address the ethical concern: {ethical_concern}
   b) Explain how your simulation incorporates ethical considerations into its modeling and decision-making processes.
   c) Discuss potential long-term consequences of terraforming Mars and how your simulation helps in evaluating them.

6. Validation and Future Development (150-200 words):
   a) Propose methods for validating your simulation's accuracy and reliability.
   b) Suggest areas for future improvement or expansion of your simulation system.
   c) Discuss how your system could adapt to new scientific discoveries or technological advancements.

Ensure your response demonstrates a deep understanding of the scientific principles involved in Mars terraforming, as well as the computational challenges of simulating complex planetary systems. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Your total response should be between 1250-1550 words. Include at least one diagram or pseudocode snippet to illustrate a key aspect of your simulation system."""

        return base_instructions.format(focus=t["focus"], ethical_concern=t["ethical_concern"])

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of Mars terraforming concepts and challenges.",
            "The simulation system design is comprehensive, innovative, and scientifically plausible.",
            "The response effectively integrates knowledge from multiple scientific disciplines.",
            "The ethical considerations are thoughtfully addressed and incorporated into the simulation design.",
            "The response includes a clear diagram or pseudocode snippet illustrating a key aspect of the simulation system."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
