import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'society_type': 'Post-scarcity economy',
                'ethical_dilemma': 'Balancing individual freedom with societal harmony',
                'policy_area': 'Resource allocation and personal fulfillment'
            },
            {
                'society_type': 'Interplanetary civilization',
                'ethical_dilemma': 'Preserving alien ecosystems vs. human expansion',
                'policy_area': 'Sustainable colonization and diplomatic relations'
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are tasked with designing and analyzing a simulated AI-governed society based on the following parameters:

Society Type: {t['society_type']}
Ethical Dilemma: {t['ethical_dilemma']}
Policy Area: {t['policy_area']}

Your response should include the following sections:

1. Society Design (250-300 words):
   a) Describe the key features and structures of your AI-governed society.
   b) Explain how AI systems are integrated into governance and decision-making processes.
   c) Outline the main ethical principles guiding your society's governance.

2. Ethical Framework (200-250 words):
   a) Develop an ethical framework for AI decision-making in your society.
   b) Explain how this framework addresses the given ethical dilemma.
   c) Discuss potential conflicts between different ethical principles and how they are resolved.

3. Policy Implementation (250-300 words):
   a) Propose a specific policy to address the given policy area.
   b) Describe how the AI governance system would implement and enforce this policy.
   c) Analyze potential consequences (both intended and unintended) of this policy.

4. Scenario Analysis (200-250 words):
   a) Present a specific scenario that challenges your society's ethical framework and policies.
   b) Explain how the AI governance system would approach and resolve this scenario.
   c) Discuss any limitations or potential improvements revealed by this scenario.

5. Comparative Evaluation (200-250 words):
   a) Compare your AI-governed society to current human governance systems.
   b) Analyze the potential benefits and risks of your proposed system.
   c) Discuss the implications of your model for real-world AI development and governance.

Ensure your response demonstrates a deep understanding of ethics, governance, and AI capabilities. Be creative and thorough in your analysis, considering multiple perspectives and potential consequences. Use clear headings for each section of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all required sections comprehensively.",
            "The proposed society and ethical framework are logically consistent and well-reasoned.",
            "The analysis demonstrates a deep understanding of ethics, governance, and AI capabilities.",
            "The response shows creativity and originality in addressing the given parameters.",
            "The comparative evaluation provides insightful analysis of the proposed system's implications."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
