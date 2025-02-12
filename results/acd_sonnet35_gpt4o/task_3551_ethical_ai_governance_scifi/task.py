import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "society_type": "Multi-planetary federation",
                "ai_challenge": "Balancing individual privacy with collective security",
                "ethical_dilemma": "Rights of artificial beings"
            },
            {
                "society_type": "Post-scarcity space habitats",
                "ai_challenge": "Fair resource allocation across diverse species",
                "ethical_dilemma": "Limits of genetic and cybernetic enhancements"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI governance system for a {t['society_type']} that addresses the AI challenge of {t['ai_challenge']} and the ethical dilemma of {t['ethical_dilemma']}. Your response should include:

1. Governance Structure (250-300 words):
   a) Describe the key components of your AI governance system.
   b) Explain how it integrates with the existing societal structure.
   c) Detail how it addresses the specified AI challenge.

2. Ethical Framework (200-250 words):
   a) Outline the ethical principles guiding your governance system.
   b) Explain how these principles address the given ethical dilemma.
   c) Discuss any potential conflicts between different ethical considerations.

3. Implementation and Oversight (200-250 words):
   a) Describe the mechanisms for implementing and enforcing AI governance.
   b) Explain how your system ensures transparency and accountability.
   c) Discuss how it adapts to evolving technological and societal changes.

4. Societal Impact Analysis (200-250 words):
   a) Analyze the potential positive and negative impacts of your system on society.
   b) Discuss how it might affect different groups or species within the society.
   c) Propose methods for mitigating potential negative consequences.

5. Speculative Scenario (150-200 words):
   a) Present a specific scenario that tests the limits of your governance system.
   b) Explain how your system would respond to this challenge.
   c) Discuss any insights or potential improvements revealed by this scenario.

Ensure your response demonstrates creative problem-solving, ethical reasoning, and a deep understanding of the complex interplay between AI, governance, and society. Use appropriate terminology and provide clear explanations for your design choices. Be innovative in your approach while considering the practical challenges of implementation in a futuristic setting.

Format your response with clear headings for each section. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates creative and original thinking in designing the AI governance system.",
            "The ethical framework is well-reasoned and addresses the given dilemma comprehensively.",
            "The implementation and oversight mechanisms are practical and well-explained.",
            "The societal impact analysis is thorough and considers multiple perspectives.",
            "The speculative scenario effectively tests the governance system and provides valuable insights.",
            "The overall response is coherent, well-structured, and adheres to the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
