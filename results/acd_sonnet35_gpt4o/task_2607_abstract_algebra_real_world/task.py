import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "concept": "Group Theory",
                "application": "Cryptography",
                "system": "Secure Communication Protocol"
            },
            {
                "concept": "Ring Theory",
                "application": "Digital Signal Processing",
                "system": "Noise Reduction Algorithm"
            },
            {
                "concept": "Field Theory",
                "application": "Quantum Computing",
                "system": "Error Correction Code"
            },
            {
                "concept": "Lattice Theory",
                "application": "Artificial Intelligence",
                "system": "Knowledge Representation Framework"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            f"Apply concepts from {t['concept']} to design a novel {t['system']} for use in {t['application']}. Your response should include:\n\n"
            f"1. Concept Explanation (200-250 words):\n"
            f"   a) Briefly explain the key principles of {t['concept']}.\n"
            f"   b) Discuss how these principles relate to {t['application']}.\n\n"
            f"2. System Design (300-350 words):\n"
            f"   a) Describe your proposed {t['system']}.\n"
            f"   b) Explain how it incorporates principles from {t['concept']}.\n"
            f"   c) Detail the key components and their interactions.\n"
            f"   d) Provide at least one mathematical formula or theorem that underlies your design.\n\n"
            f"3. Application Analysis (200-250 words):\n"
            f"   a) Analyze how your {t['system']} would be used in {t['application']}.\n"
            f"   b) Discuss the potential advantages of your approach over traditional methods.\n"
            f"   c) Identify any limitations or potential issues with your system.\n\n"
            f"4. Interdisciplinary Connections (150-200 words):\n"
            f"   a) Explore how your system connects {t['concept']} with other fields.\n"
            f"   b) Propose a novel research question that arises from this connection.\n\n"
            f"5. Ethical Considerations (100-150 words):\n"
            f"   a) Discuss potential ethical implications of implementing your system.\n"
            f"   b) Propose guidelines for responsible development and use.\n\n"
            f"Ensure your response demonstrates a deep understanding of both the mathematical concepts and the application domain. Use appropriate technical terminology and provide clear explanations of complex ideas. Be innovative in your approach while maintaining mathematical rigor and practical feasibility.\n\n"
            f"Format your answer with clear headings for each section. Your total response should be between 950-1200 words. Include a word count at the end of your response."
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of {t['concept']} and its relevance to {t['application']}.",
            f"The proposed {t['system']} design is innovative and effectively incorporates principles from {t['concept']}.",
            "The response includes at least one relevant mathematical formula or theorem.",
            f"The analysis of the system's application in {t['application']} is thorough and identifies both advantages and limitations.",
            "The response makes meaningful interdisciplinary connections and proposes a novel research question.",
            "Ethical considerations are thoughtfully discussed with proposed guidelines for responsible use.",
            "The response demonstrates a high level of mathematical reasoning and creative problem-solving.",
            "The proposed system is innovative while maintaining mathematical rigor and practical feasibility.",
            "The response is within the specified word count range (950-1200 words)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
