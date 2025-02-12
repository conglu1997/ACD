import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'climate_factor': 'Ocean acidification',
                'ai_technique': 'Reinforcement learning',
                'ethical_concern': 'Unintended consequences'
            },
            {
                'climate_factor': 'Deforestation',
                'ai_technique': 'Federated learning',
                'ethical_concern': 'Data privacy'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system for advanced climate modeling and intervention planning, focusing on the climate factor of {t['climate_factor']} and utilizing the AI technique of {t['ai_technique']}. Then, analyze its potential applications and ethical implications, with particular attention to the ethical concern of {t['ethical_concern']}.

Provide your response in the following format:

1. AI System Design (300-350 words):
   a) Describe the key components and architecture of your AI system for climate modeling and intervention planning.
   b) Explain how your system incorporates {t['ai_technique']} to address {t['climate_factor']}.
   c) Discuss how your AI system integrates climate data, models, and potential intervention strategies.
   d) Provide a high-level pseudocode or diagram illustrating a key algorithm in your system.

2. Climate Science Integration (200-250 words):
   a) Explain how your AI system models and analyzes {t['climate_factor']}.
   b) Discuss the types of data and climate models your system would use.
   c) Describe how your system would generate and evaluate potential intervention strategies.

3. Potential Applications (200-250 words):
   a) Propose three specific applications of your AI system in climate change mitigation or adaptation efforts.
   b) Explain the potential benefits and challenges of each application.
   c) Discuss how your system could interface with existing climate policies and initiatives.

4. Ethical Analysis (250-300 words):
   a) Analyze the ethical implications of your AI system, focusing on {t['ethical_concern']}.
   b) Discuss potential risks and benefits of using AI for climate intervention planning.
   c) Propose at least three guidelines or safeguards to address the ethical issues you've identified.
   d) Consider the global and long-term consequences of implementing your AI system.

5. Technical Challenges and Future Directions (150-200 words):
   a) Identify at least two major technical challenges in implementing your system.
   b) Propose potential solutions or research directions to address these challenges.
   c) Suggest how your system could be expanded or improved in future iterations.

Ensure your response demonstrates a deep understanding of artificial intelligence, climate science, and ethical reasoning. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility and addressing real-world challenges. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of AI techniques, particularly {t['ai_technique']}, and their application to climate modeling and intervention planning.",
            "The AI system design is innovative, plausible, and clearly explained, with a focus on addressing {t['climate_factor']}.",
            "The climate science integration is well-reasoned and shows a strong understanding of relevant climate models and data.",
            "The proposed applications are practical, impactful, and well-explained.",
            "The ethical analysis is thorough and specifically addresses {t['ethical_concern']}, with thoughtful guidelines proposed.",
            "The discussion of technical challenges and future directions shows insight into the complexities of the problem.",
            "The overall response shows strong integration of knowledge from AI, climate science, and ethics.",
            "The response includes a clear pseudocode or diagram illustrating a key algorithm.",
            "The response adheres to the specified word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
