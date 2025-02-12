class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "social_scenario": "mass protest movement",
                "cognitive_bias": "confirmation bias",
                "ai_technique": "multi-agent reinforcement learning"
            },
            "2": {
                "social_scenario": "viral misinformation spread",
                "cognitive_bias": "availability cascade",
                "ai_technique": "graph neural networks"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models and predicts collective human behavior in complex social situations, integrating principles from cognitive science, social psychology, and artificial intelligence. Your task is to create a system capable of simulating and forecasting emergent social phenomena in the context of a {t['social_scenario']}, with a focus on the influence of {t['cognitive_bias']} and using {t['ai_technique']} as a key AI component. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for modeling collective behavior.
   b) Explain how your system integrates cognitive science, social psychology, and AI principles.
   c) Detail how the system incorporates the specified cognitive bias into its modeling.
   d) Discuss how the chosen AI technique is applied to predict emergent social phenomena.

2. Data Integration and Preprocessing (200-250 words):
   a) Describe the types of data your model would require (e.g., social media data, historical event data, psychological profiles).
   b) Explain how you would preprocess and integrate diverse data sources.
   c) Discuss ethical considerations in data collection and usage for this task.

3. Modeling Process (250-300 words):
   a) Outline the step-by-step process of how your AI system models collective behavior.
   b) Explain how individual cognitive processes are scaled to group-level phenomena.
   c) Describe how your system accounts for the dynamics of the specified social scenario.

4. Prediction and Analysis Capabilities (200-250 words):
   a) Detail the types of predictions your system can make about collective behavior.
   b) Explain how you would validate these predictions against real-world outcomes.
   c) Discuss the potential applications of your system in social science research or policy-making.

5. Handling Complexity and Uncertainty (150-200 words):
   a) Describe how your system manages the complexity of human social behavior.
   b) Explain your approach to quantifying and communicating uncertainty in predictions.
   c) Discuss any novel techniques used to handle emergent or chaotic social phenomena.

6. Ethical Implications and Safeguards (150-200 words):
   a) Analyze potential ethical issues arising from predicting collective human behavior.
   b) Propose specific safeguards to prevent misuse or manipulation of the system.
   c) Discuss the broader societal implications of such predictive capabilities.

7. Limitations and Future Directions (100-150 words):
   a) Identify key limitations of your current system design.
   b) Propose two potential improvements or extensions to enhance its capabilities.
   c) Suggest a future research direction that could address a current shortcoming in collective behavior prediction.

Ensure your response demonstrates a deep understanding of cognitive science, social psychology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively incorporates the specified social scenario ({t['social_scenario']}) in the system design.",
            f"The cognitive bias ({t['cognitive_bias']}) is accurately modeled and integrated into the collective behavior predictions.",
            f"The AI technique ({t['ai_technique']}) is appropriately applied and explained in the context of collective behavior modeling.",
            "The response demonstrates a deep understanding of cognitive science, social psychology, and artificial intelligence.",
            "The proposed system presents an innovative and plausible approach to modeling and predicting collective human behavior.",
            "The response addresses ethical implications and provides thoughtful safeguards against potential misuse.",
            "The overall response is well-structured, coherent, and adheres to the word count requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
