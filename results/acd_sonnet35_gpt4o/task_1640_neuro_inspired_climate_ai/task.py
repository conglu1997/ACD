import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "brain_region": "Hippocampus",
                "climate_factor": "Ocean circulation patterns",
                "ai_technique": "Reinforcement learning"
            },
            {
                "brain_region": "Prefrontal cortex",
                "climate_factor": "Atmospheric carbon dioxide levels",
                "ai_technique": "Generative adversarial networks"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a brain-inspired AI system for global climate modeling and intervention strategies, focusing on the {t['brain_region']} as inspiration, {t['climate_factor']} as the primary climate factor to model, and incorporating {t['ai_technique']} as a key AI technique. Your response should include:

1. Neuro-Inspired Architecture (250-300 words):
   a) Describe the key components of your AI system and how they correspond to the functions of the {t['brain_region']}.
   b) Explain how your system processes and represents climate data, drawing parallels to neural information processing.
   c) Discuss how your architecture incorporates principles of neural plasticity and learning in the context of climate modeling.
   d) Include a simple diagram or flowchart of your system's architecture (described textually).

2. Climate Modeling Capabilities (200-250 words):
   a) Explain how your system would model and predict changes in {t['climate_factor']}.
   b) Describe the specific algorithms or neural network structures used for this modeling.
   c) Discuss how your system could identify patterns and anomalies in climate data.
   d) Provide a brief analysis of how your system might process and interpret a recent climate phenomenon related to {t['climate_factor']}.

3. Intervention Strategy Generation (200-250 words):
   a) Outline how your system would generate and evaluate potential climate intervention strategies.
   b) Explain how it incorporates {t['ai_technique']} in this process.
   c) Describe how your system balances short-term and long-term consequences in strategy formulation.
   d) Provide an example of a specific intervention strategy your system might propose for addressing changes in {t['climate_factor']}.

4. Learning and Adaptation (150-200 words):
   a) Propose a method for training and continuously updating your AI system with new climate data.
   b) Discuss how your system would adapt to unexpected climate events or paradigm shifts in climate science.
   c) Explain how the system's learning process mirrors that of the {t['brain_region']}.

5. Ethical and Policy Implications (150-200 words):
   a) Discuss the potential ethical issues arising from using AI to guide climate intervention strategies.
   b) Analyze how policymakers might interact with and use your system.
   c) Propose guidelines for responsible development and use of such AI systems in climate science.

6. Interdisciplinary Insights (150-200 words):
   a) Discuss what your system's performance might reveal about the relationship between neural processing and complex system modeling.
   b) Explore potential applications of your neuro-inspired approach to other complex global challenges.
   c) Suggest areas for future research at the intersection of neuroscience, climate science, and AI.

7. Case Study (200-250 words):
   Provide a detailed case study demonstrating how your system would address a specific climate crisis scenario related to {t['climate_factor']}. Include the system's analysis, proposed interventions, and potential outcomes.

8. Limitations and Challenges (100-150 words):
   Discuss potential limitations of your proposed system and challenges that might arise in its implementation or use.

Ensure your response demonstrates a deep understanding of neuroscience, climate science, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section, numbered exactly as above. Your total response should be between 1400-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response focuses on the {t['brain_region']} as inspiration for the AI architecture, with clear parallels drawn between brain function and system design.",
            f"The system effectively models and addresses {t['climate_factor']} as the primary climate factor, with specific algorithms and techniques explained.",
            f"The design incorporates {t['ai_technique']} as a key AI technique in the system, with a clear explanation of its role and implementation.",
            "The architecture demonstrates a clear and plausible integration of neuroscience principles with climate modeling and AI.",
            "The response covers all eight required sections with appropriate detail and coherence, adhering to the specified word counts.",
            "The climate modeling capabilities are well-explained, scientifically plausible, and include a specific example of data interpretation.",
            "The intervention strategy generation process is clearly described, innovative, and includes a concrete example.",
            "The ethical and policy implications are thoughtfully discussed, with specific guidelines proposed.",
            "The response includes a textual description of a diagram or flowchart of the system's architecture.",
            "The interdisciplinary insights section provides novel and thought-provoking ideas for future research and applications.",
            "The case study presents a detailed and plausible scenario demonstrating the system's capabilities.",
            "The limitations and challenges section critically assesses the proposed system."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
