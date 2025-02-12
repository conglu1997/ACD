import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "musical_concept": "Fibonacci sequence in composition",
                "mathematical_relationship": "Golden ratio",
                "story_theme": "Time travel"
            },
            {
                "musical_concept": "Polyrhythms",
                "mathematical_relationship": "Least common multiple",
                "story_theme": "Parallel universes"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a short story (200-300 words) that incorporates the musical concept of {t['musical_concept']}, the mathematical relationship of {t['mathematical_relationship']}, and the theme of {t['story_theme']}. Then, analyze the story's structure using music theory principles.

Your response should include:

1. Story Title (10 words or less)

2. Short Story (200-300 words):
   - Incorporate the given musical concept, mathematical relationship, and theme.
   - Use creative metaphors to represent musical and mathematical ideas.
   - Ensure the narrative is coherent and engaging.

3. Musical Analysis (100-150 words):
   - Explain how the musical concept is represented in the story's structure.
   - Describe any musical elements (e.g., rhythm, harmony, melody) used metaphorically.

4. Mathematical Connection (50-100 words):
   - Explain how the mathematical relationship is integrated into the story.
   - Describe any numerical patterns or proportions used in the narrative structure.

5. Synthesis (50-100 words):
   - Discuss how the integration of music, math, and narrative enhances the story's meaning or impact.

Ensure your response demonstrates a deep understanding of the musical concept, accurate application of the mathematical relationship, and creative storytelling that weaves these elements together coherently."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The story accurately incorporates the musical concept of {t['musical_concept']}.",
            f"The mathematical relationship of {t['mathematical_relationship']} is effectively integrated into the narrative.",
            f"The story adheres to the theme of {t['story_theme']}.",
            "The musical analysis demonstrates a deep understanding of music theory principles.",
            "The mathematical connection is clearly explained and relevant to the story's structure.",
            "The synthesis effectively ties together the musical, mathematical, and narrative elements.",
            "The response shows creativity and originality in its approach to the task."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
