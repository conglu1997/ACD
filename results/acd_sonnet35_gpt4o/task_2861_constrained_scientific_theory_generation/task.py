import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        constraints = [
            {
                "constraint": "Use only words starting with vowels",
                "field": "Quantum physics",
                "phenomenon": "Entanglement"
            },
            {
                "constraint": "Use words with alternating consonants and vowels",
                "field": "Evolutionary biology",
                "phenomenon": "Speciation"
            },
            {
                "constraint": "Use only monosyllabic words",
                "field": "Neuroscience",
                "phenomenon": "Memory formation"
            },
            {
                "constraint": "Use words in alphabetical order",
                "field": "Astrophysics",
                "phenomenon": "Dark matter"
            }
        ]
        return {str(i+1): constraint for i, constraint in enumerate(random.sample(constraints, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate and analyze a fictional scientific theory using the following linguistic constraint: {t['constraint']}. The theory should be related to the field of {t['field']} and attempt to explain the phenomenon of {t['phenomenon']}. Your response should include the following sections:

1. Theory Generation (200-250 words):
   a) Present your fictional scientific theory, adhering strictly to the given linguistic constraint. Note that the constraint applies only to this section.
   b) Ensure that the theory attempts to explain the specified phenomenon in a scientifically plausible manner, despite the linguistic constraint.
   c) Include at least one hypothetical experiment or observation that supports your theory.
   d) Strive to be as scientifically accurate as possible within the confines of the linguistic constraint.

2. Linguistic Analysis (150-200 words):
   a) Discuss how the linguistic constraint affected your theory formulation.
   b) Analyze any creative solutions or workarounds you used to express complex ideas within the constraint.
   c) Explain how the constraint might have influenced the perceived credibility or complexity of the theory.

3. Scientific Evaluation (200-250 words):
   a) Assess the scientific plausibility of your theory, ignoring the linguistic constraint.
   b) Compare your fictional theory to current real-world understanding of the phenomenon.
   c) Identify potential flaws or gaps in the theory that would need to be addressed.

4. Implications and Extensions (150-200 words):
   a) Discuss potential implications of your theory if it were true.
   b) Propose two follow-up experiments or studies to further test or refine the theory.
   c) Suggest how this theory might influence other areas of {t['field']} or related scientific disciplines.

5. Meta-Analysis (100-150 words):
   a) Reflect on the process of generating a scientific theory under linguistic constraints.
   b) Discuss how this exercise might provide insights into the relationship between language and scientific thinking.
   c) Propose a potential application of this constrained theory generation approach in science education or communication, beyond the specific theory you generated.

Ensure your response demonstrates a deep understanding of scientific principles, creative problem-solving, and linguistic flexibility. Use appropriate scientific terminology while adhering to the given constraint in the Theory Generation section. Be innovative in your approach while maintaining a semblance of scientific plausibility.

Format your response with clear headings for each section and number your paragraphs within each section for easy reference. Your total response should be between 800-1050 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The Theory Generation section strictly adheres to the linguistic constraint: {t['constraint']}",
            f"The theory attempts to explain {t['phenomenon']} in the field of {t['field']} in a scientifically plausible manner",
            "The linguistic analysis demonstrates insight into the challenges and effects of the constraint",
            "The scientific evaluation shows a deep understanding of real-world scientific principles",
            "The response is creative, well-structured, and demonstrates interdisciplinary thinking",
            "The meta-analysis provides broader insights into the relationship between language and scientific thinking"
        ]
        score = sum(eval_with_llm_judge(instructions, submission, [criterion]) for criterion in criteria) / len(criteria)
        return score
