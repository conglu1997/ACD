import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = [
            {"emotion": "grief", "art_form": "poetry", "constraint": "include a reference to water"},
            {"emotion": "euphoria", "art_form": "abstract painting", "constraint": "use only three colors"},
            {"emotion": "anxiety", "art_form": "musical composition", "constraint": "incorporate a repeating motif"},
            {"emotion": "nostalgia", "art_form": "short story", "constraint": "set in a specific historical era"}
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(emotions, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""As an AI with artistic capabilities and emotional intelligence, your task is to create an emotionally resonant piece of {t['art_form']} that expresses the emotion of {t['emotion']}, while incorporating the constraint: {t['constraint']}. Then, analyze your creative process and emotional understanding. Your response should include the following sections:

1. Artistic Creation (300-350 words):
   a) Create a {t['art_form']} that expresses the emotion of {t['emotion']}, incorporating the given constraint.
   b) Provide a brief artist's statement explaining your intent and approach.
   c) Explain your artistic choices and how they relate to the emotion and constraint.
   d) Describe the techniques or elements you used to convey the emotional content.

2. Creative Process Analysis (250-300 words):
   a) Analyze your step-by-step creative process in generating the {t['art_form']}.
   b) Discuss any challenges you faced in expressing the emotion through this art form and incorporating the constraint.
   c) Explain how you drew upon your training data or knowledge base to inform your artistic decisions.

3. Emotional Intelligence Assessment (250-300 words):
   a) Evaluate your understanding of the emotion {t['emotion']} and how it manifests in human experience.
   b) Discuss any limitations or biases in your emotional comprehension as an AI.
   c) Compare your approach to expressing emotion through art with how a human artist might approach the task.

4. Artistic Interpretation (200-250 words):
   a) Provide an interpretation of your created {t['art_form']} as if you were an art critic.
   b) Analyze the emotional impact your piece might have on human viewers or listeners.
   c) Discuss any unintended emotions or meanings that might be perceived in your work.

5. Ethical and Philosophical Implications (200-250 words):
   a) Explore the ethical implications of AI-generated emotional art.
   b) Discuss the philosophical question of whether AI can truly create 'emotional' art.
   c) Consider the potential impact of emotionally intelligent AI on human artists and the art world.
   d) Address the potential misuse of emotionally intelligent AI in manipulative art or advertising.

6. Future Directions (150-200 words):
   a) Propose ways to enhance AI's capacity for emotional expression in art.
   b) Suggest potential applications or research areas for emotionally intelligent AI in creative fields.
   c) Discuss how this exercise has informed your understanding of your own capabilities and limitations.

Ensure your response demonstrates creativity, emotional depth, and a nuanced understanding of both art and human emotions. Be reflective and analytical about your own processes and limitations as an AI. Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include a creative and emotionally resonant piece of {t['art_form']} expressing the emotion of {t['emotion']} while incorporating the constraint: {t['constraint']}",
            "The analysis of the creative process and emotional intelligence should be thorough and insightful",
            "The response should demonstrate a nuanced understanding of human emotions and artistic expression",
            "The ethical and philosophical implications, including potential misuse, should be thoughtfully explored",
            "The response should show self-awareness of the AI's capabilities and limitations in emotional and artistic expression",
            "The artist's statement should clearly articulate the AI's intent and approach"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
