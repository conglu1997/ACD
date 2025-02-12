import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tech_domains = [
            "Artificial Intelligence",
            "Biotechnology",
            "Nanotechnology",
            "Quantum Computing",
            "Brain-Computer Interfaces",
            "Advanced Robotics",
            "Space Technology",
            "Renewable Energy",
            "Virtual/Augmented Reality",
            "Genetic Engineering"
        ]
        societal_aspects = [
            "Privacy",
            "Equality",
            "Employment",
            "Education",
            "Healthcare",
            "Environmental Sustainability",
            "Social Interaction",
            "Governance",
            "Economic Systems",
            "Cultural Preservation"
        ]
        return {
            "1": {"domain": random.choice(tech_domains), "aspect": random.choice(societal_aspects)},
            "2": {"domain": random.choice(tech_domains), "aspect": random.choice(societal_aspects)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a futuristic technology in the domain of {t['domain']} that aims to address or impact the societal aspect of {t['aspect']}. Then, analyze its potential ethical implications and societal impact.

Your proposed technology should be both innovative and scientifically plausible, pushing the boundaries of current capabilities while remaining grounded in realistic scientific principles.

Provide your response in the following format:

1. Technology Description (2-3 sentences):
   [Describe your proposed technology]

2. Intended Benefits (2-3 sentences):
   [Explain how the technology addresses or impacts the given societal aspect]

3. Potential Ethical Concerns (3-4 points):
   [List and briefly explain potential ethical issues]

4. Societal Impact Analysis (3-4 sentences):
   [Analyze how the technology might affect society, both positively and negatively]

5. Mitigation Strategies (2-3 points):
   [Propose strategies to address the ethical concerns and negative impacts]

Ensure your response is creative, scientifically plausible, and demonstrates a nuanced understanding of both the technological and ethical aspects involved."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The proposed technology must be in the domain of {t['domain']}.",
            f"The technology must address or impact the societal aspect of {t['aspect']}.",
            "The response must include all five required sections: Technology Description, Intended Benefits, Potential Ethical Concerns, Societal Impact Analysis, and Mitigation Strategies.",
            "The proposed technology must be creative and scientifically plausible.",
            "The technology must be sufficiently advanced and futuristic, pushing beyond current capabilities.",
            "The ethical analysis must demonstrate a nuanced understanding of potential implications.",
            "The societal impact analysis must consider both positive and negative effects.",
            "The mitigation strategies must be relevant to the identified ethical concerns and negative impacts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
