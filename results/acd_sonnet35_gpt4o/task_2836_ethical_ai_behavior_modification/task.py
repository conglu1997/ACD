import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        behavior_targets = [
            "Improving sleep habits",
            "Reducing procrastination",
            "Enhancing emotional regulation",
            "Promoting sustainable lifestyle choices",
            "Increasing physical activity"
        ]
        psychological_principles = [
            "Operant conditioning",
            "Cognitive restructuring",
            "Mindfulness-based interventions",
            "Social learning theory",
            "Motivational interviewing"
        ]
        ethical_frameworks = [
            "Utilitarianism",
            "Deontological ethics",
            "Virtue ethics",
            "Care ethics",
            "Principlism"
        ]
        
        tasks = {
            "1": {
                "behavior_target": random.choice(behavior_targets),
                "psychological_principle": random.choice(psychological_principles),
                "ethical_framework": random.choice(ethical_frameworks)
            },
            "2": {
                "behavior_target": random.choice(behavior_targets),
                "psychological_principle": random.choice(psychological_principles),
                "ethical_framework": random.choice(ethical_frameworks)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system for personalized behavior modification targeting {t['behavior_target']}. Your system should incorporate the psychological principle of {t['psychological_principle']} and address ethical considerations using the framework of {t['ethical_framework']}. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the overall structure and components of your AI behavior modification system.
   b) Explain how your system incorporates the specified psychological principle.
   c) Detail the data collection, analysis, and intervention methods used by your system.
   d) Discuss how your system adapts its approach based on individual user responses and progress.

2. Psychological Mechanism (250-300 words):
   a) Explain in depth how your system applies the given psychological principle to influence behavior.
   b) Discuss potential cognitive and emotional impacts of your system on users.
   c) Describe how your system accounts for individual differences in personality, motivation, and learning styles.

3. Ethical Considerations (250-300 words):
   a) Analyze the ethical implications of your system using the specified ethical framework.
   b) Discuss potential risks or negative consequences of your system and how you address them.
   c) Explain how your system ensures user autonomy, informed consent, and the right to discontinue use.
   d) Describe safeguards implemented to protect user privacy and prevent misuse of personal data.

4. Technological Implementation (200-250 words):
   a) Outline the key algorithms or AI techniques used in your system (e.g., machine learning, natural language processing, recommendation systems).
   b) Explain how your system integrates with users' daily lives (e.g., through smartphones, wearables, smart home devices).
   c) Discuss any novel technological approaches you've incorporated to enhance the system's effectiveness.

5. User Interaction Example (150-200 words):
   Provide a concrete example of how your system would interact with a user over the course of a day or week, illustrating key features and intervention strategies.

6. Evaluation and Improvement (200-250 words):
   a) Propose methods for evaluating the effectiveness and safety of your system.
   b) Describe how you would collect and analyze user feedback to improve the system.
   c) Propose a novel metric for measuring the system's effectiveness that goes beyond traditional behavioral outcomes.
   d) Discuss potential long-term societal impacts of widespread adoption of your system.

7. Unintended Consequences and Limitations (250-300 words):
   a) Critically analyze potential unintended consequences or negative impacts of your system on individuals and society.
   b) Propose a detailed mitigation strategy for one of the unintended consequences you've identified.
   c) Acknowledge the limitations of your current system design.
   d) Suggest areas for future research or improvement.
   e) Discuss how your system might be adapted for other behavior modification targets.

8. Cross-Cultural Considerations (200-250 words):
   a) Analyze potential challenges in implementing your system across different cultural contexts.
   b) Discuss how your system could be adapted to respect and accommodate diverse cultural values and norms.
   c) Propose strategies for ensuring cultural sensitivity and avoiding cultural biases in your system's design and implementation.

Ensure your response demonstrates a deep understanding of psychological principles, ethical reasoning, AI technologies, and cross-cultural awareness. Be creative in your approach while maintaining scientific plausibility and ethical responsibility. Your total response should be between 1800-2200 words. Adhere to the specified word count for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all eight required sections with appropriate detail and adheres to the specified word count for each section.",
            f"The system architecture effectively incorporates the psychological principle of {t['psychological_principle']} for the behavior target of {t['behavior_target']}.",
            f"The ethical considerations are thoroughly analyzed using the framework of {t['ethical_framework']}.",
            "The technological implementation is well-explained and integrates AI techniques appropriately.",
            "The user interaction example is concrete, illustrative, and aligns with the proposed system design.",
            "The response demonstrates creativity, interdisciplinary knowledge integration, and critical thinking in addressing the complex challenge of ethical AI-based behavior modification.",
            "The proposed system is practical, innovative, and shows potential for real-world application.",
            "The response includes a novel and well-justified metric for measuring the system's effectiveness.",
            "The analysis of unintended consequences and limitations demonstrates deep critical thinking and awareness of potential negative impacts.",
            "The proposed mitigation strategy for an unintended consequence is detailed and feasible.",
            "The cross-cultural considerations demonstrate awareness of diverse perspectives and propose culturally sensitive adaptations.",
            "The limitations, potential risks, and future directions are thoughtfully discussed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
