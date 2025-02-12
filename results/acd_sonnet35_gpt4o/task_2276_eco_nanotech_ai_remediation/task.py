import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environmental_issues = [
            {
                "issue": "Microplastic pollution in oceans",
                "location": "Great Pacific Garbage Patch",
                "scale": "Global"
            },
            {
                "issue": "Heavy metal contamination in soil",
                "location": "Former industrial sites in Eastern Europe",
                "scale": "Regional"
            }
        ]
        return {
            "1": random.choice(environmental_issues),
            "2": random.choice(environmental_issues)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI-driven nanotechnology system for environmental remediation of {t['issue']} in {t['location']}, and analyze its potential ecological impact. Your response should include:\n\n1. Nanotechnology Design (250-300 words):\n   a) Describe the nanoparticles or nanostructures you would use for remediation.\n   b) Explain their mechanism of action in addressing the environmental issue.\n   c) Discuss any novel properties or functionalities of your nanotechnology.\n\n2. AI Integration (200-250 words):\n   a) Explain how AI would be integrated into your nanotechnology system.\n   b) Describe the role of AI in optimizing the remediation process.\n   c) Discuss any machine learning algorithms or techniques you would employ.\n\n3. Implementation Strategy (200-250 words):\n   a) Outline a plan for deploying your system in the specified location.\n   b) Discuss any challenges specific to the {t['scale']} scale of the issue.\n   c) Propose methods for monitoring and controlling the nanotechnology post-deployment.\n\n4. Ecological Impact Analysis (250-300 words):\n   a) Analyze potential positive and negative impacts of your system on the local ecosystem.\n   b) Discuss any long-term effects or unintended consequences.\n   c) Propose methods to mitigate any potential ecological risks.\n\n5. Ethical and Regulatory Considerations (150-200 words):\n   a) Discuss ethical implications of using AI-driven nanotechnology for environmental remediation.\n   b) Propose guidelines for responsible development and deployment of such systems.\n   c) Suggest regulatory frameworks that might be necessary for this technology.\n\n6. Future Developments (150-200 words):\n   a) Suggest potential improvements or extensions to your system.\n   b) Discuss how advancements in AI or nanotechnology could enhance environmental remediation.\n   c) Propose a novel research direction that arises from this intersection of technologies.\n\nEnsure your response demonstrates a deep understanding of environmental science, nanotechnology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1200-1500 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of environmental science, nanotechnology, and artificial intelligence.",
            "The proposed nanotechnology system is innovative and scientifically plausible.",
            "The AI integration is well-explained and relevant to the remediation process.",
            "The ecological impact analysis is comprehensive and considers both positive and negative effects.",
            "Ethical and regulatory considerations are thoughtfully addressed.",
            "The response is well-structured and adheres to the specified format and word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
