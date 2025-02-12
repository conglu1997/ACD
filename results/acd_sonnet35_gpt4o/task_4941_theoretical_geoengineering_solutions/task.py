import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        geoengineering_approaches = [
            "Stratospheric aerosol injection",
            "Marine cloud brightening",
            "Ocean iron fertilization",
            "Space-based solar radiation management",
            "Enhanced weathering",
            "Artificial upwelling"
        ]
        focus_areas = [
            "Arctic ice preservation",
            "Reduction of urban heat islands",
            "Mitigation of extreme weather events",
            "Ocean acidification reversal",
            "Atmospheric carbon dioxide removal",
            "Global albedo modification"
        ]
        return {
            "1": {
                "approach": random.choice(geoengineering_approaches),
                "focus": random.choice(focus_areas)
            },
            "2": {
                "approach": random.choice(geoengineering_approaches),
                "focus": random.choice(focus_areas)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical geoengineering solution using the approach of {t['approach']} to address the focus area of {t['focus']}. Your response should include:

1. Solution Design (300-350 words):
   a) Describe the key components and functioning of your geoengineering solution.
   b) Explain the advanced physics principles underlying your approach.
   c) Discuss how your solution specifically addresses the given focus area.
   d) Provide a high-level diagram or mathematical representation of a key aspect of your solution (describe it textually).

2. Environmental Impact Analysis (250-300 words):
   a) Analyze the potential positive and negative environmental impacts of your solution.
   b) Discuss any unintended consequences and how they might be mitigated.
   c) Explain how your solution interacts with other Earth systems (e.g., atmosphere, hydrosphere, biosphere).

3. Feasibility and Scalability (200-250 words):
   a) Assess the technical feasibility of implementing your solution with current or near-future technology.
   b) Discuss the scalability of your approach to achieve a significant global impact.
   c) Identify key technological or scientific breakthroughs needed to fully realize your solution.

4. Geopolitical Implications (200-250 words):
   a) Analyze potential international cooperation or conflicts arising from the development and deployment of your solution.
   b) Discuss how your geoengineering approach might affect global power dynamics.
   c) Consider legal and governance challenges in implementing your solution on a global scale.

5. Ethical Considerations (150-200 words):
   a) Identify key ethical issues related to your geoengineering solution.
   b) Discuss the moral implications of intentionally modifying Earth's climate systems.
   c) Propose guidelines for responsible research and potential implementation of your solution.

6. Comparative Analysis (200-250 words):
   a) Compare your solution to at least two other geoengineering approaches or conventional climate change mitigation strategies.
   b) Discuss the relative advantages and disadvantages of your approach.
   c) Explain how your solution could complement or conflict with other climate interventions.

Ensure your response demonstrates a deep understanding of climate science, advanced physics, and global politics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and considering real-world constraints.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The solution uses the specified approach of {t['approach']} and addresses the focus area of {t['focus']}",
            "The response demonstrates a deep understanding of advanced physics principles and climate science",
            "The environmental impact analysis is thorough and considers multiple Earth systems",
            "The feasibility and scalability assessment is realistic and identifies key challenges",
            "The geopolitical implications are thoughtfully analyzed",
            "Ethical considerations are addressed comprehensively",
            "The comparative analysis provides meaningful insights into the proposed solution's strengths and weaknesses",
            "The overall response is innovative while maintaining scientific plausibility"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
