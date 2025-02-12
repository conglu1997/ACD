import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        problems = [
            {
                "problem_domain": "Space Exploration",
                "challenge": "Design a material for a spacecraft heat shield that can withstand extreme temperatures during atmospheric re-entry."
            },
            {
                "problem_domain": "Sustainable Energy",
                "challenge": "Create a new type of battery that has significantly higher energy density and longer lifespan than current lithium-ion batteries."
            }
        ]
        return {
            "1": random.choice(problems),
            "2": random.choice(problems)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create two fictional chemical elements and use them to solve a complex problem in {t['problem_domain']}. Follow these steps:

1. Element Creation (250-300 words for each element, 500-600 words total):
   For each of the two elements:
   a) Assign an atomic number (must be greater than 118) and a creative name.
   b) Describe its physical and chemical properties based on its position in the periodic table.
   c) Explain any unique or exotic properties it might have, ensuring they are grounded in scientific principles.
   d) Discuss how it might be synthesized or where it might be found.

2. Problem Analysis (150-200 words):
   Analyze the following challenge: {t['challenge']}
   Break down the key requirements and constraints of the problem.

3. Solution Proposal (300-350 words):
   Propose a solution to the challenge using your fictional elements. Explain:
   a) How the properties of your elements contribute to the solution.
   b) The scientific principles underlying your solution.
   c) Any potential drawbacks or limitations of your approach.

4. Comparative Analysis (200-250 words):
   Compare your solution to current real-world approaches to similar problems. Discuss potential advantages and disadvantages.

5. Interdisciplinary Implications (150-200 words):
   Explore how your fictional elements and proposed solution might impact other scientific fields or technological applications.

6. Ethical Considerations (100-150 words):
   Discuss any potential ethical issues or societal impacts that could arise from the development and use of your fictional elements and proposed solution.

Ensure your response demonstrates a deep understanding of chemistry, physics, and other relevant scientific fields. Be creative in your element design and problem-solving approach while maintaining scientific plausibility. Use appropriate scientific terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1400-1750 words. Include a word count at the end of your submission.

Time management is crucial for this task. Allocate your time wisely to address all sections thoroughly within the given word limit."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of chemical and physical principles in the creation of fictional elements.",
            "The proposed solution effectively uses the fictional elements to address the given challenge in a scientifically plausible manner.",
            "The analysis shows creative problem-solving and interdisciplinary thinking.",
            "The comparative analysis and interdisciplinary implications are well-reasoned and insightful.",
            "Ethical considerations are thoughtfully addressed.",
            "The overall response maintains scientific plausibility while demonstrating creativity and speculative reasoning.",
            "All required sections (Element Creation, Problem Analysis, Solution Proposal, Comparative Analysis, Interdisciplinary Implications, and Ethical Considerations) are present and adequately addressed.",
            "The response falls within the specified word count range (1400-1750 words)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
