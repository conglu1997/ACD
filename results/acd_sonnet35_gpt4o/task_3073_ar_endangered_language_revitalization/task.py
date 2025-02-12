import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = ['Ainu', 'Cornish', 'Manx', 'Yurok', 'Livonian']
        ar_features = ['real-time translation', 'interactive storytelling', 'gamified learning', 'cultural context visualization', 'pronunciation feedback']
        application_contexts = ['education', 'tourism', 'community engagement', 'linguistic research', 'cultural events']
        
        tasks = {
            "1": {
                "language": random.choice(languages),
                "ar_feature": random.choice(ar_features),
                "context": random.choice(application_contexts)
            },
            "2": {
                "language": random.choice(languages),
                "ar_feature": random.choice(ar_features),
                "context": random.choice(application_contexts)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an augmented reality (AR) system for preserving and revitalizing the endangered {t['language']} language, focusing on the AR feature of {t['ar_feature']} in the context of {t['context']}. Then, analyze its potential impact on linguistic diversity and cultural preservation.

Augmented Reality (AR) technology overlays digital information onto the real world, typically through mobile devices or specialized glasses. For example, an AR language learning app might display virtual labels on real-world objects, allowing users to learn vocabulary in context.

As a brief example, for the Ainu language, a 'cultural context visualization' AR feature could overlay traditional Ainu patterns onto modern clothing when viewed through an AR device, helping learners understand the cultural significance of these designs in daily life.

Your response should include the following sections:

1. AR System Design (300-350 words):
   a) Describe the key components and functionalities of your AR system.
   b) Explain how the system implements the specified AR feature for language revitalization.
   c) Discuss how your design considers the unique characteristics of the {t['language']} language.
   d) Detail how the system would be used in the given context of {t['context']}.

2. Linguistic and Cultural Integration (275-325 words):
   a) Explain how your AR system incorporates linguistic principles for effective language learning and preservation.
   b) Describe how the system respects and promotes the cultural context of the {t['language']} language.
   c) Discuss any challenges in accurately representing the language and culture in an AR environment.

3. User Experience and Interaction (200-250 words):
   a) Describe the user interface and interaction methods of your AR system.
   b) Explain how the system caters to different user groups (e.g., native speakers, learners, researchers).
   c) Discuss how user feedback and progress are incorporated into the system.

4. Technical Implementation (225-275 words):
   a) Outline the key technologies and algorithms used in your AR system.
   b) Explain any novel approaches or adaptations required for the {t['language']} language.
   c) Discuss potential technical challenges and how you would address them.

5. Impact Analysis (275-325 words):
   a) Analyze the potential impact of your AR system on the preservation and revitalization of the {t['language']} language.
   b) Discuss broader implications for linguistic diversity and cultural preservation.
   c) Consider potential unintended consequences and how to mitigate them.

6. Ethical Considerations (175-225 words):
   a) Identify ethical challenges in using AR for language revitalization.
   b) Propose guidelines for responsible development and use of such technology.
   c) Discuss how to ensure community involvement and ownership in the process.

7. Future Developments (175-225 words):
   a) Suggest two potential extensions or improvements to your AR system.
   b) Discuss how this approach could be adapted for other endangered languages or cultural preservation efforts.
   c) Speculate on the long-term implications of AR technology in linguistic and cultural studies.

Ensure your response demonstrates a deep understanding of AR technology, linguistics, and cultural anthropology. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while considering practical implementation and ethical implications. Remember to balance creativity with feasibility and cultural sensitivity throughout your design.

Format your response with clear headings for each section. Your total response should be between 1625-1975 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of AR technology, linguistics, and cultural anthropology.",
            "The AR system design is innovative and well-suited for language revitalization.",
            "The approach effectively integrates linguistic principles and cultural context.",
            "The user experience and interaction design are well-considered and appropriate for different user groups.",
            "The technical implementation is feasible and addresses potential challenges.",
            "The impact analysis is thorough and considers both positive outcomes and potential issues.",
            "Ethical considerations are addressed comprehensively with appropriate guidelines proposed.",
            "Future developments and adaptations are innovative and well-reasoned.",
            "The response is well-structured, clear, and within the specified word count.",
            "The proposed system demonstrates creativity while maintaining practicality and cultural sensitivity."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
