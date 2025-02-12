import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        threat_types = [
            "phishing attempt",
            "social engineering",
            "insider threat",
            "data exfiltration"
        ]
        communication_channels = [
            "email",
            "instant messaging",
            "social media posts",
            "internal memos"
        ]
        linguistic_features = [
            "urgency indicators",
            "unusual jargon",
            "emotional manipulation",
            "inconsistent language patterns"
        ]
        
        return {
            "1": {
                "threat_type": random.choice(threat_types),
                "communication_channel": random.choice(communication_channels),
                "linguistic_feature": random.choice(linguistic_features)
            },
            "2": {
                "threat_type": random.choice(threat_types),
                "communication_channel": random.choice(communication_channels),
                "linguistic_feature": random.choice(linguistic_features)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a natural language processing system to detect potential {t['threat_type']} in {t['communication_channel']}, with a focus on analyzing {t['linguistic_feature']}. Your response should include:\n\n1. System Architecture (250-300 words):\n   a) Describe the key components of your NLP system for cybersecurity threat detection.\n   b) Explain how these components interact to process and analyze text.\n   c) Discuss any specific algorithms or models you would use (e.g., named entity recognition, sentiment analysis, etc.).\n   d) Include a high-level diagram or pseudocode to illustrate your system's architecture.\n\n2. Linguistic Feature Analysis (200-250 words):\n   a) Explain in detail how your system would detect and analyze the specified linguistic feature.\n   b) Provide examples of patterns or indicators your system would look for.\n   c) Discuss how this feature relates to the specified threat type.\n\n3. Threat Detection Process (200-250 words):\n   a) Outline the step-by-step process your system would use to identify potential threats.\n   b) Explain how your system would differentiate between normal and suspicious communications.\n   c) Describe any thresholds or scoring mechanisms used to flag potential threats.\n\n4. Adaptation to Communication Channel (150-200 words):\n   a) Discuss how your system would be tailored to the specific communication channel.\n   b) Explain any challenges or opportunities presented by this channel.\n   c) Describe how your system would handle channel-specific features (e.g., email headers, social media metadata).\n\n5. False Positive Mitigation (150-200 words):\n   a) Propose strategies to reduce false positives in threat detection.\n   b) Discuss how your system would balance sensitivity with specificity.\n   c) Describe any human-in-the-loop components for verification.\n\n6. Ethical Considerations and Limitations (150-200 words):\n   a) Discuss potential privacy concerns and how they would be addressed.\n   b) Explain any limitations of your approach and areas for future improvement.\n   c) Consider potential unintended consequences or misuses of the system.\n\nEnsure your response demonstrates a deep understanding of both NLP techniques and cybersecurity principles. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility and practical applicability.\n\nYour total response should be between 1100-1400 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both NLP techniques and cybersecurity principles.",
            "The system architecture is well-designed and clearly explained, with appropriate use of NLP and cybersecurity concepts.",
            "The linguistic feature analysis is thorough and relevant to the specified threat type.",
            "The threat detection process is logical and well-explained.",
            "The system is appropriately adapted to the specified communication channel.",
            "Strategies for false positive mitigation are thoughtful and practical.",
            "Ethical considerations are thoroughly addressed.",
            "The overall response is well-structured, clear, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
