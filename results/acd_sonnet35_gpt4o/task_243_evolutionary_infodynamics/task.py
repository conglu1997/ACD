import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "environment": "Deep sea hydrothermal vents",
                "constraint": "Limited energy sources",
                "information_challenge": "Efficient signal transmission in a noisy environment"
            },
            {
                "environment": "Extreme radiation planet",
                "constraint": "High mutation rate",
                "information_challenge": "Maintaining genetic stability across generations"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical biological system for organisms living in the following scenario:

Environment: {t['environment']}
Constraint: {t['constraint']}
Information Challenge: {t['information_challenge']}

Your task is to create a detailed proposal for this biological system, including:

1. Organism Design (200-250 words):
   - Describe the key features of your hypothetical organism.
   - Explain how it is adapted to the given environment and constraint.
   - Detail at least one novel biological mechanism that addresses the information challenge.

2. Information Theory Application (200-250 words):
   - Apply a specific concept from information theory to analyze your biological system.
   - Explain how this concept relates to the information challenge and the organism's survival.
   - Provide at least one equation or formal representation of your analysis.

3. Evolutionary Dynamics (200-250 words):
   - Describe how your organism might evolve over time in response to its environment and information challenge.
   - Discuss potential evolutionary trade-offs in your system.
   - Propose a mechanism for how beneficial traits related to information processing might be selected for.

4. Quantitative Model (200-250 words):
   - Develop a simple mathematical model that captures a key aspect of your biological system's information processing.
   - Explain the variables and parameters in your model.
   - Describe what insights can be gained from this model.

5. Experimental Design (150-200 words):
   - Propose an experiment to test a hypothesis about your biological system's information processing capabilities.
   - Describe the methodology, including controls and measurements.
   - Explain how the results would validate or challenge your design.

Ensure your response demonstrates a deep understanding of evolutionary biology, information theory, and their interdisciplinary applications. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility.

Format your response using clear headings for each section. Your total response should be between 950-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include all five required sections: Organism Design, Information Theory Application, Evolutionary Dynamics, Quantitative Model, and Experimental Design",
            "The proposed biological system should be creative yet scientifically plausible",
            "The response should demonstrate a clear understanding of both evolutionary biology and information theory concepts",
            "The quantitative model should be relevant and well-explained",
            "The experimental design should be logical and appropriate for testing the proposed system"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
