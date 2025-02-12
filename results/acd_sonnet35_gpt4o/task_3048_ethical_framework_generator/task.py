import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'ethical_tradition': 'Utilitarianism',
                'novel_concept': 'Artificial sentience (the potential for AI systems to develop consciousness or subjective experiences)',
                'societal_challenge': 'Climate change'
            },
            {
                'ethical_tradition': 'Virtue ethics',
                'novel_concept': 'Digital immortality (the hypothetical concept of preserving or transferring human consciousness to digital or virtual form)',
                'societal_challenge': 'Wealth inequality'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of analyzing existing ethical frameworks and generating novel, coherent ethical systems. Your task is to create a new ethical framework that incorporates elements from {t['ethical_tradition']}, addresses the concept of {t['novel_concept']}, and provides guidance on the societal challenge of {t['societal_challenge']}. Your response should include:

1. System Architecture (200-250 words):
   a) Describe the key components of your AI ethical framework generator.
   b) Explain how it analyzes and incorporates existing ethical traditions.
   c) Detail how it generates novel ethical principles and systems.

2. Ethical Framework Analysis (200-250 words):
   a) Analyze the key principles and strengths of {t['ethical_tradition']}.
   b) Discuss how these principles might be applied or adapted to address {t['novel_concept']}.
   c) Identify any potential conflicts or limitations in this application.

3. Novel Ethical Framework (250-300 words):
   a) Present a new ethical framework that builds upon {t['ethical_tradition']} while incorporating {t['novel_concept']}.
   b) Explain the core principles and reasoning behind this new framework.
   c) Demonstrate how this framework provides guidance on {t['societal_challenge']}.

4. Illustrative Scenario (150-200 words):
   a) Provide a specific example or scenario that illustrates how your novel ethical framework would be applied in practice.
   b) Explain the ethical reasoning and decision-making process in this scenario.

5. Meta-Ethical Analysis (150-200 words):
   a) Discuss the meta-ethical assumptions underlying your AI's approach to generating ethical frameworks.
   b) Analyze potential biases or limitations in your AI's ethical reasoning process.

6. Practical Application (150-200 words):
   a) Describe how your new ethical framework could be applied in real-world scenarios related to {t['societal_challenge']}.
   b) Discuss potential challenges in implementing this framework and how they might be addressed.

7. Evaluation and Implications (150-200 words):
   a) Propose criteria for evaluating the coherence and effectiveness of AI-generated ethical frameworks.
   b) Discuss the broader implications of AI systems capable of generating ethical frameworks.

Ensure your response demonstrates a deep understanding of ethical philosophy, meta-ethics, and the complex interplay between technology and morality. Use appropriate philosophical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining logical consistency and philosophical rigor.

Format your response with clear headings for each section. Your total response should be between 1250-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified ethical tradition and its principles.",
            "The novel ethical framework coherently incorporates the given novel concept and addresses the societal challenge.",
            "The illustrative scenario effectively demonstrates the application of the new ethical framework.",
            "The meta-ethical analysis shows sophisticated reasoning about the AI's own ethical generation process.",
            "The proposed framework is creative yet logically consistent and philosophically rigorous.",
            "The response effectively discusses practical applications and potential challenges of the new ethical framework."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
