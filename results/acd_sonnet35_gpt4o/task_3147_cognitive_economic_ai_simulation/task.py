import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "economic_context": "Stock market during a financial crisis",
                "cognitive_bias": "Loss aversion",
                "heuristic": "Availability heuristic"
            },
            {
                "economic_context": "Consumer behavior in a new product launch",
                "cognitive_bias": "Anchoring effect",
                "heuristic": "Representativeness heuristic"
            },
            {
                "economic_context": "Housing market bubble",
                "cognitive_bias": "Overconfidence bias",
                "heuristic": "Affect heuristic"
            },
            {
                "economic_context": "Cryptocurrency trading",
                "cognitive_bias": "Herd mentality",
                "heuristic": "Availability heuristic"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates human economic decision-making in the context of {t['economic_context']}, incorporating the cognitive bias of {t['cognitive_bias']} and the {t['heuristic']}. Then, apply your system to analyze and predict outcomes in this economic scenario. Your response should seamlessly integrate concepts from economics, cognitive science, and artificial intelligence throughout. Address all subpoints in each section comprehensively.

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for simulating economic decision-making.
   b) Explain how it incorporates the specified cognitive bias and heuristic.
   c) Detail the mechanism for generating and evaluating economic decisions.
   d) Discuss how your system handles uncertainty and incomplete information.

2. Cognitive-Economic Integration (250-300 words):
   a) Analyze how the specified cognitive bias influences economic decisions in your system.
   b) Explain the role of the given heuristic in the decision-making process.
   c) Describe how these psychological factors interact with traditional economic principles in your model.

3. Simulation Example (200-250 words):
   a) Provide a detailed description of a simulation run in the given economic context.
   b) Explain how the cognitive bias and heuristic affected the outcomes.
   c) Compare the results to what might be expected from a purely rational economic model.

4. Predictive Analysis (250-300 words):
   a) Use your system to make three specific predictions about economic behavior or outcomes in the given context.
   b) Explain the reasoning behind each prediction, referring to both economic principles and cognitive factors.
   c) Discuss the potential real-world implications of these predictions.

5. Model Evaluation and Refinement (200-250 words):
   a) Propose a method for evaluating the accuracy and reliability of your system's simulations and predictions.
   b) Describe how the system could learn and improve from real-world data.
   c) Discuss potential biases in your approach and how to mitigate them.

6. Ethical Considerations and Societal Impact (150-200 words):
   a) Identify potential ethical concerns related to using AI to simulate and predict human economic behavior.
   b) Discuss possible societal impacts of widespread use of such systems in economic policy-making or financial institutions.
   c) Propose guidelines for responsible development and use of cognitive-economic AI simulations.

Ensure your response demonstrates a deep understanding of economics, cognitive science, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility.

Provide concrete examples and specific details throughout your response. For instance, in the System Architecture section, you might describe a specific neural network architecture or decision tree model. In the Simulation Example, provide numerical data or graphs to illustrate the outcomes.

Format your response using clear headings for each section and address all subpoints comprehensively. Your total response should be between 1350-1650 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of economics, cognitive science, and artificial intelligence, integrating all three fields throughout.",
            "The AI system design effectively incorporates the specified cognitive bias and heuristic, with clear explanations of their roles.",
            "The simulation example and predictive analysis are detailed and plausible, with concrete examples, specific details, and numerical data where appropriate.",
            "The ethical considerations and societal impact are thoroughly discussed, with specific guidelines proposed.",
            "The response is well-structured, addressing all required sections and subpoints comprehensively.",
            "The response falls within the specified word count range (1350-1650 words).",
            "The response provides innovative ideas while maintaining scientific plausibility.",
            "The proposed evaluation and refinement methods are well-reasoned and feasible."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
