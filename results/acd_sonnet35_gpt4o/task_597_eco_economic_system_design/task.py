import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'environmental_principle': 'Circular Economy',
                'economic_focus': 'Resource Allocation',
                'societal_challenge': 'Urbanization'
            },
            {
                'environmental_principle': 'Biomimicry',
                'economic_focus': 'Value Creation',
                'societal_challenge': 'Aging Population'
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a novel economic system based on the environmental principle of {t['environmental_principle']}, focusing on the economic aspect of {t['economic_focus']}, and addressing the societal challenge of {t['societal_challenge']}. Your response should include:

1. System Design (300-350 words):
   a) Describe the key features and mechanisms of your economic system.
   b) Explain how it incorporates the given environmental principle.
   c) Detail how it addresses the specified economic focus.
   d) Discuss how it takes into account the societal challenge.
   e) Provide a visual representation or diagram of your system (describe it textually).

2. Economic Analysis (250-300 words):
   a) Analyze how your system might influence production, consumption, and distribution patterns.
   b) Discuss potential impacts on employment, innovation, and economic growth.
   c) Compare your system's economic outcomes with those of current capitalist and socialist models.

3. Environmental Impact (200-250 words):
   a) Evaluate the potential environmental benefits of your system.
   b) Identify possible unintended ecological consequences and how they might be mitigated.
   c) Discuss how your system might adapt to or mitigate climate change.

4. Societal Implications (200-250 words):
   a) Explore how your system might impact social structures, values, and behaviors.
   b) Discuss potential changes in education, healthcare, and social welfare.
   c) Consider how it might influence inequality and social mobility.

5. Implementation and Transition (150-200 words):
   a) Propose a method for transitioning from current economic systems to your proposed system.
   b) Discuss challenges in adoption and how they might be overcome.
   c) Suggest policy measures or technological innovations that could support implementation.

6. Future Scenarios (150-200 words):
   a) Describe a best-case scenario for your system 50 years after implementation.
   b) Describe a worst-case scenario and potential system failures.
   c) Discuss how the system might evolve or adapt over time.

7. Critical Reflection (100-150 words):
   a) Identify potential limitations or drawbacks of your system.
   b) Discuss ethical considerations or dilemmas that might arise.
   c) Propose areas for further research or refinement of the system.

Ensure your response demonstrates a deep understanding of economics, environmental science, and social dynamics. Be creative in your design while maintaining scientific plausibility and addressing potential limitations or challenges.

Format your response with clear headings for each section, and number your paragraphs within each section. Your total response should be between 1350-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The economic system effectively incorporates the environmental principle of {t['environmental_principle']}.",
            f"The system addresses the economic focus of {t['economic_focus']} in a novel and coherent way.",
            f"The design takes into account the societal challenge of {t['societal_challenge']} and proposes relevant solutions.",
            "The response demonstrates a deep understanding of economics, environmental science, and social dynamics.",
            "The analysis considers both potential benefits and drawbacks of the proposed system, showing critical thinking.",
            "The implementation and transition plan is well-thought-out and addresses potential challenges.",
            "The future scenarios and critical reflection show an ability to consider long-term consequences and ethical implications."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
