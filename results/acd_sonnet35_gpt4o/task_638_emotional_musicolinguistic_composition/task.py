import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotional_states = [
            "Bittersweet nostalgia with a hint of hope",
            "Anxious anticipation mixed with excitement",
            "Melancholic contentment in solitude",
            "Frustrated determination in the face of adversity"
        ]
        musical_elements = [
            "Chord progressions",
            "Melodic contour",
            "Rhythm patterns",
            "Instrumentation"
        ]
        linguistic_features = [
            "Metaphorical mapping",
            "Semantic framing",
            "Prosodic features",
            "Conceptual blending"
        ]
        return {
            "1": {
                "emotional_state": random.choice(emotional_states),
                "musical_element": random.choice(musical_elements),
                "linguistic_feature": random.choice(linguistic_features)
            },
            "2": {
                "emotional_state": random.choice(emotional_states),
                "musical_element": random.choice(musical_elements),
                "linguistic_feature": random.choice(linguistic_features)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that translates the complex emotional state of '{t['emotional_state']}' into a musical composition, focusing on the musical element of {t['musical_element']} and utilizing the cognitive linguistic principle of {t['linguistic_feature']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your emotion-to-music translation system.
   b) Explain how it incorporates principles from cognitive linguistics, particularly {t['linguistic_feature']}.
   c) Detail how the system processes emotional input and generates musical output, focusing on {t['musical_element']}.
   d) Include a simple diagram or flowchart of your system's architecture.

2. Emotional State Analysis (200-250 words):
   a) Break down the given emotional state ('{t['emotional_state']}') into its component parts.
   b) Explain how your system would represent and process this complex emotion.
   c) Describe how the {t['linguistic_feature']} is used to map the emotion to musical concepts.

3. Musical Translation Process (200-250 words):
   a) Detail how your system translates the analyzed emotion into musical elements, particularly {t['musical_element']}.
   b) Explain any algorithms or rules used in this translation process.
   c) Describe how musical theory principles are applied in this stage.

4. Output Description (150-200 words):
   Provide a detailed description of the musical composition your system would generate for the given emotional state, focusing on the {t['musical_element']}. Explain how this output reflects the input emotion and the applied linguistic principle.

5. Cognitive Science Connection (150-200 words):
   Discuss how your system's approach relates to current understanding of how the human brain processes emotions and music. Reference relevant cognitive science theories or studies.

6. Evaluation and Limitations (100-150 words):
   a) Propose methods for evaluating the effectiveness of your system in translating emotions to music.
   b) Discuss potential limitations or challenges in implementing your system.

7. Ethical Considerations (100-150 words):
   Discuss potential ethical implications or concerns related to AI systems that generate emotive music, and propose guidelines for responsible development and use.

8. Code Snippet (50-100 words of explanation + code):
   Provide a small Python code snippet (10-20 lines) that demonstrates a key aspect of your system, such as emotion representation or musical element generation. Briefly explain what the code does and how it relates to your overall system design.

Ensure your response demonstrates a deep understanding of music theory, cognitive linguistics, and emotional intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility.

Format your response using clear headings for each section. Your total response should be between 1200-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of music theory, cognitive linguistics, and emotional intelligence.",
            f"The system effectively incorporates the linguistic feature of {t['linguistic_feature']} in translating emotions to music.",
            f"The musical translation process focuses on the specified element of {t['musical_element']}.",
            f"The system convincingly analyzes and processes the complex emotional state of '{t['emotional_state']}'.",
            "The response includes all required sections with appropriate depth and creativity.",
            "The proposed system is scientifically plausible and grounded in cognitive science principles."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
