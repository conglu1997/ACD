import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "ethical_framework": "utilitarianism",
                "brain_region": "prefrontal cortex",
                "cultural_context": "individualistic society",
                "dilemma": "autonomous vehicle decision-making in accident scenarios"
            },
            {
                "ethical_framework": "virtue ethics",
                "brain_region": "anterior cingulate cortex",
                "cultural_context": "collectivist society",
                "dilemma": "resource allocation during a global health crisis"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neuro-inspired AI system that simulates ethical decision-making processes based on the {t['ethical_framework']} framework and the function of the {t['brain_region']}, then use it to analyze the moral dilemma of {t['dilemma']} within a {t['cultural_context']}. Your response should include:

1. Neuro-AI System Architecture (300-350 words):
   a) Describe the key components of your AI system and how they integrate neuroscientific principles.
   b) Explain how your system models the function of the {t['brain_region']} in ethical decision-making.
   c) Detail how your system incorporates the {t['ethical_framework']} framework.
   d) Discuss how your system accounts for cultural influences on moral reasoning.
   e) Include a high-level diagram of your system architecture (described textually).

2. Ethical Decision-Making Process (250-300 words):
   a) Explain the step-by-step process your system uses to analyze and make decisions about moral dilemmas.
   b) Describe how your system balances competing ethical considerations.
   c) Discuss how your system handles uncertainty or conflicting information.

3. Dilemma Analysis (250-300 words):
   a) Apply your neuro-AI system to analyze the dilemma of {t['dilemma']}.
   b) Describe the key ethical considerations identified by your system.
   c) Explain how the {t['cultural_context']} influences the analysis.
   d) Present the decision or recommendation made by your system, with justification.

4. Comparative Analysis (200-250 words):
   a) Compare your neuro-AI approach to traditional AI methods for ethical reasoning.
   b) Discuss potential advantages and limitations of your system.
   c) Analyze how your system's decision might differ in a contrasting cultural context.

5. Philosophical Implications (200-250 words):
   a) Discuss the implications of your system for our understanding of moral decision-making.
   b) Explore how your approach might inform debates in moral philosophy.
   c) Consider the ethical implications of using AI systems for moral reasoning.

6. Future Directions and Challenges (150-200 words):
   a) Propose two potential improvements or extensions to your neuro-AI ethics system.
   b) Identify key challenges in developing more advanced ethical AI systems.
   c) Suggest potential applications of your system beyond ethical decision-making.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and moral philosophy. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and philosophical plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, AI, and moral philosophy.",
            f"The proposed system effectively integrates the {t['ethical_framework']} framework and the function of the {t['brain_region']}.",
            f"The analysis of the {t['dilemma']} dilemma is thorough and considers the {t['cultural_context']}.",
            "The response is creative and innovative while maintaining scientific and philosophical plausibility.",
            "The philosophical implications and future directions are thoughtfully addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
