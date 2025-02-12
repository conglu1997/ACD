import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        human_emotions = [
            "joy",
            "sadness",
            "anger",
            "fear",
            "disgust",
            "surprise",
            "contentment",
            "anxiety"
        ]
        alien_traits = [
            "hive mind consciousness",
            "non-linear time perception",
            "synesthesia-like sensory integration",
            "electromagnetic field sensitivity",
            "quantum entanglement-based communication"
        ]
        communication_modes = [
            "color changes",
            "pheromone release",
            "bioluminescent patterns",
            "gravitational wave modulation",
            "telepathic imagery"
        ]
        
        return {
            "1": {
                "human_emotion": random.choice(human_emotions),
                "alien_trait": random.choice(alien_traits),
                "communication_mode": random.choice(communication_modes)
            },
            "2": {
                "human_emotion": random.choice(human_emotions),
                "alien_trait": random.choice(alien_traits),
                "communication_mode": random.choice(communication_modes)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system capable of translating the human emotion of '{t['human_emotion']}' into a hypothetical alien language, considering that the alien species possesses {t['alien_trait']} and primarily communicates through {t['communication_mode']}. Your response should include:\n\n1. Alien Cognitive Model (250-300 words):\n   a) Describe how the alien species might perceive and process emotions, given their unique trait.\n   b) Explain how their communication mode influences their emotional expression.\n   c) Propose a model for how the aliens might conceptualize the given human emotion.\n\n2. Translation System Architecture (300-350 words):\n   a) Outline the key components of your AI translation system.\n   b) Explain how the system processes human emotional input.\n   c) Describe the methods used to map human emotions to alien concepts.\n   d) Detail how the system generates output in the alien communication mode.\n\n3. Linguistic and Cognitive Challenges (200-250 words):\n   a) Identify potential obstacles in translating emotions across species.\n   b) Discuss how your system addresses the lack of direct emotional equivalents.\n   c) Explain how cultural and evolutionary differences are accounted for.\n\n4. Example Translation (200-250 words):\n   a) Provide a specific example of how your system would translate the given human emotion.\n   b) Describe the alien 'emotional' response in detail, using their communication mode.\n   c) Explain the rationale behind this translation.\n\n5. Ethical Considerations (150-200 words):\n   a) Discuss potential ethical issues in emotion translation between species.\n   b) Address concerns about miscommunication or misunderstanding.\n   c) Propose guidelines for responsible use of the translation system.\n\n6. Validation and Improvement (150-200 words):\n   a) Suggest methods to validate the accuracy of emotional translations.\n   b) Describe how the system could learn and improve over time.\n   c) Discuss the role of feedback from both humans and hypothetical aliens.\n\n7. Broader Implications (150-200 words):\n   a) Explore how this system could advance our understanding of emotions and cognition.\n   b) Discuss potential applications beyond alien communication.\n   c) Speculate on how this technology might influence human-AI interaction.\n\nEnsure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.\n\nFormat your response with clear headings for each section. Your total response should be between 1400-1750 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence principles.",
            "The alien cognitive model and translation system architecture are innovative, plausible, and well-suited to the given alien trait and communication mode.",
            "The response addresses all required sections comprehensively and coherently.",
            "The proposed system effectively tackles the challenges of cross-species emotion translation.",
            "The example translation is creative, detailed, and logically consistent with the proposed system.",
            "Ethical considerations and broader implications are thoughtfully analyzed.",
            "The response is well-structured, clear, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
