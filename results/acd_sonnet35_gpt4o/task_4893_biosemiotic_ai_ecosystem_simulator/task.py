import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = ['Coral Reef', 'Tropical Rainforest', 'Arctic Tundra', 'Deep Sea Hydrothermal Vent']
        artificial_entities = ['Nanobots', 'Synthetic Bacteria', 'AI-controlled Drones', 'Bionic Plants']
        time_spans = [100, 500, 1000, 5000]
        
        tasks = {
            "1": {
                "ecosystem": random.choice(ecosystems),
                "artificial_entity": random.choice(artificial_entities),
                "time_span": random.choice(time_spans)
            },
            "2": {
                "ecosystem": random.choice(ecosystems),
                "artificial_entity": random.choice(artificial_entities),
                "time_span": random.choice(time_spans)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates the evolution of biosemiotic processes in a {t['ecosystem']} ecosystem, incorporating {t['artificial_entity']} as artificial entities. Use this system to analyze the emergence of novel communication systems between artificial and biological entities over a {t['time_span']} year period. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for simulating biosemiotic evolution.
   b) Explain how your system models biological and artificial entities and their interactions.
   c) Detail how your system simulates the emergence and evolution of communication systems.
   d) Include a diagram or pseudocode representing the core algorithm of your system.
   e) Cite at least two relevant scientific papers to support your system's theoretical foundation.

2. Biosemiotic Modeling (250-300 words):
   a) Explain how your system represents and evolves biosemiotic processes.
   b) Describe how you model the interactions between biological and artificial entities.
   c) Discuss how your system accounts for the specific characteristics of the {t['ecosystem']} ecosystem.
   d) Explain how the {t['artificial_entity']} are integrated into the biosemiotic framework.

3. Evolutionary Dynamics (250-300 words):
   a) Detail how your system models evolutionary processes over the {t['time_span']} year period.
   b) Explain how new communication systems emerge and evolve in your simulation.
   c) Describe how your system handles co-evolution between biological and artificial entities.
   d) Discuss how you balance randomness and determinism in your evolutionary model.

4. Simulation Results and Analysis (250-300 words):
   a) Present the outcomes of your simulation, including at least one quantitative prediction and one qualitative insight.
   b) Analyze the implications of your findings for our understanding of biosemiotics and artificial-biological interactions.
   c) Discuss any unexpected or counterintuitive results from your simulation.
   d) Propose a novel hypothesis about the nature of communication in mixed artificial-biological systems based on your results.

5. Ethical Considerations (200-250 words):
   a) Discuss the ethical implications of introducing artificial entities into natural ecosystems.
   b) Address concerns about potential unintended consequences of artificial-biological communication.
   c) Propose guidelines for responsible research and application of biosemiotic AI systems.
   d) Consider potential societal impacts if this technology becomes widely available.

6. Limitations and Future Directions (150-200 words):
   a) Identify at least three potential limitations or challenges in your proposed system.
   b) Suggest how these limitations might be addressed in future research.
   c) Propose two potential applications or extensions of your biosemiotic AI system.
   d) Speculate on how this approach might influence our understanding of consciousness and cognition in non-human entities.

Ensure your response demonstrates a deep understanding of biosemiotics, artificial intelligence, and evolutionary biology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1400-1700 words. Include a word count at the end of each section.

Cite relevant scientific literature throughout your response using in-text citations (Author, Year). Include at least five unique citations across your entire response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of biosemiotics, artificial intelligence, and evolutionary biology",
            "The proposed system architecture is innovative and scientifically plausible",
            "The biosemiotic modeling approach is well-explained and incorporates both biological and artificial entities",
            "The evolutionary dynamics are clearly described and account for the specified time span",
            "The simulation results are presented with both quantitative and qualitative insights",
            "Ethical considerations are thoroughly discussed with proposed guidelines",
            "Limitations and future directions are adequately addressed",
            "The response includes at least five unique and relevant scientific citations",
            "The writing is clear, well-organized, and adheres to the specified format and word count guidelines",
            f"The response effectively incorporates the specific ecosystem ({t['ecosystem']}), artificial entity ({t['artificial_entity']}), and time span ({t['time_span']} years) into the proposed system and analysis"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
