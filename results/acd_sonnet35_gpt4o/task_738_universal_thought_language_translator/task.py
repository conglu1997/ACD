import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        thought_categories = [
            "Emotional concepts",
            "Spatial reasoning",
            "Temporal concepts",
            "Abstract philosophical ideas",
            "Mathematical relationships"
        ]
        tasks = {
            "1": {"thought_category": random.choice(thought_categories)},
            "2": {"thought_category": random.choice(thought_categories)}
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical system that can translate abstract thoughts directly into a universal language, bypassing natural languages. Focus on thoughts related to {t['thought_category']}. Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your thought-to-universal-language translation system.
   b) Explain how your system interfaces with the human mind to capture abstract thoughts.
   c) Detail the process of converting thoughts into the universal language.
   d) Include a simple diagram or pseudocode snippet illustrating a key aspect of your system.

2. Universal Language Structure (200-250 words):
   a) Describe the fundamental elements and syntax of your universal language.
   b) Explain how it represents complex, abstract concepts from {t['thought_category']}.
   c) Discuss how your language achieves universality across different cultures and cognitive frameworks.

3. Cognitive-Linguistic Mapping (200-250 words):
   a) Explain how your system maps cognitive processes to linguistic structures.
   b) Describe how it handles ambiguities and contextual nuances in thought.
   c) Provide an example of translating a specific abstract thought from {t['thought_category']} into your universal language.

4. Challenges and Solutions (150-200 words):
   a) Identify potential challenges in implementing this system.
   b) Propose innovative solutions to these challenges.
   c) Discuss any assumptions or simplifications in your model.

5. Applications and Implications (150-200 words):
   a) Explore potential applications of your thought-to-universal-language system.
   b) Discuss its implications for human communication, cognition, and AI development.
   c) Address any ethical considerations related to direct thought translation.

6. Comparative Analysis (100-150 words):
   a) Compare your system to existing language models and translation technologies.
   b) Highlight the unique advantages and potential limitations of your approach.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific and theoretical plausibility.

Format your response using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a comprehensive explanation of the thought-to-universal-language translation system architecture",
            "The universal language structure is well-described and capable of representing complex, abstract concepts",
            "The cognitive-linguistic mapping process is clearly explained with a specific example",
            f"The system effectively handles thoughts related to {t['thought_category']}",
            "Potential challenges are identified and innovative solutions are proposed",
            "The response demonstrates deep understanding of cognitive science, linguistics, and artificial intelligence",
            "The proposed system is creative while remaining scientifically and theoretically plausible"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
