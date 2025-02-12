import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "neurological_principle": "Reward Prediction Error",
                "economic_context": "Stock Market"
            },
            "2": {
                "neurological_principle": "Cognitive Control",
                "economic_context": "Cryptocurrency Trading"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel economic market model for the {t['economic_context']} based on the neurological principle of {t['neurological_principle']}. Then, analyze its implications for decision-making and market behavior. Your response should include:

1. Neuroeconomic Model Design (300-350 words):
   a) Explain the chosen neurological principle and its relevance to economic behavior.
   b) Describe your novel market model, detailing how it incorporates the neurological principle.
   c) Outline the key components and mechanisms of your model.
   d) Provide a simple diagram or flowchart representing your model (describe it textually).

2. Decision-Making Analysis (250-300 words):
   a) Analyze how your model affects individual decision-making processes in the given economic context.
   b) Discuss potential cognitive biases that might be amplified or mitigated by your model.
   c) Compare decision-making under your model to traditional economic assumptions of rationality.

3. Market Behavior Predictions (250-300 words):
   a) Predict how your neuroeconomic model would influence overall market behavior.
   b) Describe potential emergent phenomena or patterns at the macro level.
   c) Discuss how your model might change market efficiency or stability.

4. Comparative Analysis (200-250 words):
   a) Compare your neuroeconomic model to a well-known traditional economic model.
   b) Discuss the advantages and limitations of your approach.
   c) Analyze how your model might change economic theories or practices in the given context.

5. Ethical Implications and Regulatory Considerations (150-200 words):
   a) Discuss potential ethical concerns raised by implementing your neuroeconomic model.
   b) Propose regulatory measures to address these concerns.
   c) Analyze the potential societal impacts of widespread adoption of your model.

6. Case Study (200-250 words):
   Provide a specific example or case study that demonstrates the application of your neuroeconomic model in the given economic context. Include how it would affect decision-making and market behavior in this concrete scenario.

Ensure your response demonstrates a deep understanding of neuroscience, economics, and psychology. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific and economic plausibility. Your total response should be between 1350-1650 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding and integration of the specified neurological principle and economic context.",
            "The neuroeconomic model design is creative, well-explained, and effectively combines neuroscience with economic theory.",
            "The decision-making analysis shows depth of understanding and critical thinking about cognitive processes in economic contexts.",
            "The market behavior predictions demonstrate insight into complex systems and emergent phenomena.",
            "The comparative analysis provides a thoughtful evaluation of the model's strengths and limitations relative to traditional approaches.",
            "The ethical implications and regulatory considerations show awareness of potential issues and propose thoughtful guidelines for responsible implementation.",
            "The case study provides a concrete and relevant example that effectively demonstrates the application of the neuroeconomic model."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
