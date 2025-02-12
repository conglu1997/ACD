import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            "deep ocean trenches",
            "volcanic active zones",
            "radioactive waste sites",
            "dense jungle canopies",
            "Martian surface"
        ]
        inspirations = [
            "cephalopods",
            "extremophile bacteria",
            "tardigrades",
            "tree-dwelling mammals",
            "resilient insects"
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "environment": random.choice(environments),
                "biological_inspiration": random.choice(inspirations)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an evolutionary algorithm that generates biomimetic robot designs adapted to {t['environment']}, drawing inspiration from {t['biological_inspiration']}. Your response should include the following sections:

1. Evolutionary Algorithm Design (300-350 words):
   a) Describe the key components of your evolutionary algorithm (e.g., genome representation, fitness function, selection method, mutation and crossover operators).
   b) Explain how your algorithm incorporates biomimetic principles inspired by {t['biological_inspiration']}.
   c) Discuss how the algorithm evaluates and optimizes robot designs for the specific challenges of {t['environment']}.
   d) Include a high-level pseudocode (15-20 lines) illustrating the main steps of your evolutionary algorithm.

2. Robot Design Space (250-300 words):
   a) Define the range of possible robot designs your algorithm can generate.
   b) Explain how the design space reflects adaptations to {t['environment']}.
   c) Describe how features inspired by {t['biological_inspiration']} are represented and evolved.
   d) Discuss any constraints or trade-offs in the design space.

3. Environmental Adaptation Mechanisms (250-300 words):
   a) Analyze how your algorithm promotes adaptation to the specific challenges of {t['environment']}.
   b) Describe at least three specific adaptations that might emerge in the evolved robots.
   c) Explain how these adaptations relate to both the environment and the biological inspiration.

4. Simulated Evolution Analysis (200-250 words):
   a) Describe a hypothetical run of your evolutionary algorithm, including initial population, key generations, and final output.
   b) Analyze the trends and patterns in the evolving population.
   c) Discuss any unexpected or emergent features in the evolved robot designs.

5. Potential Applications and Implications (200-250 words):
   a) Propose three potential applications for the evolved robots in {t['environment']}.
   b) Discuss the ethical implications of deploying such robots in real-world scenarios.
   c) Analyze the potential impact on scientific research and exploration in extreme environments.

6. Limitations and Future Directions (150-200 words):
   a) Identify potential limitations of your evolutionary algorithm or the resulting robot designs.
   b) Propose two ways to extend or improve your system.
   c) Suggest areas for future research in evolutionary robotics for extreme environments.

Ensure your response demonstrates a deep understanding of evolutionary algorithms, biomechanics, robotics, and environmental science. Use appropriate terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific and technological plausibility.

Format your response with clear headings for each section and number your paragraphs within each section. Your total response should be between 1350-1650 words, not including the pseudocode."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should design an evolutionary algorithm for generating biomimetic robot designs adapted to {t['environment']}.",
            f"The algorithm should incorporate biomimetic principles inspired by {t['biological_inspiration']}.",
            "The response should include all six required sections with appropriate content for each.",
            "The design should demonstrate integration of evolutionary algorithms, biomechanics, robotics, and environmental science.",
            "The response should include a high-level pseudocode illustrating the main steps of the evolutionary algorithm.",
            "The response should analyze specific adaptations that might emerge in the evolved robots.",
            "The response should discuss potential applications, ethical implications, and future directions for the technology.",
            "The response should be creative while maintaining scientific and technological plausibility.",
            "The response should be formatted with clear headings and numbered paragraphs within each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
