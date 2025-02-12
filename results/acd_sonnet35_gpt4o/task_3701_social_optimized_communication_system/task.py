import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        social_contexts = [
            "conflict resolution",
            "collaborative decision-making",
            "cross-cultural negotiation",
            "emotional support networks"
        ]
        linguistic_principles = [
            "semantic compression",
            "pragmatic inference",
            "phonological optimization",
            "syntactic flexibility"
        ]
        information_theory_concepts = [
            "channel capacity",
            "error correction",
            "data compression",
            "signal-to-noise ratio"
        ]
        social_psychology_factors = [
            "group cohesion",
            "social identity",
            "power dynamics",
            "cognitive biases"
        ]
        return {
            "1": {
                "social_context": random.choice(social_contexts),
                "linguistic_principle": random.choice(linguistic_principles),
                "information_theory_concept": random.choice(information_theory_concepts),
                "social_psychology_factor": random.choice(social_psychology_factors)
            },
            "2": {
                "social_context": random.choice(social_contexts),
                "linguistic_principle": random.choice(linguistic_principles),
                "information_theory_concept": random.choice(information_theory_concepts),
                "social_psychology_factor": random.choice(social_psychology_factors)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel communication system optimized for {t['social_context']}, integrating principles from linguistics, information theory, and social psychology. Your system should specifically incorporate {t['linguistic_principle']}, {t['information_theory_concept']}, and address the social psychological factor of {t['social_psychology_factor']}. Your response should include:

1. System Design (300-350 words):
   a) Describe the key features of your communication system.
   b) Explain how it incorporates {t['linguistic_principle']}, {t['information_theory_concept']}, and addresses {t['social_psychology_factor']}.
   c) Provide examples of how these features optimize communication for {t['social_context']}.
   d) Discuss any trade-offs or potential limitations in your design.

2. Linguistic Analysis (200-250 words):
   a) Analyze the linguistic properties of your communication system.
   b) Explain how {t['linguistic_principle']} is implemented and its effects on communication.
   c) Discuss how your system might influence or be influenced by existing language structures.

3. Information Theory Application (200-250 words):
   a) Describe how {t['information_theory_concept']} is applied in your system.
   b) Analyze the theoretical efficiency and effectiveness of your communication system.
   c) Compare your system's information handling capabilities to traditional language or communication methods.

4. Social Dynamics (200-250 words):
   a) Explain how your system addresses {t['social_psychology_factor']} in the context of {t['social_context']}.
   b) Discuss potential social implications of implementing your communication system.
   c) Analyze how your system might influence group dynamics and individual behavior.

5. Implementation and Adoption (150-200 words):
   a) Propose a method for introducing and teaching your communication system.
   b) Discuss potential challenges in adoption and how they might be overcome.
   c) Describe how your system could be integrated with existing communication technologies.

6. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues raised by your communication system.
   b) Discuss how these issues might be addressed or mitigated.
   c) Analyze the potential long-term societal impacts of your system.

7. Experimental Validation (150-200 words):
   a) Propose an experiment to test the effectiveness of your communication system in {t['social_context']}.
   b) Describe the metrics you would use to evaluate its performance.
   c) Discuss how you would control for potential confounding factors in your experiment.

Ensure your response demonstrates a deep understanding of linguistics, information theory, and social psychology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility and ethical considerations.

Format your response with clear headings for each section (e.g., '1. System Design', '2. Linguistic Analysis', etc.). Your total response should be between 1350-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively integrates {t['linguistic_principle']}, {t['information_theory_concept']}, and addresses {t['social_psychology_factor']} in the context of {t['social_context']}",
            "The proposed communication system demonstrates a deep understanding of linguistics, information theory, and social psychology",
            "The system design is innovative, plausible, and well-suited to the specified social context",
            "The response includes a thoughtful analysis of linguistic properties, information theory application, and social dynamics",
            "The implementation, adoption, and ethical considerations are thoroughly addressed",
            "The proposed experimental validation is well-designed and appropriate for evaluating the system's effectiveness",
            "The response is well-structured, following the specified format with clear headings for each section",
            "The explanation of complex concepts is clear and accessible while maintaining technical accuracy",
            "The response demonstrates creativity and innovation while remaining scientifically plausible",
            "The ethical implications and potential societal impacts are critically analyzed"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
