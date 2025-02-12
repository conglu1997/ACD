import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        natural_systems = [
            "Ant colonies",
            "Bee hives",
            "Mycorrhizal networks",
            "Neuronal networks",
            "Flocking birds"
        ]
        social_challenges = [
            "Information dissemination",
            "Resource allocation",
            "Consensus building",
            "Innovation diffusion",
            "Conflict resolution"
        ]
        return {
            "1": {
                "natural_system": random.choice(natural_systems),
                "social_challenge": random.choice(social_challenges)
            },
            "2": {
                "natural_system": random.choice(natural_systems),
                "social_challenge": random.choice(social_challenges)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biomimetic computing system inspired by {t['natural_system']} to optimize human social networks and improve collaborative problem-solving, focusing on the social challenge of {t['social_challenge']}. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your biomimetic social network optimization system.
   b) Explain how your system mimics the principles and mechanisms of {t['natural_system']}.
   c) Discuss how your system interfaces with and optimizes human social networks.
   d) Include a diagram or flowchart of your system's architecture (describe it textually).

2. Biomimetic Principles (250-300 words):
   a) Analyze the key characteristics of {t['natural_system']} that make it suitable for addressing {t['social_challenge']}.
   b) Explain how these characteristics are translated into computational algorithms or processes in your system.
   c) Discuss any novel adaptations or innovations you've made to apply these natural principles to human social networks.

3. Social Challenge Application (250-300 words):
   a) Describe in detail how your system addresses the challenge of {t['social_challenge']}.
   b) Provide specific examples of how your system would optimize social networks to improve collaborative problem-solving in this context.
   c) Explain how your approach differs from or improves upon traditional methods of addressing this social challenge.

4. Implementation and Scalability (200-250 words):
   a) Outline the technical requirements for implementing your system in real-world social networks.
   b) Discuss how your system would scale to accommodate large, complex social structures.
   c) Address potential challenges in implementation and how they might be overcome.

5. Ethical Considerations (150-200 words):
   a) Analyze potential ethical implications of using biomimetic systems to optimize human social networks.
   b) Discuss how your system ensures privacy, autonomy, and fairness in social optimization.
   c) Propose guidelines for the responsible development and use of such systems.

6. Evaluation and Validation (200-250 words):
   a) Propose methods for evaluating the effectiveness of your system in optimizing social networks and improving collaborative problem-solving.
   b) Describe potential metrics or indicators that could be used to measure success.
   c) Suggest an experimental design to validate your system's performance in a controlled setting.

7. Future Directions and Implications (150-200 words):
   a) Discuss potential future enhancements or extensions of your system.
   b) Explore broader implications of biomimetic social network optimization for society, technology, and human interaction.
   c) Propose two potential research directions that could further advance this field.

Ensure your response demonstrates a deep understanding of complex adaptive systems, social network theory, and the chosen natural system. Use appropriate technical terminology and provide clear explanations where necessary. Be creative and innovative in your approach while maintaining scientific and technological plausibility.

Format your response with clear headings for each section. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified natural system and its application to social network optimization.",
            "The proposed biomimetic system is innovative, scientifically plausible, and clearly explained.",
            "The submission addresses all required sections comprehensively, providing insightful analysis of the system's potential impact, ethical implications, and future directions.",
            "The response shows strong interdisciplinary knowledge integration, effectively combining concepts from biology, computer science, and social sciences.",
            "The writing is clear, well-structured, and uses appropriate technical terminology throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
