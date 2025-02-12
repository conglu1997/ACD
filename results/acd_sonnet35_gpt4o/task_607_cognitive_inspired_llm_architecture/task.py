import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_theories = [
            'Chomsky\'s Universal Grammar',
            'Connectionist models of language acquisition',
            'Usage-based theory of language development',
            'Dual-route model of reading',
            'Parallel Distributed Processing (PDP) model',
            'Construction Grammar',
            'Embodied Cognition theory',
            'Predictive Processing framework',
            'Dynamic Systems Theory in language acquisition',
            'Declarative/Procedural model of language'
        ]
        
        task1 = {
            'theory': random.choice(cognitive_theories),
            'focus': random.choice(['language acquisition', 'language processing'])
        }
        
        task2 = {
            'theory': random.choice(cognitive_theories),
            'focus': random.choice(['language acquisition', 'language processing'])
        }
        
        return {
            "1": task1,
            "2": task2
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel large language model (LLM) architecture inspired by the cognitive theory of {t['theory']}, focusing on {t['focus']}. Your task is to:

1. Architecture Design (250-300 words):
   a) Describe the key components and mechanisms of your LLM architecture.
   b) Explain how your design incorporates principles from {t['theory']}.
   c) Discuss how your architecture addresses {t['focus']}.
   d) Include at least one innovative feature that distinguishes your model from existing LLMs.

2. Training and Data Processing (200-250 words):
   a) Propose a training methodology for your model, explaining how it aligns with the chosen cognitive theory.
   b) Describe how your model would process and represent linguistic data.
   c) Discuss any unique data requirements or preprocessing steps necessary for your architecture.

3. Potential Capabilities and Limitations (200-250 words):
   a) Predict two potential capabilities where your model might outperform traditional LLMs.
   b) Identify two possible limitations or challenges of your approach.
   c) Explain the reasoning behind your predictions, grounding them in the principles of {t['theory']}.

4. Implications for AI and Cognitive Science (200-250 words):
   a) Discuss how your model could contribute to our understanding of human language {t['focus']}.
   b) Explore potential applications of your architecture in AI research or practical language technologies.
   c) Propose an experiment to test a hypothesis about language {t['focus']} using your model.

5. Ethical Considerations (150-200 words):
   a) Identify two potential ethical implications or challenges arising from your model's design or application.
   b) Propose guidelines or safeguards to address these ethical concerns.

Ensure your response demonstrates a deep understanding of both cognitive science and AI principles. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified cognitive theory and its application to language models.",
            "The proposed architecture is innovative and clearly distinct from existing LLM approaches.",
            "The design effectively incorporates principles from the given cognitive theory and addresses the specified focus area.",
            "The training methodology and data processing approach are well-aligned with the chosen cognitive theory.",
            "The analysis of potential capabilities and limitations is insightful and well-reasoned.",
            "The discussion of implications for AI and cognitive science is thoughtful and demonstrates interdisciplinary thinking.",
            "The proposed experiment is well-designed and relevant to testing hypotheses about language acquisition or processing.",
            "The ethical considerations are relevant and the proposed guidelines are thoughtful and practical.",
            "The response is well-structured, clear, and within the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
