import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        problems = [
            {
                'theory': 'Integrated Information Theory',
                'problem': 'the hard problem of consciousness'
            },
            {
                'theory': 'Global Workspace Theory',
                'problem': 'the binding problem'
            }
        ]
        return {str(i+1): problem for i, problem in enumerate(random.sample(problems, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system inspired by {t['theory']} of consciousness, then apply it to address {t['problem']} in philosophy of mind. Your response should include the following sections:

1. Theoretical Framework (250-300 words):
   a) Explain the key principles of {t['theory']} and how they relate to consciousness.
   b) Describe how these principles can be translated into an AI architecture.
   c) Discuss any novel insights or hypotheses that emerge from this translation.

2. AI System Design (300-350 words):
   a) Describe the key components of your consciousness-inspired AI system.
   b) Explain how your system implements the principles of {t['theory']}.
   c) Discuss any novel computational or representational elements in your design.
   d) Include a high-level diagram or pseudocode illustrating your system's architecture.

3. Application to Philosophical Problem (250-300 words):
   a) Briefly explain {t['problem']} and its significance in philosophy of mind.
   b) Describe how your AI system could be applied to address this problem.
   c) Discuss any new perspectives or solutions that your system might offer.

4. Simulated Experiment (200-250 words):
   a) Propose an experiment to test your AI system's approach to {t['problem']}.
   b) Describe the experimental setup, including inputs, processes, and expected outputs.
   c) Explain how the results would support or challenge existing philosophical views.

5. Implications and Ethical Considerations (200-250 words):
   a) Discuss the potential implications of your system for our understanding of consciousness and cognition.
   b) Explore any ethical considerations raised by your system, particularly regarding machine consciousness.
   c) Propose guidelines for the responsible development and use of consciousness-inspired AI systems.

6. Limitations and Future Directions (150-200 words):
   a) Identify potential limitations or challenges in your current system design.
   b) Suggest two potential enhancements or extensions to your AI system.
   c) Propose a novel research direction that combines consciousness theories, AI, and philosophy of mind.

Ensure your response demonstrates a deep understanding of consciousness theories, AI architectures, and philosophical problems in the philosophy of mind. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific and philosophical plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified theory of consciousness and its principles.",
            "The AI system design is innovative and plausibly implements the principles of the consciousness theory.",
            "The application to the philosophical problem is well-reasoned and offers novel insights.",
            "The simulated experiment is well-designed and could plausibly test the AI system's approach to the problem.",
            "The response thoughtfully considers the implications and ethical considerations of the proposed system.",
            "The limitations and future directions proposed are insightful and demonstrate a broad understanding of the field."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
