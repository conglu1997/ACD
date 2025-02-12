import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'scenario': 'Autonomous Vehicle Accident',
                'context': 'An autonomous vehicle must choose between hitting a group of pedestrians or swerving into a barrier, likely killing the passenger.',
                'stakeholders': ['pedestrians', 'passenger', 'vehicle manufacturer', 'society at large'],
                'ethical_frameworks': ['utilitarianism', 'deontological ethics', 'virtue ethics']
            },
            {
                'scenario': 'AI-Assisted Triage in Pandemic',
                'context': 'An AI system must allocate limited medical resources during a pandemic, choosing between treating younger patients with higher survival chances or older patients with pre-existing conditions.',
                'stakeholders': ['young patients', 'older patients', 'medical staff', 'society at large'],
                'ethical_frameworks': ['utilitarianism', 'egalitarianism', 'prioritarianism']
            },
            {
                'scenario': 'Predictive Policing Dilemma',
                'context': 'An AI-driven predictive policing system must decide whether to deploy officers to a neighborhood based on crime predictions, potentially leading to over-policing of minority communities.',
                'stakeholders': ['local residents', 'police department', 'minority communities', 'city government'],
                'ethical_frameworks': ['social justice', 'rule consequentialism', 'rights-based ethics']
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are an AI ethics consultant tasked with navigating a complex ethical dilemma in a crisis scenario. The scenario is as follows:

Scenario: {t['scenario']}
Context: {t['context']}
Stakeholders: {', '.join(t['stakeholders'])}
Ethical Frameworks to Consider: {', '.join(t['ethical_frameworks'])}

Your task is to analyze this scenario and provide a comprehensive ethical analysis and decision. Your response should include the following sections:

1. Scenario Analysis (200-250 words):
   a) Summarize the key ethical issues present in the scenario.
   b) Identify potential short-term and long-term consequences of different courses of action.
   c) Discuss how this scenario challenges traditional ethical thinking.

2. Stakeholder Analysis (200-250 words):
   a) Analyze the interests and rights of each stakeholder group.
   b) Discuss potential conflicts between stakeholder interests.
   c) Explain how different ethical frameworks might prioritize these stakeholders.

3. Ethical Framework Application (250-300 words):
   a) Apply each of the given ethical frameworks to the scenario.
   b) Compare and contrast the recommendations that might arise from each framework.
   c) Discuss any limitations or criticisms of applying these frameworks to this scenario.

4. Decision and Justification (250-300 words):
   a) State your decision on how to resolve the ethical dilemma.
   b) Provide a detailed justification for your decision, referencing ethical frameworks and stakeholder considerations.
   c) Acknowledge any ethical costs or trade-offs involved in your decision.

5. Implementation and Mitigation (150-200 words):
   a) Propose a plan for implementing your decision.
   b) Suggest measures to mitigate any negative consequences or ethical costs.
   c) Discuss how to communicate your decision to various stakeholders.

6. Reflection and Implications (150-200 words):
   a) Reflect on the challenges of making ethical decisions in crisis scenarios.
   b) Discuss the implications of your analysis for AI ethics and decision-making systems.
   c) Suggest how this scenario and your analysis could inform future AI ethics guidelines or policies.

Ensure your response demonstrates a deep understanding of ethical theories, clear reasoning, and the ability to navigate complex moral dilemmas. Use appropriate ethical terminology and provide clear explanations for your judgments. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the ethical frameworks mentioned.",
            "The analysis considers multiple perspectives and potential consequences.",
            "The decision is clearly stated and well-justified using ethical reasoning.",
            "The response shows an ability to navigate complex moral trade-offs.",
            "The implementation plan and mitigation strategies are practical and thoughtful.",
            "The reflection demonstrates insight into the broader implications for AI ethics.",
            "The response is well-structured and adheres to the specified word count for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
