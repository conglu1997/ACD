import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        composers = ['Schoenberg', 'Webern', 'Berg', 'Babbitt', 'Boulez']
        set_operations = ['transposition', 'inversion', 'retrograde', 'complementation']
        pitch_class_sets = [
            [0, 1, 4],  # 3-3 trichord
            [0, 1, 3, 7],  # 4-Z15 tetrachord
            [0, 1, 2, 6, 7],  # 5-7 pentachord
            [0, 1, 2, 3, 4, 5],  # 6-1 hexachord
        ]
        
        tasks = {
            "1": {
                "composer": random.choice(composers),
                "set_operation": random.choice(set_operations),
                "pitch_class_set": random.choice(pitch_class_sets)
            },
            "2": {
                "composer": random.choice(composers),
                "set_operation": random.choice(set_operations),
                "pitch_class_set": random.choice(pitch_class_sets)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze and manipulate a musical composition using set theory, focusing on the work of {t['composer']} and the {t['set_operation']} operation on the pitch class set {t['pitch_class_set']}. Your task involves the following steps:

1. Set Theory Basics (150-200 words):
   a) Explain the concept of pitch class sets in music theory.
   b) Describe how the {t['set_operation']} operation works in musical set theory.
   c) Discuss the significance of these concepts in {t['composer']}'s compositional style.

2. Mathematical Analysis (200-250 words):
   a) Represent the given pitch class set {t['pitch_class_set']} in standard form and prime form.
   b) Calculate the interval vector for this set.
   c) Apply the {t['set_operation']} operation to the set and show the resulting set.
   d) Determine if the original and transformed sets are related by transposition or inversion.

3. Musical Interpretation (200-250 words):
   a) Describe how the original pitch class set might be used in a composition by {t['composer']}.
   b) Explain how the {t['set_operation']} operation would affect the sound and structure of the music.
   c) Propose a short musical phrase that uses both the original and transformed sets.

4. Comparative Analysis (150-200 words):
   a) Compare the use of this pitch class set and operation to a different composer's approach.
   b) Discuss how this analysis reflects broader trends in 20th-century art music.

5. Creative Application (150-200 words):
   a) Propose an original composition technique that extends or combines set theory operations.
   b) Explain how this technique could be used to create new musical structures or expressions.

Ensure your response demonstrates a deep understanding of both music theory and mathematical set theory. Be precise in your mathematical calculations and creative in your musical interpretations. Use clear headings for each section and number your paragraphs within each section.

Your total response should be between 850-1100 words. Manage your time wisely to address all sections thoroughly."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately explains pitch class sets and the {t['set_operation']} operation in musical set theory",
            f"The mathematical analysis correctly represents the pitch class set {t['pitch_class_set']} in standard and prime form",
            f"The interval vector calculation and {t['set_operation']} operation are performed correctly",
            f"The musical interpretation demonstrates understanding of {t['composer']}'s style and the effects of set theory operations",
            "The comparative analysis shows knowledge of different compositional approaches in 20th-century art music",
            "An original composition technique extending set theory operations is proposed and explained",
            "The response demonstrates interdisciplinary knowledge of music theory and mathematics",
            "The ideas presented are creative while maintaining musical and mathematical accuracy",
            "The response is well-structured with clear headings and numbered paragraphs",
            "The total response falls within the specified word count range of 850-1100 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
