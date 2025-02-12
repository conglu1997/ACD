import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'scenario': 'First contact with a civilization orbiting a neutron star',
                'key_challenge': 'Extreme time dilation effects'
            },
            {
                'scenario': 'Communication with a civilization living in the atmosphere of a gas giant',
                'key_challenge': 'Constantly changing atmospheric conditions'
            },
            {
                'scenario': 'Diplomatic exchange with a civilization on a rogue planet',
                'key_challenge': 'Absence of a fixed reference point in space'
            },
            {
                'scenario': 'Negotiation with a civilization in a binary star system',
                'key_challenge': 'Complex orbital dynamics affecting signal transmission'
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a comprehensive interstellar communication protocol for diplomatic relations with a hypothetical alien civilization, incorporating principles from physics, linguistics, information theory, and cultural anthropology. Your task focuses on the following scenario: {t['scenario']}. Pay special attention to addressing the key challenge: {t['key_challenge']}.

Your response should include the following sections:

1. Physical Layer Design (250-300 words):
   a) Propose a method for transmitting signals across interstellar distances, considering the scenario's constraints.
   b) Explain how your method addresses the key challenge presented in the scenario.
   c) Discuss the physical principles underlying your transmission method.
   d) Analyze potential limitations and propose mitigation strategies.

2. Information Encoding (200-250 words):
   a) Design an encoding system for translating complex diplomatic messages into transmissible signals.
   b) Explain how your encoding system ensures accuracy and reduces ambiguity.
   c) Discuss how your system handles cultural and linguistic nuances in diplomatic communication.
   d) Propose a method for encoding non-verbal cues or emotional content.

3. Universal Grammar and Semantics (200-250 words):
   a) Develop a framework for a universal grammar that could facilitate interspecies communication.
   b) Explain how this grammar accounts for potentially radically different cognitive structures.
   c) Propose a method for establishing shared semantic references across species.
   d) Discuss how your system handles abstract concepts and complex ideas.

4. Cultural Exchange Protocol (200-250 words):
   a) Design a protocol for initial cultural exchange to establish diplomatic relations.
   b) Explain how your protocol minimizes the risk of cultural misunderstandings or offense.
   c) Propose methods for conveying cultural context and values through your communication system.
   d) Discuss ethical considerations in interstellar cultural exchange.

5. Temporal and Causal Logic (150-200 words):
   a) Explain how your protocol handles potential differences in perception of time and causality.
   b) Propose a method for synchronizing communication across vast distances and potential time dilation effects.
   c) Discuss how your system ensures logical consistency in long-term diplomatic negotiations.

6. Security and Verification (150-200 words):
   a) Design a system for ensuring the authenticity and integrity of diplomatic communications.
   b) Propose methods for detecting and preventing potential miscommunications or deliberate deceptions.
   c) Discuss how your security measures account for unknown alien technologies or capabilities.

7. Adaptive Learning and Evolution (100-150 words):
   a) Explain how your communication protocol can adapt and evolve over time as mutual understanding grows.
   b) Propose mechanisms for incorporating new knowledge and refining the protocol.
   c) Discuss potential long-term implications of your protocol for interstellar relations.

Ensure your response demonstrates a deep understanding of physics, linguistics, information theory, and cultural anthropology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1250-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response addresses the specific scenario: {t['scenario']}, with particular attention to the key challenge: {t['key_challenge']}.",
            "The proposed communication protocol integrates principles from physics, linguistics, information theory, and cultural anthropology.",
            "The response demonstrates creativity and innovation while maintaining scientific plausibility.",
            "The protocol design accounts for potential radical differences in alien biology, cognition, and culture.",
            "The response includes all required sections with appropriate depth and technical accuracy."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
