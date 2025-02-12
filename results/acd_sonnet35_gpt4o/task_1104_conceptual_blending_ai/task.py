import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            {
                "concept1": "Time",
                "concept2": "Money",
                "domain": "Economics"
            },
            {
                "concept1": "Light",
                "concept2": "Information",
                "domain": "Quantum Computing"
            },
            {
                "concept1": "Evolution",
                "concept2": "Algorithm",
                "domain": "Artificial Intelligence"
            },
            {
                "concept1": "Memory",
                "concept2": "Architecture",
                "domain": "Cognitive Neuroscience"
            }
        ]
        return {
            "1": random.choice(concepts),
            "2": random.choice(concepts)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that performs conceptual blending of '{t['concept1']}' and '{t['concept2']}' in the domain of {t['domain']}. Your task has the following parts:

1. Conceptual Analysis (200-250 words):
   a) Briefly explain the theory of conceptual blending.
   b) Analyze the key features and associations of both '{t['concept1']}' and '{t['concept2']}'.
   c) Discuss how these concepts relate to the domain of {t['domain']}.

2. Blending Process Design (250-300 words):
   a) Describe the step-by-step process your AI system would use to blend these concepts.
   b) Explain how your system would identify and select relevant features from each concept.
   c) Detail how your system would combine these features to create a new, emergent concept.
   d) Discuss how your system would ensure the blended concept is both novel and meaningful in the context of {t['domain']}.

3. AI System Architecture (200-250 words):
   a) Outline the key components of your AI system (e.g., knowledge representation, reasoning engine, etc.).
   b) Explain how these components work together to perform conceptual blending.
   c) Discuss any novel AI techniques or approaches you've incorporated to handle the complexities of conceptual blending.

4. Example Blend (150-200 words):
   a) Provide an example of a potential blended concept your system might produce.
   b) Explain how this blend emerges from the input concepts and relates to {t['domain']}.
   c) Discuss the potential implications or applications of this blended concept.

5. Evaluation and Limitations (150-200 words):
   a) Propose criteria for evaluating the quality and creativity of the blends produced by your system.
   b) Discuss potential limitations or challenges of your approach.
   c) Suggest one way to expand or improve your system in future iterations.

Ensure your response demonstrates a deep understanding of conceptual blending theory, artificial intelligence, and the specific domain of {t['domain']}. Be creative in your system design while maintaining scientific plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of conceptual blending theory and its application in AI.",
            "The proposed AI system design is innovative, detailed, and scientifically plausible.",
            "The conceptual analysis shows deep insight into the given concepts and their relation to the specified domain.",
            "The blending process design is logical, comprehensive, and well-explained.",
            "The AI system architecture is well-thought-out and incorporates relevant AI techniques.",
            "The example blend is creative, meaningful, and properly contextualized within the given domain.",
            "The evaluation criteria and limitations discussion show critical thinking and awareness of the challenges in this field.",
            "The response maintains coherence and relevance throughout all sections."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
