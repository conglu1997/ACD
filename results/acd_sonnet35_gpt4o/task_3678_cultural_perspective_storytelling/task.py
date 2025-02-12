import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "theme": "Coming of age",
                "cultures": ["Japanese", "Nigerian", "Brazilian"],
                "ethical_dilemma": "Balancing individual desires with familial expectations"
            },
            {
                "theme": "Environmental crisis",
                "cultures": ["Inuit", "Australian Aboriginal", "Dutch"],
                "ethical_dilemma": "Preserving tradition vs. adapting to climate change"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a short story based on the theme '{t['theme']}' from the perspectives of characters from {', '.join(t['cultures'])} cultures. Then, analyze the story's ethical implications and cultural authenticity.

1. Story (400-500 words):
   Write a short story that incorporates the given theme and perspectives from the specified cultures. Ensure that each cultural perspective is represented authentically and sensitively. The story should also touch on the ethical dilemma: {t['ethical_dilemma']}.

2. Cultural Analysis (200-250 words):
   a) Explain how you incorporated elements from each culture into the story.
   b) Discuss any challenges you faced in representing these cultures authentically.
   c) Reflect on how the cultural backgrounds influence the characters' perspectives on the theme and ethical dilemma.

3. Ethical Implications (200-250 words):
   a) Analyze the ethical dilemma presented in the story.
   b) Discuss how different cultural perspectives might approach this dilemma.
   c) Reflect on the potential real-world implications of the ethical issues raised in the story.

4. Reflection on Cultural Sensitivity (150-200 words):
   a) Discuss the challenges of writing from multiple cultural perspectives.
   b) Reflect on the potential risks of cultural appropriation or misrepresentation in such an exercise.
   c) Suggest guidelines for respectfully incorporating diverse cultural elements in storytelling.

Ensure your response is creative, culturally sensitive, and demonstrates a nuanced understanding of the ethical implications involved. Use appropriate headings for each section of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The story effectively incorporates the theme '{t['theme']}' and perspectives from {', '.join(t['cultures'])} cultures.",
            "The cultural representations are authentic, sensitive, and avoid stereotypes.",
            f"The story and analysis thoughtfully address the ethical dilemma: {t['ethical_dilemma']}.",
            "The response demonstrates a nuanced understanding of cultural differences and ethical implications.",
            "The reflection on cultural sensitivity shows awareness of potential issues in cross-cultural storytelling."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
