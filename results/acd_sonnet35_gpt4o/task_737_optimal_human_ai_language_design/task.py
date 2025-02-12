import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "focus_area": "Semantic Representation",
                "constraint": "Minimize ambiguity",
                "cognitive_aspect": "Working memory limitations"
            },
            {
                "focus_area": "Syntactic Structure",
                "constraint": "Optimize for parallel processing",
                "cognitive_aspect": "Attention mechanisms"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an artificial language optimized for efficient and unambiguous communication between humans and AI systems. Focus on the area of {t['focus_area']}, with the primary constraint to {t['constraint']}, while considering the cognitive aspect of {t['cognitive_aspect']}. Your response should include:

1. Language Overview (250-300 words):
   a) Describe the key features of your artificial language.
   b) Explain how it addresses the focus area of {t['focus_area']}.
   c) Discuss how your language design considers both human cognitive limitations and AI processing capabilities.

2. Linguistic Structure (200-250 words):
   a) Detail the specific linguistic elements (e.g., phonology, morphology, syntax) of your language.
   b) Explain how these elements contribute to the constraint of {t['constraint']}.
   c) Provide examples of how your language structure differs from natural languages to better suit human-AI communication.

3. Cognitive Considerations (200-250 words):
   a) Analyze how your language design accounts for {t['cognitive_aspect']}.
   b) Discuss potential cognitive benefits and challenges for human users of this language.
   c) Explain how the language optimizes for AI processing while remaining accessible to human cognition.

4. Computational Implementation (200-250 words):
   a) Describe how your language could be computationally implemented in AI systems.
   b) Discuss any novel data structures or algorithms needed to process this language efficiently.
   c) Explain how your language design minimizes computational complexity while maximizing expressiveness.

5. Sample Dialogue (150-200 words):
   Provide a short sample dialogue in your artificial language, with translations and explanations. The dialogue should demonstrate:
   a) How the language addresses the focus area of {t['focus_area']}.
   b) How it achieves the constraint to {t['constraint']}.
   c) How it accounts for {t['cognitive_aspect']}.

6. Evaluation Metrics (150-200 words):
   a) Propose quantitative and qualitative metrics to evaluate the effectiveness of your language for human-AI communication.
   b) Describe an experimental setup to test these metrics.
   c) Discuss potential challenges in evaluating such an artificial language.

7. Ethical and Societal Implications (150-200 words):
   a) Analyze potential ethical concerns or societal impacts of implementing this language for human-AI communication.
   b) Discuss how your language design addresses or mitigates these concerns.
   c) Propose guidelines for responsible development and use of artificial languages for human-AI interaction.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and AI capabilities. Use appropriate technical terminology and provide explanations where necessary. Be creative in your language design while maintaining scientific plausibility and addressing the unique challenges of human-AI communication.

Your total response should be between 1300-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address the focus area of {t['focus_area']} in the language design.",
            f"The proposed language must effectively address the constraint to {t['constraint']}.",
            f"The language design must consider the cognitive aspect of {t['cognitive_aspect']} in a meaningful way.",
            "The artificial language must be logically consistent and demonstrate a clear understanding of linguistic principles.",
            "The response must include all seven required elements as specified in the instructions, with each section adequately addressing its respective topics.",
            "The proposed language must balance optimization for AI processing with accessibility for human users.",
            "The sample dialogue must effectively demonstrate the key features of the proposed language.",
            "The response must demonstrate creativity and innovation in language design while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
