import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "environment": "Harsh desert with scarce resources",
                "initial_tech": "Stone tools",
                "social_structure": "Nomadic tribes",
                "time_span": "5000 years",
                "external_influence": "Rare contact with other cultures"
            },
            {
                "environment": "Archipelago with abundant marine life",
                "initial_tech": "Basic seafaring",
                "social_structure": "Island-based clans",
                "time_span": "10000 years",
                "external_influence": "Frequent trade with distant lands"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(scenarios)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a simulation model for the evolution of a fictional culture's language and communication system over millennia, accounting for environmental, technological, and social factors. Your task has the following components:

1. Initial Language Design (250-300 words):
   a) Create a basic structure for the initial language of your fictional culture, including:
      - Phonology: Provide a set of phonemes and basic phonological rules.
      - Morphology: Describe word formation processes and grammatical categories.
      - Syntax: Outline basic sentence structures and word order.
   b) Explain how this language reflects the initial environment ({t['environment']}) and technology level ({t['initial_tech']}).
   c) Describe the primary mode(s) of communication used by the culture.
   d) Provide a sample sentence in your constructed language with a gloss and translation.

2. Evolutionary Factors (200-250 words):
   a) Identify at least five key factors that will drive the evolution of the language and communication system.
   b) Explain how each factor relates to the given scenario (environment, technology, social structure, etc.).
   c) Describe potential interactions between these factors.

3. Simulation Model Design (250-300 words):
   a) Outline the structure of your simulation model, including key variables and parameters.
   b) Explain how your model simulates linguistic and communicative changes over time.
   c) Describe how you incorporate the identified evolutionary factors into your model.
   d) Discuss how your model handles the interaction between language, culture, and technology.

4. Predictive Algorithms (200-250 words):
   a) Propose at least two algorithms or mathematical models your simulation would use to predict language changes.
   b) Explain the linguistic or cultural theory behind each algorithm.
   c) Provide a simple pseudocode or formula for one of your proposed algorithms.
   d) Give a concrete example of how one of your algorithms would predict a specific language change.

5. Projected Linguistic Evolution (250-300 words):
   a) Based on your model, describe the projected state of the language and communication system after {t['time_span']}.
   b) Explain major changes in phonology, morphology, syntax, and communication modalities. Provide specific examples for each.
   c) Discuss how these changes reflect the culture's adaptation to its environment and technological progress.
   d) Address the impact of {t['external_influence']} on the language's evolution.
   e) Provide an example of a unique linguistic feature that evolves in your simulated language and explain its development.
   f) Present a sample sentence in the evolved language, with gloss and translation, and compare it to the initial language sample.

6. Cross-cultural Comparison (200-250 words):
   a) Compare your simulated language evolution to a real-world language family or historical linguistic change.
   b) Identify similarities and differences in the evolutionary processes.
   c) Discuss how your simulation might inform or challenge existing theories in historical linguistics.

7. Simulation Output and Analysis (200-250 words):
   a) Describe the types of data and visualizations your simulation would produce.
   b) Explain how you would validate the simulation results against linguistic and anthropological theories.
   c) Propose a method for comparing the simulated language evolution with real-world language families.

8. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical implications of simulating cultural and linguistic evolution.
   b) Address limitations of your model and areas where it may not accurately reflect real-world language evolution.
   c) Suggest how this simulation could be used responsibly in anthropological or linguistic research.

Ensure your response demonstrates a deep understanding of linguistics, anthropology, and complex system modeling. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1700-2000 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, anthropology, and complex system modeling.",
            "The initial language design is comprehensive, creative, and plausibly reflects the given environment and technology level.",
            "The evolutionary factors identified are relevant, well-explained, and their interactions are considered.",
            "The simulation model design is comprehensive and effectively incorporates the identified evolutionary factors.",
            "The predictive algorithms are based on sound linguistic or cultural theories and include a concrete example.",
            "The projected linguistic evolution is detailed, consistent with the given scenario, and includes specific examples of changes.",
            "The cross-cultural comparison draws meaningful parallels with real-world linguistic evolution.",
            "The simulation output and analysis methods are well-described, scientifically valid, and consider validation against real-world data.",
            "Ethical considerations and limitations are thoughtfully addressed and contextualized within the field of research.",
            "The response is creative and innovative while maintaining scientific plausibility.",
            "The response follows the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
