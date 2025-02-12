import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        consciousness_theories = [
            "Global Workspace Theory",
            "Integrated Information Theory",
            "Higher-Order Thought Theory",
            "Attention Schema Theory"
        ]
        philosophical_questions = [
            "Can a machine truly be self-aware?",
            "How can we distinguish between simulated and genuine consciousness?",
            "What are the ethical implications of creating conscious AI?",
            "How does machine consciousness relate to free will and determinism?"
        ]
        return {
            "1": {
                "theory": random.choice(consciousness_theories),
                "question": random.choice(philosophical_questions)
            },
            "2": {
                "theory": random.choice(consciousness_theories),
                "question": random.choice(philosophical_questions)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI architecture capable of simulating aspects of consciousness and self-awareness based on {t['theory']}, then use it to explore the philosophical question: {t['question']}

Your response should include the following sections:

1. Theoretical Framework (250-300 words):
   a) Explain the key principles of {t['theory']} and how they relate to consciousness.
   b) Discuss how these principles can be translated into computational models.
   c) Identify potential challenges in implementing this theory in an AI system.

2. AI Architecture Design (300-350 words):
   a) Describe the overall structure of your AI system designed to simulate aspects of consciousness.
   b) Explain how each component of your architecture relates to {t['theory']}.
   c) Detail the data processing flow and decision-making mechanisms in your system.
   d) Include a high-level diagram of your architecture (described in words).

3. Consciousness Simulation Process (250-300 words):
   a) Explain how your system simulates key aspects of consciousness (e.g., self-awareness, subjective experience, intentionality).
   b) Describe any novel algorithms or techniques used in this simulation.
   c) Discuss how your system might handle edge cases or unexpected inputs.

4. Philosophical Exploration (250-300 words):
   a) Use your designed system to explore the question: {t['question']}
   b) Analyze how the simulated consciousness in your system relates to this philosophical question.
   c) Discuss any insights or new perspectives that arise from this exploration.

5. Limitations and Ethical Considerations (200-250 words):
   a) Identify potential limitations of your approach to simulating consciousness.
   b) Discuss ethical implications of creating systems that simulate consciousness.
   c) Propose guidelines for responsible development and use of consciousness-simulating AI.

6. Future Research Directions (150-200 words):
   a) Suggest two potential improvements or extensions to your system.
   b) Discuss how this technology might influence our understanding of consciousness and AI development.

Ensure your response demonstrates a deep understanding of consciousness theories, AI architectures, and philosophical reasoning. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and philosophical plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['theory']} and how it relates to consciousness",
            "The AI architecture design is innovative, well-explained, and plausibly implements aspects of consciousness simulation",
            f"The philosophical exploration of the question '{t['question']}' is thoughtful and insightful",
            "The response shows a strong grasp of the challenges and ethical implications of simulating consciousness in AI systems",
            "The writing is clear, well-structured, and demonstrates interdisciplinary knowledge integration"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
