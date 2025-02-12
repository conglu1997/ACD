import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        math_concepts = [
            {
                'concept': 'Fractal geometry',
                'key_property': 'Self-similarity at different scales',
                'example': 'Mandelbrot set'
            },
            {
                'concept': 'Non-Euclidean geometry',
                'key_property': 'Curved space where parallel lines can intersect',
                'example': 'Hyperbolic geometry'
            },
            {
                'concept': 'Topology',
                'key_property': 'Properties that remain unchanged under continuous deformations',
                'example': 'Möbius strip'
            },
            {
                'concept': 'Complex numbers',
                'key_property': 'Numbers with real and imaginary components',
                'example': 'Argand plane'
            }
        ]
        return {str(i+1): concept for i, concept in enumerate(random.sample(math_concepts, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a fictional economic system based on the mathematical concept of {t['concept']}. Your task is to:

1. Briefly explain the given mathematical concept and its key property (2-3 sentences).

2. Design an innovative and logically consistent economic system that incorporates this mathematical concept as its fundamental principle. Describe its key components and functioning (5-6 sentences). Include at least one mathematical equation or formula in your explanation.

3. Provide two specific examples of how transactions or economic activities would occur in this system, demonstrating the mathematical principle in action.

4. Analyze how this economic system could potentially offer insights into both mathematics and economics (3-4 sentences).

5. Discuss possible challenges in implementing or participating in this economic system and how they might be addressed (2-3 sentences).

6. Explore the potential societal implications of this mathematically-inspired economy, considering aspects such as wealth distribution, economic growth, and social structures (3-4 sentences).

7. Propose a simple experiment or simulation that could be conducted to test the viability of your economic system (2-3 sentences).

Format your response as follows:

Concept Explanation:
[Your explanation of the mathematical concept]

Economic System Design:
[Your description of the fictional economic system]

Economic Examples:
1. [First example]
2. [Second example]

Interdisciplinary Insights:
[Your analysis of potential insights]

Challenges and Solutions:
[Your discussion of challenges and potential solutions]

Societal Implications:
[Your exploration of potential societal implications]

Proposed Experiment:
[Your proposal for an experiment or simulation]

Ensure that your economic system is logically consistent and takes into account the specific properties of the given mathematical concept. Use appropriate economic and mathematical terminology where applicable. Be creative in your approach while maintaining scientific and economic plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The explanation of {t['concept']} and its key property ({t['key_property']}) is accurate and clear.",
            "The economic system design creatively and logically incorporates the mathematical concept.",
            "At least one relevant mathematical equation or formula is included in the explanation.",
            "The two economic examples effectively demonstrate the mathematical principle in action.",
            "The analysis of interdisciplinary insights is thoughtful and connects mathematics and economics.",
            "Challenges and potential solutions are realistic and well-considered.",
            "The exploration of societal implications is insightful and considers multiple aspects.",
            "The proposed experiment or simulation is relevant and could feasibly test the system's viability.",
            "The response is well-organized and follows the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
