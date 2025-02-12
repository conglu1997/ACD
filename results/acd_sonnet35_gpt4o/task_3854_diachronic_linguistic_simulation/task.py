import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        historical_events = [
            "Industrial Revolution",
            "Age of Exploration",
            "Digital Revolution",
            "Global Pandemic"
        ]
        cultural_interactions = [
            "Trade with neighboring civilizations",
            "Colonization by a foreign power",
            "Mass migration",
            "Cultural Renaissance"
        ]
        cognitive_shifts = [
            "Widespread literacy",
            "Emergence of scientific thinking",
            "Shift to visual communication",
            "Enhanced cognitive augmentation"
        ]
        
        return {
            "1": {
                "event": random.choice(historical_events),
                "interaction": random.choice(cultural_interactions),
                "shift": random.choice(cognitive_shifts)
            },
            "2": {
                "event": random.choice(historical_events),
                "interaction": random.choice(cultural_interactions),
                "shift": random.choice(cognitive_shifts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates the evolution of a fictional language over centuries, accounting for the following factors:

Historical Event: {t['event']}
Cultural Interaction: {t['interaction']}
Cognitive Shift: {t['shift']}

Your response should include the following sections:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for simulating language evolution.
   b) Explain how your system incorporates linguistic theories of language change.
   c) Detail how the AI models the interaction between historical events, cultural exchanges, and cognitive shifts in shaping language.
   d) Include a brief diagram or flowchart representing your system's architecture (use ASCII art or a clear textual description).

2. Initial Language Design (200-250 words):
   a) Briefly describe the initial state of your fictional language, including its linguistic family, basic grammatical structure, and notable features.
   b) Explain how this initial design allows for realistic evolution over time.

3. Evolutionary Simulation (250-300 words):
   a) Describe how your AI system simulates language evolution over centuries.
   b) Explain how it incorporates the specified historical event, cultural interaction, and cognitive shift.
   c) Detail the mechanisms for introducing and propagating linguistic changes in your model.

4. Linguistic Changes (250-300 words):
   a) Provide specific examples of how your language evolves in response to each factor.
   b) Include changes in phonology, morphology, syntax, and semantics.
   c) Explain the reasoning behind each change, grounded in linguistic theory.

5. Comparative Analysis (200-250 words):
   a) Compare your simulated language evolution to known patterns of change in natural languages.
   b) Discuss any novel insights your simulation might provide about language change processes.

6. Validation and Limitations (150-200 words):
   a) Propose methods for validating your AI system's predictions against historical linguistic data.
   b) Discuss limitations of your model and areas where it may not accurately reflect real-world language evolution.

7. Ethical Considerations and Applications (150-200 words):
   a) Discuss potential ethical implications of using AI to model language evolution.
   b) Suggest applications of your system in fields such as historical linguistics, language preservation, or future language planning.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence.",
            "The AI system design is innovative, plausible, and well-suited to simulating language evolution.",
            "The evolutionary simulation effectively incorporates the specified historical event, cultural interaction, and cognitive shift.",
            "The linguistic changes described are diverse, specific, and grounded in linguistic theory.",
            "The comparative analysis provides insightful connections to real-world language change patterns.",
            "The response addresses validation methods, limitations, and ethical considerations thoughtfully."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
