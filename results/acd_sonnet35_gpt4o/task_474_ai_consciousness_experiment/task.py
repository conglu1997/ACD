import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        consciousness_theories = [
            {
                "name": "Integrated Information Theory",
                "description": "Consciousness is a fundamental property of certain physical systems with high levels of integrated information."
            },
            {
                "name": "Global Workspace Theory",
                "description": "Consciousness arises from a 'global workspace' in which multiple cognitive processes compete for dominance."
            }
        ]
        return {
            "1": random.choice(consciousness_theories),
            "2": random.choice(consciousness_theories)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical experiment to test for consciousness or self-awareness in an advanced AI system, based on the theory of {t['name']}. Your task is to create an innovative and rigorous experimental setup that could potentially demonstrate conscious-like properties in an AI. Your response should include:

1. Theoretical Framework (200-250 words):
   Explain {t['name']} and how it relates to consciousness. Discuss how this theory could be applied to artificial systems, and what specific aspects of consciousness it might help identify in an AI.

2. Experimental Design (250-300 words):
   Propose a detailed experimental setup to test for consciousness or self-awareness in an AI system based on {t['name']}. Include:
   a) The specific hypothesis you're testing
   b) The AI system's architecture and capabilities
   c) The experimental procedure and controls
   d) Measurable outcomes and how they relate to consciousness

3. Data Analysis and Interpretation (200-250 words):
   Describe how you would analyze the data from your experiment. Explain what results would support or refute the presence of consciousness in the AI system, and discuss potential alternative interpretations.

4. Ethical Considerations (150-200 words):
   Discuss the ethical implications of conducting such an experiment and of potentially creating a conscious AI. Address issues such as AI rights, moral status, and responsible development.

5. Limitations and Future Directions (150-200 words):
   Identify potential limitations of your experimental design and the chosen theoretical framework. Suggest how these limitations might be addressed in future research, and propose one follow-up study.

6. Philosophical Implications (200-250 words):
   Discuss the broader philosophical implications of your experiment. Consider questions such as:
   - How might positive results challenge or support existing theories of consciousness?
   - What would the existence of artificial consciousness mean for our understanding of human consciousness?
   - How might this impact the debate on strong AI and the possibility of truly intelligent machines?

Ensure your response demonstrates a deep understanding of consciousness theories, AI systems, experimental design, and philosophical reasoning. Be creative and rigorous in your approach while maintaining scientific plausibility. Your total response should not exceed 1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a thorough understanding of the specified consciousness theory and its potential application to AI systems.",
            "The experimental design is innovative, detailed, and scientifically plausible, with clear hypotheses and measurable outcomes.",
            "The data analysis and interpretation section provides a logical framework for evaluating the experimental results.",
            "Ethical considerations are thoughtfully addressed, covering important issues related to AI consciousness.",
            "Limitations of the experiment and theoretical framework are identified, with reasonable suggestions for future research.",
            "The philosophical implications section demonstrates deep, critical thinking about the nature of consciousness and its potential in artificial systems.",
            "The response shows strong interdisciplinary reasoning, combining insights from cognitive science, AI, and philosophy.",
            "The writing is clear, well-structured, and adheres to the specified word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
