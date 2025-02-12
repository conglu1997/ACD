import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            "Arctic tundra",
            "Saharan desert",
            "Amazonian rainforest",
            "Himalayan mountains",
            "Pacific island"
        ]
        cultural_contexts = [
            "Indigenous community",
            "Refugee settlement",
            "Urban renewal project",
            "Historical preservation site",
            "Multicultural educational center"
        ]
        building_types = [
            "Community center",
            "Residential complex",
            "Healthcare facility",
            "Educational institution",
            "Cultural museum"
        ]
        sustainability_challenges = [
            "Water scarcity",
            "Extreme temperature fluctuations",
            "Limited access to electricity",
            "Natural disaster vulnerability",
            "Biodiversity preservation"
        ]
        
        return {
            "1": {
                "environment": random.choice(environments),
                "cultural_context": random.choice(cultural_contexts),
                "building_type": random.choice(building_types),
                "sustainability_challenge": random.choice(sustainability_challenges)
            },
            "2": {
                "environment": random.choice(environments),
                "cultural_context": random.choice(cultural_contexts),
                "building_type": random.choice(building_types),
                "sustainability_challenge": random.choice(sustainability_challenges)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a sustainable {t['building_type']} for a {t['cultural_context']} in a {t['environment']} environment, addressing the primary sustainability challenge of {t['sustainability_challenge']}. Your response should include:\n\n1. Architectural Concept (250-300 words):\n   a) Describe the overall design concept and how it responds to the cultural context and environment.\n   b) Explain how your design incorporates sustainable features to address the primary challenge.\n   c) Discuss how the building's form and function reflect and respect local cultural values and practices.\n\n2. Technical Specifications (200-250 words):\n   a) Detail the materials and construction techniques used, emphasizing sustainability and local sourcing.\n   b) Explain the energy systems and resource management strategies employed in your design.\n   c) Describe how your design mitigates environmental impact and promotes ecosystem health.\n\n3. Cultural Integration (200-250 words):\n   a) Analyze how your design supports and enhances the community's cultural practices and social structures.\n   b) Discuss any potential cultural challenges or sensitivities addressed in your design.\n   c) Explain how local knowledge and traditions are incorporated into the building's design and function.\n\n4. Sustainability Analysis (200-250 words):\n   a) Evaluate the long-term sustainability of your design, considering environmental, social, and economic factors.\n   b) Discuss how your design addresses the primary sustainability challenge and any secondary challenges.\n   c) Propose metrics for measuring the success of your design in terms of sustainability and cultural responsiveness.\n\n5. Community Impact (150-200 words):\n   a) Predict the potential positive and negative impacts of your design on the local community.\n   b) Discuss how your design might influence local economic development and social dynamics.\n   c) Propose strategies for community engagement and participation in the building's ongoing use and maintenance.\n\n6. Innovative Features (100-150 words):\n   a) Highlight any particularly innovative or unique aspects of your design.\n   b) Explain how these features address specific challenges or opportunities presented by the project parameters.\n\n7. Ethical Considerations (100-150 words):\n   a) Discuss any ethical challenges or dilemmas encountered in the design process.\n   b) Explain how you balanced competing needs or values in your design decisions.\n\nEnsure your response demonstrates a deep understanding of sustainable architecture, cultural anthropology, and environmental science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining feasibility and cultural sensitivity.\n\nFormat your response with clear headings for each section. Your total response should be between 1200-1550 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The design effectively addresses the primary sustainability challenge while respecting the cultural context and environmental conditions.",
            "The response demonstrates a deep understanding of sustainable architecture principles and their application in the given context.",
            "The design shows cultural sensitivity and effectively integrates local knowledge and traditions.",
            "The technical specifications are well-thought-out and appropriate for the given environment and sustainability challenges.",
            "The analysis of community impact and ethical considerations is thorough and insightful.",
            "The response includes innovative features that creatively address the project's unique challenges.",
            "The writing is clear, well-structured, and effectively uses technical terminology from relevant fields."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
