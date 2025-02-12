import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "setting": "United Nations Climate Summit",
                "cultures": ["Western", "East Asian"],
                "communication_challenge": "Negotiating carbon emission targets"
            },
            {
                "setting": "International Space Station",
                "cultures": ["Russian", "American"],
                "communication_challenge": "Coordinating emergency response procedures"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of integrating verbal, visual, and haptic modes of communication in an embodied context. Then, apply this system to a complex scenario involving cross-cultural communication in a high-stakes diplomatic setting: {t['setting']}. The system should facilitate communication between {t['cultures'][0]} and {t['cultures'][1]} cultures, addressing the challenge of {t['communication_challenge']}.

Your response should include:

1. System Architecture (250-300 words):
   a) Describe the main components of your AI system and how they interact.
   b) Explain how the system integrates verbal, visual, and haptic modes of communication.
   c) Discuss how the system incorporates principles of embodied cognition.
   d) Include a high-level diagram or pseudocode representing the system's workflow.

2. Multimodal Integration (200-250 words):
   a) Explain how your system processes and synthesizes information from different communication modes.
   b) Describe any novel techniques or algorithms used for multimodal integration.
   c) Discuss how the system handles potential conflicts or inconsistencies between different modes.

3. Cross-Cultural Adaptation (200-250 words):
   a) Describe how your system adapts its communication strategies for different cultures.
   b) Explain how it recognizes and interprets culture-specific nonverbal cues.
   c) Discuss how the system maintains cultural sensitivity while facilitating communication.

4. Scenario Application (250-300 words):
   a) Apply your system to the given scenario, explaining how it would facilitate communication.
   b) Describe specific examples of how the system would use each communication mode.
   c) Explain how the system would address the particular communication challenge.
   d) Discuss potential outcomes and benefits of using your system in this scenario.

5. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to using AI for cross-cultural communication.
   b) Discuss privacy concerns and potential biases in the system.
   c) Propose guidelines for responsible development and use of such systems.

6. Evaluation and Future Improvements (150-200 words):
   a) Suggest methods to evaluate the effectiveness and accuracy of your system.
   b) Propose two potential improvements or expansions to enhance its capabilities.
   c) Discuss any limitations of your current design and how they might be addressed.

Ensure your response demonstrates a deep understanding of multimodal communication, embodied cognition, cross-cultural dynamics, and AI technologies. Be creative in your approach while maintaining scientific and ethical plausibility. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of multimodal communication and embodied cognition.",
            "The system design integrates verbal, visual, and haptic modes of communication effectively.",
            "The cross-cultural adaptation strategy is well-thought-out and culturally sensitive.",
            "The application to the given scenario is detailed and addresses the specific communication challenge.",
            "Ethical considerations are thoroughly discussed, including privacy and bias concerns.",
            "The evaluation methods and proposed improvements are relevant and insightful."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
