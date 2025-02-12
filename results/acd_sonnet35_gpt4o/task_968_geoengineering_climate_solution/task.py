import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "climate_issue": "Ocean acidification",
                "geoengineering_approach": "Ocean alkalinization",
                "constraint": "Minimize disruption to marine ecosystems"
            },
            {
                "climate_issue": "Global warming",
                "geoengineering_approach": "Stratospheric aerosol injection",
                "constraint": "Ensure equitable global temperature reduction"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Geoengineering has been proposed as a potential solution to address various aspects of climate change. In this task, you will design and analyze a specific geoengineering solution, considering its scientific basis, potential impacts, and ethical implications.\n\nYour task: Design and analyze a geoengineering solution to combat {t['climate_issue']} using the approach of {t['geoengineering_approach']}, while addressing the constraint: {t['constraint']}. Your response should include the following sections:\n\n1. Solution Design (250-300 words):\n   a) Describe the key components and mechanisms of your geoengineering solution.\n   b) Explain how it specifically addresses {t['climate_issue']}.\n   c) Discuss how your design considers the constraint: {t['constraint']}.\n   d) Include a simple diagram or schematic representation of your solution (describe it in words, as if you were explaining a visual representation).\n\n2. Scientific Principles (200-250 words):\n   a) Explain the underlying scientific principles that make your solution effective for {t['climate_issue']}.\n   b) Discuss any relevant chemical, physical, or biological processes involved.\n   c) Address potential interactions between your solution and existing Earth systems.\n\n3. Implementation and Scalability (200-250 words):\n   a) Outline a plan for implementing your solution on a global scale.\n   b) Discuss technological and logistical challenges in deployment.\n   c) Propose methods to monitor and control the effects of your solution.\n\n4. Environmental Impact Assessment (200-250 words):\n   a) Analyze potential short-term and long-term environmental impacts of your solution.\n   b) Discuss any unintended consequences or side effects, particularly in relation to {t['constraint']}.\n   c) Propose mitigation strategies for identified negative impacts.\n\n5. Socioeconomic and Political Considerations (150-200 words):\n   a) Discuss the potential socioeconomic impacts of implementing your solution.\n   b) Address international cooperation and governance challenges.\n   c) Propose a framework for equitable implementation and benefit-sharing.\n\n6. Ethical Analysis (150-200 words):\n   a) Identify and discuss key ethical concerns related to your geoengineering solution.\n   b) Analyze the moral implications of intervening in Earth's climate systems to address {t['climate_issue']}.\n   c) Propose ethical guidelines for the development and use of your solution.\n\n7. Alternative Approaches (100-150 words):\n   a) Briefly discuss two alternative geoengineering approaches to address {t['climate_issue']}.\n   b) Compare their potential effectiveness and drawbacks to your proposed solution.\n\nEnsure your response demonstrates a deep understanding of climate science, environmental systems, and geoengineering principles. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and addressing real-world constraints.\n\nFormat your response with clear headings for each section. Adhere to the specified word count for each section, and ensure your total response is between 1250-1600 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of climate science, environmental systems, and geoengineering principles.",
            f"The proposed solution is innovative yet scientifically plausible and specifically addresses {t['climate_issue']} while considering the constraint: {t['constraint']}.",
            "The analysis covers all required sections comprehensively, including scientific principles, implementation, environmental impact, socioeconomic considerations, and ethical implications.",
            "The response shows evidence of systems thinking and considers potential unintended consequences and interactions with Earth systems.",
            "The ethical analysis is thoughtful and considers multiple perspectives on intervening in Earth's climate systems.",
            "The response is well-structured, uses appropriate scientific terminology, and provides clear explanations for complex concepts.",
            "The total response falls within the specified word count range (1250-1600 words) and uses clear headings for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
