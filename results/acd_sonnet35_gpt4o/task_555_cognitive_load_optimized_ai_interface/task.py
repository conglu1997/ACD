import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        interfaces = [
            "voice assistant",
            "chatbot",
            "visual programming environment",
            "augmented reality interface"
        ]
        user_profiles = [
            "elderly individual with mild cognitive impairment",
            "child with ADHD",
            "non-native English speaker with intermediate proficiency",
            "expert programmer with dyslexia"
        ]
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                "interface": random.choice(interfaces),
                "user_profile": random.choice(user_profiles)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI-powered {t['interface']} that minimizes cognitive load for a {t['user_profile']}. Your task is to apply psycholinguistic principles to create an intuitive and efficient interface. Follow these steps:

1. Interface Design (200-250 words):
   a) Describe the key features of your {t['interface']}.
   b) Explain how you've applied at least three psycholinguistic principles to reduce cognitive load.
   c) Discuss how your design accommodates the specific needs of a {t['user_profile']}.

2. Cognitive Load Analysis (150-200 words):
   a) Identify potential sources of cognitive load in traditional interfaces for this user.
   b) Explain how your design mitigates each of these sources.
   c) Discuss any trade-offs you made between reducing cognitive load and maintaining functionality.

3. Linguistic Considerations (100-150 words):
   a) Describe the linguistic features of your interface (e.g., vocabulary, syntax, discourse structure).
   b) Explain how these features are optimized for the user's cognitive profile.
   c) Provide an example of how the interface might rephrase a complex request into a more cognitively manageable form.

4. Evaluation Metrics (100-150 words):
   a) Propose three quantitative metrics to assess the cognitive load of your interface.
   b) Describe a qualitative method to gather user feedback on cognitive ease of use.
   c) Explain how you would use these metrics to iteratively improve your design.

5. Ethical Considerations (100-150 words):
   a) Discuss potential ethical implications of optimizing interfaces for cognitive load.
   b) Address concerns about privacy, data collection, or potential cognitive dependencies.
   c) Propose guidelines for responsible development and use of cognitive-load-optimized AI interfaces.

6. Comparative Analysis (100-150 words):
   a) Compare your cognitive-load-optimized interface with a standard interface for the same purpose.
   b) Predict potential challenges in user adoption and propose solutions.

Ensure your response demonstrates a deep understanding of cognitive science, psycholinguistics, and human-computer interaction. Be creative in your design while maintaining scientific plausibility and ethical considerations.

Format your response with clear headings for each section (e.g., '1. Interface Design', '2. Cognitive Load Analysis', etc.). Include a brief summary (50-75 words) at the end, highlighting the key innovations of your design."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The design effectively addresses the needs of a {t['user_profile']}.",
            "The response demonstrates a deep understanding of cognitive load and psycholinguistic principles.",
            "The interface design is creative, plausible, and well-explained.",
            "The cognitive load analysis is thorough and insightful.",
            "The proposed evaluation metrics and ethical considerations are thoughtful and relevant.",
            "The comparative analysis provides meaningful insights.",
            "The response follows the required format with clear headings and a summary."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
