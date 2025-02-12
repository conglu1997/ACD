import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            {
                "ecosystem": "Tropical rainforest",
                "cultural_factor": "Hunter-gatherer society",
                "time_span": "1000 years"
            },
            {
                "ecosystem": "Arctic tundra",
                "cultural_factor": "Nomadic herding community",
                "time_span": "500 years"
            }
        ]
        return {
            "1": random.choice(environments),
            "2": random.choice(environments)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates the evolution of language in response to environmental and cultural factors, then use it to explore how different ecological contexts shape linguistic structures and cognitive patterns. Focus on the following scenario:

Ecosystem: {t['ecosystem']}
Cultural context: {t['cultural_factor']}
Time span: {t['time_span']}

Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for simulating eco-linguistic evolution.
   b) Explain how it models the interaction between language, cognition, and environmental factors.
   c) Detail how the system represents and evolves linguistic structures over time.
   d) Discuss any novel algorithms or techniques incorporated in your system.

2. Environmental and Cultural Modeling (200-250 words):
   a) Explain how your system models the given ecosystem and its impact on language evolution.
   b) Describe how cultural factors are represented and integrated into the simulation.
   c) Discuss how your system accounts for the interplay between environmental pressures and cultural practices in shaping language.

3. Linguistic Evolution Process (250-300 words):
   a) Detail the step-by-step process your system uses to evolve language over the specified time span.
   b) Explain how your system generates and selects linguistic innovations.
   c) Describe how your system models the spread and adoption of linguistic changes across a population.
   d) Provide a specific example of a potential linguistic change your system might generate, with explanation.

4. Cognitive Impact Analysis (200-250 words):
   a) Explain how your system analyzes the impact of evolved linguistic structures on cognitive patterns.
   b) Describe the metrics or methods used to assess cognitive changes.
   c) Discuss how your system might identify and quantify shifts in perception or thought processes resulting from language evolution.

5. Simulation Results and Interpretation (200-250 words):
   a) Present a hypothetical set of results from your simulation for the given scenario.
   b) Analyze these results, explaining what they suggest about the relationship between environment, culture, language, and cognition.
   c) Compare the evolved language features to known linguistic phenomena in similar real-world contexts.

6. Implications and Ethical Considerations (150-200 words):
   a) Discuss the potential implications of your findings for our understanding of language, cognition, and cultural evolution.
   b) Address ethical concerns related to simulating cultural and linguistic evolution.
   c) Propose guidelines for the responsible use and interpretation of such simulations in academic and practical contexts.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, cultural anthropology, and ecological systems. Use appropriate terminology from relevant fields and provide clear explanations. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cognitive science, cultural anthropology, and ecological systems.",
            "The proposed AI system is innovative and plausible, integrating multiple disciplines effectively.",
            "The explanation of the linguistic evolution process is clear, detailed, and scientifically grounded.",
            "The analysis of cognitive impacts and simulation results is insightful and well-reasoned.",
            "The response addresses all required sections comprehensively and meets the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
