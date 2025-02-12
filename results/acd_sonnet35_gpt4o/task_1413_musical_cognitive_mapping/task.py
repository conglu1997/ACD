import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_structures = [
            "Sonata form",
            "Fugue",
            "Twelve-tone technique",
            "Indian raga"
        ]
        cognitive_processes = [
            "Working memory",
            "Emotional regulation",
            "Attention switching",
            "Spatial reasoning"
        ]
        return {
            "1": {
                "musical_structure": random.choice(musical_structures),
                "cognitive_process": random.choice(cognitive_processes)
            },
            "2": {
                "musical_structure": random.choice(musical_structures),
                "cognitive_process": random.choice(cognitive_processes)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that maps the musical structure of {t['musical_structure']} to the cognitive process of {t['cognitive_process']}, and vice versa. Then, apply your system to analyze a specific musical piece and predict its cognitive effects. Your response should include:

1. System Design (300-350 words):
   a) Describe the key components of your mapping system.
   b) Explain how your system represents and translates between musical structures and cognitive processes.
   c) Discuss how your system incorporates principles from music theory, cognitive science, and mathematical modeling.
   d) Include a diagram or flowchart of your system architecture (use ASCII art or a clear textual description).

2. Mapping Process (200-250 words):
   a) Detail the step-by-step process your system uses to map {t['musical_structure']} to {t['cognitive_process']}.
   b) Explain how the system accounts for the unique characteristics of both the musical structure and the cognitive process.
   c) Describe how your system would perform the reverse mapping from {t['cognitive_process']} to {t['musical_structure']}.

3. Musical Analysis (250-300 words):
   a) Choose a specific musical piece that exemplifies {t['musical_structure']}.
   b) Apply your system to analyze this piece and predict its effects on {t['cognitive_process']}.
   c) Provide a detailed explanation of your analysis, including specific musical elements and their predicted cognitive impacts.

4. Cognitive Predictions (200-250 words):
   a) Based on your analysis, make specific predictions about how the chosen musical piece might influence {t['cognitive_process']}.
   b) Explain the reasoning behind your predictions, drawing on principles from cognitive science and music psychology.
   c) Discuss potential individual differences in cognitive responses to the music.

5. Validation and Limitations (150-200 words):
   a) Propose a method to empirically test the predictions made by your system.
   b) Discuss potential limitations of your mapping system and how they might affect its accuracy.
   c) Suggest improvements or extensions to address these limitations.

6. Interdisciplinary Implications (150-200 words):
   a) Explore potential applications of your mapping system in fields such as music therapy, cognitive enhancement, or AI-generated music.
   b) Discuss how this approach to linking musical structures and cognitive processes might inform or be informed by other areas of research.

Ensure your response demonstrates a deep understanding of music theory, cognitive science, and mathematical modeling. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section, adhering to the word limits provided. Your total response should be between 1250-1550 words, not including the system architecture diagram."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['musical_structure']} and {t['cognitive_process']}, and how they might be related.",
            "The system design is innovative, detailed, and scientifically plausible.",
            "The mapping process is clearly explained and logically sound.",
            "The musical analysis and cognitive predictions are well-reasoned and grounded in relevant theories.",
            "The proposed validation method and discussion of limitations show critical thinking.",
            "The interdisciplinary implications are creative and well-considered."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
