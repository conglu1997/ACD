import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "target_language": "Mandarin Chinese",
                "cognitive_principle": "Embodied Cognition",
                "vr_environment": "Ancient Chinese Market"
            },
            "2": {
                "target_language": "Arabic",
                "cognitive_principle": "Conceptual Metaphor Theory",
                "vr_environment": "Desert Oasis"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a virtual reality simulation for language acquisition of {t['target_language']} based on the cognitive linguistics principle of {t['cognitive_principle']}, set in a {t['vr_environment']}. Your task has the following parts:

1. Simulation Design (250-300 words):
   a) Describe the key features of your VR environment and how they relate to the target language and culture.
   b) Explain how you incorporate the specified cognitive linguistics principle into the language learning experience.
   c) Outline 3-4 specific language learning activities or scenarios within the simulation.

2. Cognitive Linguistics Integration (200-250 words):
   a) Analyze how your simulation applies the given cognitive linguistics principle to language acquisition.
   b) Discuss how the VR environment enhances or challenges traditional understanding of this principle.
   c) Predict potential cognitive benefits or challenges of learning language through this method.

3. Spatial Cognition and Language (150-200 words):
   a) Explain how your VR simulation might influence spatial cognition in language learners.
   b) Discuss any potential links between spatial reasoning in VR and language structure in the target language.
   c) Propose a hypothesis about how this method might affect learners' mental representations of language concepts.

4. Assessment and Adaptation (200-250 words):
   a) Describe how you would measure the effectiveness of your VR language acquisition simulation.
   b) Explain how the simulation adapts to individual learners' progress and learning styles.
   c) Discuss potential challenges in implementing this system and how you would address them.

5. Ethical and Cultural Considerations (150-200 words):
   a) Analyze potential ethical implications of using VR for language acquisition.
   b) Discuss how to ensure cultural authenticity and sensitivity in the VR environment.
   c) Propose guidelines for responsible development and use of such technology in language education.

Ensure your response demonstrates a deep understanding of cognitive linguistics, virtual reality technology, and language acquisition theories. Be innovative in your approach while maintaining scientific plausibility and educational value. Your total response should be between 950-1200 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding and integration of the specified cognitive linguistics principle, target language, and VR environment.",
            "The simulation design is creative, well-explained, and effectively combines linguistic theory with VR technology.",
            "The analysis of cognitive linguistics integration shows depth of understanding and critical thinking about language acquisition in VR.",
            "The discussion of spatial cognition and language demonstrates insight into the relationship between virtual environments and language learning.",
            "The assessment and adaptation section provides a plausible and innovative approach to measuring and improving the effectiveness of the VR simulation.",
            "The ethical and cultural considerations show awareness of potential issues and propose thoughtful guidelines for responsible implementation."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
