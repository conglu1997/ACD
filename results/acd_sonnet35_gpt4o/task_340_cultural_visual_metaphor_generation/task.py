import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            "time", "love", "justice", "knowledge", "power",
            "freedom", "peace", "change", "balance", "unity"
        ]
        cultures = [
            "Japanese", "Indian", "Nigerian", "Brazilian", "Egyptian",
            "Russian", "Mexican", "Australian Aboriginal", "Canadian", "Turkish"
        ]
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                "concept": random.choice(concepts),
                "culture": random.choice(cultures)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a culturally-appropriate visual metaphor for the abstract concept of '{t['concept']}' within the context of {t['culture']} culture. Follow these steps:

1. Visual Metaphor Creation (150-200 words):
   a) Describe a vivid and original visual metaphor that represents the concept.
   b) Ensure the metaphor is culturally appropriate and resonates with {t['culture']} cultural elements.
   c) Explain how specific visual elements in your metaphor relate to the abstract concept.

2. Cultural Context (100-150 words):
   a) Explain how your visual metaphor incorporates {t['culture']} cultural symbols, traditions, or beliefs.
   b) Discuss any potential cultural sensitivities or considerations in your metaphor.

3. Linguistic Expression (100-150 words):
   a) Provide a poetic or prose description of your visual metaphor in the style of {t['culture']} literary traditions.
   b) Use culturally-specific imagery, idioms, or expressions in your description.

4. Comparative Analysis (100-150 words):
   a) Briefly compare how this concept might be visually represented in two other cultures.
   b) Explain how these representations might differ from your {t['culture']} visual metaphor.

5. Reflection (50-100 words):
   Discuss how creating this culturally-specific visual metaphor challenges or expands conventional understandings of the concept.

Ensure your response is creative, culturally sensitive, and demonstrates a deep understanding of both the abstract concept and the cultural context."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The visual metaphor is original, vivid, and appropriate for {t['culture']} culture.",
            f"The metaphor accurately represents the concept of {t['concept']}.",
            "The response demonstrates deep cultural understanding and sensitivity.",
            "The linguistic expression effectively uses culturally-specific elements.",
            "The comparative analysis and reflection show insightful cross-cultural understanding."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
