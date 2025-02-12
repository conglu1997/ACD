import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environmental_problems = [
            {
                "problem": "ocean plastic pollution",
                "biological_inspiration": "marine filter feeders",
                "ai_paradigm": "swarm intelligence"
            },
            {
                "problem": "urban air pollution",
                "biological_inspiration": "plant photosynthesis",
                "ai_paradigm": "neural networks"
            },
            {
                "problem": "soil degradation",
                "biological_inspiration": "mycorrhizal networks",
                "ai_paradigm": "genetic algorithms"
            },
            {
                "problem": "invasive species management",
                "biological_inspiration": "predator-prey dynamics",
                "ai_paradigm": "reinforcement learning"
            }
        ]
        return {
            "1": random.choice(environmental_problems),
            "2": random.choice(environmental_problems)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a biologically-inspired AI system to address the environmental problem of {t['problem']}, using {t['biological_inspiration']} as your biological model and {t['ai_paradigm']} as your AI paradigm. Then, analyze its ethical implications and potential ecological impact. Your response should include:\n\n1. System Design (300-350 words):\n   a) Describe the key features of your AI system, explaining how it incorporates at least three specific principles from {t['biological_inspiration']}.\n   b) Explain how you've integrated {t['ai_paradigm']} into your system's architecture, providing at least two concrete examples.\n   c) Detail how your system would approach solving the {t['problem']} problem, outlining a step-by-step process.\n\n2. Biological-AI Integration (250-300 words):\n   a) Analyze how at least three specific mechanisms or processes from {t['biological_inspiration']} are translated into AI algorithms or structures.\n   b) Discuss two major challenges in this bio-to-AI translation and how you addressed them.\n   c) Explain how this integration enhances the system's problem-solving capabilities for {t['problem']}, providing at least one quantitative example.\n\n3. Implementation and Scalability (250-300 words):\n   a) Describe how your system would be implemented in real-world scenarios to address {t['problem']}, including necessary infrastructure and data requirements.\n   b) Discuss the scalability of your solution, addressing at least three potential limitations it might face.\n   c) Propose a method for evaluating the effectiveness of your system in addressing {t['problem']}, including specific metrics and a timeline.\n\n4. Ethical Implications (250-300 words):\n   a) Identify at least four potential ethical concerns arising from the deployment of your AI system.\n   b) Discuss how these ethical issues might be addressed or mitigated, proposing specific safeguards or policies.\n   c) Analyze the potential long-term consequences of using this system on society and the environment, considering both positive and negative outcomes.\n\n5. Ecological Impact Assessment (250-300 words):\n   a) Predict at least three potential positive and three potential negative impacts of your system on the broader ecosystem.\n   b) Discuss any unintended consequences that might arise from large-scale deployment, considering second-order effects.\n   c) Propose a comprehensive monitoring strategy to assess the ecological impact of your system over time, including specific indicators and measurement techniques.\n\nEnsure your response demonstrates a deep understanding of biological systems, AI technologies, environmental science, and ethical reasoning. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while considering real-world applicability and potential consequences. Balance creativity with scientific plausibility throughout your response.\n\nFormat your response using clear headings for each section, numbered as above. Your total response should be between 1300-1550 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately integrates at least three principles from {t['biological_inspiration']} with {t['ai_paradigm']} to address {t['problem']}.",
            "The system design is innovative, coherent, and demonstrates a deep understanding of both biological and AI systems, with concrete examples provided.",
            "The biological-AI integration section includes at least three specific mechanisms or processes and addresses two major challenges.",
            "The implementation and scalability discussion is realistic, well-reasoned, and addresses at least three potential limitations.",
            "Ethical implications are thoroughly analyzed, with at least four potential concerns identified and specific safeguards proposed.",
            "The ecological impact assessment is comprehensive, including at least three positive and three negative impacts, and a detailed monitoring strategy.",
            "The response shows creativity, interdisciplinary knowledge integration, and critical thinking throughout, while maintaining scientific plausibility.",
            "The proposed solution balances innovation with practical considerations and addresses all required elements in the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
