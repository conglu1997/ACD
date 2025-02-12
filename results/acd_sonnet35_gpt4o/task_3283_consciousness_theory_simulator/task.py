import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "theory": "Global Workspace Theory",
                "phenomenon": "Attentional Blink",
                "competing_theory": "Higher-Order Thought Theory"
            },
            "2": {
                "theory": "Integrated Information Theory",
                "phenomenon": "Blindsight",
                "competing_theory": "Predictive Processing Theory"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates and compares different theories of consciousness, then use it to analyze a specific cognitive phenomenon. Your task is to create a model that simulates {t['theory']} and applies it to the phenomenon of {t['phenomenon']}. You should also compare it with {t['competing_theory']}. Provide your response in the following format:

1. Theoretical Framework (250-300 words):
   a) Explain the key principles of {t['theory']} and how it accounts for consciousness.
   b) Describe how {t['theory']} might explain the phenomenon of {t['phenomenon']}.
   c) Briefly compare this explanation with that offered by {t['competing_theory']}.

2. AI System Architecture (300-350 words):
   a) Design an AI architecture that implements {t['theory']} of consciousness.
   b) Explain how your system models the main components and processes of this theory.
   c) Describe how your AI system would simulate the phenomenon of {t['phenomenon']}.
   d) Include a high-level diagram or pseudocode illustrating your system's structure and processes.

3. Simulation Process (250-300 words):
   a) Provide a step-by-step description of how your AI system would simulate {t['phenomenon']} using {t['theory']}.
   b) Explain how your system generates testable predictions about the phenomenon.
   c) Describe any novel insights or emergent behaviors you expect from your simulation.

4. Comparative Analysis (200-250 words):
   a) Compare how your system based on {t['theory']} and a hypothetical system based on {t['competing_theory']} would differ in simulating {t['phenomenon']}.
   b) Discuss the strengths and limitations of each approach.
   c) Propose an experiment that could differentiate between the two theories' predictions.

5. Philosophical Implications (200-250 words):
   a) Discuss what your AI system's performance might imply about the nature of consciousness.
   b) Explore the ethical considerations of simulating consciousness in AI systems.
   c) Consider how this approach might impact our understanding of machine consciousness and AI rights.

6. Future Directions (150-200 words):
   a) Suggest two potential enhancements or extensions to your AI consciousness simulator.
   b) Propose a research study that could validate or improve your system's accuracy in modeling consciousness.
   c) Speculate on how this technology might influence fields such as neuroscience, psychology, or AI development.

Ensure your response demonstrates a deep understanding of consciousness theories, artificial intelligence, and cognitive science. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific and philosophical rigor.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['theory']} and how it relates to {t['phenomenon']}",
            "The AI system architecture is well-designed and clearly explained",
            f"The simulation process for {t['phenomenon']} is logically described and aligns with {t['theory']}",
            f"The comparative analysis between {t['theory']} and {t['competing_theory']} is insightful and balanced",
            "The discussion of philosophical implications is thoughtful and considers multiple perspectives",
            "The proposed future directions are innovative and scientifically plausible",
            "The overall response is well-structured, coherent, and demonstrates interdisciplinary knowledge integration"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
