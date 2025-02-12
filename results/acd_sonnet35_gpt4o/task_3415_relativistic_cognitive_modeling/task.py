import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'relativity_principle': 'time dilation',
                'cognitive_process': 'decision-making',
                'application_domain': 'space exploration',
                'example_scenario': 'long-term space missions',
                'additional_constraint': 'gravitational effects on cognition'
            },
            {
                'relativity_principle': 'length contraction',
                'cognitive_process': 'perception',
                'application_domain': 'virtual reality',
                'example_scenario': 'simulating relativistic environments',
                'additional_constraint': 'quantum entanglement in neural networks'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework that integrates principles of special and general relativity into cognitive science and artificial intelligence to model and analyze complex cognitive processes across different reference frames and spatiotemporal scales. Your framework should focus on the relativity principle of {t['relativity_principle']}, address the cognitive process of {t['cognitive_process']}, and be applied to the domain of {t['application_domain']}. Use the example scenario of {t['example_scenario']} to illustrate your framework's application. Additionally, incorporate the constraint of {t['additional_constraint']} into your framework.

Your response should include:

1. Framework Overview (250-300 words):
   a) Describe the key components of your relativistic cognitive modeling framework.
   b) Explain how it integrates relativity theory, cognitive science, and AI.
   c) Discuss how the framework specifically addresses the given relativity principle, cognitive process, and application domain.
   d) Explain how the additional constraint is incorporated into your framework.

2. Relativistic-Cognitive Integration (200-250 words):
   a) Explain how the specified relativity principle is applied to model cognitive processes.
   b) Describe how this integration enhances traditional cognitive models or AI approaches.
   c) Provide a mathematical or conceptual representation of this integration (use LaTeX formatting for equations).
   d) Discuss how the additional constraint influences this integration.

3. AI Implementation (200-250 words):
   a) Outline how your framework would be implemented in an AI system.
   b) Describe the data structures and algorithms that would be used.
   c) Explain how the AI system would process information and make decisions using this framework.
   d) Address how the additional constraint affects the AI implementation.

4. Example Scenario Analysis (200-250 words):
   a) Describe how your framework would approach the given example scenario.
   b) Explain the step-by-step process of how the framework would analyze and solve problems in this scenario.
   c) Discuss how this approach differs from traditional methods.
   d) Illustrate how the additional constraint impacts the scenario analysis.

5. Theoretical Implications (150-200 words):
   a) Analyze the theoretical implications of your framework for our understanding of cognition, AI, and the nature of spacetime.
   b) Discuss how it challenges or extends current theories in cognitive science, AI, and physics.
   c) Propose testable hypotheses derived from your framework.
   d) Consider how the additional constraint contributes to these implications.

6. Practical Applications and Limitations (150-200 words):
   a) Suggest potential real-world applications of your framework beyond the given domain.
   b) Discuss the technical and conceptual challenges in implementing this framework.
   c) Describe the limitations of your approach and areas for future development.
   d) Evaluate how the additional constraint affects the practical applications and limitations.

Ensure your response demonstrates a deep understanding of relativity theory, cognitive science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility and logical consistency.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a detailed design of a relativistic cognitive modeling framework.",
            f"The framework integrates the relativity principle of {t['relativity_principle']}.",
            f"The framework addresses the cognitive process of {t['cognitive_process']}.",
            f"The framework is applied to the domain of {t['application_domain']}.",
            f"The response includes an analysis of the example scenario: {t['example_scenario']}.",
            f"The framework incorporates the additional constraint: {t['additional_constraint']}.",
            "The response demonstrates a deep understanding of relativity theory, cognitive science, and artificial intelligence.",
            "The response is creative and innovative while maintaining scientific plausibility.",
            "The response follows the specified format and word limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
