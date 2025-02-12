import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'biological_system': 'Gecko foot adhesion',
                'engineering_challenge': 'Creating reversible adhesives for space applications'
            },
            {
                'biological_system': 'Butterfly wing nanostructures',
                'engineering_challenge': 'Developing highly efficient solar cells'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biomimetic nanotechnology solution inspired by {t['biological_system']} to address the engineering challenge of {t['engineering_challenge']}. Your response should include the following sections:

1. Biological System Analysis (200-250 words):
   a) Describe the key features and mechanisms of the biological system.
   b) Explain the nanoscale structures or processes that make this system effective.
   c) Discuss how these features relate to the engineering challenge.

2. Nanotechnology Solution Design (300-350 words):
   a) Propose a detailed nanotechnology solution inspired by the biological system.
   b) Describe the key components and their functions at the nanoscale.
   c) Explain how your design mimics or adapts the biological system's features.
   d) Discuss any novel approaches or materials in your solution.

3. Fabrication Process (200-250 words):
   a) Outline the steps to fabricate your nanotechnology solution.
   b) Describe any specialized techniques or equipment required.
   c) Address potential challenges in the manufacturing process and how to overcome them.

4. Performance Analysis (250-300 words):
   a) Predict the performance of your solution in addressing the engineering challenge.
   b) Compare your biomimetic approach to existing non-biomimetic solutions.
   c) Discuss any limitations or trade-offs in your design.
   d) Propose metrics to evaluate the success of your solution.

5. Experimental Design (200-250 words):
   a) Propose an experiment to test the efficacy of your nanotechnology solution.
   b) Describe the experimental setup, including control groups and variables.
   c) Explain how you would analyze and interpret the results.

6. Broader Implications (150-200 words):
   a) Discuss potential applications of your solution beyond the specified challenge.
   b) Address any ethical considerations or potential risks associated with your nanotechnology.
   c) Suggest future research directions based on your biomimetic approach.

Ensure your response demonstrates a deep understanding of both the biological system and nanotechnology principles. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified biological system and its nanoscale features.",
            "The proposed nanotechnology solution clearly mimics or adapts the biological system's principles.",
            "The design effectively addresses the given engineering challenge.",
            "The fabrication process is plausible and well-explained.",
            "The performance analysis includes meaningful comparisons and metrics.",
            "The experimental design is well-thought-out and appropriate for testing the solution.",
            "The response shows creativity and innovation while maintaining scientific accuracy.",
            "The broader implications and ethical considerations are thoughtfully addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
