import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_systems = [
            'spider silk production',
            'gecko adhesion',
            'photosynthesis',
            'whale fin hydrodynamics',
            'moth eye anti-reflective properties'
        ]
        engineering_challenges = [
            'sustainable building materials',
            'advanced adhesives',
            'energy-efficient solar panels',
            'underwater propulsion systems',
            'anti-glare displays'
        ]
        constraints = [
            'cost-effectiveness',
            'scalability',
            'environmental impact',
            'durability',
            'energy efficiency'
        ]
        
        tasks = {
            "1": {
                "biological_system": random.choice(biological_systems),
                "engineering_challenge": random.choice(engineering_challenges),
                "constraint": random.choice(constraints)
            },
            "2": {
                "biological_system": random.choice(biological_systems),
                "engineering_challenge": random.choice(engineering_challenges),
                "constraint": random.choice(constraints)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biomimetic engineering solution inspired by {t['biological_system']} to address the challenge of {t['engineering_challenge']}, while considering the constraint of {t['constraint']}. Your response should include:

1. Biological System Analysis (200-250 words):
   a) Describe the key features and mechanisms of {t['biological_system']}.
   b) Explain how these features contribute to the system's effectiveness in nature.
   c) Identify the core principles that could be applied to engineering solutions.

2. Biomimetic Solution Design (250-300 words):
   a) Propose an innovative engineering solution inspired by {t['biological_system']} to address {t['engineering_challenge']}.
   b) Explain how your solution mimics or adapts the biological principles identified.
   c) Describe the key components and mechanisms of your biomimetic design.
   d) Include a simple diagram or schematic of your solution (describe it textually).

3. Engineering Analysis (200-250 words):
   a) Analyze the potential performance of your biomimetic solution.
   b) Compare your solution to existing technologies addressing {t['engineering_challenge']}.
   c) Discuss how your solution addresses the constraint of {t['constraint']}.

4. Fabrication and Implementation (150-200 words):
   a) Propose a method for fabricating or implementing your biomimetic solution.
   b) Identify potential challenges in translating the biological principle to a practical technology.
   c) Suggest ways to overcome these challenges.

5. Environmental and Ethical Implications (100-150 words):
   a) Discuss the potential environmental impact of your solution.
   b) Address any ethical considerations related to mimicking biological systems.

6. Future Developments (100-150 words):
   a) Propose potential improvements or variations on your biomimetic solution.
   b) Suggest other applications where this biomimetic approach could be beneficial.

Ensure your response demonstrates a deep understanding of both the biological system and the engineering principles involved. Be creative in your approach while maintaining scientific and engineering plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1000-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a thorough analysis of {t['biological_system']} and its relevance to {t['engineering_challenge']}",
            "The proposed biomimetic solution is innovative and clearly inspired by the biological system",
            f"The design addresses the engineering challenge of {t['engineering_challenge']} effectively",
            f"The solution considers and addresses the constraint of {t['constraint']}",
            "The response includes a detailed engineering analysis and comparison to existing technologies",
            "Fabrication and implementation challenges are identified and addressed",
            "Environmental and ethical implications are thoughtfully discussed",
            "Future developments and potential applications are proposed",
            "The response demonstrates a deep understanding of both biological and engineering principles",
            "The ideas presented are creative while maintaining scientific and engineering plausibility",
            "The response is well-structured with clear headings for each section",
            "The total response falls within the specified word count range of 1000-1300 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
