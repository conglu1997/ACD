import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_principles = [
            "working memory capacity",
            "pattern recognition",
            "mental rotation",
            "gestalt principles",
            "color perception",
            "visual attention"
        ]
        communication_contexts = [
            "emergency response coordination",
            "space exploration",
            "augmented reality interfaces",
            "cross-cultural collaboration",
            "AI-assisted medical diagnosis",
            "educational technology"
        ]
        constraints = [
            "limited display space",
            "real-time processing requirements",
            "accessibility for color-blind users",
            "multi-modal integration",
            "scalability across devices",
            "cultural neutrality"
        ]
        return {
            "1": {"cognitive_principle": random.choice(cognitive_principles),
                  "communication_context": random.choice(communication_contexts),
                  "constraint": random.choice(constraints)},
            "2": {"cognitive_principle": random.choice(cognitive_principles),
                  "communication_context": random.choice(communication_contexts),
                  "constraint": random.choice(constraints)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a visual language system for human-AI communication, focusing on the cognitive principle of {t['cognitive_principle']}, within the context of {t['communication_context']}, and addressing the constraint of {t['constraint']}.

1. Visual Language Design (250-300 words):
   a) Describe the basic elements of your visual language (e.g., shapes, colors, patterns, animations).
   b) Explain how these elements combine to create meaning.
   c) Discuss how your design incorporates the specified cognitive principle.
   d) Address how your system handles the given constraint.

2. Syntax and Grammar (200-250 words):
   a) Define the rules for combining visual elements in your language.
   b) Provide examples of how complex ideas or instructions can be represented.
   c) Explain how your system handles ambiguity or potential misinterpretations.

3. Human-AI Interaction (200-250 words):
   a) Describe how humans would input or generate messages in your visual language.
   b) Explain how AI systems would interpret and respond to these visual messages.
   c) Discuss any learning curve or training required for humans to use the system effectively.

4. Implementation in Context (200-250 words):
   a) Explain how your visual language system would be applied in the given communication context.
   b) Provide a specific example scenario and demonstrate how your system would handle it.
   c) Discuss any challenges or limitations of using your system in this context.

5. Cognitive Load and Efficiency Analysis (150-200 words):
   a) Analyze how your visual language system affects cognitive load compared to traditional language.
   b) Discuss the efficiency of information transfer in your system.
   c) Propose a method for measuring the effectiveness of your visual language in reducing cognitive load.

6. Ethical and Societal Implications (150-200 words):
   a) Discuss potential ethical concerns related to your visual language system.
   b) Analyze how widespread adoption of your system might impact society and human communication.
   c) Propose guidelines for responsible development and use of visual language systems.

Ensure your response demonstrates a deep understanding of linguistics, cognitive psychology, and human-computer interaction. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility. Format your response using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The visual language design effectively incorporates the cognitive principle of {t['cognitive_principle']}.",
            f"The system adequately addresses the constraint of {t['constraint']}.",
            f"The implementation in the context of {t['communication_context']} is well-explained and plausible.",
            "The syntax and grammar of the visual language are clearly defined and logical.",
            "The analysis of cognitive load and efficiency is insightful and well-reasoned.",
            "The discussion of ethical and societal implications is thoughtful and comprehensive.",
            "The response demonstrates creativity, interdisciplinary knowledge, and analytical skills.",
            "The submission follows the specified format and addresses all required sections."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
