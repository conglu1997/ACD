import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        metaphors = [
            {
                "domain": "Biology",
                "metaphor": "The cell is a city",
                "problem_area": "Urban Planning"
            },
            {
                "domain": "Physics",
                "metaphor": "Light is both a particle and a wave",
                "problem_area": "Conflict Resolution"
            },
            {
                "domain": "Computer Science",
                "metaphor": "The mind is a network of nodes",
                "problem_area": "Education"
            }
        ]
        return {str(i+1): metaphor for i, metaphor in enumerate(random.sample(metaphors, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the metaphor "{t['metaphor']}" from the domain of {t['domain']} and apply it to generate an innovative solution in the problem area of {t['problem_area']}. Your response should include the following sections:

1. Metaphor Analysis (200-250 words):
   a) Explain the key components and relationships in the given metaphor.
   b) Discuss how this metaphor is typically used to understand concepts in its original domain.
   c) Identify any limitations or potential misunderstandings that could arise from this metaphor.

2. Cross-Domain Application (250-300 words):
   a) Describe how you would apply this metaphor to the given problem area.
   b) Explain which aspects of the metaphor map well to the problem area and which might require creative interpretation.
   c) Propose a novel framework or approach for addressing challenges in the problem area, inspired by the metaphor.

3. Innovative Solution (300-350 words):
   a) Present a specific, innovative solution to a problem in the given area, using your metaphor-inspired framework.
   b) Explain how different elements of your solution correspond to components of the original metaphor.
   c) Discuss potential benefits and limitations of your proposed solution.

4. Implementation and Evaluation (200-250 words):
   a) Outline steps for implementing your innovative solution in a real-world context.
   b) Propose methods for evaluating the effectiveness of your solution.
   c) Discuss potential challenges in implementation and how they might be addressed.

5. Ethical Considerations (150-200 words):
   a) Identify potential ethical implications or unintended consequences of applying this metaphor-based solution.
   b) Suggest guidelines or safeguards to ensure responsible implementation of your innovation.

Ensure your response demonstrates a deep understanding of both the source domain of the metaphor and the target problem area. Be creative and innovative in your approach while maintaining logical consistency and practical feasibility. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a clear understanding of the metaphor '{t['metaphor']}' and its original context in {t['domain']}.",
            f"The proposed solution should be innovative and clearly inspired by the metaphor, addressing a specific problem in {t['problem_area']}.",
            "The cross-domain application of the metaphor should be logical and well-explained.",
            "The response should include a thoughtful discussion of implementation steps, evaluation methods, and potential challenges.",
            "Ethical considerations must be addressed thoroughly and thoughtfully."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
