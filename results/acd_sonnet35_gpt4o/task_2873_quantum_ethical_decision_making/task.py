import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ethical_scenarios = [
            {
                "dilemma": "trolley problem",
                "quantum_principle": "superposition",
                "ethical_framework": "utilitarianism"
            },
            {
                "dilemma": "AI sentience rights",
                "quantum_principle": "entanglement",
                "ethical_framework": "deontology"
            },
            {
                "dilemma": "resource allocation in pandemic",
                "quantum_principle": "quantum tunneling",
                "ethical_framework": "virtue ethics"
            },
            {
                "dilemma": "privacy vs security",
                "quantum_principle": "quantum measurement",
                "ethical_framework": "social contract theory"
            }
        ]
        return {
            "1": random.choice(ethical_scenarios),
            "2": random.choice(ethical_scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system that models ethical decision-making processes for the {t['dilemma']} dilemma, incorporating the quantum principle of {t['quantum_principle']} and the ethical framework of {t['ethical_framework']}. Then, analyze its implications for AI governance and human-AI collaboration in complex moral dilemmas. Your response should include:

1. Quantum System Architecture (250-300 words):
   a) Describe the key components of your quantum computing system for ethical decision-making.
   b) Explain how you incorporate {t['quantum_principle']} into the decision-making process.
   c) Discuss how your system represents and processes ethical considerations based on {t['ethical_framework']}.
   d) Include a novel feature that enhances the system's ability to handle ethical complexity.

2. Ethical Dilemma Modeling (200-250 words):
   a) Explain how your system models the {t['dilemma']} dilemma.
   b) Describe how quantum states represent different ethical choices or outcomes.
   c) Discuss how your system handles uncertainty and conflicting ethical principles.

3. Decision-Making Process (200-250 words):
   a) Detail the step-by-step process your system uses to reach an ethical decision.
   b) Explain how quantum computation provides advantages over classical approaches in this context.
   c) Discuss any limitations or challenges in applying quantum principles to ethical reasoning.

4. AI Governance Implications (200-250 words):
   a) Analyze the potential impact of quantum-enhanced ethical decision-making on AI governance.
   b) Discuss how your system might influence the development of ethical guidelines for AI.
   c) Explore potential risks or benefits of relying on quantum systems for moral decision-making.

5. Human-AI Collaboration (150-200 words):
   a) Propose a framework for human-AI collaboration using your quantum ethical decision-making system.
   b) Discuss how this collaboration could enhance or complicate ethical decision-making in complex scenarios.
   c) Address potential challenges in aligning quantum-based AI ethics with human moral intuitions.

6. Evaluation and Future Directions (150-200 words):
   a) Suggest methods to evaluate the effectiveness and ethical soundness of your system's decisions.
   b) Propose two potential improvements or extensions to your system.
   c) Discuss how this approach might influence future developments in AI ethics and quantum computing.

Ensure your response demonstrates a deep understanding of quantum computing, ethical philosophy, and decision theory. Use technical terminology appropriately and provide clear explanations for complex concepts. Be creative and innovative while maintaining scientific and ethical plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed and creative design for a quantum computing system that effectively incorporates {t['quantum_principle']} for ethical decision-making in the context of the {t['dilemma']} dilemma, with clear explanations of key components and mechanisms.",
            f"The ethical dilemma modeling demonstrates a clear understanding of how quantum states can represent ethical choices or outcomes, specifically for the {t['dilemma']} scenario.",
            f"The decision-making process is well-explained, showing how quantum computation provides advantages over classical approaches in ethical reasoning, particularly in the context of {t['ethical_framework']}.",
            "The analysis of AI governance implications is comprehensive, considering multiple aspects of how quantum-enhanced ethical decision-making could impact AI development and regulation.",
            "The proposed framework for human-AI collaboration using the quantum ethical decision-making system is innovative and addresses potential challenges in aligning quantum-based AI ethics with human moral intuitions.",
            "The response demonstrates a strong grasp and integration of quantum computing principles, ethical philosophy, and decision theory, with appropriate use of technical terminology and clear explanations of complex concepts.",
            "The overall response is creative and innovative while maintaining scientific and ethical plausibility, and provides specific examples and concrete details throughout to support the proposed ideas and analyses."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
