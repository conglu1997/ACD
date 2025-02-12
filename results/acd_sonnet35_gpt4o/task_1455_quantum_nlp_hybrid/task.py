import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "nlp_task": "Sentiment analysis",
                "quantum_approach": "Quantum state superposition for multi-dimensional sentiment representation"
            },
            {
                "nlp_task": "Machine translation",
                "quantum_approach": "Quantum entanglement for capturing cross-lingual semantic relationships"
            }
        ]
        return {
            "1": random.choice(tasks),
            "2": random.choice(tasks)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical hybrid quantum-classical system for the NLP task of {t['nlp_task']}, focusing on {t['quantum_approach']}. Your response should include:

1. Quantum-Classical Architecture (200-250 words):
   a) Describe the overall structure of your hybrid system.
   b) Explain which parts of the system are quantum and which are classical.
   c) Justify your choices for quantum vs. classical components.

2. Quantum Approach (250-300 words):
   a) Explain in detail how you would implement {t['quantum_approach']}.
   b) Describe the quantum algorithms or techniques you would use.
   c) Discuss how this quantum approach enhances the NLP task.

3. Data Encoding and Measurement (150-200 words):
   a) Explain how you would encode classical NLP data into quantum states.
   b) Describe your approach to measuring quantum states to obtain meaningful NLP results.

4. Potential Advantages (100-150 words):
   a) Discuss the theoretical advantages of your quantum-enhanced approach over classical methods.
   b) Provide quantitative estimates of potential improvements, if possible.

5. Challenges and Limitations (100-150 words):
   a) Identify key challenges in implementing your system.
   b) Discuss any limitations of your approach.

6. Future Implications (100-150 words):
   a) Speculate on how your system might impact the field of NLP.
   b) Discuss potential applications beyond the specified NLP task.

Ensure your response demonstrates a deep understanding of both quantum computing and NLP principles. Use appropriate terminology from both fields and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both quantum computing and NLP principles.",
            "The proposed system is innovative and creative while maintaining scientific plausibility.",
            "The explanation of the quantum approach is clear and well-justified.",
            "The response addresses all required sections comprehensively.",
            "The discussion of advantages, challenges, and future implications is insightful and well-reasoned."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
