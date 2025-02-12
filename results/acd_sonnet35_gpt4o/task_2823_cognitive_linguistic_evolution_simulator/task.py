import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'cognitive_constraint': 'Working memory capacity',
                'environmental_factor': 'Technological advancement',
                'time_span': 500
            },
            {
                'cognitive_constraint': 'Social cognition',
                'environmental_factor': 'Climate change',
                'time_span': 1000
            },
            {
                'cognitive_constraint': 'Analogical reasoning',
                'environmental_factor': 'Interplanetary colonization',
                'time_span': 2000
            },
            {
                'cognitive_constraint': 'Attention span',
                'environmental_factor': 'Global digital connectivity',
                'time_span': 300
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a computational model that simulates the evolution of language based on cognitive constraints and environmental factors, then use it to project linguistic changes over an extended time period. Focus on the cognitive constraint of {t['cognitive_constraint']} and the environmental factor of {t['environmental_factor']}. Project linguistic changes over the next {t['time_span']} years.

Your response should include the following sections:

1. Model Architecture (250-300 words):
   a) Describe the key components of your language evolution simulation model.
   b) Explain how your model incorporates the cognitive constraint of {t['cognitive_constraint']}.
   c) Detail how the environmental factor of {t['environmental_factor']} is integrated into the model.
   d) Discuss any novel computational approaches or algorithms used in your design.
   e) Include a simple diagram or flowchart of your model's architecture.

2. Linguistic Features and Processes (200-250 words):
   a) Identify the specific linguistic features (e.g., phonology, syntax, semantics) your model simulates.
   b) Explain the mechanisms by which these features evolve in your model.
   c) Describe how {t['cognitive_constraint']} influences the evolution of these features.
   d) Discuss how {t['environmental_factor']} interacts with linguistic processes in your model.

3. Simulation and Projection (250-300 words):
   a) Outline the initial conditions and parameters for your simulation.
   b) Describe the step-by-step process of running the simulation over {t['time_span']} years.
   c) Present 3-4 key linguistic changes projected by your model, explaining the underlying factors.
   d) Discuss any emergent properties or unexpected outcomes from your simulation.

4. Validation and Evaluation (150-200 words):
   a) Propose methods to validate your model against historical linguistic data.
   b) Discuss potential limitations of your approach and how they might affect the projections.
   c) Suggest criteria for evaluating the plausibility of the projected linguistic changes.

5. Interdisciplinary Implications (150-200 words):
   a) Analyze how your model and projections might inform theories in cognitive science and linguistics.
   b) Discuss potential applications of your model in fields such as artificial intelligence, sociolinguistics, or language preservation.
   c) Explore how your approach could contribute to our understanding of the relationship between cognition, environment, and language.

6. Future Research Directions (100-150 words):
   a) Propose two specific areas for future research that could enhance or extend your model.
   b) Briefly describe how these research directions could address current limitations or expand the model's capabilities.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and computational modeling. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of linguistics, cognitive science, and computational modeling, particularly in relation to {t['cognitive_constraint']} and {t['environmental_factor']}.",
            "The model architecture is well-explained and clearly incorporates both the specified cognitive constraint and environmental factor.",
            f"The simulation and projection over {t['time_span']} years is logically described and includes plausible linguistic changes.",
            "The validation and evaluation methods are appropriate and address potential limitations.",
            "The interdisciplinary implications and future research directions are thoughtfully explored.",
            "The response is creative and innovative while maintaining scientific plausibility.",
            "The response is well-formatted with clear headings and adheres to the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
