import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ancient_languages = [
            {
                "language": "Sumerian",
                "time_period": "3rd millennium BCE",
                "region": "Mesopotamia",
                "artifacts": ["cuneiform tablets", "cylinder seals"],
                "key_features": ["agglutinative morphology", "ergative-absolutive alignment"]
            },
            {
                "language": "Linear A",
                "time_period": "2nd millennium BCE",
                "region": "Minoan Crete",
                "artifacts": ["clay tablets", "votive figurines"],
                "key_features": ["undeciphered script", "possible syllabic writing system"]
            }
        ]
        return {str(i+1): lang for i, lang in enumerate(ancient_languages)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that reconstructs the ancient extinct language of {t['language']} from the {t['time_period']} in the region of {t['region']}, and uses it to create a futuristic communication protocol. Then, analyze its potential impact on linguistic diversity and global communication. Your response should include the following sections:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for language reconstruction and protocol creation.
   b) Explain how your system integrates techniques from computational linguistics, machine learning, and historical linguistics.
   c) Detail how your system handles the uncertainties and gaps in our knowledge of the ancient language.
   d) Provide a high-level diagram or pseudocode illustrating the main processes in your system.

2. Ancient Language Reconstruction (250-300 words):
   a) Outline the approach your AI system takes to reconstruct {t['language']}.
   b) Discuss how your system utilizes the available artifacts ({', '.join(t['artifacts'])}) in the reconstruction process.
   c) Explain how your system addresses the key linguistic features of {t['language']} ({', '.join(t['key_features'])}).
   d) Provide an example of a reconstructed word or phrase, with an explanation of the reconstruction process.

3. Futuristic Communication Protocol (250-300 words):
   a) Describe how your system develops a communication protocol based on the reconstructed language.
   b) Explain the key features of this protocol that make it suitable for futuristic communication.
   c) Discuss how this protocol incorporates or improves upon existing communication technologies.
   d) Provide an example of how a modern concept (e.g., 'artificial intelligence' or 'space travel') would be expressed using this protocol.

4. Cognitive and Linguistic Analysis (200-250 words):
   a) Analyze how the structures and concepts in the ancient language might influence the cognitive patterns in the new protocol.
   b) Discuss potential cognitive advantages or challenges of using this protocol for communication.
   c) Explore how this protocol might affect language acquisition and multilingualism.

5. Impact on Linguistic Diversity (200-250 words):
   a) Assess the potential impact of your system on global linguistic diversity.
   b) Discuss how the revival of an ancient language in a modern context might affect current language ecosystems.
   c) Propose strategies to ensure that this technology supports rather than diminishes linguistic diversity.

6. Ethical Implications (200-250 words):
   a) Discuss the ethical considerations of reconstructing and repurposing an extinct language.
   b) Analyze potential cultural and social impacts of introducing this communication protocol.
   c) Address concerns related to privacy, cultural appropriation, and potential misuse of the technology.

7. Future Applications and Research (150-200 words):
   a) Propose two potential applications of your system beyond communication protocols.
   b) Suggest areas for future research that could enhance our understanding of ancient languages or improve communication technologies.
   c) Discuss how this technology might evolve and its potential long-term effects on human communication and cognition.

Ensure your response demonstrates a deep understanding of linguistics, artificial intelligence, cognitive science, and communication theory. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your system design while maintaining scientific and technological plausibility.

Format your response with clear headings for each section and use numbered or bulleted lists where appropriate. Your total response should be between 1550-1900 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The AI System Architecture section must clearly explain how the system integrates techniques from computational linguistics, machine learning, and historical linguistics for reconstructing {t['language']}.",
            f"The Ancient Language Reconstruction section must provide a plausible approach to reconstructing {t['language']}, addressing key challenges specific to this language and utilizing the mentioned artifacts ({', '.join(t['artifacts'])}).",
            f"The Futuristic Communication Protocol section should describe an innovative protocol based on the reconstructed {t['language']}, with clear examples of its application to modern concepts.",
            "The Cognitive and Linguistic Analysis section must thoughtfully explore the potential cognitive impacts of using the new protocol, considering both advantages and challenges.",
            "The Impact on Linguistic Diversity and Ethical Implications sections should demonstrate a nuanced understanding of the potential consequences of this technology, including specific strategies and concerns.",
            "The overall response must showcase interdisciplinary knowledge integration, creativity, critical thinking, and ethical reasoning in the domains of linguistics, AI, cognitive science, and communication technology.",
            "The response must adhere to the specified word count range (1550-1900 words) and include a word count at the end."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
