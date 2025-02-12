import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "domain1": "Climate Science",
                "domain2": "Economics",
                "problem": "Predict the economic impact of rising sea levels on coastal cities over the next 50 years"
            },
            {
                "domain1": "Genomics",
                "domain2": "Artificial Intelligence",
                "problem": "Design a system to predict potential off-target effects in CRISPR gene editing"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a novel AI memory system inspired by the human hippocampus and neocortex, then use it to solve the following complex, multi-domain problem: {t['problem']}. Your response should include the following sections:\n\n1. Neuro-Inspired AI Memory System Design (300-350 words):\n   a) Describe the key components of your AI memory system and how they are inspired by the hippocampus and neocortex.\n   b) Explain how your system handles memory encoding, consolidation, and retrieval.\n   c) Detail any novel features that distinguish your system from existing AI memory architectures.\n   d) Discuss how your system integrates information from different domains ({t['domain1']} and {t['domain2']}).\n\n2. Neuroscientific Basis (250-300 words):\n   a) Explain the relevant functions of the hippocampus and neocortex in human memory.\n   b) Discuss how your AI system mimics or diverges from these biological processes.\n   c) Analyze potential advantages and limitations of using a neuro-inspired approach for AI memory.\n\n3. Problem-Solving Approach (250-300 words):\n   a) Outline how your AI memory system would approach solving the given problem.\n   b) Explain how the system would integrate and process information from {t['domain1']} and {t['domain2']}.\n   c) Describe any specific techniques or algorithms your system would employ.\n\n4. Simulated Output (200-250 words):\n   a) Provide a detailed description of the hypothetical output or solution your system would generate for the given problem.\n   b) Explain how this output demonstrates the capabilities of your neuro-inspired AI memory system.\n\n5. Comparative Analysis (200-250 words):\n   a) Compare your neuro-inspired approach to traditional AI methods for solving complex, multi-domain problems.\n   b) Discuss potential advantages and disadvantages of your system.\n   c) Propose a method for empirically evaluating the performance of your system against existing approaches.\n\n6. Ethical Considerations and Societal Impact (150-200 words):\n   a) Identify potential ethical concerns related to the development and use of neuro-inspired AI memory systems.\n   b) Discuss possible societal impacts of widespread adoption of such technologies.\n   c) Propose guidelines for responsible development and use of neuro-inspired AI systems.\n\n7. Future Research Directions (150-200 words):\n   a) Suggest two potential improvements or extensions to your AI memory system.\n   b) Propose a research question that arises from your system design.\n   c) Discuss how your system might contribute to our understanding of human memory and cognition.\n\nEnsure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and the specified problem domains. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.\n\nFormat your response with clear headings for each section, numbered as above. Your total response should be between 1500-1850 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, artificial intelligence, and the specified problem domains.",
            "The proposed AI memory system is innovative and scientifically plausible.",
            "The system design clearly incorporates inspiration from the hippocampus and neocortex.",
            "The problem-solving approach effectively integrates information from both specified domains.",
            "The simulated output is detailed and demonstrates the capabilities of the proposed system.",
            "The comparative analysis and ethical considerations are thoughtful and well-reasoned.",
            "The response is well-structured, clear, and within the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
