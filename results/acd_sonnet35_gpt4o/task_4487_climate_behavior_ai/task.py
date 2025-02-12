import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'climate_factor': 'carbon footprint reduction',
                'target_population': 'urban professionals',
                'behavioral_challenge': 'commuting habits'
            },
            {
                'climate_factor': 'energy consumption',
                'target_population': 'suburban families',
                'behavioral_challenge': 'household appliance usage'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that integrates climate science, machine learning, and social psychology to predict and influence climate-friendly behaviors on a large scale. Your system should focus on {t['climate_factor']} for the target population of {t['target_population']}, addressing the specific behavioral challenge of {t['behavioral_challenge']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system and how they interact.
   b) Explain how your system integrates climate science, machine learning, and social psychology.
   c) Detail how your system models and predicts human behavior related to the specified climate factor.
   d) Provide a high-level diagram or flowchart of your system architecture (describe this textually).

2. Climate Science Integration (200-250 words):
   a) Explain how your system incorporates climate models and data.
   b) Describe how it quantifies the impact of individual behaviors on the specified climate factor.
   c) Discuss any novel approaches to linking individual actions to larger-scale climate effects.

3. Machine Learning Approach (250-300 words):
   a) Detail the machine learning techniques used in your system.
   b) Explain how your AI learns from and adapts to changing behavioral patterns.
   c) Describe any innovative algorithms developed for this specific application.
   d) Discuss how your system handles the complexity and uncertainty inherent in climate and behavioral data.

4. Social Psychology Application (200-250 words):
   a) Explain how your system incorporates principles of social psychology to influence behavior.
   b) Describe the strategies used to encourage climate-friendly actions in the target population.
   c) Discuss how your system accounts for individual differences and cultural factors.

5. Behavioral Prediction and Intervention (250-300 words):
   a) Outline the process your system uses to predict individual behaviors related to the specified climate factor.
   b) Describe how it generates personalized interventions to promote climate-friendly behaviors.
   c) Provide an example scenario demonstrating how your system would work for a specific individual in the target population.
   d) Explain how your system measures the effectiveness of its interventions and adapts accordingly.

6. Ethical Considerations and Privacy (150-200 words):
   a) Discuss potential ethical issues related to using AI to influence human behavior.
   b) Explain how your system ensures user privacy and data protection.
   c) Propose guidelines for the responsible development and use of such technology.

7. Scalability and Future Directions (150-200 words):
   a) Discuss how your system could be scaled to address multiple climate factors and populations.
   b) Propose two potential enhancements or extensions to your system for future development.
   c) Speculate on the potential long-term impact of widespread adoption of your AI system.

Ensure your response demonstrates a deep understanding of climate science, machine learning techniques, and social psychology principles. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and addressing real-world constraints.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of climate science, machine learning, and social psychology",
            "The proposed AI system is innovative and scientifically plausible",
            "The system architecture and processes are clearly explained and logically sound",
            "The response addresses all required sections and adheres to the specified word count",
            "The integration of climate science, machine learning, and social psychology is well-detailed and coherent",
            "The response includes a thoughtful discussion of ethical considerations and future directions",
            "The proposed system effectively addresses the specified climate factor, target population, and behavioral challenge",
            "The response is well-formatted with clear headings and numbered sections"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
