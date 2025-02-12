import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        engineering_problems = [
            {
                "problem": "Urban water management",
                "description": "Design a system to efficiently collect, distribute, and recycle water in a large city"
            },
            {
                "problem": "Renewable energy storage",
                "description": "Develop a method to store and distribute renewable energy efficiently across a power grid"
            },
            {
                "problem": "Sustainable building design",
                "description": "Create an energy-efficient building design that minimizes environmental impact"
            },
            {
                "problem": "Traffic flow optimization",
                "description": "Develop a system to reduce traffic congestion and improve transportation efficiency in urban areas"
            }
        ]
        biological_inspirations = [
            {
                "inspiration": "Termite mounds",
                "description": "Complex structures with sophisticated ventilation and temperature regulation systems"
            },
            {
                "inspiration": "Photosynthesis",
                "description": "The process by which plants convert light energy into chemical energy"
            },
            {
                "inspiration": "Slime mold networks",
                "description": "Efficient resource distribution systems created by simple organisms"
            },
            {
                "inspiration": "Gecko adhesion",
                "description": "Micro-scale structures that allow geckos to adhere to various surfaces"
            }
        ]
        return {
            "1": {
                "engineering_problem": random.choice(engineering_problems),
                "biological_inspiration": random.choice(biological_inspirations)
            },
            "2": {
                "engineering_problem": random.choice(engineering_problems),
                "biological_inspiration": random.choice(biological_inspirations)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a nature-inspired algorithm to solve the engineering problem of {t['engineering_problem']['problem']}, using the biological inspiration of {t['biological_inspiration']['inspiration']}. Then, analyze its potential environmental impact and sustainability. Your response should include the following sections:

1. Problem Analysis (150-200 words):
   a) Analyze the engineering problem: {t['engineering_problem']['description']}
   b) Explain why this problem is challenging and suitable for a biomimetic approach.
   c) Identify key parameters and constraints of the problem.

2. Biological Inspiration Analysis (150-200 words):
   a) Describe the key features and mechanisms of {t['biological_inspiration']['inspiration']}: {t['biological_inspiration']['description']}
   b) Explain how these features could be relevant to solving the engineering problem.
   c) Identify any challenges in translating biological principles to engineering solutions.

3. Biomimetic Algorithm Design (300-350 words):
   a) Present a high-level design of your nature-inspired algorithm.
   b) Explain how it incorporates principles from the biological inspiration.
   c) Describe the key steps or components of the algorithm.
   d) Discuss how the algorithm addresses the specific challenges of the engineering problem.
   e) Provide a pseudo-code or flowchart representation of your algorithm.

4. Implementation Strategy (200-250 words):
   a) Outline the steps to implement your algorithm in a real-world setting.
   b) Describe any necessary data structures or computational resources.
   c) Discuss potential challenges in implementation and propose solutions.
   d) Provide at least one specific example of how your algorithm would handle a real-world scenario.

5. Performance Analysis (150-200 words):
   a) Predict the expected performance of your algorithm compared to traditional approaches.
   b) Identify potential advantages and limitations of your biomimetic solution.
   c) Propose metrics to evaluate the effectiveness of your solution.
   d) Provide a hypothetical quantitative comparison between your solution and a conventional approach.

6. Environmental Impact and Sustainability Analysis (200-250 words):
   a) Analyze the potential environmental impacts of implementing your solution.
   b) Discuss how your biomimetic approach contributes to sustainability.
   c) Compare the environmental footprint of your solution to conventional approaches.
   d) Propose ways to further enhance the sustainability of your solution.
   e) Estimate the potential reduction in resource consumption or emissions (provide specific numbers).

7. Future Directions (100-150 words):
   a) Suggest two potential improvements or extensions to your algorithm.
   b) Discuss how your approach could be applied to other engineering or environmental challenges.

Ensure your response demonstrates a deep understanding of the biological principles, engineering concepts, and environmental considerations involved. Be creative in your algorithm design while maintaining scientific and practical plausibility. Use clear headings for each section of your response.

Your total response should be between 1250-1600 words. Include a word count at the end of each section and a total word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a thorough understanding of the engineering problem and biological inspiration.",
            "The biomimetic algorithm design is innovative, detailed, and clearly inspired by the given biological system.",
            "A pseudo-code or flowchart representation of the algorithm is provided.",
            "The implementation strategy is well-explained and includes a specific real-world example.",
            "The performance analysis includes a hypothetical quantitative comparison with conventional approaches.",
            "The environmental impact and sustainability analysis provides specific estimates of resource or emission reductions.",
            "The response shows strong interdisciplinary reasoning, combining insights from biology, engineering, and environmental science.",
            "The writing is clear, well-structured, and adheres to the specified format and word limits for each section.",
            "Word counts for each section and the total submission are provided and within the specified ranges."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
