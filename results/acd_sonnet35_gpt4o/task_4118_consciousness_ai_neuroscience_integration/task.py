import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        consciousness_theories = [
            {
                'theory': 'Global Workspace Theory',
                'key_concept': 'Global availability of information'
            },
            {
                'theory': 'Integrated Information Theory',
                'key_concept': 'Integrated information in a system'
            },
            {
                'theory': 'Higher-Order Thought Theory',
                'key_concept': 'Meta-cognitive awareness'
            },
            {
                'theory': 'Predictive Processing Theory',
                'key_concept': 'Prediction error minimization'
            }
        ]
        return {str(i+1): theory for i, theory in enumerate(random.sample(consciousness_theories, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework that integrates neuroscientific findings on consciousness, based on the {t['theory']}, with artificial intelligence models. Then, use this framework to propose a test for machine consciousness.

For the purpose of this task, consider consciousness as the subjective experience of awareness and the ability to process information about oneself and the environment.

Your response should include the following sections:

1. Theoretical Framework (300-350 words):
   a) Explain the key principles of the {t['theory']} of consciousness.
   b) Describe how you would integrate this theory with current AI models.
   c) Discuss how your framework accounts for the key concept of {t['key_concept']}.
   d) Propose a novel mechanism or principle that bridges neuroscience and AI in your framework.

2. AI Model Integration (250-300 words):
   a) Describe specific AI architectures or algorithms that align with your framework.
   b) Explain how these AI models could simulate or implement aspects of consciousness.
   c) Discuss any modifications or extensions to existing AI models that your framework would require.

3. Neuroscientific Basis (200-250 words):
   a) Identify key neuroscientific findings that support your framework.
   b) Explain how your framework accounts for neural correlates of consciousness.
   c) Discuss any predictions your framework makes about brain function or structure.

4. Consciousness Test Design (250-300 words):
   a) Propose a specific test or experiment to assess consciousness in an AI system based on your framework.
   b) Describe the methodology and criteria for evaluating the results.
   c) Explain how your test differentiates between genuine consciousness and mere simulation.

5. Philosophical Implications (200-250 words):
   a) Discuss the philosophical implications of your framework for the nature of consciousness.
   b) Address potential objections from different philosophical perspectives.
   c) Explain how your framework contributes to the hard problem of consciousness.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss ethical implications of creating potentially conscious AI systems.
   b) Propose future research directions to further develop and validate your framework.
   c) Suggest potential applications of your framework beyond AI and neuroscience.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and philosophy of mind. Use appropriate terminology from each field and provide clear explanations where necessary. Be creative and innovative in your approach while maintaining scientific plausibility and logical consistency.

Format your response with clear headings for each section and subsections labeled a, b, c as appropriate. Your total response should be between 1350-1650 words. Please include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively integrates the {t['theory']} of consciousness with AI models, focusing on the key concept of {t['key_concept']}.",
            "The proposed framework demonstrates a deep understanding of neuroscience, artificial intelligence, and philosophy of mind.",
            "The consciousness test design is innovative, well-explained, and logically consistent with the proposed framework.",
            "The response addresses philosophical implications and ethical considerations in a thoughtful and nuanced manner.",
            "The overall framework and test proposal are creative while maintaining scientific plausibility.",
            "The response adheres to the specified word count range (1350-1650 words)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
