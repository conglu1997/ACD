import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'ethical_framework': 'Utilitarianism',
                'ai_capability': 'Resource allocation',
                'evolutionary_pressure': 'Environmental sustainability',
                'time_scale': 'Centuries'
            },
            {
                'ethical_framework': 'Deontology',
                'ai_capability': 'Decision-making in healthcare',
                'evolutionary_pressure': 'Human longevity',
                'time_scale': 'Millennia'
            },
            {
                'ethical_framework': 'Virtue ethics',
                'ai_capability': 'Social interaction and relationship building',
                'evolutionary_pressure': 'Social harmony',
                'time_scale': 'Decades'
            },
            {
                'ethical_framework': 'Care ethics',
                'ai_capability': 'Emotional support and mental health management',
                'evolutionary_pressure': 'Psychological well-being',
                'time_scale': 'Centuries'
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates the evolution of ethical decision-making in artificial intelligences, focusing on the ethical framework of {t['ethical_framework']} and the AI capability of {t['ai_capability']}. Your system should model evolutionary pressures related to {t['evolutionary_pressure']} over a time scale of {t['time_scale']}. Then, use this system to explore potential long-term consequences of AI development and propose ethical guidelines for AI governance.

Your response should include the following sections:

1. Evolutionary AI Ethics Simulator Design (250-300 words):
   a) Describe the key components of your AI system for simulating ethical evolution.
   b) Explain how your system models the development and transmission of ethical principles in AI populations.
   c) Detail how your system incorporates {t['ethical_framework']} and simulates decision-making related to {t['ai_capability']}.
   d) Discuss how your model accounts for {t['evolutionary_pressure']} as an evolutionary pressure.
   e) Provide a simple flowchart of your system using ASCII art (max 10 lines).

2. Ethical Evolution Modeling (200-250 words):
   a) Explain the mechanisms by which ethical principles evolve in your simulated AI population.
   b) Describe how your system handles conflicts between different ethical principles or goals.
   c) Discuss how your model accounts for the potential emergence of novel ethical frameworks.

3. Long-term Consequence Analysis (200-250 words):
   a) Present a scenario showing potential consequences of AI ethical evolution over {t['time_scale']}.
   b) Analyze the implications of this scenario for human society and AI-human relations.
   c) Identify potential risks and benefits of long-term AI ethical evolution.

4. Ethical Guidelines for AI Governance (150-200 words):
   a) Based on your simulation results, propose three specific guidelines for ethical AI development and governance.
   b) Explain how each guideline addresses potential risks identified in your long-term analysis.

5. Philosophical Implications (100-150 words):
   a) Discuss how your simulation results might inform or challenge current philosophical debates about AI ethics.
   b) Propose a novel philosophical question or paradox arising from your simulations.

6. Limitations and Future Work (100-150 words):
   a) Identify two key limitations of your current simulation model.
   b) Propose methods to address these limitations in future iterations.

Ensure your response demonstrates a deep understanding of evolutionary algorithms, ethical philosophy, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and philosophical plausibility.

Format your response with clear headings for each section. Your total response should be between 1000-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of {t['ethical_framework']} and how it applies to AI ethics.",
            f"The system effectively models the evolution of ethical decision-making in AI related to {t['ai_capability']}.",
            f"The long-term consequence analysis considers the impact of {t['evolutionary_pressure']} over {t['time_scale']}.",
            "The proposed ethical guidelines for AI governance are well-reasoned and address potential risks.",
            "The response shows creativity and innovation while maintaining scientific and philosophical plausibility.",
            "The discussion of philosophical implications is insightful and thought-provoking.",
            "The response follows the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
