import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "dimension": 4,
                "object": "tesseract",
                "problem": "Calculate the surface area of a 4-dimensional hypersphere inscribed within a tesseract."
            },
            {
                "dimension": 5,
                "object": "5-cube",
                "problem": "Determine the number of 3-dimensional cross-sections possible when slicing a 5-cube with a hyperplane."
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system for visualizing and manipulating {t['dimension']}-dimensional geometric objects, with a focus on the {t['object']}. Then, use your system to solve the following problem and propose novel applications. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your visualization system.
   b) Explain how it represents and manipulates {t['dimension']}-dimensional objects.
   c) Detail any novel algorithms or techniques used in your design.
   d) Include a simple diagram or pseudocode to illustrate your system's architecture.

2. Visualization Technique (200-250 words):
   a) Explain your method for projecting {t['dimension']}-dimensional objects onto a 2D or 3D display.
   b) Describe how users can interact with and manipulate the {t['object']} in your system.
   c) Discuss any challenges in representing higher-dimensional objects and how you address them.

3. Problem Solution (200-250 words):
   Use your system to solve the following problem:
   {t['problem']}
   Provide a step-by-step explanation of how your system aids in solving this problem, including any visualizations or manipulations used.

4. Mathematical Analysis (150-200 words):
   a) Discuss the mathematical principles underlying your visualization system.
   b) Explain how your system maintains mathematical accuracy when projecting to lower dimensions.
   c) Analyze any trade-offs between mathematical precision and visual intuitiveness in your design.

5. Novel Applications (200-250 words):
   a) Propose two novel applications of your hyperdimensional visualization system outside of pure mathematics.
   b) Explain how each application could benefit from the ability to visualize and manipulate higher-dimensional objects.
   c) Discuss any modifications needed to adapt your system for these applications.

6. Cognitive Implications (150-200 words):
   a) Analyze how your system might affect users' understanding of higher-dimensional geometry.
   b) Discuss potential cognitive benefits or challenges in using your system for mathematical reasoning.
   c) Propose an experiment to measure the impact of your system on spatial reasoning skills.

Ensure your response demonstrates a deep understanding of higher-dimensional geometry, visualization techniques, and creative problem-solving. Use appropriate mathematical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining mathematical rigor and plausibility.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The system architecture for visualizing and manipulating higher-dimensional objects is well-designed and explained clearly.",
            "The visualization technique effectively addresses the challenges of representing higher-dimensional objects.",
            "The problem solution demonstrates correct application of the visualization system and mathematical principles.",
            "The mathematical analysis shows a deep understanding of the principles underlying higher-dimensional geometry and visualization.",
            "The proposed novel applications are creative and well-reasoned.",
            "The discussion of cognitive implications demonstrates insight into the relationship between visualization and mathematical understanding."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
