import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_functions = [
            "memory consolidation",
            "attention control",
            "language processing",
            "decision making",
            "emotional regulation"
        ]
        ethical_concerns = [
            "privacy and data security",
            "cognitive liberty and autonomy",
            "social inequality and access",
            "identity and authenticity",
            "long-term neuroplasticity effects"
        ]
        return {
            "1": {
                "cognitive_function": random.choice(cognitive_functions),
                "ethical_concern": random.choice(ethical_concerns)
            },
            "2": {
                "cognitive_function": random.choice(cognitive_functions),
                "ethical_concern": random.choice(ethical_concerns)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neural interface system for enhancing {t['cognitive_function']} in humans. Your task has five parts:

1. System Architecture (250-300 words):
   a) Describe the overall structure and components of your neural interface system.
   b) Explain how it interfaces with the brain to enhance {t['cognitive_function']}.
   c) Detail the key technologies involved and any novel approaches you're proposing.

2. Neuroscientific Basis (200-250 words):
   a) Explain the neuroscientific principles underlying your system's approach to enhancing {t['cognitive_function']}.
   b) Discuss how your system interacts with relevant brain regions and neural circuits.
   c) Address potential challenges in maintaining brain plasticity and avoiding unintended effects on other cognitive functions.

3. Data Processing and AI Integration (200-250 words):
   a) Describe how your system processes neural signals and translates them into cognitive enhancement.
   b) Explain any AI algorithms or machine learning techniques used in your system.
   c) Discuss how your system adapts to individual users and optimizes performance over time.

4. Ethical Implications (200-250 words):
   a) Analyze the ethical implications of your system, particularly focusing on {t['ethical_concern']}.
   b) Propose safeguards or guidelines to address these ethical concerns.
   c) Discuss potential societal impacts of widespread adoption of your technology.

5. Future Developments and Challenges (150-200 words):
   a) Predict potential future advancements that could improve your system.
   b) Identify major technical or ethical challenges that need to be overcome.
   c) Propose a framework for ongoing assessment and regulation of neuroenhancement technologies.

Ensure your response demonstrates a deep understanding of neuroscience, AI, and neuroethics. Be innovative in your approach while maintaining scientific plausibility and ethical responsibility. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should demonstrate a clear understanding of {t['cognitive_function']} and how it could be enhanced through a neural interface.",
            f"The ethical implications, particularly regarding {t['ethical_concern']}, should be thoroughly addressed.",
            "The proposed system should be innovative yet scientifically plausible.",
            "The response should show interdisciplinary knowledge of neuroscience, AI, and ethics.",
            "The future developments and challenges should be insightful and well-reasoned."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
