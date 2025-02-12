import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scientific_domains = [
            {
                'domain': 'Astrophysics',
                'problem': 'Explain the nature of dark matter'
            },
            {
                'domain': 'Neuroscience',
                'problem': 'Develop a model for consciousness'
            }
        ]
        
        source_domains = [
            'Fluid dynamics',
            'Quantum mechanics',
            'Evolutionary biology',
            'Information theory'
        ]
        
        return {
            str(i+1): {
                'scientific_domain': domain,
                'source_domain': random.choice(source_domains)
            } for i, domain in enumerate(scientific_domains)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that uses analogical reasoning to generate hypotheses and potential solutions for scientific problems. Apply your system to the following scenario:

Target Scientific Domain: {t['scientific_domain']['domain']}
Problem to Solve: {t['scientific_domain']['problem']}
Source Domain for Analogy: {t['source_domain']}

Your response should include the following sections:

1. Analogical Reasoning Framework (250-300 words):
   a) Explain the cognitive processes involved in analogical reasoning and how they apply to scientific discovery.
   b) Describe how your AI system implements these processes.
   c) Discuss any novel approaches or algorithms used in your system for generating and evaluating analogies.

2. AI System Architecture (200-250 words):
   a) Provide a high-level overview of your AI system's architecture.
   b) Detail the components for knowledge representation, analogy generation, and hypothesis formation.
   c) Explain how the system integrates information from different scientific domains.
   d) Include a diagram or pseudocode to illustrate your system's workflow.

3. Application to the Given Scenario (300-350 words):
   a) Describe how your system would approach the given scientific problem using analogical reasoning.
   b) Generate at least two potential hypotheses or solutions based on analogies from the source domain.
   c) Explain the reasoning behind each analogy and how it leads to the proposed hypotheses.
   d) Discuss how your system would evaluate and refine these hypotheses.

4. Cross-Domain Knowledge Integration (200-250 words):
   a) Explain how your system integrates knowledge from the source and target domains.
   b) Discuss challenges in translating concepts between different scientific fields and how your system addresses them.
   c) Provide an example of how a concept from the source domain might be reinterpreted in the context of the target domain.

5. Evaluation and Refinement (150-200 words):
   a) Propose methods for evaluating the quality and novelty of the generated hypotheses.
   b) Describe how your AI system would improve its analogical reasoning process based on feedback and results.
   c) Discuss potential limitations of using analogical reasoning for scientific discovery and how you might address them.

6. Ethical and Societal Implications (100-150 words):
   a) Discuss potential ethical implications of using AI for scientific discovery through analogical reasoning.
   b) Consider the impact on the scientific process and human creativity in research.
   c) Propose guidelines for responsible development and use of such AI systems in scientific research.

Ensure your response demonstrates a deep understanding of analogical reasoning, the specified scientific domains, and AI technologies. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of analogical reasoning and its application to scientific discovery",
            "The AI system design is innovative, coherent, and scientifically plausible",
            "The application to the given scenario is creative and well-reasoned, with at least two plausible hypotheses generated",
            "The response shows a strong grasp of both the source and target scientific domains",
            "The ethical implications and societal impacts are thoughtfully considered"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
