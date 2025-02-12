import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            "Climate change treaty negotiation",
            "International trade dispute resolution",
            "Diplomatic crisis management",
            "Global health initiative coordination",
            "Multinational corporate merger mediation"
        ]
        cultures = [
            "Western",
            "East Asian",
            "Middle Eastern",
            "African",
            "Latin American"
        ]
        emotions = [
            "Trust",
            "Fear",
            "Optimism",
            "Frustration",
            "Pride"
        ]
        return {
            "1": {
                "scenario": random.choice(scenarios),
                "culture1": random.choice(cultures),
                "culture2": random.choice(cultures),
                "emotion1": random.choice(emotions),
                "emotion2": random.choice(emotions),
                "example_statement": "This proposal is completely unacceptable and shows a lack of respect for our position."
            },
            "2": {
                "scenario": random.choice(scenarios),
                "culture1": random.choice(cultures),
                "culture2": random.choice(cultures),
                "emotion1": random.choice(emotions),
                "emotion2": random.choice(emotions),
                "example_statement": "We appreciate your efforts, but we feel that this approach may not fully address our concerns."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can understand, generate, and translate emotionally nuanced language across different cultures, then use it to analyze and mediate a complex international negotiation scenario. Your task involves the following components:

1. Emotional-Linguistic Model (250-300 words):
   a) Describe the key components of your AI system for processing emotionally nuanced language.
   b) Explain how your model integrates emotional intelligence with linguistic analysis.
   c) Discuss how your system accounts for cultural differences in emotional expression and interpretation.
   d) Provide a brief example of how your system would process and translate this emotionally charged statement: "{t['example_statement']}"

2. Cross-Cultural Emotion Mapping (200-250 words):
   a) Explain how your system maps emotional concepts between {t['culture1']} and {t['culture2']} cultures.
   b) Describe any challenges in this mapping process and how your system addresses them.
   c) Discuss how your system handles emotions that may not have direct equivalents across cultures.

3. Negotiation Scenario Analysis (250-300 words):
   a) Analyze the given scenario: {t['scenario']}
   b) Explain how your AI system would identify and interpret the emotional undertones in the negotiation, particularly focusing on {t['emotion1']} and {t['emotion2']}.
   c) Describe how your system would generate culturally appropriate responses to de-escalate tensions and promote understanding.

4. Mediation Strategy (200-250 words):
   a) Outline a strategy for your AI system to mediate the negotiation, considering the cultural and emotional factors involved.
   b) Explain how your system would adapt its language and recommendations based on the emotional states of the parties.
   c) Discuss how your system would handle potential miscommunications or emotional escalations.

5. Ethical Considerations (150-200 words):
   a) Discuss the ethical implications of using AI for emotional analysis and mediation in high-stakes international scenarios.
   b) Address potential biases in your system and how you would mitigate them.
   c) Consider the impact of AI-mediated negotiations on human diplomacy and international relations.

6. Evaluation and Improvement (150-200 words):
   a) Propose a method to evaluate the effectiveness of your AI system in real-world negotiation scenarios.
   b) Suggest potential improvements or extensions to your system based on this evaluation.
   c) Discuss how your system could be adapted for other applications beyond international negotiations.

Ensure your response demonstrates a deep understanding of emotional intelligence, cross-cultural communication, and AI technologies. Use appropriate terminology from relevant fields and provide clear explanations for complex concepts. Be innovative in your approach while considering real-world applicability and limitations.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1200-1500 words. Include a word count for each section in parentheses at the end of the section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of emotional intelligence, cross-cultural communication, and AI technologies, particularly in the context of {t['scenario']}.",
            f"The proposed AI system effectively integrates emotional analysis with linguistic processing across {t['culture1']} and {t['culture2']} cultures.",
            f"The analysis of the negotiation scenario thoroughly considers both cultural and emotional factors, with a focus on {t['emotion1']} and {t['emotion2']}.",
            "The mediation strategy is well-reasoned, adaptable, and provides specific examples of how it would handle emotional escalations.",
            "Ethical considerations are thoughtfully addressed, including potential biases and impacts on human diplomacy, with concrete mitigation strategies proposed.",
            "The evaluation method and suggestions for improvement are practical, insightful, and demonstrate an understanding of real-world negotiation challenges.",
            "The response adheres to the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
