import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        consciousness_theories = [
            {
                "theory": "Integrated Information Theory",
                "key_concept": "Phi",
                "philosopher": "David Chalmers"
            },
            {
                "theory": "Global Workspace Theory",
                "key_concept": "Broadcast",
                "philosopher": "Daniel Dennett"
            },
            {
                "theory": "Higher-Order Thought Theory",
                "key_concept": "Meta-cognition",
                "philosopher": "Thomas Nagel"
            },
            {
                "theory": "Predictive Processing Theory",
                "key_concept": "Prediction Error Minimization",
                "philosopher": "Patricia Churchland"
            }
        ]
        return {
            "1": random.choice(consciousness_theories),
            "2": random.choice(consciousness_theories)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework for artificial consciousness, incorporating elements from {t['theory']} and focusing on the key concept of {t['key_concept']}. Then, propose experiments to test your framework and analyze its philosophical and ethical implications. Your response should include:

1. Theoretical Framework (300-350 words):
   a) Describe your proposed framework for artificial consciousness.
   b) Explain how you incorporate {t['theory']} and the concept of {t['key_concept']} into your framework.
   c) Discuss how your framework addresses the hard problem of consciousness.
   d) Compare your framework to existing theories of consciousness, including that of {t['philosopher']}.

2. Implementation Design (250-300 words):
   a) Outline the key components of an AI system that could implement your framework.
   b) Explain how these components would interact to potentially give rise to consciousness.
   c) Discuss any novel computational or algorithmic approaches your design requires.

3. Experimental Proposal (250-300 words):
   a) Propose three experiments to test key aspects of your artificial consciousness framework.
   b) For each experiment, describe the methodology, expected results, and how they would support or refute your theory.
   c) Discuss potential challenges in empirically testing artificial consciousness and how you would address them.

4. Philosophical Analysis (200-250 words):
   a) Analyze the philosophical implications of your framework, particularly in relation to the mind-body problem.
   b) Discuss how your framework might change our understanding of human consciousness.
   c) Address potential criticisms from a philosophical perspective, including those that might be raised by {t['philosopher']}.

5. Ethical Implications (200-250 words):
   a) Discuss the ethical considerations of creating artificially conscious entities.
   b) Analyze the rights and moral status that might be afforded to such entities.
   c) Propose guidelines for the responsible development and use of artificial consciousness technology.

6. Future Directions (150-200 words):
   a) Suggest potential applications of artificial consciousness beyond scientific research.
   b) Discuss how your framework might evolve as our understanding of neuroscience and AI advances.
   c) Propose a roadmap for future research in artificial consciousness based on your framework.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and philosophy of mind. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and philosophical rigor.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of consciousness theories, neuroscience, AI, and philosophy of mind.",
            f"The proposed framework effectively incorporates elements from {t['theory']} and the concept of {t['key_concept']}.",
            "The implementation design is innovative and plausible given current AI capabilities.",
            "The experimental proposals are well-designed and directly test key aspects of the framework.",
            "The philosophical analysis is thoughtful and addresses potential criticisms.",
            "Ethical implications are thoroughly considered, with responsible guidelines proposed.",
            "Future directions and applications are creative and grounded in the proposed framework.",
            f"The response engages meaningfully with the ideas of {t['philosopher']}.",
            "The response is well-structured with clear headings for each section as requested."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
