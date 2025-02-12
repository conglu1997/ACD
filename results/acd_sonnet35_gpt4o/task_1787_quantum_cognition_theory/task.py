import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "superposition",
            "entanglement",
            "tunneling",
            "quantum coherence"
        ]
        cognitive_processes = [
            "decision making",
            "memory formation",
            "perception",
            "attention"
        ]
        return {
            "1": {"quantum_principle": random.choice(quantum_principles), "cognitive_process": random.choice(cognitive_processes)},
            "2": {"quantum_principle": random.choice(quantum_principles), "cognitive_process": random.choice(cognitive_processes)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Develop and analyze a theoretical framework that integrates the quantum mechanical principle of {t['quantum_principle']} with cognitive science to explain the cognitive process of {t['cognitive_process']}. Your response should include:

1. Theoretical Framework (300-350 words):
   a) Explain the key aspects of {t['quantum_principle']} and how it might apply to brain function.
   b) Describe your proposed mechanism for how {t['quantum_principle']} could influence {t['cognitive_process']}.
   c) Discuss how this quantum cognitive model differs from classical neuroscientific explanations.
   d) Address potential challenges in reconciling quantum effects with the warm, wet environment of the brain.

2. Experimental Predictions (250-300 words):
   a) Propose two specific, testable predictions that your quantum cognition theory makes about {t['cognitive_process']}.
   b) Describe potential experiments or observations that could validate or refute these predictions.
   c) Discuss any technological limitations in testing your theory and suggest how they might be overcome.

3. Philosophical Implications (200-250 words):
   a) Analyze how your quantum cognition theory might impact our understanding of consciousness and free will.
   b) Discuss potential implications for the nature of reality and the relationship between mind and matter.
   c) Consider how your theory relates to existing philosophical theories of mind (e.g., physicalism, dualism).

4. Interdisciplinary Connections (200-250 words):
   a) Explain how your theory integrates concepts from quantum physics, neuroscience, and cognitive psychology.
   b) Discuss potential implications of your theory for artificial intelligence and machine learning.
   c) Propose how insights from your quantum cognition theory could be applied in another scientific or technological domain.

5. Critical Analysis (200-250 words):
   a) Identify and discuss two major criticisms or limitations of your proposed quantum cognition theory.
   b) Compare your theory to other existing quantum consciousness theories (e.g., Orchestrated Objective Reduction).
   c) Suggest future research directions that could help refine or validate your theory.

Ensure your response demonstrates a deep understanding of both quantum mechanics and cognitive science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and speculative in your approach while maintaining scientific plausibility and acknowledging the highly theoretical nature of the topic.

Format your response with clear headings for each section and number your paragraphs within each section. Your total response should be between 1150-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of {t['quantum_principle']} and how it could potentially relate to {t['cognitive_process']}",
            "The proposed quantum cognition theory is creative, logically consistent, and scientifically plausible",
            "The experimental predictions are specific, testable, and logically follow from the proposed theory",
            "The philosophical implications are thoughtfully considered and discussed",
            "The response shows a deep integration of knowledge from quantum physics, neuroscience, and cognitive psychology",
            "The critical analysis demonstrates an understanding of the speculative nature of the theory and potential limitations"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
