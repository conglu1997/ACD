import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_principles = [
            "Image schemas",
            "Conceptual metaphors",
            "Frame semantics",
            "Conceptual blending",
            "Prototype theory"
        ]
        ai_architectures = [
            "Transformer-based language models",
            "Convolutional neural networks",
            "Recurrent neural networks",
            "Graph neural networks",
            "Neuro-symbolic systems"
        ]
        interaction_contexts = [
            "Creative collaboration",
            "Scientific research",
            "Healthcare diagnostics",
            "Educational tutoring",
            "Crisis management"
        ]
        return {
            "1": {
                "cognitive_principle": random.choice(cognitive_principles),
                "ai_architecture": random.choice(ai_architectures),
                "interaction_context": random.choice(interaction_contexts)
            },
            "2": {
                "cognitive_principle": random.choice(cognitive_principles),
                "ai_architecture": random.choice(ai_architectures),
                "interaction_context": random.choice(interaction_contexts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel communication interface between humans and AI systems based on principles of cognitive linguistics and embodied cognition. Your interface should focus on the cognitive principle of {t['cognitive_principle']}, be compatible with {t['ai_architecture']}, and be optimized for the interaction context of {t['interaction_context']}.

Your response should include the following sections:

1. Cognitive-Linguistic Framework (250-300 words):
   a) Explain the chosen cognitive principle and its relevance to human-AI communication.
   b) Describe how this principle can be applied to create more intuitive and effective interactions.
   c) Discuss any challenges in adapting this principle for AI systems.

2. Interface Design (300-350 words):
   a) Describe the key components and features of your communication interface.
   b) Explain how your design incorporates the chosen cognitive principle.
   c) Discuss how the interface adapts to or leverages the specified AI architecture.
   d) Include a high-level diagram or pseudocode to illustrate your interface design.

3. Interaction Process (200-250 words):
   a) Provide a step-by-step explanation of how a typical interaction would unfold using your interface.
   b) Give a specific example of how it would handle a complex communication task in the given context.
   c) Explain how your interface bridges differences between human and AI cognition.

4. Evaluation and Adaptation (200-250 words):
   a) Propose methods to evaluate the effectiveness of your communication interface.
   b) Discuss how your interface could adapt or learn from interactions over time.
   c) Compare your cognitive approach to traditional human-AI interfaces.

5. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss potential ethical implications of your communication interface.
   b) Propose two potential applications of your interface beyond the specified context.
   c) Suggest one area for future research to enhance cognitive-linguistic interfaces for human-AI interaction.

Ensure your response demonstrates a deep understanding of cognitive linguistics, AI systems, and human-computer interaction. Be creative in your design while maintaining scientific plausibility. Use technical terminology appropriately and provide explanations where necessary."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address the cognitive principle of {t['cognitive_principle']}.",
            f"The interface design must be compatible with {t['ai_architecture']}.",
            f"The system should be optimized for the interaction context of {t['interaction_context']}.",
            "The response must include all five required sections: Cognitive-Linguistic Framework, Interface Design, Interaction Process, Evaluation and Adaptation, and Ethical Considerations and Future Directions.",
            "The interface design must be innovative and demonstrate a clear integration of cognitive linguistics principles with AI and human-computer interaction.",
            "The response should show a deep understanding of the chosen cognitive principle and its application to human-AI communication.",
            "The interaction process must provide a clear and plausible example of how the interface would facilitate communication.",
            "The evaluation methods and adaptation strategies should be well-reasoned and specific to the proposed interface.",
            "The ethical considerations should be thoughtful and relevant to human-AI communication interfaces."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
