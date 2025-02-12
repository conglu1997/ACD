import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "culture": "Maya",
                "artifact_type": "hieroglyphic texts",
                "preservation_challenge": "climate change",
                "time_period": "Classic Period (250-900 CE)"
            },
            "2": {
                "culture": "Indus Valley",
                "artifact_type": "urban planning systems",
                "preservation_challenge": "rapid urbanization",
                "time_period": "Mature Harappan phase (2600-1900 BCE)"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that reconstructs and preserves lost or endangered cultural heritage of the {t['culture']} civilization from the {t['time_period']}, focusing on {t['artifact_type']} and addressing the preservation challenge of {t['preservation_challenge']}. Your response should include:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for cultural reconstruction and preservation.
   b) Explain how the system integrates knowledge from archaeology, machine learning, and cultural anthropology.
   c) Detail how the AI processes and analyzes archaeological data to reconstruct cultural elements.
   d) Include a brief diagram (described in text) illustrating the main features of your system.
   e) Discuss any novel approaches or technologies used in your design.
   f) Provide a specific example of how your system would process a piece of archaeological data.

2. Cultural Reconstruction Methodology (250-300 words):
   a) Explain the specific methods your AI uses to reconstruct {t['artifact_type']} of the {t['culture']} civilization.
   b) Describe how the system handles incomplete or ambiguous archaeological data.
   c) Discuss how the AI ensures accuracy and authenticity in its reconstructions.
   d) Address potential biases in the reconstruction process and how the AI mitigates them.
   e) Provide a case study of how your system would reconstruct a specific {t['artifact_type']} from the {t['time_period']}.

3. Preservation Strategies (200-250 words):
   a) Detail how your AI system addresses the challenge of {t['preservation_challenge']}.
   b) Explain any innovative preservation techniques employed by the system.
   c) Discuss how the AI adapts its preservation strategies to changing environmental or social conditions.
   d) Describe how the system ensures long-term accessibility and relevance of the preserved cultural heritage.
   e) Provide an example of how your system would preserve a specific artifact against the threat of {t['preservation_challenge']}.

4. Ethical Implications (200-250 words):
   a) Identify at least three ethical concerns raised by this technology.
   b) Discuss the potential impact on indigenous communities and their rights to cultural heritage.
   c) Address the ethics of AI interpretation and potential misrepresentation of cultural elements.
   d) Propose guidelines for responsible development and use of AI in cultural heritage reconstruction and preservation.
   e) Describe a scenario where an ethical dilemma might arise and how your system would address it.

5. Societal Impact (150-200 words):
   a) Analyze how this technology might change our understanding and appreciation of ancient cultures.
   b) Discuss potential educational and cultural implications of widespread access to reconstructed heritage.
   c) Consider how it might affect archaeological practices and cultural preservation policies.
   d) Provide an example of a potential positive and negative societal impact of your system.

6. Future Developments (150-200 words):
   a) Propose two potential advancements or extensions of your AI system.
   b) Suggest areas for future research to enhance the system's capabilities and cultural sensitivity.
   c) Speculate on how this technology might evolve over the next few decades and its potential applications beyond archaeology.
   d) Describe a potential future scenario where your system could be applied in an unexpected field.

Ensure your response demonstrates a deep understanding of archaeology, artificial intelligence, and cultural anthropology. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and addressing ethical concerns.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1250-1550 words.

You have 45 minutes to complete this task. Good luck!"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of archaeology, artificial intelligence, and cultural anthropology.",
            "The AI system design is innovative and addresses the specific cultural reconstruction and preservation challenges.",
            "The response adequately addresses ethical implications and proposes responsible guidelines.",
            "The analysis of societal impact and future developments is insightful and well-reasoned.",
            f"The solution effectively addresses the preservation challenge of {t['preservation_challenge']}.",
            f"The cultural reconstruction methodology is well-suited for {t['artifact_type']} of the {t['culture']} civilization from the {t['time_period']}.",
            "The response includes specific examples and case studies as requested in the instructions.",
            "The proposed system demonstrates adaptability to changing conditions and potential future applications.",
            "The ethical considerations are thorough and include a relevant scenario addressing a potential dilemma.",
            "The response is well-structured, within the specified word count, and addresses all required points in the instructions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
