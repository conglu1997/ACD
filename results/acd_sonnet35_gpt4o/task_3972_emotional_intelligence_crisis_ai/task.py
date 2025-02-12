import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "crisis_type": "Natural disaster",
                "emotional_challenge": "Mass panic and fear",
                "ethical_dilemma": "Resource allocation"
            },
            {
                "crisis_type": "Hostage situation",
                "emotional_challenge": "Extreme stress and anxiety",
                "ethical_dilemma": "Negotiation tactics"
            },
            {
                "crisis_type": "Global pandemic",
                "emotional_challenge": "Widespread uncertainty and misinformation",
                "ethical_dilemma": "Individual freedom vs. public safety"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models and applies emotional intelligence in a high-stakes crisis management scenario. Your system should be capable of understanding and responding to complex human emotions while making critical decisions. Focus on the following scenario:

Crisis Type: {t['crisis_type']}
Emotional Challenge: {t['emotional_challenge']}
Ethical Dilemma: {t['ethical_dilemma']}

Your response should include:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for modeling emotional intelligence.
   b) Explain how your system integrates emotional understanding with decision-making processes.
   c) Detail how the system accounts for the specific emotional challenges of the given crisis scenario.
   d) Discuss any novel approaches or technologies used in your design.

2. Emotional Intelligence Model (250-300 words):
   a) Explain your approach to modeling emotional intelligence in an AI system.
   b) Describe how your system recognizes and interprets human emotions in high-stress situations.
   c) Discuss how your model accounts for cultural differences in emotional expression and interpretation.

3. Decision-Making Process (250-300 words):
   a) Outline the decision-making framework your AI uses in the given crisis scenario.
   b) Explain how emotional intelligence informs and influences the decision-making process.
   c) Provide an example of how your system would handle a specific situation within the given scenario.

4. Ethical Considerations (200-250 words):
   a) Analyze the ethical implications of using AI with emotional intelligence in crisis management.
   b) Address the specific ethical dilemma presented in the scenario.
   c) Propose guidelines for responsible development and use of emotionally intelligent AI in high-stakes situations.

5. Performance Evaluation (150-200 words):
   a) Suggest metrics to evaluate your AI system's performance in the given scenario.
   b) Describe a method for comparing your system's decisions with those of human experts.
   c) Discuss potential limitations of your approach and how they might be addressed.

6. Future Implications (150-200 words):
   a) Discuss the potential impact of emotionally intelligent AI on crisis management and decision-making.
   b) Explore how this technology might evolve and its potential applications in other fields.
   c) Consider long-term societal implications of AI systems with advanced emotional intelligence.

Ensure your response demonstrates a deep understanding of emotional intelligence, crisis management, and artificial intelligence. Use appropriate terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific and ethical plausibility.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should address the specific crisis type: {t['crisis_type']}",
            f"The AI system should handle the emotional challenge: {t['emotional_challenge']}",
            f"The ethical dilemma of {t['ethical_dilemma']} should be thoroughly discussed",
            "The AI system design should be innovative yet plausible",
            "The response should demonstrate a deep understanding of emotional intelligence and its application in AI",
            "The ethical considerations should be comprehensive and thoughtful"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
