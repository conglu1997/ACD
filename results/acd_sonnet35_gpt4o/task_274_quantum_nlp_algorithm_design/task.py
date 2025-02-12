import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        nlp_tasks = [
            "text classification",
            "named entity recognition",
            "sentiment analysis",
            "machine translation",
            "text summarization",
            "question answering"
        ]
        quantum_concepts = [
            "superposition",
            "entanglement",
            "quantum interference",
            "quantum annealing",
            "variational quantum circuits",
            "quantum walks"
        ]
        tasks = {
            "1": {
                "nlp_task": random.choice(nlp_tasks),
                "quantum_concept": random.choice(quantum_concepts)
            },
            "2": {
                "nlp_task": random.choice(nlp_tasks),
                "quantum_concept": random.choice(quantum_concepts)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum algorithm for the natural language processing task of {t['nlp_task']}, leveraging the quantum computing concept of {t['quantum_concept']}. Your response should include:

1. Algorithm Overview (200-250 words):
   - Briefly explain the chosen NLP task and its challenges.
   - Describe your proposed quantum algorithm, focusing on how it incorporates {t['quantum_concept']}.
   - Outline the key steps of the algorithm and how they address the NLP task.

2. Quantum Advantage (150-200 words):
   - Analyze the potential advantages of your quantum algorithm over classical approaches.
   - Discuss any speedup or improvement in accuracy that might be achieved.
   - Explain how the chosen quantum concept contributes to these advantages.

3. Implementation Challenges (150-200 words):
   - Identify potential obstacles in implementing your algorithm on current or near-term quantum hardware.
   - Discuss any limitations or assumptions in your approach.
   - Propose potential solutions or areas for further research to address these challenges.

4. Linguistic Implications (150-200 words):
   - Analyze how your quantum NLP algorithm might impact our understanding of language processing.
   - Discuss any novel insights or approaches to linguistics that your algorithm might enable.
   - Speculate on potential long-term implications for the field of computational linguistics.

5. Pseudocode or Circuit Diagram:
   - Provide a high-level pseudocode or a simplified quantum circuit diagram (using ASCII art) that illustrates the key components of your algorithm.

Ensure your response demonstrates a deep understanding of both quantum computing principles and natural language processing techniques. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide brief explanations of complex concepts."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a clear algorithm overview that incorporates the specified quantum concept",
            "The potential quantum advantages are thoroughly analyzed",
            "Implementation challenges are identified and discussed",
            "The linguistic implications of the quantum NLP algorithm are explored",
            "A pseudocode or circuit diagram is provided to illustrate the algorithm",
            "The response demonstrates understanding of both quantum computing and NLP concepts",
            "The proposed algorithm is creative while maintaining scientific plausibility"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
