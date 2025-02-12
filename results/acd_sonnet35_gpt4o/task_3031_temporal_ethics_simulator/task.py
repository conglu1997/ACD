import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "era": "World War II",
                "ethical_dilemma": "Preventing a historical atrocity",
                "paradox": "Grandfather paradox"
            },
            {
                "era": "Industrial Revolution",
                "ethical_dilemma": "Accelerating technological progress",
                "paradox": "Predestination paradox"
            },
            {
                "era": "Ancient Rome",
                "ethical_dilemma": "Saving a historical figure",
                "paradox": "Butterfly effect"
            },
            {
                "era": "Near future",
                "ethical_dilemma": "Preventing an environmental disaster",
                "paradox": "Information paradox"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design and analyze a time travel scenario set in the {t['era']} era, focusing on the ethical dilemma of {t['ethical_dilemma']} and incorporating the {t['paradox']}. Your response should include:\n\n1. Scenario Design (250-300 words):\n   a) Describe a detailed time travel scenario that incorporates the given ethical dilemma and paradox.\n   b) Explain the potential consequences of intervention in this historical period.\n   c) Discuss how the specified paradox complicates the scenario.\n\n2. Temporal Logic Analysis (200-250 words):\n   a) Analyze the logical consistency of the timeline in your scenario.\n   b) Identify any potential temporal contradictions or loopholes.\n   c) Propose a resolution to maintain logical consistency, if possible.\n\n3. Ethical Implications (250-300 words):\n   a) Discuss the ethical considerations of intervening in this historical event.\n   b) Analyze the scenario using at least two different ethical frameworks (e.g., utilitarianism, deontology, virtue ethics).\n   c) Explain how time travel complicates traditional ethical decision-making.\n\n4. Decision and Consequences (200-250 words):\n   a) Propose a course of action for the time traveler in this scenario.\n   b) Justify your decision based on both ethical and logical considerations.\n   c) Describe the potential short-term and long-term consequences of this action.\n\n5. Philosophical Implications (150-200 words):\n   a) Discuss how this scenario challenges our understanding of free will and determinism.\n   b) Explore the implications of your scenario for the nature of time and causality.\n\n6. Comparative Analysis (150-200 words):\n   a) Compare your scenario to a similar ethical dilemma without time travel.\n   b) Analyze how the introduction of time travel alters the ethical and logical considerations.\n\nEnsure your response demonstrates a deep understanding of temporal logic, ethical philosophy, and creative problem-solving. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining logical consistency.\n\nFormat your response with clear headings for each section. Your total response should be between 1200-1500 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of temporal logic and time travel paradoxes.",
            "The ethical analysis is thorough and considers multiple ethical frameworks.",
            "The scenario is creative, logically consistent, and incorporates the specified paradox effectively.",
            "The decision and its consequences are well-reasoned and consider both ethical and logical implications.",
            "The philosophical implications are insightful and demonstrate deep understanding of free will, determinism, and causality.",
            "The comparative analysis effectively highlights the unique challenges introduced by time travel in ethical decision-making."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
