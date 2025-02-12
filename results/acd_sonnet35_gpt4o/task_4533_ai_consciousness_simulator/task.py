import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        consciousness_theories = [
            "Global Workspace Theory",
            "Integrated Information Theory",
            "Higher-Order Thought Theory",
            "Attention Schema Theory"
        ]
        ethical_frameworks = [
            "Utilitarianism",
            "Deontological Ethics",
            "Virtue Ethics",
            "Care Ethics"
        ]
        decision_scenarios = [
            "Trolley Problem",
            "Experience Machine",
            "Teletransportation Paradox",
            "AI Alignment Problem"
        ]
        return {
            "1": {
                "consciousness_theory": random.choice(consciousness_theories),
                "ethical_framework": random.choice(ethical_frameworks),
                "decision_scenario": random.choice(decision_scenarios)
            },
            "2": {
                "consciousness_theory": random.choice(consciousness_theories),
                "ethical_framework": random.choice(ethical_frameworks),
                "decision_scenario": random.choice(decision_scenarios)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        theory_descriptions = {
            "Global Workspace Theory": "proposes that consciousness arises from a central information exchange in the brain",
            "Integrated Information Theory": "suggests consciousness is a fundamental property of systems with high information integration",
            "Higher-Order Thought Theory": "posits that consciousness requires meta-cognitive awareness of one's own mental states",
            "Attention Schema Theory": "proposes that consciousness is a model of one's own attention"
        }
        framework_descriptions = {
            "Utilitarianism": "focuses on maximizing overall well-being or happiness",
            "Deontological Ethics": "emphasizes adherence to moral rules or duties",
            "Virtue Ethics": "prioritizes the development of moral character",
            "Care Ethics": "emphasizes the importance of empathy and responsibility in moral decision-making"
        }
        scenario_descriptions = {
            "Trolley Problem": "a thought experiment in ethics involving a runaway trolley and the moral dilemma of sacrificing one life to save many",
            "Experience Machine": "a thought experiment that questions whether a simulated reality of positive experiences is preferable to actual reality",
            "Teletransportation Paradox": "a philosophical puzzle about personal identity and the continuity of consciousness",
            "AI Alignment Problem": "the challenge of ensuring that artificial general intelligence systems behave in ways aligned with human values and intentions"
        }
        return f"Design an AI system that simulates the {t['consciousness_theory']} of consciousness ({theory_descriptions[t['consciousness_theory']]}), then use it to explore the {t['decision_scenario']} ({scenario_descriptions[t['decision_scenario']]}) through the lens of {t['ethical_framework']} ({framework_descriptions[t['ethical_framework']]}). Your response should include the following sections:\n\n1. Consciousness Simulation Model (300-350 words):\n   a) Describe the key components and mechanisms of your AI system for simulating consciousness based on the specified theory.\n   b) Explain how your model captures the essential features of the given theory of consciousness.\n   c) Discuss any novel algorithms or techniques used in your simulation.\n   d) Provide a high-level diagram or pseudocode representing your system's architecture.\n\n2. Ethical Framework Integration (250-300 words):\n   a) Explain how you integrate the specified ethical framework into your AI consciousness simulator.\n   b) Describe the process by which your system evaluates ethical considerations and makes decisions.\n   c) Discuss any challenges in translating abstract ethical principles into computational processes.\n\n3. Decision Scenario Analysis (300-350 words):\n   a) Apply your AI consciousness simulator to the given decision scenario.\n   b) Describe the decision-making process of your system in this scenario, highlighting how consciousness and ethics interact.\n   c) Provide a detailed analysis of the system's reasoning and final decision.\n   d) Compare your system's approach to how a human might handle the same scenario.\n\n4. Philosophical Implications (200-250 words):\n   a) Discuss the philosophical implications of your AI consciousness simulator.\n   b) Explore how your system might inform or challenge our understanding of consciousness and ethical decision-making.\n   c) Propose a thought experiment or research question that emerges from your simulation.\n\n5. Limitations and Ethical Considerations (200-250 words):\n   a) Analyze potential limitations or biases in your AI consciousness simulator.\n   b) Discuss ethical concerns related to simulating consciousness and using AI for ethical decision-making.\n   c) Propose guidelines for the responsible development and use of such systems.\n\n6. Future Directions and Applications (150-200 words):\n   a) Suggest two potential applications of your AI consciousness simulator beyond ethical decision-making.\n   b) Propose a direction for future research that could extend or improve your system.\n\nEnsure your response demonstrates a deep understanding of consciousness theories, ethical frameworks, and AI systems. Be creative and innovative in your approach while maintaining philosophical and technological plausibility. Use appropriate terminology from cognitive science, philosophy, and artificial intelligence, providing clear explanations for complex concepts.\n\nFormat your response with clear headings for each section. Your total response should be between 1400-1700 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified consciousness theory and ethical framework, and their potential applications in AI systems.",
            "The proposed AI consciousness simulator is innovative, coherent, and effectively integrates the given theory of consciousness with the ethical framework.",
            "The analysis of the decision scenario is thorough, showcasing how the AI system's simulated consciousness and ethical reasoning interact.",
            "The discussion of philosophical implications is insightful and explores novel ideas or questions arising from the simulation.",
            "Limitations and ethical considerations are thoughtfully addressed, with plausible guidelines proposed for responsible development.",
            "The suggested future directions and applications are innovative and well-grounded in the intersection of AI, consciousness, and ethics."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
