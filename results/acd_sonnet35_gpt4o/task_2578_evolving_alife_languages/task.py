import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'environment': 'Sparse resources with high competition',
                'communication_medium': 'Visual signals',
                'population_size': 1000,
                'generations': 500,
                'mutation_rate': 0.01
            },
            {
                'environment': 'Abundant resources with low competition',
                'communication_medium': 'Acoustic signals',
                'population_size': 500,
                'generations': 1000,
                'mutation_rate': 0.05
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and simulate the evolution of artificial languages in a computational ecosystem with the following characteristics:

Environment: {t['environment']}
Communication Medium: {t['communication_medium']}
Population Size: {t['population_size']}
Generations: {t['generations']}
Mutation Rate: {t['mutation_rate']}

Your task has the following parts:

1. Language Design (250-300 words):
   a) Describe the basic elements and structure of your artificial language.
   b) Explain how the language is encoded in the artificial organisms.
   c) Discuss how the language can express different concepts or messages.
   d) Explain how the communication medium ({t['communication_medium']}) influences the language design and structure.

2. Evolutionary Algorithm (200-250 words):
   a) Outline the key components of your evolutionary algorithm.
   b) Explain how fitness is calculated based on communication success.
   c) Describe how language traits are inherited and mutated across generations.

3. Simulation Results (250-300 words):
   a) Summarize the main trends observed in language evolution over the specified generations.
   b) Describe any emergent properties or unexpected behaviors in the evolved languages.
   c) Analyze how the environment and communication medium influenced language evolution.

4. Linguistic Analysis (200-250 words):
   a) Compare the evolved artificial languages to natural human languages.
   b) Identify any universal features that emerged across multiple simulation runs.
   c) Discuss the implications of your results for theories of language evolution.

5. Information Theory Application (150-200 words):
   a) Apply concepts from information theory to analyze the efficiency of the evolved languages.
   b) Discuss how the language's information density changed over generations.
   c) Propose a hypothesis about the relationship between language complexity and communication efficiency.

6. Future Directions (100-150 words):
   a) Suggest two potential extensions or modifications to your simulation.
   b) Propose a research question that could be explored using your evolved languages.

Ensure your response demonstrates a deep understanding of linguistics, evolutionary algorithms, and information theory. Use appropriate terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, evolutionary algorithms, and information theory.",
            "The language design is creative, well-structured, and appropriate for the given environment and communication medium.",
            "The evolutionary algorithm is clearly explained and incorporates relevant concepts from evolutionary biology.",
            "The simulation results are plausible and show a clear evolution of the artificial languages over time.",
            "The linguistic analysis draws meaningful comparisons between the artificial languages and natural human languages.",
            "The application of information theory concepts is accurate and insightful.",
            "The proposed future directions and research questions are innovative and scientifically valuable.",
            "The response is well-organized, coherent, and adheres to the specified word counts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
