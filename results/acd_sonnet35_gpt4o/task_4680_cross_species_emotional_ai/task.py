import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        species_pairs = [
            ("Human", "Dolphin"),
            ("Chimpanzee", "Dog"),
            ("Elephant", "Parrot"),
            ("Octopus", "Cat")
        ]
        emotions = ["Joy", "Fear", "Anger", "Curiosity", "Contentment"]
        
        tasks = {}
        for i in range(1, 3):
            species_pair = random.choice(species_pairs)
            emotion = random.choice(emotions)
            tasks[str(i)] = {
                "species_pair": species_pair,
                "emotion": emotion
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of interpreting and generating non-verbal emotional cues between {t['species_pair'][0]} and {t['species_pair'][1]}, focusing on the emotion of {t['emotion']}. Your response should include the following sections:

1. Theoretical Framework (250-300 words):
   a) Explain key theories from comparative psychology and ethology relevant to non-verbal emotional communication in the given species pair. Cite at least two relevant research studies.
   b) Describe how these theories apply to the expression and interpretation of {t['emotion']} in both species.
   c) Discuss unique challenges or opportunities in computationally representing and translating {t['emotion']} between these species.
   d) Provide at least one specific example of a non-verbal cue expressing {t['emotion']} for each species in the pair.

2. System Architecture (300-350 words):
   a) Describe the main components of your AI system and how they interact.
   b) Explain how your system processes and interprets non-verbal cues from each species.
   c) Detail how your system generates appropriate non-verbal responses for each species.
   d) Provide a visual representation of your system architecture (describe it textually, using ASCII art if helpful).

3. Cross-Species Translation Process (250-300 words):
   a) Provide a step-by-step example of how your system would interpret a non-verbal cue expressing {t['emotion']} from one species and translate it for the other.
   b) Explain how this process incorporates principles from comparative psychology and ethology.
   c) Describe how your system ensures accurate emotional translation while respecting species-specific behaviors.
   d) Include a pseudocode snippet (5-10 lines) illustrating a key algorithm in your translation process.

4. Evaluation Methods (200-250 words):
   a) Propose quantitative and qualitative methods to evaluate your system's ability to accurately interpret and generate non-verbal emotional cues for each species.
   b) Describe how you would compare your system's performance to that of human experts in animal behavior.
   c) Suggest a novel metric for measuring the cross-species emotional communication accuracy.

5. Ethical Considerations and Future Directions (200-250 words):
   a) Discuss potential ethical issues related to AI-mediated cross-species emotional communication.
   b) Address any limitations of your approach, particularly in capturing the nuances of species-specific emotional expression.
   c) Propose guidelines for the responsible development and use of cross-species emotional AI systems.
   d) Suggest potential applications of your system beyond emotional communication (e.g., in conservation, animal welfare, or human-animal interaction).

Ensure your response demonstrates a deep understanding of animal behavior, cognitive science, affective computing, and AI system design. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.

Format your response with clear headings for each section and subsections labeled a, b, c, d as appropriate. Your total response should be between 1200-1450 words. Each section should meet the minimum word count specified."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of comparative psychology, ethology, and affective computing.",
            "The proposed AI system is innovative and scientifically plausible.",
            "The theoretical framework is well-grounded in relevant theories, cites at least two research studies, and addresses the specific species pair and emotion.",
            "The system architecture is clearly described and includes all necessary components for cross-species emotional communication.",
            "The cross-species translation process is logically explained and includes a relevant pseudocode snippet.",
            "Evaluation methods are comprehensive and include a novel metric for measuring cross-species emotional communication accuracy.",
            "Ethical considerations are thoroughly discussed, and future directions are insightful and relevant.",
            "The response is well-structured, within the specified word count, and uses appropriate terminology from all relevant fields.",
            "At least one specific example of a non-verbal cue expressing the given emotion is provided for each species in the pair."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
