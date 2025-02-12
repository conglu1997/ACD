class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "cultures": ["Ancient Greece", "Renaissance Italy", "Modern Japan"],
                "abstract_concept": "Justice",
                "time_span": "2500 years"
            },
            "2": {
                "cultures": ["Mayan Civilization", "Industrial Revolution Britain", "Digital Age Silicon Valley"],
                "abstract_concept": "Progress",
                "time_span": "2000 years"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates the evolution of abstract thought across different cultures and time periods. Your system should model how the concept of {t['abstract_concept']} has evolved across {t['cultures']} over a span of {t['time_span']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for simulating abstract thought evolution.
   b) Explain how your system models cultural, linguistic, and cognitive factors.
   c) Detail how your system simulates changes over time and across cultures.
   d) Include a diagram or pseudocode representing the core algorithm of your system.

2. Cultural and Linguistic Modeling (250-300 words):
   a) Explain how your system represents and evolves cultural and linguistic features.
   b) Describe how you model the interactions between culture, language, and abstract thought.
   c) Discuss how your system accounts for historical events and technological advancements.

3. Cognitive Development Simulation (250-300 words):
   a) Detail how your system models individual and collective cognitive processes.
   b) Explain how abstract concepts are represented and manipulated in your simulation.
   c) Describe how your system simulates the emergence and evolution of new ideas.

4. Simulation Process (200-250 words):
   a) Outline the steps your system would take to simulate the evolution of {t['abstract_concept']}.
   b) Explain how your system handles transitions between different cultural contexts and time periods.
   c) Describe how your system measures and tracks changes in the conception of {t['abstract_concept']}.

5. Analysis and Interpretation (250-300 words):
   a) Describe the methods your system uses to analyze the results of the simulation.
   b) Explain how you would identify and interpret significant trends or shifts in the understanding of {t['abstract_concept']}.
   c) Discuss how your system might generate insights about the nature of abstract thought and its relationship to culture and language.
   d) Provide a hypothetical example of how the concept of {t['abstract_concept']} might have evolved across the given cultures and time span.

6. Ethical Considerations and Limitations (200-250 words):
   a) Discuss potential biases and limitations in your simulation approach.
   b) Address ethical concerns related to modeling cultural and cognitive evolution.
   c) Propose guidelines for the responsible use and interpretation of results from such simulations.
   d) Suggest potential applications and implications of your system for fields such as anthropology, philosophy, and cognitive science.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, cultural anthropology, and complex systems modeling. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section and use numbered subsections (e.g., 1a, 1b, 1c) to organize your thoughts. Your total response should be between 1450-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all required sections with appropriate word counts.",
            "The proposed AI system demonstrates a clear understanding of cognitive science, linguistics, cultural anthropology, and complex systems modeling.",
            "The system architecture and simulation process are well-explained and scientifically plausible.",
            "The response shows creativity and innovation in approaching the challenge of modeling abstract thought evolution.",
            "The analysis and interpretation section provides insightful hypothetical examples and demonstrates critical thinking.",
            "Ethical considerations and limitations are thoughtfully addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
