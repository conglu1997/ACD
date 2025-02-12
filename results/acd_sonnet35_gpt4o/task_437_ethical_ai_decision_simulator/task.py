class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "Autonomous vehicle accident avoidance",
                "ethical_framework": "Utilitarianism",
                "cognitive_bias": "Loss aversion"
            },
            "2": {
                "scenario": "AI-assisted medical triage in a disaster",
                "ethical_framework": "Deontological ethics",
                "cognitive_bias": "Availability heuristic"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates human-like ethical decision-making processes for the scenario of {t['scenario']}. Your system should incorporate the ethical framework of {t['ethical_framework']} and account for the cognitive bias of {t['cognitive_bias']}.

Brief explanations:
- {t['ethical_framework']}: {TaskFamily._get_ethical_framework_explanation(t['ethical_framework'])}
- {t['cognitive_bias']}: {TaskFamily._get_cognitive_bias_explanation(t['cognitive_bias'])}

Your task has the following parts:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI ethical decision-making system.
   b) Explain how it integrates principles from cognitive science, ethics, and artificial intelligence.
   c) Discuss how the system incorporates the specified ethical framework and cognitive bias.
   d) Provide a simple diagram or flowchart of your system architecture.

2. Decision-Making Process (200-250 words):
   a) Detail the step-by-step process your AI system uses to make ethical decisions in the given scenario.
   b) Explain how the system weighs different ethical considerations and potential outcomes.
   c) Describe how the specified cognitive bias is modeled and influences the decision-making process.

3. Scenario Analysis (200-250 words):
   a) Apply your AI system to a specific instance of the given scenario.
   b) Describe the ethical dilemma and the decision reached by your system.
   c) Analyze how the ethical framework and cognitive bias influenced the outcome.

4. Comparison to Human Decision-Making (150-200 words):
   a) Compare your AI system's decision-making process to typical human ethical reasoning.
   b) Discuss similarities and differences in approach and potential outcomes.
   c) Analyze potential advantages and limitations of your AI approach compared to human decision-making.

5. Ethical Implications (150-200 words):
   a) Discuss the ethical implications of using AI systems for moral decision-making in real-world scenarios.
   b) Address potential concerns about AI bias, transparency, and accountability.
   c) Propose guidelines for the responsible development and use of ethical AI decision-making systems.

6. Future Developments (100-150 words):
   a) Suggest two potential improvements or extensions to your AI ethical decision-making system.
   b) Briefly describe how these developments could enhance the system's capabilities or address current limitations.

Ensure your response demonstrates a deep understanding of cognitive science, ethics, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility.

Include references or examples to support your reasoning throughout your response. Also, address any potential conflicts between the ethical framework and the cognitive bias in your system design and analysis.

Format your response using clear headings for each section, adhering to the word limits provided. Your total response should be between 1050-1350 words, not including the diagram. Include the diagram as a text-based representation (e.g., ASCII art or a structured text description) within your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive science, ethics, and artificial intelligence, integrating these disciplines effectively.",
            "The AI system design is creative, plausible, and adequately incorporates the specified ethical framework and cognitive bias.",
            "The decision-making process and scenario analysis are well-explained and logically consistent.",
            "The comparison to human decision-making and discussion of ethical implications show insightful analysis.",
            "The response addresses potential conflicts between the ethical framework and the cognitive bias, and provides a reasonable approach to handling these conflicts.",
            "The response includes relevant references or examples to support the reasoning throughout.",
            "The response adheres to the specified format and word limits, and includes a clear system architecture diagram."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

    @staticmethod
    def _get_ethical_framework_explanation(framework: str) -> str:
        explanations = {
            "Utilitarianism": "An ethical theory that states the most ethical choice is the one that produces the greatest good for the greatest number of people.",
            "Deontological ethics": "An ethical theory that judges the morality of an action based on the action's adherence to a rule or rules."
        }
        return explanations.get(framework, "No explanation available.")

    @staticmethod
    def _get_cognitive_bias_explanation(bias: str) -> str:
        explanations = {
            "Loss aversion": "The tendency to prefer avoiding losses to acquiring equivalent gains.",
            "Availability heuristic": "The tendency to overestimate the likelihood of events with greater 'availability' in memory, which can be influenced by how unusual or emotionally charged they may be."
        }
        return explanations.get(bias, "No explanation available.")
