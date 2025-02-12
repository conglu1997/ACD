import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scientific_concepts = [
            {
                "concept": "Quantum entanglement",
                "field": "Quantum physics",
                "existing_metaphor": "Quantum entanglement is like having two coins that always land on opposite sides, no matter how far apart they are."
            },
            {
                "concept": "DNA replication",
                "field": "Molecular biology",
                "existing_metaphor": "DNA replication is like unzipping a zipper and using each side as a template to create two new zippers."
            },
            {
                "concept": "Black holes",
                "field": "Astrophysics",
                "existing_metaphor": "A black hole is like a cosmic whirlpool, pulling in everything that comes too close to its event horizon."
            }
        ]
        return {str(i+1): concept for i, concept in enumerate(random.sample(scientific_concepts, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the existing metaphor for the scientific concept and generate a novel metaphor to explain it. Your task has four parts:

1. Metaphor Analysis (150-200 words):
   a) Explain the scientific concept of {t['concept']} in {t['field']}.
   b) Analyze the existing metaphor: "{t['existing_metaphor']}"
   c) Discuss the strengths and limitations of this metaphor in explaining the concept.

2. Novel Metaphor Generation (200-250 words):
   a) Create a new metaphor to explain {t['concept']}.
   b) Ensure your metaphor is distinct from the existing one and draws from a different domain.
   c) Explain how your metaphor captures key aspects of the scientific concept.

3. Comparative Analysis (150-200 words):
   a) Compare and contrast your novel metaphor with the existing one.
   b) Discuss how each metaphor might be more effective for different aspects of the concept or different audiences.
   c) Analyze any potential misconceptions that could arise from each metaphor.

4. Metaphor Application (150-200 words):
   a) Propose how your novel metaphor could be used in science education or communication.
   b) Discuss any limitations of your metaphor and how they could be addressed.
   c) Suggest how this metaphor-generation process could be applied to other complex scientific concepts.

Ensure your response demonstrates a deep understanding of the scientific concept, creative thinking in metaphor generation, and analytical skills in comparing and evaluating metaphors. Be creative while maintaining scientific accuracy. Your total response should be between 650-850 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a clear explanation of the scientific concept",
            "The analysis of the existing metaphor should be thorough and insightful",
            "The novel metaphor should be creative, distinct from the existing one, and accurately represent the scientific concept",
            "The comparative analysis should provide meaningful insights into the strengths and limitations of both metaphors",
            "The proposed application of the novel metaphor should be practical and demonstrate understanding of science communication challenges",
            "The response should be between 650-850 words in total"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
