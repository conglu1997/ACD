import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        moral_frameworks = [
            "Utilitarianism",
            "Deontology",
            "Virtue ethics",
            "Care ethics"
        ]
        brain_regions = [
            "Ventromedial prefrontal cortex",
            "Dorsolateral prefrontal cortex",
            "Anterior cingulate cortex",
            "Insula"
        ]
        decision_scenarios = [
            "Autonomous vehicle accident",
            "Medical resource allocation",
            "Environmental policy",
            "AI-human collaboration in the workplace"
        ]
        ethical_challenges = [
            "Trolley problem variations",
            "Privacy vs. public good",
            "Fairness and bias in AI systems",
            "Long-term consequences vs. short-term benefits"
        ]
        tasks = [
            {
                "moral_framework": mf,
                "brain_region": br,
                "decision_scenario": ds,
                "ethical_challenge": ec
            }
            for mf in moral_frameworks
            for br in brain_regions
            for ds in decision_scenarios
            for ec in ethical_challenges
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates human-like ethical decision-making based on neuroscientific models of moral cognition, focusing on the moral framework of {t['moral_framework']} and the brain region {t['brain_region']}. Then, apply your system to the decision scenario of {t['decision_scenario']}, addressing the ethical challenge of {t['ethical_challenge']}. Your response should include:

1. Neuroethical AI System Design (300-350 words):
   a) Describe the key components of your AI system for ethical decision-making.
   b) Explain how it incorporates the {t['moral_framework']} framework and models the {t['brain_region']}.
   c) Detail the algorithms or neural network architectures used in your design.
   d) Discuss how your system integrates neuroscientific insights with AI techniques.
   e) Provide a high-level diagram or flowchart of your system (describe it textually).

2. Neuroscientific Basis (250-300 words):
   a) Explain the role of the {t['brain_region']} in moral decision-making.
   b) Describe how your AI system models the neural processes in this brain region.
   c) Discuss any challenges in translating neuroscientific knowledge into AI algorithms.
   d) Explain how your system accounts for the complexity and variability of human moral cognition.

3. Ethical Framework Implementation (200-250 words):
   a) Detail how your system implements the principles of {t['moral_framework']}.
   b) Explain how these principles are translated into computational processes.
   c) Discuss any modifications or adaptations made to the framework for AI implementation.

4. Decision Scenario Analysis (250-300 words):
   a) Apply your AI system to the {t['decision_scenario']} scenario.
   b) Walk through the decision-making process step by step.
   c) Explain how the system addresses the ethical challenge of {t['ethical_challenge']}.
   d) Discuss any trade-offs or dilemmas the system encounters in this scenario.

5. Comparative Analysis (200-250 words):
   a) Compare your AI system's decision-making process to human moral reasoning.
   b) Discuss similarities and differences in approach and outcome.
   c) Analyze the strengths and limitations of your system compared to human decision-makers.

6. Ethical Implications (200-250 words):
   a) Discuss the ethical implications of using AI systems for moral decision-making.
   b) Address concerns about AI bias, transparency, and accountability in ethical reasoning.
   c) Propose guidelines for the responsible development and use of neuroethical AI systems.

7. Future Directions (150-200 words):
   a) Suggest two potential improvements or extensions to your neuroethical AI system.
   b) Discuss how advancements in neuroscience or AI might enhance ethical decision-making systems.
   c) Propose a related area of research that could further the field of AI ethics.

Ensure your response demonstrates a deep understanding of neuroscience, ethics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1550-1900 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately explains how {t['moral_framework']} is implemented in the AI system",
            f"The system design effectively models and incorporates the {t['brain_region']}",
            f"The decision scenario of {t['decision_scenario']} is thoroughly analyzed using the proposed system",
            f"The ethical challenge of {t['ethical_challenge']} is comprehensively addressed in the context of the decision scenario",
            "The response demonstrates a deep understanding of neuroscience, ethics, and artificial intelligence",
            "The proposed system and analysis are innovative while maintaining scientific plausibility",
            "The response addresses all required sections and is within the specified word count range"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
