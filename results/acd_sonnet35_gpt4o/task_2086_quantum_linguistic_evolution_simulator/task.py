import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "linguistic_feature": "Phonological change",
                "quantum_principle": "Superposition",
                "time_scale": "100 years",
                "cultural_context": "Isolated island community"
            },
            {
                "linguistic_feature": "Semantic shift",
                "quantum_principle": "Entanglement",
                "time_scale": "500 years",
                "cultural_context": "Interplanetary colonization"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired language model that simulates linguistic drift and evolution over time. Your model should focus on the following parameters:

1. Linguistic feature to model: {t['linguistic_feature']}
2. Quantum principle to incorporate: {t['quantum_principle']}
3. Time scale for simulation: {t['time_scale']}
4. Cultural context: {t['cultural_context']}

Brief overview of quantum computing principles:
Quantum computing utilizes quantum mechanical phenomena such as superposition (the ability of a quantum system to be in multiple states simultaneously) and entanglement (the correlation between quantum particles) to perform computations. These principles allow for the exploration of multiple possibilities simultaneously and the modeling of complex, interconnected systems.

Your response should include:

1. Model Architecture (300-350 words):
   a) Describe the key components of your quantum-inspired language model.
   b) Explain how you incorporate the specified quantum principle into your model.
   c) Detail how your model simulates linguistic change over time.
   d) Include a high-level diagram or pseudocode to illustrate your model's structure.

2. Linguistic Evolution Simulation (250-300 words):
   a) Explain how your model simulates the specified linguistic feature's evolution.
   b) Describe the role of the quantum principle in this simulation.
   c) Discuss how your model accounts for the given cultural context in language change.

3. Quantum-Linguistic Mapping (200-250 words):
   a) Explain how you map linguistic concepts to quantum states or operations.
   b) Describe how the specified quantum principle enhances the modeling of language evolution.
   c) Discuss any novel insights this quantum approach might offer to linguistic theory.

4. Sample Output (150-200 words):
   a) Provide a brief example of your model's output, showing language evolution over the specified time scale.
   b) Explain how this output demonstrates the influence of the quantum principle and cultural context.

5. Evaluation and Implications (200-250 words):
   a) Propose methods to evaluate the accuracy and usefulness of your model.
   b) Discuss potential implications of your quantum-inspired approach for understanding language change and cultural evolution.
   c) Explore how this technology might impact fields such as historical linguistics, cultural anthropology, and artificial intelligence.

6. Limitations and Challenges (100-150 words):
   a) Discuss potential limitations of your proposed model.
   b) Identify challenges in implementing or scaling your quantum-inspired language model.
   c) Suggest possible ways to address these limitations and challenges in future research.

Ensure your response demonstrates a deep understanding of quantum computing, linguistics, and evolutionary theory. Use technical terminology appropriately and provide explanations where necessary. Be innovative in your approach while maintaining scientific plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of both quantum computing principles and linguistic theory",
            "The proposed model effectively incorporates the specified quantum principle in modeling language evolution",
            "The simulation of linguistic change is plausible and accounts for the given cultural context",
            "The quantum-linguistic mapping is innovative and well-explained",
            "The sample output and its explanation are coherent and illustrate the model's capabilities",
            "The evaluation methods and discussion of implications show deep insight into the interdisciplinary nature of the task",
            "The response identifies relevant limitations and challenges, and proposes thoughtful solutions",
            "The overall approach demonstrates creativity and originality in addressing the task"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
