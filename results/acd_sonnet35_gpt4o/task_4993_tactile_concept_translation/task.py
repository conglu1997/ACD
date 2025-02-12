import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        philosophical_concepts = [
            {
                "concept": "Plato's Theory of Forms",
                "key_elements": ["ideal forms", "physical objects", "imperfect representations", "true knowledge"],
                "brief_explanation": "Plato's theory suggests that abstract ideas or forms are more real than physical objects, which are imperfect representations of these ideal forms."
            },
            {
                "concept": "Descartes' Cogito Ergo Sum",
                "key_elements": ["thinking", "existence", "doubt", "self-awareness"],
                "brief_explanation": "Descartes' principle asserts that the act of thinking proves one's existence, as doubt itself is a form of thought."
            }
        ]
        return {str(i+1): concept for i, concept in enumerate(random.sample(philosophical_concepts, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f'''Design an AI system that translates abstract concepts into tactile experiences, then use it to create a tactile representation of the philosophical concept: {t['concept']}. Brief context: {t['brief_explanation']}

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for translating abstract concepts into tactile experiences.
   b) Explain how your system integrates knowledge from cognitive science, haptic technology, and philosophy.
   c) Detail the process by which your system creates tactile representations, including any novel algorithms or techniques.
   d) Discuss how your system ensures the tactile experience accurately represents the abstract concept.

2. Conceptual Analysis (200-250 words):
   a) Analyze the key components and characteristics of {t['concept']}.
   b) Identify potential tactile elements that could represent different aspects of the concept.
   c) Explain how your system would map the abstract philosophical idea to concrete tactile experiences.

3. Tactile Representation Design (250-300 words):
   a) Present a detailed description of the tactile experience designed by your system to represent {t['concept']}.
   b) Explain how each element of the tactile experience corresponds to a key aspect of the philosophical concept.
   c) Describe at least three distinct tactile sensations used in your design and their significance.
   d) Specify the physical components or devices that would be used to create this tactile experience.

4. User Interaction and Learning (200-250 words):
   a) Describe how a user would interact with the tactile representation to understand the philosophical concept.
   b) Discuss potential challenges users might face in interpreting the tactile experience.
   c) Propose methods to evaluate the effectiveness of the tactile representation in enhancing understanding of the concept.
   d) Address how your system might accommodate users with different sensory capabilities.

5. Ethical Considerations and Limitations (150-200 words):
   a) Identify potential ethical issues in using AI-generated tactile representations for abstract concepts.
   b) Discuss limitations of your approach, including potential misrepresentations or oversimplifications.
   c) Address challenges in translating abstract thoughts into physical sensations.
   d) Propose guidelines for responsible development and application of tactile concept translation in educational contexts.

6. Future Directions and Implications (150-200 words):
   a) Suggest two potential extensions or applications of your tactile concept translation system.
   b) Discuss how this approach might impact philosophy education, accessibility, or human-computer interaction.
   c) Propose a research question that could further the development of AI-driven tactile representations of abstract concepts.

Ensure your response demonstrates a deep understanding of cognitive science, haptic technology, and the specified philosophical concept. Be creative and innovative in your tactile representation design while maintaining conceptual accuracy. Use appropriate terminology from all relevant fields.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words.'''

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive science, haptic technology, and the specified philosophical concept.",
            "The AI system architecture is well-designed, innovative, and integrates knowledge from relevant fields.",
            "The tactile representation is creative, detailed, and accurately represents the philosophical concept using at least three distinct tactile sensations.",
            "The user interaction and learning section provides a clear explanation of how the tactile experience would be used, evaluated, and adapted for different users.",
            "Ethical considerations and limitations are thoughtfully addressed, including potential misrepresentations and challenges in translating abstract thoughts to physical sensations.",
            "Future directions and implications are insightful and demonstrate an understanding of the potential impact of this technology across multiple domains.",
            "The overall response is well-structured, coherent, within the specified word limit, and addresses all required components of the task."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
