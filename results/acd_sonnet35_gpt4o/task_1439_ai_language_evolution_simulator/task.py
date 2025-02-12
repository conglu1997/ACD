class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "linguistic_focus": "Phonological changes",
                "cognitive_principle": "Statistical learning",
                "evolutionary_mechanism": "Natural selection",
                "initial_population": 1000,
                "simulation_duration": "500 generations",
                "environmental_factor": "Increased social group size"
            },
            "2": {
                "linguistic_focus": "Syntactic complexity",
                "cognitive_principle": "Theory of mind",
                "evolutionary_mechanism": "Cultural transmission",
                "initial_population": 500,
                "simulation_duration": "1000 generations",
                "environmental_factor": "Introduction of writing system"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates the evolution of language in a population of artificial agents, focusing on the following aspects:

Linguistic Focus: {t['linguistic_focus']}
Cognitive Principle: {t['cognitive_principle']}
Evolutionary Mechanism: {t['evolutionary_mechanism']}
Initial Population: {t['initial_population']}
Simulation Duration: {t['simulation_duration']}
Environmental Factor: {t['environmental_factor']}

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI language evolution simulator.
   b) Explain how these components interact to model language evolution.
   c) Discuss how your system incorporates the specified linguistic focus, cognitive principle, and evolutionary mechanism.
   d) Propose a novel algorithm or technique that enables your system to model language change over time.

2. Agent Design (250-300 words):
   a) Describe the cognitive architecture of your artificial agents.
   b) Explain how agents acquire, process, and produce language.
   c) Detail how the specified cognitive principle is implemented in the agents' decision-making processes.
   d) Discuss how individual differences among agents are modeled and how they influence language evolution.

3. Evolutionary Dynamics (250-300 words):
   a) Explain how your system models the specified evolutionary mechanism in the context of language change.
   b) Describe how linguistic innovations arise and spread through the population.
   c) Discuss how your system handles the interaction between biological and cultural evolution in language change.
   d) Propose a method for quantifying and visualizing language evolution in your simulation.

4. Simulation Scenario (200-250 words):
   a) Design a specific scenario to test your language evolution simulator using the given parameters.
   b) Describe how the initial population, simulation duration, and environmental factor influence the simulation.
   c) Predict potential outcomes of the simulation and explain your reasoning.
   d) Discuss how you would validate the results of your simulation against real-world language evolution data.

5. Interdisciplinary Implications (200-250 words):
   a) Discuss how your system could contribute to our understanding of human language evolution.
   b) Propose two novel research questions in linguistics or cognitive science that could be explored using your simulator.
   c) Explain how your system could be adapted to study other aspects of cultural evolution or cognitive development.

6. Ethical Considerations and Limitations (150-200 words):
   a) Identify potential ethical concerns related to simulating language evolution and cognitive processes.
   b) Discuss any limitations or potential biases in your approach to modeling language evolution.
   c) Propose guidelines for the responsible development and use of AI systems that model human cognitive processes.

7. Technical Implementation (200-250 words):
   a) Provide a high-level pseudocode or code snippet for a key component of your system (e.g., agent interaction, language change algorithm, or fitness evaluation).
   b) Explain how this component integrates with the rest of your system.
   c) Discuss any technical challenges in implementing this component and how you would address them.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and evolutionary theory. Use appropriate technical terminology and provide clear explanations where necessary. Be creative and innovative in your approach while maintaining scientific plausibility and coherence across all sections of your response.

Format your response with clear headings for each section, numbered 1-7 as outlined above. Your total response should be between 1550-1900 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cognitive science, and evolutionary theory.",
            "The proposed AI system effectively incorporates the specified linguistic focus, cognitive principle, evolutionary mechanism, and environmental factor.",
            "The system architecture and agent design are innovative, coherent, and scientifically plausible.",
            "The evolutionary dynamics and simulation scenario are well-designed and demonstrate creative problem-solving.",
            "The interdisciplinary implications and ethical considerations are thoughtfully discussed.",
            "The technical implementation section includes a relevant pseudocode or code snippet that integrates well with the proposed system.",
            "The response is well-structured, adhering to the specified word limits and format requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
