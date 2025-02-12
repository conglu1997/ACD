import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "ecosystem_type": "Marine",
                "ai_agent_role": "Predator",
                "biological_focus": "Symbiotic relationships",
                "evolutionary_pressure": "Climate change"
            },
            {
                "ecosystem_type": "Terrestrial",
                "ai_agent_role": "Decomposer",
                "biological_focus": "Genetic diversity",
                "evolutionary_pressure": "Resource scarcity"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design and analyze an artificial ecosystem where evolving AI agents and simulated biological organisms coexist and co-evolve. Focus on a {t['ecosystem_type']} ecosystem where AI agents play the role of {t['ai_agent_role']}. Pay special attention to {t['biological_focus']} and consider {t['evolutionary_pressure']} as a key evolutionary pressure. Then, explore the implications for understanding complex adaptive systems and AI development. Your response should include:\n\n1. Ecosystem Design (300-350 words):\n   a) Describe the key components of your artificial ecosystem, including both AI agents and biological organisms.\n   b) Explain how AI agents are integrated into the ecosystem and how they interact with biological organisms.\n   c) Detail the mechanisms for evolution and adaptation in both AI agents and biological organisms.\n   d) Discuss how you've incorporated the specified evolutionary pressure into your ecosystem model.\n\n2. Co-evolution Dynamics (250-300 words):\n   a) Analyze how AI agents and biological organisms might co-evolve in your ecosystem.\n   b) Explain how the specified biological focus influences the co-evolutionary process.\n   c) Describe potential emergent behaviors or properties that might arise from this co-evolution.\n   d) Propose a mathematical model or algorithm to simulate this co-evolutionary process.\n\n3. Simulation and Analysis (200-250 words):\n   a) Outline a method for simulating your ecosystem over multiple generations.\n   b) Describe key metrics or indicators you would use to analyze the ecosystem's development.\n   c) Propose an experiment to test a specific hypothesis about your ecosystem's behavior.\n\n4. Implications for Complex Systems (200-250 words):\n   a) Discuss how your ecosystem model could inform our understanding of complex adaptive systems.\n   b) Analyze potential insights into natural ecosystem dynamics that could be gained from your model.\n   c) Explain how this model might challenge or extend current theories in ecology or evolutionary biology.\n\n5. AI Development Insights (200-250 words):\n   a) Explore how the co-evolution process in your ecosystem could inform AI development strategies.\n   b) Discuss potential applications of your model in developing more adaptive and robust AI systems.\n   c) Analyze ethical considerations in creating AI systems that can evolve in complex environments.\n\n6. Limitations and Future Directions (150-200 words):\n   a) Acknowledge potential limitations or simplifications in your ecosystem model.\n   b) Propose future research directions or expansions of your model.\n   c) Speculate on long-term implications of such ecosystem simulations for science and technology.\n\nEnsure your response demonstrates a deep understanding of evolutionary biology, artificial intelligence, and complex systems theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1300-1600 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of evolutionary biology, artificial intelligence, and complex systems theory.",
            "The ecosystem design is innovative, coherent, and scientifically plausible.",
            "The co-evolution dynamics are well-explained and consider both AI agents and biological organisms.",
            "The simulation and analysis methods are clearly described and appropriate for the ecosystem model.",
            "The implications for complex systems and AI development are thoughtfully explored.",
            "The response is well-structured, within the specified word count, and uses appropriate technical terminology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
