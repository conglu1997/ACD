import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'ecosystem': 'Aquatic bioluminescent creatures',
                'communication_mode': 'Light patterns and bioluminescence',
                'evolutionary_pressure': 'Predator avoidance and mate selection'
            },
            {
                'ecosystem': 'Subterranean crystal-based lifeforms',
                'communication_mode': 'Vibrational resonance through crystal structures',
                'evolutionary_pressure': 'Resource competition and environmental adaptation'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a simulation of language evolution in a hypothetical alien ecosystem. Your task is to create a model that simulates the development of a communication system for the following scenario:

Ecosystem: {t['ecosystem']}
Primary mode of communication: {t['communication_mode']}
Main evolutionary pressure: {t['evolutionary_pressure']}

Your response should include the following sections:

1. Ecosystem and Species Description (200-250 words):
   a) Describe the key characteristics of the ecosystem and the species inhabiting it.
   b) Explain how the primary mode of communication relates to the species' biology and environment.
   c) Discuss how the main evolutionary pressure influences the species' behavior and communication needs.

2. Language Evolution Model (300-350 words):
   a) Design a computational model that simulates the evolution of a communication system in this ecosystem.
   b) Explain how your model incorporates principles from linguistics, such as phonology, syntax, or semantics.
   c) Describe how your model simulates evolutionary processes, including mutation, selection, and adaptation.
   d) Detail how artificial intelligence techniques are used in your simulation (e.g., neural networks, genetic algorithms).
   e) Provide a high-level pseudocode (10-15 lines) describing your model's key components and processes. Use standard programming constructs (e.g., loops, conditionals, functions) and clear variable names.

3. Simulation Results and Analysis (250-300 words):
   a) Describe the results of running your simulation over an extended period (e.g., thousands of generations).
   b) Analyze the key features of the evolved communication system.
   c) Explain how the evolved language reflects the species' biology, environment, and evolutionary pressures.
   d) Discuss any unexpected or emergent properties in the evolved communication system.
   e) Provide at least two specific examples of evolved language constructs or communication patterns.

4. Comparative Analysis (200-250 words):
   a) Compare the evolved alien communication system to human language.
   b) Discuss similarities and differences in structure, complexity, and function.
   c) Hypothesize how the alien language might handle abstract concepts or complex ideas.
   d) Provide an example of how a specific human language feature might be represented in the alien system.

5. Implications and Extensions (200-250 words):
   a) Discuss the implications of your simulation for our understanding of language evolution.
   b) Propose how this model could be applied to study real-world linguistic phenomena.
   c) Suggest potential extensions or improvements to your simulation.
   d) Describe a hypothetical experiment that could test a prediction made by your model.

6. Ethical Considerations (150-200 words):
   a) Discuss ethical implications of simulating language evolution and applying these models to real-world scenarios.
   b) Address potential concerns about using AI to model fundamental aspects of intelligence and communication.
   c) Propose guidelines for responsible use of language evolution simulations in research and applications.

Ensure your response demonstrates a deep understanding of linguistics, evolutionary biology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, evolutionary biology, and artificial intelligence.",
            "The proposed language evolution model is innovative, coherent, and scientifically plausible.",
            "The simulation results and analysis are detailed and insightful, including specific examples of evolved language constructs.",
            "The comparative analysis between the alien communication system and human language is thorough and well-reasoned, with a concrete example of feature representation.",
            "The discussion of implications, extensions, and ethical considerations is thoughtful and comprehensive, including a proposed experiment and ethical guidelines.",
            "The pseudocode provided is clear, concise, and effectively represents the key components of the language evolution model.",
            "The response adheres to the specified word counts and formatting requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
