import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scientific_revolutions = [
            "Copernican Revolution",
            "Darwinian Evolution",
            "Einstein's Relativity",
            "Quantum Mechanics",
            "DNA Structure Discovery"
        ]
        cognitive_processes = [
            "Analogical Reasoning",
            "Conceptual Blending",
            "Abductive Inference",
            "Intuitive Leaps",
            "Pattern Recognition"
        ]
        
        tasks = {
            "1": {
                "revolution": random.choice(scientific_revolutions),
                "cognitive_process": random.choice(cognitive_processes)
            },
            "2": {
                "revolution": random.choice(scientific_revolutions),
                "cognitive_process": random.choice(cognitive_processes)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates the cognitive processes involved in scientific discovery and breakthrough moments, then apply it to the {t['revolution']} with a focus on the cognitive process of {t['cognitive_process']}. Your response should include:

1. Cognitive Model of Scientific Discovery (250-300 words):
   a) Describe the key components of your AI system for modeling scientific discovery.
   b) Explain how your model incorporates the specified cognitive process.
   c) Discuss how your system simulates other aspects of scientific thinking (e.g., hypothesis formation, experimentation, theory revision).

2. Historical Context Simulation (200-250 words):
   a) Briefly describe the historical context of the specified scientific revolution.
   b) Explain how your AI system would model the state of knowledge and scientific thinking at that time.
   c) Discuss how your system accounts for the social and cultural factors influencing scientific progress.

3. Breakthrough Simulation (250-300 words):
   a) Describe how your AI system would simulate the key breakthrough(s) of the specified scientific revolution.
   b) Explain the role of the focused cognitive process in this simulated breakthrough.
   c) Provide a step-by-step walkthrough of how your system might generate the critical insights leading to the breakthrough.

4. Comparative Analysis (200-250 words):
   a) Compare your AI's simulated process of discovery with the historical account of how the breakthrough actually occurred.
   b) Discuss any discrepancies and their potential causes.
   c) Analyze what this comparison reveals about human vs. AI approaches to scientific discovery.

5. Implications and Applications (150-200 words):
   a) Discuss the potential implications of your AI system for our understanding of scientific creativity and cognition.
   b) Propose how this system could be used to accelerate real-world scientific discoveries.
   c) Consider any ethical implications or potential risks of using such AI systems in scientific research.

6. Limitations and Future Directions (150-200 words):
   a) Identify key limitations of your current AI model for simulating scientific discovery.
   b) Propose two potential improvements or extensions to your model.
   c) Suggest one way your approach could be applied to other domains of human creativity and innovation.

Ensure your response demonstrates a deep understanding of cognitive science, artificial intelligence, and the history and philosophy of science. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology from all relevant fields and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive science, artificial intelligence, and the history and philosophy of science.",
            "The AI system design for modeling scientific discovery is innovative and well-explained.",
            "The historical context of the specified scientific revolution is accurately represented.",
            "The simulation of the scientific breakthrough is plausible and incorporates the specified cognitive process.",
            "The comparative analysis between the AI simulation and historical events is insightful.",
            "The implications and potential applications of the AI system are thoughtfully discussed.",
            "Limitations of the model are identified and future directions are proposed.",
            "The response is creative while maintaining scientific plausibility.",
            "Appropriate technical terminology is used and complex concepts are clearly explained.",
            "The response follows the required format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
