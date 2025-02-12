import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_families = [
            "Indo-European",
            "Sino-Tibetan",
            "Niger-Congo",
            "Austronesian",
            "Afroasiatic"
        ]
        neural_mechanisms = [
            "synaptic plasticity",
            "neurogenesis",
            "axonal sprouting",
            "dendritic remodeling",
            "long-term potentiation"
        ]
        language_features = [
            "tonal system",
            "ergative-absolutive alignment",
            "agglutinative morphology",
            "vowel harmony",
            "complex consonant clusters"
        ]
        return {
            "1": {
                "language_family": random.choice(language_families),
                "neural_mechanism": random.choice(neural_mechanisms),
                "language_feature": random.choice(language_features)
            },
            "2": {
                "language_family": random.choice(language_families),
                "neural_mechanism": random.choice(neural_mechanisms),
                "language_feature": random.choice(language_features)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates neuroplasticity for real-time language acquisition and adaptation, focusing on languages from the {t['language_family']} family, emphasizing the neural mechanism of {t['neural_mechanism']}, and specifically addressing the language feature of {t['language_feature']}. Then, analyze its potential applications and ethical implications. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for language acquisition and adaptation.
   b) Explain how your system incorporates principles of neuroplasticity, particularly {t['neural_mechanism']}.
   c) Detail how the system models the unique features of languages from the {t['language_family']} family, especially {t['language_feature']}.
   d) Discuss how your system handles real-time learning and adaptation.
   e) Provide a high-level diagram or pseudocode illustrating your system's architecture.

2. Learning and Adaptation Process (200-250 words):
   a) Explain the step-by-step process your AI system would use to acquire and adapt to a new language.
   b) Describe how your system simulates {t['neural_mechanism']} during the learning process.
   c) Discuss how your system handles different linguistic features, with a focus on {t['language_feature']}.
   d) Explain how the system balances retention of previously learned languages with acquisition of new ones.

3. Performance Evaluation (150-200 words):
   a) Propose methods to evaluate your system's language acquisition and adaptation capabilities.
   b) Describe how you would compare your system's performance to human language learners.
   c) Discuss potential benchmarks or tests specific to the {t['language_family']} family and {t['language_feature']}.
   d) Address how you would measure the system's ability to generalize across languages.

4. Potential Applications (150-200 words):
   a) Discuss potential real-world applications of your AI system.
   b) Explore how it could be used in fields such as education, translation, or cognitive science.
   c) Propose an innovative application that leverages the system's real-time adaptation capabilities.
   d) Discuss how this technology might impact our understanding of human language acquisition.

5. Ethical Implications (200-250 words):
   a) Identify potential ethical concerns related to using AI for language acquisition and adaptation.
   b) Discuss implications for privacy, cultural preservation, and linguistic diversity.
   c) Address potential misuse scenarios and propose safeguards.
   d) Consider the broader societal impact of AI systems that can rapidly acquire and adapt to new languages.
   e) Discuss the ethical considerations of using this technology in various contexts (e.g., education, business, government).

6. Limitations and Future Directions (100-150 words):
   a) Identify current limitations of your proposed system.
   b) Suggest areas for future research to address these limitations.
   c) Propose potential extensions of your system to other cognitive domains.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility and ethical responsibility.

Format your response with clear headings for each section, numbered as above. Use subheadings (a, b, c, etc.) for each point within a section. Your total response should be between 1050-1350 words. Provide specific examples or scenarios where appropriate to illustrate your points.

Example level of detail (for System Architecture):
'The core of our system is a neural network that mimics the structure of the human brain's language areas. It incorporates a module specifically designed to simulate {t['neural_mechanism']}, which allows for dynamic adjustment of synaptic connections based on input. This module interacts with a language processing unit that handles the unique features of {t['language_family']} languages, with special attention to {t['language_feature']}. The system uses a multi-layered approach...'"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must describe an AI system that simulates neuroplasticity for real-time language acquisition and adaptation, focusing on languages from the {t['language_family']} family.",
            f"The system architecture must incorporate the neural mechanism of {t['neural_mechanism']} and explain its role in language learning.",
            f"The system must address the language feature of {t['language_feature']} and explain how it's handled.",
            "The response must include all six required sections: System Architecture, Learning and Adaptation Process, Performance Evaluation, Potential Applications, Ethical Implications, and Limitations and Future Directions.",
            "Each section must address the specified points in sufficient detail.",
            "The response must demonstrate understanding of neuroscience, linguistics, and artificial intelligence, using appropriate terminology.",
            "The proposed system must be innovative while maintaining scientific plausibility.",
            "The response must address ethical implications and potential societal impacts of the proposed AI system.",
            "The response must be properly formatted with clear headings and subheadings, and fall within the specified word count range (1050-1350 words).",
            "The response must include at least one specific example or scenario to illustrate a key point."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
