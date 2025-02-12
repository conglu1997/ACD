import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        urban_problems = [
            "Water scarcity",
            "Air pollution",
            "Urban heat islands",
            "Waste management",
            "Traffic congestion",
            "Energy efficiency"
        ]
        biological_inspirations = [
            "Lotus leaf",
            "Termite mounds",
            "Spider silk",
            "Butterfly wings",
            "Whale fins",
            "Gecko feet"
        ]
        tasks = {
            "1": {
                "urban_problem": random.choice(urban_problems),
                "biological_inspiration": random.choice(biological_inspirations)
            },
            "2": {
                "urban_problem": random.choice(urban_problems),
                "biological_inspiration": random.choice(biological_inspirations)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biomimetic engineering solution for the urban problem of {t['urban_problem']}, inspired by the biological structure or process of {t['biological_inspiration']}. Your response should include:

        1. Biomimetic Solution Design (300-350 words):
           a) Describe the key features of your biomimetic solution.
           b) Explain how it addresses the urban problem.
           c) Detail how it mimics or is inspired by the given biological structure or process.
           d) Include a simple diagram or schematic of your solution using ASCII art.

        2. Scientific Principles (200-250 words):
           a) Explain the biological principles underlying your chosen inspiration.
           b) Discuss how these principles are translated into engineering concepts in your solution.
           c) Identify any challenges in adapting the biological system to an urban context.

        3. Implementation and Scalability (200-250 words):
           a) Describe the steps needed to implement your solution in a real urban environment.
           b) Discuss how your solution could be scaled up or adapted to different urban contexts.
           c) Identify potential obstacles to implementation and propose strategies to overcome them.

        4. Environmental Impact Analysis (150-200 words):
           a) Analyze the potential environmental impacts (positive and negative) of your solution.
           b) Compare its environmental footprint to traditional solutions for the same urban problem.
           c) Suggest ways to minimize any negative environmental impacts.

        5. Socioeconomic Implications (150-200 words):
           a) Discuss the potential social and economic impacts of implementing your solution.
           b) Consider both short-term and long-term effects on urban communities.
           c) Address any potential equity issues in the implementation or access to your solution.

        6. Future Developments (100-150 words):
           a) Propose two potential improvements or extensions to your biomimetic solution.
           b) Suggest a novel research direction that could enhance the effectiveness of your approach.

        Ensure your response demonstrates a deep understanding of both biological systems and urban engineering challenges. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and addressing practical considerations.

        Format your response with clear headings for each section. Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both biological systems and urban engineering challenges.",
            "The biomimetic solution effectively addresses the given urban problem and clearly draws inspiration from the specified biological structure or process.",
            "The scientific principles are accurately explained and well-translated into engineering concepts.",
            "The implementation and scalability analysis is thorough and realistic.",
            "The environmental impact analysis is comprehensive and considers both positive and negative effects.",
            "The socioeconomic implications are thoughtfully discussed, including potential equity issues.",
            "The proposed future developments and research directions are innovative and relevant.",
            "The response is well-structured, adheres to the word count, and uses appropriate technical terminology.",
            "The ASCII art diagram effectively illustrates the key features of the biomimetic solution."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
