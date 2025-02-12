import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        therapy_areas = [
            "Depression",
            "Anxiety",
            "Post-Traumatic Stress Disorder (PTSD)",
            "Obsessive-Compulsive Disorder (OCD)",
            "Eating Disorders"
        ]
        return {
            "1": {"therapy_area": random.choice(therapy_areas)},
            "2": {"therapy_area": random.choice(therapy_areas)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical AI-powered therapy chatbot that leverages psycholinguistic principles to improve its effectiveness in providing mental health support for {t['therapy_area']}. Your response should include:

1. Chatbot Overview (100-150 words):
   a) Provide a brief description of your AI therapy chatbot, including its primary functions and target user group.
   b) Explain how it integrates principles from both artificial intelligence and psycholinguistics.

2. Key Psycholinguistic Features (150-200 words):
   a) Describe three specific psycholinguistic principles or theories that your chatbot incorporates.
   b) For each principle, explain how it is implemented in the chatbot's language processing or generation algorithms.
   c) Discuss how these features could potentially enhance the therapeutic effectiveness of the chatbot.

3. Adaptive Language Techniques (100-150 words):
   a) Explain how your chatbot adapts its language use based on the user's linguistic patterns or emotional state.
   b) Provide an example dialogue showcasing this adaptation for a user dealing with {t['therapy_area']}.

4. Ethical Considerations (100-150 words):
   a) Identify two potential ethical concerns related to using AI for therapy in the context of {t['therapy_area']}.
   b) Propose safeguards or guidelines to address these concerns.

5. Evaluation Method (100-150 words):
   a) Describe a method to evaluate the effectiveness of your chatbot, focusing on both linguistic appropriateness and therapeutic outcomes.
   b) Explain how you would measure improvements in the user's mental health state.

Ensure your response demonstrates a deep understanding of both psycholinguistics and AI principles, as well as their potential applications in mental health therapy. Use appropriate terminology from both fields and provide clear, logical explanations throughout your design."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of psycholinguistic principles and their application in AI-powered therapy.",
            "The chatbot design incorporates specific, relevant psycholinguistic theories or concepts.",
            "The adaptive language techniques are well-explained and appropriate for the given therapy area.",
            "Ethical considerations are thoughtfully addressed with relevant safeguards proposed.",
            "The evaluation method effectively assesses both linguistic appropriateness and therapeutic outcomes.",
            "The overall response shows creativity, interdisciplinary knowledge integration, and logical coherence."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
