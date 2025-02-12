import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "system_type": "magic system",
                "key_feature": "Magic is a finite resource that regenerates based on lunar cycles",
                "example": "In this world, a full moon might restore all magical energy, while a new moon leaves magicians powerless."
            },
            {
                "system_type": "alien ecosystem",
                "key_feature": "All organisms share genetic information through airborne spores",
                "example": "Creatures in this ecosystem might rapidly evolve traits from other species they encounter."
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a {t['system_type']} with the key feature: {t['key_feature']}. Then, analyze its logical implications and potential paradoxes. For context, here's an example of how this feature might manifest: {t['example']}

Your response should adhere to the following structure:

1. System Design (250-300 words):
   a) Describe the fundamental principles and mechanisms of your {t['system_type']}.
   b) Explain how the key feature integrates into the overall system.
   c) Provide 3-4 specific examples of how the system operates.

2. Logical Implications (250-300 words):
   a) Analyze at least three logical consequences of your system's design.
   b) Explain how these implications would affect the world or environment in which the system exists.
   c) Discuss any potential interactions with existing scientific principles or laws.

3. Potential Paradoxes (200-250 words):
   a) Identify two potential paradoxes or logical inconsistencies in your system.
   b) Explain the reasoning behind each paradox.
   c) Propose potential resolutions or workarounds for these paradoxes.

4. Interdisciplinary Analysis (200-250 words):
   a) Examine how your system might impact or interact with two other disciplines (e.g., economics, psychology, or technology).
   b) Provide specific examples of these interdisciplinary effects.

5. Creative Application (150-200 words):
   a) Describe a unique scenario or problem that could arise in a world with your system.
   b) Propose a creative solution to this problem using the rules established in your system.

Ensure your response demonstrates logical consistency, creative problem-solving, and the ability to apply abstract reasoning across disciplines. Use clear examples and explanations throughout your response.

Format your response with clear headings for each section (e.g., '1. System Design', '2. Logical Implications'). Your total response should be between 1050-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must include a detailed design of a {t['system_type']} incorporating the key feature: {t['key_feature']}.",
            "The system design should be original and not simply an elaboration of the given example.",
            "The analysis should demonstrate logical consistency and identify valid implications and paradoxes that are not immediately obvious.",
            "The interdisciplinary analysis should show a deep understanding of how the system interacts with other fields, providing non-trivial insights.",
            "The creative application should present a unique and well-reasoned scenario using the established rules, demonstrating innovative problem-solving.",
            "The overall response should exhibit high-level abstract reasoning and creative problem-solving skills, going beyond surface-level analysis.",
            "The response must adhere to the specified structure and word count requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
