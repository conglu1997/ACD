import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        problems = [
            {
                "domain1": "Quantum Physics",
                "domain2": "Urban Planning",
                "challenge": "Design a sustainable city transportation system"
            },
            {
                "domain1": "Neuroscience",
                "domain2": "Artificial Intelligence",
                "challenge": "Develop a novel approach to machine learning"
            },
            {
                "domain1": "Ecology",
                "domain2": "Economics",
                "challenge": "Create a new model for sustainable resource management"
            },
            {
                "domain1": "Music Theory",
                "domain2": "Data Science",
                "challenge": "Develop an innovative method for analyzing and predicting trends in social media"
            }
        ]
        return {
            "1": random.choice(problems),
            "2": random.choice(problems)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a conceptual blending framework that combines principles from {t['domain1']} and {t['domain2']} to address the following challenge: {t['challenge']}.

Your response should include:

1. Conceptual Framework (200-250 words):
   a) Identify key concepts from both domains that will be used in the blend.
   b) Explain how these concepts will be integrated to form a new conceptual space.
   c) Describe the emergent structure that arises from this blend.

2. Innovation Proposal (250-300 words):
   a) Present a detailed innovative solution to the challenge using your conceptual blend.
   b) Explain how elements from both domains contribute to the solution.
   c) Discuss any novel insights or approaches that emerge from this interdisciplinary blend.

3. Analogical Mapping (150-200 words):
   a) Identify at least three analogical mappings between the two domains.
   b) Explain how these mappings contribute to the solution or provide new perspectives on the challenge.

4. Potential Implications (150-200 words):
   a) Discuss potential broader implications of your conceptual blend for both source domains.
   b) Propose a new research question or application that arises from this interdisciplinary integration.

5. Limitations and Refinements (100-150 words):
   a) Identify potential limitations or conflicts in your conceptual blend.
   b) Suggest ways to refine or extend the framework to address these issues.

Ensure your response demonstrates a deep understanding of both domains, creative problem-solving, and the ability to generate novel insights through conceptual integration. Use domain-specific terminology appropriately and provide explanations where necessary.

Please format your response using the numbered structure provided above, with clear headings for each section. Your total response should be between 850-1100 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must include a well-defined conceptual framework that integrates concepts from {t['domain1']} and {t['domain2']}.",
            f"The innovation proposal should directly address the challenge: {t['challenge']}.",
            "At least three clear analogical mappings between the two domains must be identified and explained.",
            "The response should discuss broader implications and propose a new research question or application.",
            "Potential limitations of the conceptual blend must be identified, with suggestions for refinement.",
            "The overall response should demonstrate creativity, interdisciplinary knowledge integration, and novel insights.",
            "The response should follow the provided structure and word limits."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
