import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "environment": "coastal_region",
                "social_structure": "small_nomadic_groups",
                "cognitive_constraint": "limited_working_memory"
            },
            {
                "environment": "dense_forest",
                "social_structure": "large_settled_communities",
                "cognitive_constraint": "color_blindness"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a simulation system that models the evolution of a multimodal communication system incorporating gesture, vocalization, and visual symbols. Then, analyze its implications for human language evolution and AI communication models. Use the following scenario:

Environment: {t['environment']}
Social Structure: {t['social_structure']}
Cognitive Constraint: {t['cognitive_constraint']}

Your response should include the following sections:

1. Simulation System Design (300-350 words):
   a) Describe the key components of your simulation system.
   b) Explain how your system models the evolution of gesture, vocalization, and visual symbols.
   c) Discuss how your system incorporates the given environment, social structure, and cognitive constraint.
   d) Outline the evolutionary mechanisms (e.g., mutation, selection) used in your simulation.

2. Multimodal Integration (250-300 words):
   a) Explain how your system models the integration of different communication modalities.
   b) Describe how the given cognitive constraint influences this integration.
   c) Discuss any emergent properties or unexpected interactions between modalities.

3. Evolutionary Trajectory (200-250 words):
   a) Describe the expected evolutionary trajectory of the communication system in your simulation.
   b) Explain how the environment and social structure influence this trajectory.
   c) Identify key stages or milestones in the evolution of the multimodal system.

4. Comparative Analysis (200-250 words):
   a) Compare the evolved communication system to human language evolution theories.
   b) Discuss similarities and differences between your simulated system and known human language families.
   c) Analyze how the multimodal aspect of your system relates to human language acquisition and use.

5. AI Implications (200-250 words):
   a) Discuss how insights from your simulation could inform the development of multimodal AI communication systems.
   b) Propose a specific AI application that could benefit from your findings.
   c) Explain how your simulation might help address current challenges in AI language models.

6. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical implications of simulating language evolution.
   b) Identify limitations of your simulation system and propose future improvements.
   c) Consider how biases in the simulation design might affect its outcomes and applications.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, evolutionary biology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations of complex concepts. Be creative in your approach while maintaining scientific plausibility and rigor.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of linguistics, cognitive science, evolutionary biology, and artificial intelligence in the context of {t['environment']} and {t['social_structure']}.",
            f"The simulation system effectively models the evolution of gesture, vocalization, and visual symbols, while incorporating the cognitive constraint of {t['cognitive_constraint']}.",
            "The multimodal integration is well-explained and considers the given cognitive constraint.",
            "The evolutionary trajectory is logically derived and considers the influence of the environment and social structure.",
            "The comparative analysis with human language evolution theories is insightful and well-reasoned.",
            "The AI implications are innovative and demonstrate a clear understanding of current challenges in AI language models.",
            "The response addresses ethical considerations and limitations of the simulation system.",
            "The response is well-structured, following the specified format and word count guidelines."
        ]
        return float(eval_with_llm_judge(instructions, submission, criteria))
