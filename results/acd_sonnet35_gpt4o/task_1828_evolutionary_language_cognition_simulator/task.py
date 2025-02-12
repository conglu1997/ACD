import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'initial_language_features': ['Subject-Verb-Object word order', 'Tonal distinctions', 'Agglutinative morphology'],
                'cognitive_focus': 'Spatial reasoning',
                'environmental_factor': 'Nomadic lifestyle'
            },
            {
                'initial_language_features': ['Verb-Subject-Object word order', 'Evidentiality markers', 'Isolating morphology'],
                'cognitive_focus': 'Theory of mind',
                'environmental_factor': 'Dense urban living'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates the co-evolution of language and cognitive structures in a virtual society over multiple generations. Your system should model how language features and thought patterns emerge and change over time, influenced by cognitive processes and environmental factors. Use the following parameters for your simulation:

Initial language features: {', '.join(t['initial_language_features'])}
Cognitive focus: {t['cognitive_focus']}
Environmental factor: {t['environmental_factor']}

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for simulating language and cognitive evolution.
   b) Explain how your system models individual agents, their cognitive processes, and linguistic interactions.
   c) Detail how your system simulates generational changes and evolutionary processes.
   d) Provide a text-based representation of your system architecture (use ASCII characters to create a simple flowchart or diagram).

2. Linguistic and Cognitive Modeling (250-300 words):
   a) Explain how your system represents and evolves language features over time.
   b) Describe how you model the specified cognitive focus and its influence on language evolution.
   c) Discuss how environmental factors are incorporated into your simulation.

3. Simulation Process (200-250 words):
   a) Outline the steps your system would take to run a multi-generational simulation.
   b) Explain how linguistic interactions between agents are modeled and how language is transmitted across generations.
   c) Describe how your system measures and tracks changes in language and cognitive structures over time.

4. Emergent Phenomena (200-250 words):
   a) Predict and explain at least three potential emergent linguistic features or cognitive patterns that might arise from your simulation, given the initial conditions.
   b) Discuss how these emergent phenomena relate to the initial conditions and simulation parameters.
   c) Provide concrete examples of how the language might evolve over time, considering the given initial features and environmental factors.

5. Analysis and Interpretation (200-250 words):
   a) Describe the methods your system would use to analyze the results of the simulation.
   b) Explain how you would identify and interpret significant trends or patterns in language and cognitive evolution.
   c) Discuss how your system might generate hypotheses about the relationship between language, cognition, and environment based on the simulation results.
   d) Compare your predicted outcomes with at least two real-world examples of language evolution or linguistic diversity.

6. Limitations and Ethical Considerations (150-200 words):
   a) Discuss the limitations of your simulation approach and potential sources of bias.
   b) Address ethical considerations related to modeling human cognitive and linguistic evolution.
   c) Propose guidelines for the responsible use and interpretation of results from such simulations.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, evolutionary theory, and complex systems modeling. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section and use numbered subsections (e.g., 1a, 1b, 1c) to organize your thoughts. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cognitive science, evolutionary theory, and complex systems modeling",
            "The proposed AI system is innovative and scientifically plausible",
            "The simulation process and analysis methods are clearly explained and logically sound",
            "The response addresses all required sections and adheres to the specified word count",
            "The analysis of emergent phenomena includes at least three concrete predictions based on the given parameters",
            "The response compares predicted outcomes with real-world examples of language evolution",
            "The system architecture is clearly presented using a text-based diagram or flowchart",
            "The response is well-formatted with clear headings and numbered subsections"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
