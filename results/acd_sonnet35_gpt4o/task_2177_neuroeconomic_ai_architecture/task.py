import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'decision_type': 'intertemporal choice',
                'brain_region': 'prefrontal cortex',
                'economic_context': 'personal investment strategies'
            },
            {
                'decision_type': 'risk assessment',
                'brain_region': 'amygdala',
                'economic_context': 'stock market trading'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neural network architecture inspired by neuroeconomic principles to model and predict human economic decision-making in complex scenarios. Focus on the decision type of {t['decision_type']}, incorporating the function of the {t['brain_region']} in the context of {t['economic_context']}.

Your response should include the following sections:

1. Neuroeconomic Framework (150-200 words):
   a) Explain the key principles of neuroeconomics relevant to {t['decision_type']}.
   b) Describe the role of the {t['brain_region']} in this type of decision-making.
   c) Discuss how these principles manifest in the context of {t['economic_context']}.

2. Neural Network Architecture (200-250 words):
   a) Design a detailed neural network architecture inspired by the neuroeconomic principles and brain region function.
   b) Explain each component of your architecture and its biological counterpart.
   c) Describe how your model incorporates key features of {t['decision_type']} and the {t['brain_region']}.
   d) Include a diagram of your architecture (using ASCII art or a clear textual description).

3. Data Processing and Decision Modeling (150-200 words):
   a) Explain how your network processes input data related to {t['economic_context']}.
   b) Describe the decision-making process within your model.
   c) Discuss how your model accounts for factors such as emotion, bias, and uncertainty in decision-making.

4. Training and Optimization (150-200 words):
   a) Propose a training methodology for your neuroeconomic AI model.
   b) Describe the types of data needed to train the model effectively.
   c) Explain how you would optimize the model to accurately reflect human decision-making patterns.

5. Model Evaluation and Validation (100-150 words):
   a) Suggest metrics to evaluate your model's performance in predicting human economic decisions.
   b) Describe an experimental setup to validate your model against real human behavior in {t['economic_context']}.
   c) Discuss potential limitations of your model and how they might be addressed.

6. Ethical Considerations and Applications (100-150 words):
   a) Discuss ethical implications of using AI to model and predict human economic decision-making.
   b) Propose potential applications of your model in fields such as finance, public policy, or behavioral economics.
   c) Address concerns about privacy, manipulation, and the potential for misuse of such technology.

7. Case Study (150-200 words):
   Provide a detailed case study demonstrating how your model would be applied in a specific real-world scenario related to {t['economic_context']}. Include:
   a) A description of the scenario and its economic implications.
   b) How your model would process the relevant data and make predictions.
   c) The potential impact of using your model in this scenario.

Ensure your response demonstrates a deep understanding of neuroscience, economics, and machine learning. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Note: Balance depth and breadth in your response. While you should cover all sections, feel free to emphasize areas where you can provide the most insightful and innovative ideas.

Hint: For the Neural Network Architecture section, consider how you might incorporate recurrent connections to model the temporal aspects of decision-making, similar to how the brain processes information over time.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1000-1350 words, not including the architecture diagram."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The neural network architecture effectively incorporates principles of neuroeconomics, particularly related to {t['decision_type']} and the function of the {t['brain_region']}.",
            f"The model demonstrates a plausible approach to simulating human decision-making in the context of {t['economic_context']}.",
            "The response includes a clear explanation of the neural network architecture, with at least one innovative feature inspired by neuroscience.",
            "The proposed training methodology and evaluation metrics are appropriate and well-reasoned.",
            "The response addresses ethical considerations and suggests at least one concrete application of the technology.",
            "The case study provides a specific, realistic example of how the model would be applied in a real-world scenario.",
            "The overall response demonstrates interdisciplinary thinking, balancing insights from neuroscience, economics, and machine learning.",
            "The response adheres to the specified word limits for each section and the overall word count, while maintaining depth in key areas."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
