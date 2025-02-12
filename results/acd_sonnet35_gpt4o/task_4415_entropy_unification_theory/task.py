import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        problems = [
            {
                "domain": "Cosmology",
                "concept": "Black hole information paradox",
                "constraint": "Conservation of information"
            },
            {
                "domain": "Quantum Computing",
                "concept": "Quantum error correction",
                "constraint": "Decoherence"
            }
        ]
        return {
            "1": random.choice(problems),
            "2": random.choice(problems)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Develop a unified theory of entropy that bridges thermodynamics, information theory, and biological evolution, then apply it to solve a complex interdisciplinary problem in the domain of {t['domain']}, focusing on the concept of {t['concept']}, while considering the constraint of {t['constraint']}. Your response should include:

1. Unified Entropy Theory (300-350 words):
   a) Describe the key principles of your unified entropy theory.
   b) Explain how it integrates concepts from thermodynamics, information theory, and biological evolution.
   c) Discuss any novel mathematical formulations or models you've developed.
   d) Provide an example of how your theory reconciles apparent contradictions between different entropy concepts.

2. Application to {t['domain']} (250-300 words):
   a) Explain how your unified entropy theory applies to the given domain.
   b) Describe how it provides new insights into the specified concept.
   c) Discuss how your theory addresses the given constraint.
   d) Propose a specific problem or paradox in this domain that your theory could help resolve.

3. Mathematical Framework (200-250 words):
   a) Present the core mathematical equations or formalism of your unified entropy theory.
   b) Explain how these equations incorporate principles from different disciplines.
   c) Demonstrate how your mathematical framework applies to the given domain and concept.

4. Experimental Predictions (200-250 words):
   a) Propose at least two testable predictions derived from your unified entropy theory.
   b) Describe potential experiments or observations that could validate these predictions.
   c) Discuss any technological challenges in testing your theory and how they might be overcome.

5. Interdisciplinary Implications (150-200 words):
   a) Analyze the potential impact of your theory on other scientific disciplines.
   b) Discuss how it might influence our understanding of complex systems in nature and technology.
   c) Explore any philosophical or conceptual shifts implied by your unified entropy theory.

6. Limitations and Future Directions (150-200 words):
   a) Acknowledge any limitations or potential weaknesses in your unified theory.
   b) Suggest areas for future research or refinement of your theory.
   c) Propose potential collaborations across disciplines that could further develop your ideas.

Ensure your response demonstrates a deep understanding of entropy concepts across multiple disciplines. Use appropriate technical terminology and provide clear explanations for complex ideas. Be innovative in your approach while maintaining scientific plausibility and rigor.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of entropy concepts across thermodynamics, information theory, and biological evolution.",
            "The unified entropy theory presented is coherent, novel, and effectively bridges multiple disciplines.",
            "The application to the given domain is well-explained and addresses the specified concept and constraint.",
            "The mathematical framework is sound and appropriately integrates principles from different fields.",
            "The experimental predictions are logical, testable, and flow from the unified theory.",
            "The interdisciplinary implications and limitations are thoughtfully discussed.",
            "The response is creative and innovative while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
