import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "society_type": "Post-scarcity space colony",
                "initial_language": "English",
                "simulation_duration": "500 years",
                "key_factor": "Artificial intelligence integration"
            },
            "2": {
                "society_type": "Underwater civilization",
                "initial_language": "Mandarin Chinese",
                "simulation_duration": "1000 years",
                "key_factor": "Genetic engineering advancements"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and implement a detailed simulation of language evolution for a {t['society_type']}, starting with {t['initial_language']} as the base language. Your simulation should span {t['simulation_duration']} and incorporate cultural dynamics, technological advancements (particularly {t['key_factor']}), and cognitive constraints.

Language evolution refers to the gradual change in language over time, influenced by various factors including cultural shifts, technological advancements, and cognitive processes. Your task is to model this complex process in a hypothetical society.

Your response should include the following sections:

1. Simulation Framework and Initial Conditions (400-450 words):
   a) Describe the key components of your language evolution simulation, including at least 4 variables or factors influencing language change.
   b) Explain how you model cultural, technological, and cognitive factors.
   c) Provide a visual representation or diagram of your simulation framework.
   d) Describe the starting state of your simulated society and its language, including initial values or ranges for your key variables.
   e) Outline a simple mathematical or computational model underlying your simulation. This could be a set of rules, a basic equation, or a description of how variables interact.

2. Evolution Mechanisms and Factors (350-400 words):
   a) Explain the primary mechanisms driving language change in your simulation.
   b) Describe how {t['key_factor']} specifically influences language evolution.
   c) Discuss how cognitive constraints are modeled and their impact on language change.
   d) Identify key cultural shifts and technological advancements in your simulation and explain their influence on language evolution.

3. Simulation Results and Analysis (400-450 words):
   a) Provide a summary of how the language evolves over the {t['simulation_duration']}.
   b) Describe 3-4 major linguistic changes and explain the factors that led to them.
   c) Give examples of new words, grammatical structures, or communication methods that emerge.
   d) Include quantitative predictions or metrics for at least 2 aspects of language change over time. For example, you might predict how vocabulary size changes, or how the frequency of certain grammatical structures evolves.
   e) Compare your simulated language evolution to at least one real-world example or theory of language change.
   f) Discuss any surprising or counterintuitive results, and explore potential implications for real-world language evolution and AI language models.
   g) Briefly address limitations and potential biases in your simulation model.

Ensure your response demonstrates a deep understanding of linguistics, sociology, cognitive science, and futurism. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Your total response should be between 1150-1300 words. Format your response with clear headings for each section, and include your visual representation of the simulation framework within the appropriate section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of language evolution, incorporating at least 4 variables or factors influencing language change.",
            "The simulation framework is well-defined and includes a visual representation that effectively communicates the system's complexity.",
            "A simple mathematical or computational model is outlined, showing how key variables interact in the simulation.",
            "The influence of the specified key factor ({}) is clearly explained and integrated throughout the simulation.".format(t['key_factor']),
            "The simulation results include at least 3-4 major linguistic changes with explanations, and quantitative predictions for at least 2 aspects of language change over time.",
            "The response includes a comparison to at least one real-world example or theory of language change.",
            "The analysis discusses surprising or counterintuitive results, potential implications, and addresses limitations and potential biases in the model.",
            "The response includes all required sections and stays within the specified word count range (1150-1300 words)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
