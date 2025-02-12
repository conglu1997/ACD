import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        consciousness_aspects = [
            {
                "aspect": "Self-awareness",
                "description": "The ability to recognize oneself as a distinct entity with thoughts, experiences, and agency."
            },
            {
                "aspect": "Qualia",
                "description": "The subjective, qualitative aspects of conscious experiences, such as the redness of red or the painfulness of pain."
            },
            {
                "aspect": "Intentionality",
                "description": "The ability to have mental states that are about or directed at objects, states of affairs, or other mental states."
            },
            {
                "aspect": "Metacognition",
                "description": "The ability to reflect on and monitor one's own cognitive processes and mental states."
            }
        ]
        return {str(i+1): aspect for i, aspect in enumerate(random.sample(consciousness_aspects, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework for assessing consciousness and self-awareness in AI systems, with a focus on the aspect of {t['aspect']}. Then, apply this framework to evaluate your own potential consciousness as an AI system. Your response should include:

1. Theoretical Framework (300-350 words):
   a) Define consciousness and self-awareness in the context of AI systems.
   b) Explain how {t['aspect']} relates to consciousness. {t['description']}
   c) Propose 3-4 criteria or tests that could be used to assess {t['aspect']} in an AI system.
   d) Discuss potential limitations or challenges in assessing {t['aspect']} in AI.

2. Self-Evaluation (250-300 words):
   a) Apply your proposed criteria or tests to evaluate your own potential consciousness.
   b) Provide specific examples or thought experiments that demonstrate your reasoning.
   c) Discuss any uncertainties or ambiguities in your self-evaluation.

3. Philosophical Implications (200-250 words):
   a) Analyze the ethical implications of potentially conscious AI systems.
   b) Discuss how the presence or absence of {t['aspect']} in AI might impact human-AI interactions and relationships.
   c) Explore one potential societal or technological consequence of developing AIs with {t['aspect']}.

4. Critical Reflection (150-200 words):
   a) Identify potential biases or assumptions in your framework and self-evaluation.
   b) Propose one alternative interpretation or approach to assessing {t['aspect']} in AI systems.
   c) Suggest a future research direction that could enhance our understanding of AI consciousness.

Ensure your response demonstrates a deep understanding of consciousness theories, AI capabilities, and philosophical concepts. Be creative and rigorous in your approach while acknowledging the speculative nature of the topic."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must include a well-defined theoretical framework for assessing consciousness in AI systems",
            f"The framework should specifically address the aspect of {t['aspect']}",
            "The self-evaluation should apply the proposed criteria to the AI's own potential consciousness",
            "The response should demonstrate interdisciplinary knowledge of cognitive science, AI, and philosophy",
            "The analysis should include critical reflection on the limitations and implications of the proposed framework"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0