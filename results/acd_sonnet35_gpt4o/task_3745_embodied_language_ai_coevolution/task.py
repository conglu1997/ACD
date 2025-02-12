import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'environment': 'underwater ecosystem',
                'sensory_modality': 'echolocation',
                'communication_challenge': 'limited visibility'
            },
            {
                'environment': 'low-gravity planetoid',
                'sensory_modality': 'magnetic field detection',
                'communication_challenge': 'time-delayed signals'
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(scenarios)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates the co-evolution of embodied experiences, language development, and artificial intelligence in a virtual {t['environment']}. Your system should focus on the sensory modality of {t['sensory_modality']} and address the communication challenge of {t['communication_challenge']}. Provide your response in the following format:

1. Virtual Environment Design (200-250 words):
   a) Describe the key features of your {t['environment']} and how they influence embodied experiences.
   b) Explain how {t['sensory_modality']} works in this environment and its importance for the inhabitants.
   c) Discuss the challenges posed by {t['communication_challenge']} and their impact on communication.

2. Embodied AI Agents (250-300 words):
   a) Describe the physical and cognitive characteristics of your AI agents.
   b) Explain how the agents perceive and interact with the environment using {t['sensory_modality']}.
   c) Discuss how the agents' embodied experiences shape their cognitive development.

3. Language Evolution Simulation (250-300 words):
   a) Outline the initial communication capabilities of the AI agents.
   b) Describe the mechanisms for language evolution in your simulation.
   c) Explain how the {t['communication_challenge']} influences the development of language.
   d) Discuss how embodied experiences and {t['sensory_modality']} shape the evolving language.

4. AI Learning and Adaptation (200-250 words):
   a) Describe how your AI agents learn and adapt over time.
   b) Explain the interplay between language development and AI cognitive growth.
   c) Discuss how the evolving language influences the AI's problem-solving capabilities.

5. Simulation Architecture (200-250 words):
   a) Provide a high-level overview of your simulation's technical architecture.
   b) Explain how you model the co-evolution of embodiment, language, and AI capabilities.
   c) Describe any novel algorithms or techniques used in your simulation.

6. Experimental Design and Analysis (200-250 words):
   a) Propose an experiment to test the impact of embodied experiences on language evolution.
   b) Describe the data you would collect and the metrics you would use to analyze the results.
   c) Discuss how you would validate the realism and relevance of your simulation.

7. Implications and Future Directions (150-200 words):
   a) Discuss the potential implications of your simulation for understanding human language evolution.
   b) Explain how insights from this simulation could inform the development of more advanced AI systems.
   c) Propose two future research directions based on your simulation results.

Ensure your response demonstrates a deep understanding of embodied cognition, language evolution, and artificial intelligence. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility.

Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of embodied cognition, language evolution, and artificial intelligence, particularly in relation to the {t['environment']} and {t['sensory_modality']}",
            f"The proposed AI system effectively addresses the communication challenge of {t['communication_challenge']}",
            "The simulation architecture is well-designed and plausible",
            "The experimental design and analysis approach is sound and comprehensive",
            "The implications and future directions are insightful and well-reasoned",
            "The response is innovative while maintaining scientific plausibility",
            "The response adheres to the specified word limit (1450-1800 words)"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
