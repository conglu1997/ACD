import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "environment": "Post-apocalyptic Earth with limited resources",
                "cultural_shift": "Prioritization of survival skills and resource management",
                "time_span": "200 years",
                "initial_language": "Modern English"
            },
            {
                "environment": "Colonization of a water-covered exoplanet",
                "cultural_shift": "Adaptation to aquatic lifestyle and alien ecosystem",
                "time_span": "500 years",
                "initial_language": "Mandarin Chinese"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates the evolution of language in response to environmental and cultural changes, then use it to predict linguistic adaptations for the following scenario:

Environment: {t['environment']}
Cultural Shift: {t['cultural_shift']}
Time Span: {t['time_span']}
Initial Language: {t['initial_language']}

You have 60 minutes to complete this task. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for simulating language evolution.
   b) Explain how your system models linguistic features, environmental factors, and cultural influences.
   c) Detail how your system incorporates principles from historical linguistics and sociolinguistics.
   d) Discuss any novel AI techniques or algorithms used in your simulation.
   e) Provide a high-level diagram of your system architecture (describe it textually).

2. Linguistic Feature Modeling (250-300 words):
   a) Explain how your system represents and evolves different linguistic features (e.g., phonology, morphology, syntax, semantics).
   b) Describe how you model the interactions between these features during the evolutionary process.
   c) Discuss how your system handles the emergence of new linguistic structures or the loss of existing ones.

3. Environmental and Cultural Integration (250-300 words):
   a) Detail how your system incorporates the given environmental factors and cultural shifts into the language evolution process.
   b) Explain your approach to modeling the impact of these factors on specific linguistic features.
   c) Describe how your system accounts for potential feedback loops between language, environment, and culture.

4. Simulation Process (200-250 words):
   a) Provide a step-by-step description of how your AI system would run a simulation for the given scenario.
   b) Explain how your system handles the specified time span and initial language.
   c) Discuss how you ensure the plausibility of the simulated language changes.

5. Predicted Linguistic Adaptations (250-300 words):
   a) Present the key linguistic adaptations predicted by your system for the given scenario.
   b) Explain the reasoning behind these predictions, linking them to the environmental and cultural factors.
   c) Provide examples of how specific words, grammatical structures, or communication modes might change.

6. Evaluation and Validation (150-200 words):
   a) Propose methods to evaluate the plausibility and coherence of your system's predictions.
   b) Discuss how you would validate your system using historical data or expert knowledge.
   c) Suggest an experiment to test the accuracy of your system's predictions in a controlled setting.

7. Ethical Considerations and Implications (150-200 words):
   a) Discuss the ethical implications of using AI to predict language evolution.
   b) Address concerns about linguistic diversity and the potential impact on minority languages.
   c) Propose guidelines for the responsible use of language evolution simulation technology.

Ensure your response demonstrates a deep understanding of linguistics, cultural anthropology, and AI capabilities. Use appropriate terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility. Remember to balance creativity with scientific rigor throughout your response.

Format your response with clear headings for each section, numbered as above. Use subheadings a), b), c) etc. as appropriate. Your total response should be between 1550-1900 words.

Example of a linguistic adaptation (not a full solution):
In a post-apocalyptic scenario, the word "green" might evolve to primarily mean "safe from radiation" rather than referring to a color, reflecting the new environmental priorities."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cultural anthropology, and AI technologies, using appropriate terminology and concepts.",
            "The proposed system architecture is comprehensive, integrating principles from multiple disciplines and including novel AI techniques.",
            "The linguistic feature modeling approach is well-explained and accounts for various aspects of language evolution, including emergent structures.",
            "The system effectively incorporates the given environmental and cultural factors into the language evolution process, with clear examples.",
            "The predicted linguistic adaptations are plausible, well-reasoned, and directly linked to the scenario's environmental and cultural factors.",
            "The evaluation and validation methods proposed are appropriate, specific, and include a concrete experiment design.",
            "Ethical considerations are thoroughly discussed, with specific guidelines proposed for responsible use of the technology.",
            "The response balances creativity and innovation with scientific plausibility throughout all sections.",
            "The response follows the specified format with clear headings and subheadings, and falls within the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
