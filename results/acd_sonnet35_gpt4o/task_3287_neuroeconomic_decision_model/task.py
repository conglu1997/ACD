import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        neurobiological_mechanisms = [
            "dopamine reward signaling",
            "amygdala-based emotion processing",
            "prefrontal cortex executive function",
            "hippocampal memory formation"
        ]
        economic_principles = [
            "prospect theory",
            "hyperbolic discounting",
            "bounded rationality",
            "game theory"
        ]
        emerging_technologies = [
            "brain-computer interfaces",
            "augmented reality commerce",
            "decentralized finance (DeFi)",
            "personalized medicine"
        ]
        
        return {
            "1": {
                "mechanism": random.choice(neurobiological_mechanisms),
                "principle": random.choice(economic_principles),
                "technology": random.choice(emerging_technologies)
            },
            "2": {
                "mechanism": random.choice(neurobiological_mechanisms),
                "principle": random.choice(economic_principles),
                "technology": random.choice(emerging_technologies)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neuroeconomic model of decision-making that integrates the neurobiological mechanism of {t['mechanism']} with the economic principle of {t['principle']}. Then, apply this model to analyze consumer behavior in the context of {t['technology']}. Your response should include:

1. Model Design (250-300 words):
   a) Describe the key components of your neuroeconomic decision model.
   b) Explain how you integrate {t['mechanism']} with {t['principle']} in your model.
   c) Discuss how your model accounts for both rational and irrational aspects of decision-making.
   d) Include a diagram or formal representation of your model (describe it textually).
   e) Provide a basic mathematical formulation of your model, including key equations or parameters.

2. Neurobiological Basis (200-250 words):
   a) Explain the role of {t['mechanism']} in decision-making processes.
   b) Describe how your model represents and simulates this neurobiological mechanism.
   c) Discuss any simplifications or assumptions made in modeling this biological process.

3. Economic Framework (200-250 words):
   a) Provide an overview of {t['principle']} and its relevance to decision-making.
   b) Explain how you've incorporated this principle into your neuroeconomic model.
   c) Discuss how your model extends or challenges traditional economic theories of decision-making.

4. Application to {t['technology']} (250-300 words):
   a) Describe a specific consumer behavior scenario related to {t['technology']}.
   b) Apply your neuroeconomic model to analyze this scenario.
   c) Predict how consumers might behave based on your model's insights.
   d) Discuss any unique insights your model provides compared to traditional approaches.

5. Model Validation and Limitations (200-250 words):
   a) Propose a method to validate your neuroeconomic model using empirical data.
   b) Describe potential experiments or studies that could test your model's predictions.
   c) Identify potential limitations or biases in your model and suggest ways to address them.

6. Ethical Implications (150-200 words):
   a) Identify potential ethical concerns arising from the application of your model.
   b) Discuss the implications of using neuroscientific insights to influence consumer behavior.
   c) Propose guidelines for the responsible use of neuroeconomic models in marketing or policy-making.

7. Future Directions (150-200 words):
   a) Suggest two potential extensions or improvements to your model.
   b) Discuss how advancements in neuroscience or economics might impact your model in the future.
   c) Propose a new research question that could be explored using your neuroeconomic approach.

Ensure your response demonstrates an understanding of both neuroscience and economics, as well as their potential applications. Use appropriate terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1400-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should describe a neuroeconomic model that integrates {t['mechanism']} with {t['principle']}.",
            f"The model should be applied to analyze consumer behavior in the context of {t['technology']}.",
            "The response should demonstrate understanding of both neuroscience and economics.",
            "The proposed model should be coherent and scientifically plausible.",
            "All seven requested sections should be addressed.",
            "The response should include appropriate terminology with explanations for complex concepts.",
            "A basic mathematical formulation of the model should be provided.",
            "The limitations and potential biases of the model should be discussed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
