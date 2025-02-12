import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        applications = [
            {
                "field": "medicine",
                "quantum_effect": "quantum coherence",
                "biological_process": "photosynthesis",
                "application_area": "drug delivery"
            },
            {
                "field": "agriculture",
                "quantum_effect": "quantum tunneling",
                "biological_process": "enzyme catalysis",
                "application_area": "crop yield optimization"
            },
            {
                "field": "medicine",
                "quantum_effect": "quantum entanglement",
                "biological_process": "DNA mutation",
                "application_area": "cancer treatment"
            },
            {
                "field": "agriculture",
                "quantum_effect": "quantum superposition",
                "biological_process": "magnetoreception",
                "application_area": "pest control"
            }
        ]
        return {
            "1": random.choice(applications),
            "2": random.choice(applications)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a theoretical application of quantum biology principles to solve a real-world problem in {t['field']}, focusing on the quantum effect of {t['quantum_effect']} in the biological process of {t['biological_process']}. Your goal is to develop an innovative solution in the area of {t['application_area']}. Your response should include:\n\n1. Quantum Biology Principle (200-250 words):\n   a) Explain the quantum effect of {t['quantum_effect']} and how it relates to {t['biological_process']}.\n   b) Discuss current scientific understanding of this quantum biological phenomenon.\n   c) Describe any existing or proposed applications of this principle.\n\n2. Innovative Application Design (250-300 words):\n   a) Present your theoretical application for {t['application_area']} using the described quantum biology principle.\n   b) Explain how your application leverages {t['quantum_effect']} in {t['biological_process']} to achieve its goal.\n   c) Describe the potential benefits and advantages of your application over conventional approaches.\n   d) Discuss any technical challenges in implementing your application and propose potential solutions.\n\n3. Scientific Feasibility Analysis (200-250 words):\n   a) Evaluate the scientific feasibility of your proposed application based on current knowledge and technology.\n   b) Identify key areas where further research or technological advancements are needed.\n   c) Propose an experiment or study to validate a critical aspect of your application.\n\n4. Interdisciplinary Implications (150-200 words):\n   a) Discuss how your application integrates knowledge from quantum physics, biology, and {t['field']}.\n   b) Explain potential impacts of your application on related scientific fields or industries.\n   c) Suggest potential collaborations or research directions inspired by your application.\n\n5. Ethical Considerations (150-200 words):\n   a) Identify potential ethical issues or concerns raised by your application.\n   b) Discuss how these ethical considerations might be addressed or mitigated.\n   c) Propose guidelines for the responsible development and use of quantum biology applications in {t['field']}.\n\n6. Future Prospects (100-150 words):\n   a) Speculate on future developments in quantum biology and their potential impact on {t['field']}.\n   b) Suggest areas for future research building on your proposed application.\n\nEnsure your response demonstrates a deep understanding of quantum physics, biology, and {t['field']}. Use technical terminology appropriately and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility and logical consistency.\n\nFormat your response using clear headings for each section. Your total response should be between 1050-1350 words. Include a word count at the end of your response."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates understanding of {t['quantum_effect']} and its relation to {t['biological_process']}.",
            f"The proposed application for {t['application_area']} is innovative and leverages the quantum biology principle.",
            "The scientific feasibility analysis is thorough and identifies key research needs.",
            f"The response integrates knowledge from quantum physics, biology, and {t['field']}.",
            "Ethical considerations are thoughtfully explored and addressed.",
            "The response adheres to the specified word count range and formatting requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
