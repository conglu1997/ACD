import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            "Japanese",
            "Nigerian (Yoruba)",
            "Mexican",
            "Russian",
            "Australian Aboriginal",
            "Indian (Hindi)"
        ]
        linguistic_features = [
            "idioms",
            "metaphors",
            "politeness levels",
            "non-verbal cues",
            "proverbs",
            "humor"
        ]
        ai_techniques = [
            "neural machine translation",
            "sentiment analysis",
            "natural language generation",
            "knowledge graphs",
            "reinforcement learning",
            "few-shot learning"
        ]
        tasks = [
            {
                "culture": random.choice(cultures),
                "linguistic_feature": random.choice(linguistic_features),
                "ai_technique": random.choice(ai_techniques)
            },
            {
                "culture": random.choice(cultures),
                "linguistic_feature": random.choice(linguistic_features),
                "ai_technique": random.choice(ai_techniques)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can analyze and generate culturally-specific communication patterns, focusing on the following elements:

1. Culture: {t['culture']}
2. Linguistic Feature: {t['linguistic_feature']}
3. AI Technique: {t['ai_technique']}

Your task consists of the following steps:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system and how they interact.
   b) Explain how your system incorporates cultural knowledge and linguistic analysis.
   c) Discuss how the specified AI technique is utilized in your system's design.
   d) Include a simple diagram or flowchart of your system's architecture.

2. Data Collection and Analysis (200-250 words):
   a) Describe the types of data your system would need to accurately model the specified culture and linguistic feature.
   b) Explain how your system would collect and process this data.
   c) Discuss any challenges in obtaining or analyzing culturally-specific linguistic data.

3. Cultural-Linguistic Modeling (200-250 words):
   a) Explain how your system models the relationship between culture and the specified linguistic feature.
   b) Describe any novel algorithms or methods your system employs for this modeling.
   c) Discuss how your system ensures cultural authenticity and avoids stereotyping.

4. Generation and Analysis Capabilities (200-250 words):
   a) Describe how your system generates culturally-appropriate examples of the specified linguistic feature.
   b) Explain how your system analyzes and interprets these features in natural language.
   c) Provide an example output from your system, demonstrating its capabilities.

5. Cross-Cultural Application (150-200 words):
   a) Discuss how your system could be adapted to other cultures and linguistic features.
   b) Explain any challenges in scaling your system across diverse cultures and languages.
   c) Propose a method for evaluating the system's performance across different cultures.

6. Ethical Considerations and Bias Mitigation (150-200 words):
   a) Identify potential ethical issues in developing an AI system that models cultural-linguistic patterns.
   b) Discuss how your system addresses issues of bias, cultural appropriation, and misrepresentation.
   c) Propose guidelines for the responsible development and use of such systems.

Ensure your response demonstrates a deep understanding of linguistics, cultural anthropology, and artificial intelligence. Use appropriate terminology from each field and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific and practical plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively addresses the cultural context of {t['culture']}, the linguistic feature of {t['linguistic_feature']}, and the AI technique of {t['ai_technique']}.",
            "The system architecture is well-designed and clearly explained, with a coherent integration of cultural knowledge and linguistic analysis.",
            "The data collection and analysis approach is comprehensive and appropriate for the given culture and linguistic feature.",
            "The cultural-linguistic modeling approach is innovative and effectively balances accuracy with respect for cultural nuances.",
            "The generation and analysis capabilities are well-explained and demonstrated with a relevant example.",
            "The cross-cultural application discussion is thoughtful and addresses key challenges.",
            "Ethical considerations are thoroughly addressed, with appropriate guidelines for responsible use.",
            "The response demonstrates a deep understanding of linguistics, cultural anthropology, and artificial intelligence throughout.",
            "The response is creative while maintaining scientific and practical plausibility.",
            "The response follows the specified format and is within the 1150-1450 word range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
