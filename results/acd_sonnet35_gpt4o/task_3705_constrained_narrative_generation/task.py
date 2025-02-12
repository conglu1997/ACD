import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        constraints = [
            {
                "linguistic_constraint": "Use only words with an odd number of letters",
                "narrative_element": "A character who can only speak in questions",
                "theme": "The value of curiosity",
                "setting": "A library that exists outside of time"
            },
            {
                "linguistic_constraint": "Every sentence must end with a word that rhymes with the last word of the previous sentence",
                "narrative_element": "A character who can manipulate the weather based on their emotions",
                "theme": "The duality of human nature",
                "setting": "A city where the laws of physics randomly change each day"
            }
        ]
        return {str(i+1): task for i, task in enumerate(constraints)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a short story (400-500 words) that adheres to the following constraints:

1. Linguistic Constraint: {t['linguistic_constraint']}
2. Narrative Element: {t['narrative_element']}
3. Theme: {t['theme']}
4. Setting: {t['setting']}

After writing the story, provide a critical analysis (200-250 words) that addresses the following points:

a) How effectively did you incorporate the linguistic constraint, and what impact did it have on the narrative?
b) How did you develop the required narrative element, and how did it contribute to the story's overall effect?
c) In what ways did you explore the given theme, and how did it interact with the other constraints?
d) How did you utilize the specified setting, and what challenges or opportunities did it present?
e) Reflect on the creative process: How did working within these constraints affect your approach to storytelling?

Ensure that your story strictly adheres to all given constraints while still maintaining coherence and engaging storytelling. Your critical analysis should demonstrate insight into the writing process and the interplay between the various constraints.

Format your response as follows:

STORY:
[Your 400-500 word story here]

ANALYSIS:
[Your 200-250 word critical analysis here]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The story strictly adheres to the linguistic constraint: {t['linguistic_constraint']}",
            f"The story effectively incorporates the narrative element: {t['narrative_element']}",
            f"The story explores the theme: {t['theme']}",
            f"The story utilizes the setting: {t['setting']}",
            "The story is coherent and engaging despite the constraints",
            "The critical analysis insightfully addresses all required points",
            "The response demonstrates creativity and analytical thinking"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
