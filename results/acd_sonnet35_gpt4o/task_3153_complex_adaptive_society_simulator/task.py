import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        society_types = [
            "Post-scarcity",
            "Resource-constrained",
            "Information-driven",
            "Hierarchical"
        ]
        environmental_factors = [
            "Climate change",
            "Technological disruption",
            "Pandemic",
            "Interplanetary colonization"
        ]
        social_dynamics = [
            "Cooperation vs. competition",
            "Innovation vs. tradition",
            "Individualism vs. collectivism",
            "Centralization vs. decentralization"
        ]
        tasks = {}
        for i in range(1, 3):
            society = random.choice(society_types)
            environment = random.choice(environmental_factors)
            dynamic = random.choice(social_dynamics)
            tasks[str(i)] = {"society": society, "environment": environment, "dynamic": dynamic}
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a complex adaptive system simulation to model the evolution of a {t['society']} society facing {t['environment']}, with a focus on the dynamic of {t['dynamic']}. Your response should include:\n\n1. System Architecture (300-350 words):\n   a) Describe the key components of your complex adaptive system model.\n   b) Explain how you incorporate the specified society type, environmental factor, and social dynamic.\n   c) Detail the interactions and feedback loops between different system components.\n   d) Discuss any novel computational approaches used to model societal complexity.\n\n2. Agent-Based Modeling (250-300 words):\n   a) Describe the types of agents in your simulation and their characteristics.\n   b) Explain the rules governing agent behavior and decision-making processes.\n   c) Discuss how agent interactions lead to emergent societal phenomena.\n\n3. Environmental Dynamics (200-250 words):\n   a) Detail how you model the specified environmental factor in your simulation.\n   b) Explain how environmental changes affect agent behavior and system dynamics.\n   c) Describe any feedback mechanisms between society and the environment.\n\n4. Social Dynamics Implementation (250-300 words):\n   a) Explain how you model the specified social dynamic in your simulation.\n   b) Describe the metrics used to measure this dynamic over time.\n   c) Discuss how this dynamic influences overall societal evolution.\n\n5. Simulation Outcomes (200-250 words):\n   a) Describe potential scenarios or outcomes that your simulation might produce.\n   b) Explain how these outcomes emerge from the complex interactions within the system.\n   c) Discuss the implications of these outcomes for understanding real-world societal evolution.\n\n6. Ethical Considerations and Limitations (150-200 words):\n   a) Discuss potential ethical issues related to modeling societal evolution.\n   b) Analyze the limitations of your simulation in capturing real-world complexity.\n   c) Propose guidelines for responsible development and use of such simulations.\n\n7. Future Directions (100-150 words):\n   a) Suggest two potential improvements or extensions to your complex adaptive society simulator.\n   b) Propose a related research question that could further our understanding of societal evolution and complex systems.\n\nEnsure your response demonstrates a deep understanding of complex systems theory, social sciences, and computational modeling. Use appropriate terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1450-1800 words. Include a word count at the end of your response."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of complex adaptive systems and their application to modeling {t['society']} societies",
            f"The simulation effectively incorporates the environmental factor of {t['environment']}",
            f"The model adequately captures the social dynamic of {t['dynamic']}",
            "The agent-based modeling approach is well-explained and appropriate for the given scenario",
            "The simulation outcomes and their implications are thoughtfully analyzed",
            "The ethical considerations and limitations are thoroughly addressed",
            "The proposed future directions are innovative and promising for advancing the field",
            "The response adheres to the specified word count and formatting guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
