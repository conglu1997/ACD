import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'tech_advancement': 'Widespread adoption of fusion energy',
                'geopolitical_shift': 'Formation of a unified African Union as a global superpower',
                'environmental_change': 'Sea level rise of 1 meter'
            },
            {
                'tech_advancement': 'Development of efficient atmospheric carbon capture technology',
                'geopolitical_shift': 'Dissolution of current nation-states into city-states and regional blocs',
                'environmental_change': 'Desertification of 30% of current arable land'
            },
            {
                'tech_advancement': 'Mastery of weather control technology',
                'geopolitical_shift': 'Establishment of permanent lunar and Martian colonies with political representation',
                'environmental_change': 'Thawing of all permafrost regions'
            },
            {
                'tech_advancement': 'Creation of artificial photosynthesis systems at industrial scale',
                'geopolitical_shift': 'Formation of a global AI-assisted direct democracy',
                'environmental_change': 'Collapse of major ocean currents altering global weather patterns'
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a global climate governance system for the year 2100, taking into account the following projected changes:

1. Technological advancement: {t['tech_advancement']}
2. Geopolitical shift: {t['geopolitical_shift']}
3. Environmental change: {t['environmental_change']}

Your response should include the following sections:

1. System Overview (200-250 words):
   a) Provide a high-level description of your global climate governance system.
   b) Explain how it addresses the given technological, geopolitical, and environmental changes.
   c) Outline the key principles and goals of your governance system.

2. Institutional Structure (250-300 words):
   a) Describe the main institutions or bodies that comprise your governance system.
   b) Explain their roles, responsibilities, and relationships to one another.
   c) Discuss how these institutions ensure global representation and accountability.

3. Decision-Making Processes (200-250 words):
   a) Outline the key decision-making processes in your governance system.
   b) Explain how these processes balance efficiency with inclusivity and fairness.
   c) Describe any novel voting or consensus-building mechanisms you've incorporated.

4. Enforcement and Compliance (200-250 words):
   a) Describe how your system ensures compliance with global climate agreements.
   b) Explain any enforcement mechanisms or incentive structures you've designed.
   c) Discuss how your system addresses potential conflicts or non-compliance.

5. Adaptive Mechanisms (150-200 words):
   a) Explain how your governance system can adapt to unforeseen future changes.
   b) Describe any built-in review or amendment processes.
   c) Discuss how your system balances stability with flexibility.

6. Ethical Considerations (150-200 words):
   a) Discuss the ethical implications of your proposed governance system.
   b) Address potential criticisms or concerns about the system.
   c) Explain how your system ensures fairness and protects human rights.

Ensure your response demonstrates a deep understanding of climate science, political systems, and future trends. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while considering real-world constraints and challenges.

Format your response using clear headings for each section. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of climate science, political systems, and future trends.",
            "The proposed governance system effectively addresses the given technological, geopolitical, and environmental changes.",
            "The institutional structure and decision-making processes are well-designed and logically consistent.",
            "The system includes innovative yet plausible solutions for enforcement, compliance, and adaptation.",
            "Ethical considerations are thoughtfully addressed, and potential criticisms are acknowledged.",
            "The response is well-structured, clear, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
