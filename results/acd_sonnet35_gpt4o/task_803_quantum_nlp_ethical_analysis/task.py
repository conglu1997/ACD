import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'quantum_principle': 'Superposition',
                'nlp_application': 'Sentiment analysis',
                'ethical_concern': 'Privacy'
            },
            {
                'quantum_principle': 'Entanglement',
                'nlp_application': 'Machine translation',
                'ethical_concern': 'Bias'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum computing system for natural language processing, focusing on the quantum principle of {t['quantum_principle']} and its application to {t['nlp_application']}. Then, analyze the ethical implications of this system, with particular attention to the ethical concern of {t['ethical_concern']}.

Provide your response in the following format:

1. Quantum NLP System Design (250-300 words):
   a) Explain how the quantum principle of {t['quantum_principle']} can be applied to {t['nlp_application']}.
   b) Describe the key components and architecture of your quantum NLP system.
   c) Discuss the potential advantages of your quantum approach over classical NLP methods.
   d) Provide a high-level pseudocode or diagram illustrating a key algorithm in your system.

2. Technical Challenges and Solutions (200-250 words):
   a) Identify at least two major technical challenges in implementing your system.
   b) Propose potential solutions or research directions to address these challenges.
   c) Discuss any trade-offs or limitations of your proposed solutions.

3. Ethical Analysis (200-250 words):
   a) Analyze the ethical implications of your quantum NLP system, focusing on {t['ethical_concern']}.
   b) Discuss how the unique features of quantum computing might exacerbate or mitigate this ethical concern.
   c) Propose at least two concrete measures to address the ethical issues you've identified.

4. Societal Impact (150-200 words):
   a) Predict potential positive and negative societal impacts of widespread adoption of quantum NLP systems like yours.
   b) Discuss how these impacts might differ from those of classical NLP systems.

5. Interdisciplinary Implications (150-200 words):
   a) Explain how your quantum NLP system might influence or be influenced by advances in other scientific fields.
   b) Propose a novel research question at the intersection of quantum computing, NLP, and another discipline of your choice.

Ensure your response demonstrates a deep understanding of quantum computing principles, natural language processing techniques, and ethical reasoning. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified quantum principle and its application to NLP.",
            "The quantum NLP system design is innovative, plausible, and clearly explained.",
            "The technical challenges and proposed solutions are well-reasoned and relevant.",
            "The ethical analysis is thorough and specifically addresses the given ethical concern.",
            "The discussion of societal impact shows a nuanced understanding of the potential consequences of quantum NLP.",
            "The interdisciplinary implications and proposed research question are creative and insightful.",
            "The overall response shows strong integration of knowledge from quantum computing, NLP, and ethics.",
            "The response includes a clear pseudocode or diagram illustrating a key algorithm.",
            "The response adheres to the specified word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
