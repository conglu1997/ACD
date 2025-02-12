import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        synesthesia_types = [
            "grapheme-color",
            "chromesthesia",
            "lexical-gustatory",
            "spatial-sequence",
            "mirror-touch"
        ]
        sensory_modalities = [
            "visual",
            "auditory",
            "gustatory",
            "olfactory",
            "tactile"
        ]
        ai_applications = [
            "natural language processing",
            "computer vision",
            "speech recognition",
            "robotics",
            "creative AI"
        ]
        return {
            "1": {
                "synesthesia_type": random.choice(synesthesia_types),
                "primary_modality": random.choice(sensory_modalities),
                "secondary_modality": random.choice(sensory_modalities),
                "ai_application": random.choice(ai_applications)
            },
            "2": {
                "synesthesia_type": random.choice(synesthesia_types),
                "primary_modality": random.choice(sensory_modalities),
                "secondary_modality": random.choice(sensory_modalities),
                "ai_application": random.choice(ai_applications)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Synesthesia is a perceptual phenomenon in which stimulation of one sensory or cognitive pathway leads to involuntary experiences in a second sensory or cognitive pathway. For example, in grapheme-color synesthesia, letters or numbers are perceived as inherently colored.

Design a programming language based on {t['synesthesia_type']} synesthesia, focusing on the interaction between {t['primary_modality']} and {t['secondary_modality']} sensory modalities. Then, use this language to create an AI system for {t['ai_application']}. Your response should include:

1. Synesthetic Programming Language Design (300-350 words):
   a) Describe the core principles and syntax of your synesthesia-inspired programming language.
   b) Explain how your language incorporates the specified synesthesia type and sensory modalities.
   c) Provide a simple code example that demonstrates the unique features of your language.
   d) Discuss how your language might influence programmers' thinking and problem-solving approaches.

2. Cross-Modal AI System Architecture (250-300 words):
   a) Outline the main components of your AI system for {t['ai_application']}.
   b) Explain how your system processes and integrates information from {t['primary_modality']} and {t['secondary_modality']} modalities.
   c) Describe a novel mechanism or algorithm in your system that leverages the synesthetic nature of the programming language.

3. Implementation and Challenges (200-250 words):
   a) Discuss the technical challenges in implementing your synesthetic programming language.
   b) Explain how you would train or develop AI models using this language.
   c) Address potential issues in translating traditional AI algorithms into your synesthetic paradigm.

4. Cognitive Science Analysis (200-250 words):
   a) Analyze how your synesthetic programming approach might affect cognitive processes in AI development.
   b) Discuss potential benefits or drawbacks of using a synesthesia-inspired system for {t['ai_application']}.
   c) Explore how this approach might inform or challenge current theories in cognitive science and AI.

5. Ethical Implications and Future Directions (200-250 words):
   a) Discuss ethical considerations in developing AI systems inspired by cognitive phenomena like synesthesia.
   b) Propose guidelines for responsible development and use of synesthetic AI systems.
   c) Suggest potential applications or research directions beyond {t['ai_application']}.

Ensure your response demonstrates a deep understanding of synesthesia, programming language design, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1150-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed design of a programming language based on {t['synesthesia_type']} synesthesia, focusing on {t['primary_modality']} and {t['secondary_modality']} modalities.",
            f"The AI system architecture for {t['ai_application']} is clearly described, including how it processes cross-modal information.",
            "The submission addresses implementation challenges and proposes solutions.",
            "The cognitive science analysis explores the implications of the synesthetic approach on AI development and cognitive processes.",
            "Ethical implications are discussed, and guidelines for responsible development are proposed.",
            "The response demonstrates creativity and innovation while maintaining scientific plausibility.",
            "The submission follows the specified format and word count, with clear headings for each section."
        ]
        return float(sum(eval_with_llm_judge(instructions, submission, [criterion]) for criterion in criteria) / len(criteria))
