import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        philosophical_concepts = [
            'Utilitarianism',
            'Deontology',
            'Virtue Ethics',
            'Social Contract Theory',
            'Care Ethics',
            'Existentialism'
        ]
        ethical_dilemmas = [
            'AI decision-making in autonomous vehicles',
            'Resource allocation during global pandemics',
            'Privacy rights in the age of big data',
            'Genetic engineering and human enhancement',
            'Environmental ethics and climate change mitigation',
            'Wealth inequality and social justice'
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                'philosophical_concept': random.choice(philosophical_concepts),
                'ethical_dilemma': random.choice(ethical_dilemmas)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating a novel ethical framework based on the philosophical concept of {t['philosophical_concept']}, and apply it to the complex real-world scenario of {t['ethical_dilemma']}. Your response should include the following sections:

1. Philosophical Concept Analysis (250-300 words):
   a) Explain the key principles and ideas of {t['philosophical_concept']}.
   b) Discuss how these principles could be adapted or extended for AI reasoning.
   c) Identify any potential limitations or criticisms of this philosophical approach.

2. Novel Ethical Framework Design (300-350 words):
   a) Describe your AI system's architecture for generating ethical frameworks.
   b) Explain how your system incorporates and extends the principles of {t['philosophical_concept']}.
   c) Detail the key components and decision-making processes of your novel ethical framework.
   d) Discuss how your framework addresses potential limitations of the original philosophical concept.

3. Application to Real-World Scenario (250-300 words):
   a) Apply your novel ethical framework to the scenario of {t['ethical_dilemma']}.
   b) Provide a step-by-step analysis of how your AI system would approach this dilemma.
   c) Describe the ethical decisions or recommendations your system would make.
   d) Explain how these decisions differ from or improve upon traditional approaches to this dilemma.

4. Comparative Analysis (200-250 words):
   a) Compare your AI-generated ethical framework to existing human-created frameworks.
   b) Discuss the strengths and potential weaknesses of your approach.
   c) Analyze how your framework might challenge or complement human ethical reasoning.

5. Implications and Future Directions (150-200 words):
   a) Discuss the broader implications of AI-generated ethical frameworks for philosophy and society.
   b) Propose potential applications or extensions of your system beyond the given scenario.
   c) Suggest future research directions to further develop or validate your approach.

6. Ethical Considerations (100-150 words):
   a) Reflect on the ethical implications of using AI to generate ethical frameworks.
   b) Discuss potential risks or unintended consequences of your approach.
   c) Propose safeguards or guidelines for the responsible development and use of such AI systems.

Ensure your response demonstrates a deep understanding of philosophy, ethics, and AI principles. Be innovative in your approach while maintaining logical consistency and plausibility. Use appropriate terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['philosophical_concept']} and its application to AI reasoning.",
            "The novel ethical framework is logically consistent, innovative, and clearly explained.",
            f"The application to the {t['ethical_dilemma']} scenario is thorough, well-reasoned, and demonstrates the framework's utility.",
            "The comparative analysis shows critical thinking and awareness of the framework's strengths and limitations.",
            "The discussion of implications and future directions is insightful and considers broader societal impacts.",
            "The ethical considerations section demonstrates awareness of potential risks and proposes responsible development guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
