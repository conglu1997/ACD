class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "environmental_problem": "Urban air pollution",
                "biological_inspiration": "Plant leaves and their ability to filter air"
            },
            "2": {
                "environmental_problem": "Microplastic contamination in oceans",
                "biological_inspiration": "Filter-feeding organisms like mussels or whale sharks"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel biomimetic solution to address the environmental problem of {t['environmental_problem']}, drawing inspiration from {t['biological_inspiration']}. Your response should include:

1. Problem Analysis (200-250 words):
   a) Describe the key aspects and challenges of the given environmental problem.
   b) Analyze the current approaches to addressing this problem and their limitations.
   c) Explain the relevant biological system or process that will inspire your solution.

2. Biomimetic Solution Design (300-350 words):
   a) Present your novel biomimetic solution, clearly explaining how it addresses the environmental problem.
   b) Describe how your design mimics or is inspired by the given biological system.
   c) Explain the key components and mechanisms of your solution.
   d) Include a simple diagram or schematic of your design (describe it textually).

3. Scientific Principles (200-250 words):
   a) Discuss the biological principles underlying your solution.
   b) Explain the engineering and physical principles involved in your design.
   c) Describe how your solution integrates principles from biology, engineering, and environmental science.

4. Feasibility and Implementation (250-300 words):
   a) Analyze the technical feasibility of your solution with current or near-future technology.
   b) Discuss potential challenges in implementing your solution and how they might be overcome.
   c) Propose a method for testing and validating your solution's effectiveness.

5. Environmental Impact and Sustainability (200-250 words):
   a) Evaluate the potential environmental impact of your solution.
   b) Discuss the sustainability of your approach in terms of resources and long-term use.
   c) Compare the environmental footprint of your solution to existing approaches.

6. Broader Implications (150-200 words):
   a) Explore how your biomimetic solution might be adapted to solve other environmental or engineering challenges.
   b) Discuss the potential impact of your approach on the field of biomimicry and sustainable design.
   c) Consider any ethical implications or potential unintended consequences of your solution.

Ensure your response demonstrates a deep understanding of the relevant biological systems, engineering principles, and environmental science. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1600 words. Include a word count at the end of your submission.

Time management is crucial for this task. Allocate your time wisely to address all sections thoroughly within the given word limit."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution demonstrates a clear understanding and application of biomimicry principles.",
            "The design effectively addresses the given environmental problem.",
            "The response shows integration of knowledge from biology, engineering, and environmental science.",
            "The solution is innovative and goes beyond simply replicating existing approaches.",
            "The analysis of feasibility, implementation, and environmental impact is thorough and realistic.",
            "The response considers broader implications and potential adaptations of the solution.",
            "The submission adheres to the specified word limits and includes a word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
