import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_structures = [
            "Hive mind collective consciousness",
            "Quantum entangled neural networks",
            "Multi-dimensional spatial reasoning",
            "Temporal perception across multiple timelines"
        ]
        environmental_constraints = [
            "Extreme gravitational fluctuations",
            "Atmospheric composition that affects sound propagation",
            "Bioluminescent communication capabilities",
            "Electromagnetic sensitivity and manipulation"
        ]
        language_aspects = [
            "Phonology and sound system",
            "Syntax and grammar rules",
            "Semantic development",
            "Pragmatics and context-dependent meaning"
        ]
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                "cognitive_structure": random.choice(cognitive_structures),
                "environmental_constraint": random.choice(environmental_constraints),
                "language_aspect": random.choice(language_aspects)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can simulate the evolution of language in a hypothetical alien civilization with the following characteristics:

1. Cognitive Structure: {t['cognitive_structure']}
2. Environmental Constraint: {t['environmental_constraint']}
3. Language Aspect to Focus on: {t['language_aspect']}

Your response should include the following sections:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for simulating alien language evolution.
   b) Explain how your system models the given cognitive structure and environmental constraint.
   c) Detail how your system simulates the evolution of the specified language aspect.
   d) Discuss any novel AI techniques or algorithms used in your simulation.
   e) Provide a high-level diagram of your system architecture (describe it textually).

2. Alien Cognitive Model (250-300 words):
   a) Explain how you model the given cognitive structure in your AI system.
   b) Describe how this cognitive model influences language development and evolution.
   c) Discuss any assumptions or simplifications made in your cognitive model.

3. Environmental Influence Simulation (250-300 words):
   a) Detail how your system simulates the impact of the given environmental constraint on language evolution.
   b) Explain any unique features of your simulation that address this specific constraint.
   c) Describe how the environmental constraint interacts with the cognitive structure in your model.

4. Language Evolution Process (300-350 words):
   a) Outline the steps your AI system takes to simulate the evolution of the specified language aspect.
   b) Explain how your system ensures linguistic plausibility while allowing for alien uniqueness.
   c) Describe any linguistic theories or principles incorporated into your evolutionary model.
   d) Provide an example of how a specific linguistic feature might evolve in your simulation.

5. Comparative Analysis (200-250 words):
   a) Compare the simulated alien language evolution to known patterns in human language evolution.
   b) Discuss how the unique cognitive and environmental factors lead to divergent evolutionary paths.
   c) Hypothesize potential universal properties of language that might emerge despite alien differences.

6. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical implications of simulating alien language evolution.
   b) Address limitations of your approach and areas for future improvement.
   c) Consider how biases in human understanding of language might affect the simulation.

7. Interdisciplinary Implications (150-200 words):
   a) Explain how your alien language evolution simulation might influence other scientific fields.
   b) Propose two potential research questions that could be explored using your AI system.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Use appropriate terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1600-1950 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence.",
            "The AI system architecture is well-designed and clearly incorporates the given cognitive structure and environmental constraint.",
            "The language evolution process is plausible and creatively addresses the specified language aspect.",
            "The comparative analysis provides insightful comparisons between alien and human language evolution.",
            "Ethical considerations and limitations are thoroughly addressed.",
            "The interdisciplinary implications are innovative and well-reasoned.",
            "The response is creative while maintaining scientific plausibility.",
            "The response follows the required format and adheres to the word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
