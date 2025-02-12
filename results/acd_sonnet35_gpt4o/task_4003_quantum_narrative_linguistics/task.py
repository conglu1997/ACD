import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'quantum_concept': 'Quantum superposition',
                'linguistic_focus': 'Metaphor usage'
            },
            {
                'quantum_concept': 'Quantum entanglement',
                'linguistic_focus': 'Syntactic parallelism'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task involves three steps related to the quantum computing concept of {t['quantum_concept']} and the linguistic focus of {t['linguistic_focus']}:

1. Quantum Concept Explanation (100-150 words): Provide a clear, accurate explanation of the quantum computing concept. Include key principles and potential applications in quantum computing.

2. Short Story Creation (250-300 words): Write a creative short story that incorporates the quantum concept. Your story should make the concept accessible to a general audience while maintaining scientific accuracy. Use creative metaphors and analogies to illustrate the quantum principles.

3. Linguistic Analysis (200-250 words): Analyze your story focusing on the specified linguistic aspect. Explain how you used this linguistic feature to convey the quantum concept effectively. Discuss the challenges and benefits of using this linguistic approach to explain complex scientific ideas.

Format your response as follows:

Quantum Concept Explanation:
[Your explanation here]

Short Story:
[Your story here]

Linguistic Analysis:
[Your analysis here]

Ensure your response demonstrates a deep understanding of quantum computing, creative storytelling skills, and linguistic analysis capabilities."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation of the quantum computing concept is accurate and comprehensive.",
            "The short story effectively incorporates the quantum concept while being engaging and creative.",
            "The linguistic analysis demonstrates a deep understanding of the specified linguistic focus and its application in conveying complex scientific ideas.",
            "The overall response shows a strong ability to integrate knowledge from quantum computing, creative writing, and linguistics."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
