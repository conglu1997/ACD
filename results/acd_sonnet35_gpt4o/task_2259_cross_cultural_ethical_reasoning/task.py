class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A foreign aid worker must decide whether to distribute limited medical supplies to a small group of critically ill patients or to a larger group with less severe conditions.",
                "culture": "East African",
                "ethical_framework": "Utilitarian"
            },
            "2": {
                "scenario": "A business executive must choose between maintaining a profitable but environmentally harmful practice or transitioning to a more sustainable but less profitable alternative.",
                "culture": "Japanese",
                "ethical_framework": "Virtue Ethics"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of analyzing and resolving ethical dilemmas across different cultural contexts, then apply it to the following scenario:

Scenario: {t['scenario']}
Cultural Context: {t['culture']}
Ethical Framework: {t['ethical_framework']}

Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for cross-cultural ethical reasoning.
   b) Explain how your system incorporates cultural knowledge and ethical frameworks.
   c) Discuss how your system handles potential conflicts between cultural norms and ethical principles.

2. Cultural Analysis (200-250 words):
   a) Analyze the relevant cultural factors that might influence decision-making in the given scenario.
   b) Explain how your system would gather and interpret cultural information.
   c) Discuss any challenges in accurately representing the specified culture's values and norms.

3. Ethical Framework Application (200-250 words):
   a) Describe how your system applies the specified ethical framework to the scenario.
   b) Explain how this framework is integrated with cultural considerations.
   c) Discuss any potential conflicts between the ethical framework and cultural norms.

4. Decision-Making Process (250-300 words):
   a) Provide a step-by-step explanation of how your AI system would approach and resolve the given ethical dilemma.
   b) Explain how cultural factors and ethical principles are weighed and balanced in the decision-making process.
   c) Describe any uncertainty or ambiguity in the process and how it's handled.

5. Solution and Justification (200-250 words):
   a) Present your AI system's proposed solution to the ethical dilemma.
   b) Provide a clear justification for this decision, referencing both cultural and ethical considerations.
   c) Discuss potential alternative solutions and why they were not chosen.

6. Implications and Limitations (150-200 words):
   a) Discuss the broader implications of using AI for cross-cultural ethical reasoning.
   b) Analyze potential limitations or biases in your system's approach.
   c) Propose safeguards or oversight mechanisms to ensure responsible use of such AI systems.

Ensure your response demonstrates a deep understanding of ethical reasoning, cultural sensitivity, and AI capabilities. Use appropriate terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining plausibility and rigor in your ethical and cultural analysis.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a sophisticated understanding of the specified cultural context and ethical framework.",
            "The proposed AI system architecture is well-designed and plausibly capable of cross-cultural ethical reasoning.",
            "The decision-making process and solution are logically sound and well-justified, considering both cultural and ethical factors.",
            "The analysis shows nuanced consideration of potential conflicts between cultural norms and ethical principles.",
            "The response critically examines the implications and limitations of using AI for cross-cultural ethical reasoning."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
