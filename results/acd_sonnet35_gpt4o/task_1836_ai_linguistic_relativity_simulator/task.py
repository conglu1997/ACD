import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_features = [
            {"feature": "Time conception", "description": "How the language conceptualizes and expresses time (e.g., linear vs. cyclical)"},
            {"feature": "Color categorization", "description": "How the language divides the color spectrum"},
            {"feature": "Spatial relations", "description": "How the language expresses spatial relationships between objects"},
            {"feature": "Counterfactual thinking", "description": "How the language expresses and handles hypothetical scenarios"}
        ]
        cognitive_tasks = [
            "Problem-solving in a spatial navigation task",
            "Decision-making in a resource allocation scenario",
            "Pattern recognition in a visual classification task",
            "Causal reasoning in a complex system"
        ]
        return {
            "1": {
                "linguistic_feature": random.choice(linguistic_features),
                "cognitive_task": random.choice(cognitive_tasks)
            },
            "2": {
                "linguistic_feature": random.choice(linguistic_features),
                "cognitive_task": random.choice(cognitive_tasks)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates different linguistic worldviews based on the principle of linguistic relativity, focusing on the linguistic feature of {t['linguistic_feature']['feature']}. Then, analyze how this affects the AI's performance on the cognitive task of {t['cognitive_task']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system that enable the simulation of different linguistic worldviews.
   b) Explain how your system models the given linguistic feature: {t['linguistic_feature']['description']}
   c) Discuss how your system integrates this linguistic feature into its cognitive processes.

2. Linguistic Worldview Simulation (200-250 words):
   a) Describe how your system simulates at least two contrasting worldviews based on the given linguistic feature.
   b) Explain how these worldviews differ in their representation and processing of information.
   c) Discuss any challenges in implementing these simulations and how you addressed them.

3. Cognitive Task Analysis (200-250 words):
   a) Describe how your system approaches the given cognitive task: {t['cognitive_task']}
   b) Analyze how the different linguistic worldviews affect the AI's performance on this task.
   c) Provide specific examples of how the linguistic feature influences problem-solving strategies or perceptual processes.

4. Implications for AI Consciousness (150-200 words):
   a) Discuss how your system's ability to simulate different linguistic worldviews relates to the concept of machine consciousness.
   b) Explore the philosophical implications of your findings for our understanding of the relationship between language, thought, and consciousness in AI.

5. Evaluation and Future Directions (150-200 words):
   a) Propose a method to evaluate the effectiveness and validity of your AI's linguistic worldview simulations.
   b) Suggest potential applications of your system in fields such as cognitive science, AI ethics, or cross-cultural communication.
   c) Discuss limitations of your approach and propose future research directions.

Ensure your response demonstrates a deep understanding of linguistic relativity, cognitive science, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 950-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately addresses the linguistic feature of {t['linguistic_feature']['feature']} and its impact on the cognitive task of {t['cognitive_task']}.",
            "The system architecture is well-designed and clearly explained, demonstrating a deep understanding of AI and linguistics.",
            "The simulation of different linguistic worldviews is creative, plausible, and well-reasoned.",
            "The analysis of the cognitive task demonstrates a clear understanding of how linguistic features can affect cognition.",
            "The discussion of implications for AI consciousness is insightful and philosophically sound.",
            "The proposed evaluation method and future directions are relevant and demonstrate critical thinking.",
            "The response shows interdisciplinary knowledge integration and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
