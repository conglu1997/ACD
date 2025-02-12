import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'scenario': 'Antibiotic resistance evolution',
                'key_factors': 'mutation rate, selection pressure, population size'
            },
            {
                'scenario': 'Speciation in isolated populations',
                'key_factors': 'genetic drift, natural selection, gene flow'
            },
            {
                'scenario': 'Co-evolution of predator-prey relationships',
                'key_factors': 'fitness landscapes, adaptive traits, population dynamics'
            },
            {
                'scenario': 'Evolution of complex traits (e.g., eye development)',
                'key_factors': 'gene regulatory networks, pleiotropy, developmental constraints'
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a genetic algorithm to simulate and analyze the evolutionary scenario: {t['scenario']}. Your task is to create a novel approach that incorporates principles from biology, computer science, and evolutionary theory. Consider the key factors for this scenario: {t['key_factors']}.

Your response should include:

1. Algorithm Design (250-300 words):
   a) Describe the overall structure and components of your genetic algorithm.
   b) Explain how your algorithm models the key factors of the given evolutionary scenario.
   c) Discuss how your algorithm integrates biological realism with computational efficiency.

2. Genome Representation (200-250 words):
   a) Explain how you represent the genome in your algorithm.
   b) Describe any novel data structures or encoding methods used.
   c) Discuss how your representation captures the complexity of the given evolutionary scenario.

3. Fitness Function (200-250 words):
   a) Define the fitness function(s) used in your algorithm.
   b) Explain how the fitness function(s) reflect the selective pressures in the given scenario.
   c) Discuss any multi-objective or dynamic fitness considerations.

4. Genetic Operators (200-250 words):
   a) Describe the genetic operators (e.g., mutation, crossover) used in your algorithm.
   b) Explain how these operators model biological processes relevant to the scenario.
   c) Discuss any novel or scenario-specific genetic operators you've designed.

5. Population Dynamics (150-200 words):
   a) Explain how your algorithm models population-level phenomena.
   b) Describe any mechanisms for maintaining genetic diversity or preventing premature convergence.
   c) Discuss how your algorithm handles concepts like carrying capacity or population structure.

6. Analysis and Visualization (150-200 words):
   a) Propose methods for analyzing the output of your algorithm.
   b) Describe how you would visualize the evolutionary processes and outcomes.
   c) Discuss any statistical measures or indicators you would use to interpret the results.

7. Biological Implications (200-250 words):
   a) Discuss how your algorithm might provide insights into real-world evolutionary processes.
   b) Explain any limitations in extrapolating from your model to biological systems.
   c) Propose a specific hypothesis about {t['scenario']} that your algorithm could help test.

Ensure your response demonstrates a deep understanding of both evolutionary biology and computational methods. Be creative in your algorithm design while maintaining biological plausibility. Use appropriate terminology from both fields and provide explanations where necessary."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The algorithm design effectively integrates principles from biology, computer science, and evolutionary theory, with a focus on {t['scenario']}.",
            f"The genome representation and genetic operators adequately model the key factors: {t['key_factors']}.",
            "The response demonstrates creativity and innovation in the algorithm design while maintaining biological plausibility.",
            "The fitness function and population dynamics are well-defined and appropriate for the given scenario.",
            "The response shows a high level of understanding in both evolutionary biology and computational methods, using appropriate terminology from both fields."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
