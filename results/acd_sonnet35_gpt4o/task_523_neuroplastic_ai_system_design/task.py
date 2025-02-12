import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        problems = [
            "Climate change adaptation",
            "Personalized medicine",
            "Urban traffic management",
            "Language learning optimization",
            "Disaster response coordination"
        ]
        return {
            "1": {"problem": random.choice(problems)},
            "2": {"problem": random.choice(problems)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that mimics neuroplasticity and apply it to solve the complex real-world problem of {t['problem']}. Your response should include:

1. Neuroplasticity Mechanism (200-250 words):
   a) Explain the key principles of neuroplasticity you'll incorporate into your AI system.
   b) Describe how these principles will be translated into AI algorithms or architectures.
   c) Discuss how your system will adapt and learn over time, similar to the human brain.

2. System Architecture (250-300 words):
   a) Provide a high-level overview of your AI system's architecture.
   b) Explain how each component contributes to the system's neuroplastic capabilities.
   c) Describe the data inputs, processing mechanisms, and outputs of your system.
   d) Discuss how your system maintains stability while allowing for flexibility and adaptation.

3. Application to {t['problem']} (200-250 words):
   a) Explain how your neuroplastic AI system would approach solving this problem.
   b) Describe specific advantages your system would have over traditional AI approaches.
   c) Discuss potential challenges in applying your system to this problem and how you'd address them.

4. Learning and Adaptation Demonstration (150-200 words):
   a) Provide a specific scenario related to {t['problem']} that would require your system to adapt.
   b) Walk through how your system would learn and change its approach in response to this scenario.
   c) Explain how this adaptation reflects neuroplastic principles.

5. Ethical Considerations (150-200 words):
   a) Identify at least two ethical concerns raised by your neuroplastic AI system.
   b) Propose guidelines or safeguards to address these ethical issues.
   c) Discuss the broader implications of AI systems that can adapt and learn like biological brains.

6. Future Directions (100-150 words):
   a) Suggest two potential improvements or extensions to your system.
   b) Propose a research question that could further the development of neuroplastic AI systems.

Ensure your response demonstrates a deep understanding of both neuroscience and artificial intelligence principles. Be creative in your system design while maintaining scientific plausibility and addressing real-world applicability."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroplasticity principles and their application to AI.",
            "The proposed AI system architecture is innovative, well-explained, and plausibly mimics neuroplasticity.",
            "The application to the given problem is thoughtful and leverages the unique capabilities of the neuroplastic AI system.",
            "The learning and adaptation demonstration effectively illustrates the system's neuroplastic properties.",
            "Ethical considerations are thoroughly explored with relevant guidelines proposed.",
            "The response shows creativity and interdisciplinary thinking throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
