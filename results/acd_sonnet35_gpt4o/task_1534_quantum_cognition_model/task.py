import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_processes = [
            "decision making",
            "memory formation and retrieval",
            "perception and sensory processing",
            "language comprehension and production"
        ]
        quantum_concepts = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "decoherence"
        ]
        tasks = [
            {
                "cognitive_process": process,
                "quantum_concept": concept
            }
            for process, concept in zip(random.sample(cognitive_processes, 2), random.sample(quantum_concepts, 2))
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical model of quantum cognition, focusing on how the quantum mechanical concept of {t['quantum_concept']} might influence the cognitive process of {t['cognitive_process']}. Your response should include:

1. Theoretical Framework (300-350 words):
   a) Explain the basic principles of {t['quantum_concept']} in quantum mechanics.
   b) Describe current understanding of {t['cognitive_process']} in cognitive science.
   c) Propose a novel hypothesis for how {t['quantum_concept']} could play a role in {t['cognitive_process']}.
   d) Discuss how your hypothesis challenges or extends current theories in cognitive science.

2. Model Description (250-300 words):
   a) Present a detailed description of your quantum cognition model.
   b) Explain how it incorporates both {t['quantum_concept']} and {t['cognitive_process']}.
   c) Provide a mathematical or conceptual framework for your model.
   d) Discuss any assumptions or limitations of your model.

3. Predictions and Implications (200-250 words):
   a) Describe specific predictions your model makes about {t['cognitive_process']}.
   b) Explain how these predictions differ from those of classical cognitive models.
   c) Discuss potential implications of your model for our understanding of consciousness or free will.

4. Experimental Design (250-300 words):
   a) Propose an experiment to test a key prediction of your quantum cognition model.
   b) Describe the methodology, including participant selection, experimental procedure, and measurement techniques.
   c) Explain how your experiment could distinguish between quantum and classical cognitive processes.
   d) Discuss potential challenges in implementing your experiment and how you would address them.

5. Interdisciplinary Connections (150-200 words):
   a) Explore how your model might connect to other fields such as quantum biology or quantum computing.
   b) Discuss potential technological applications that could arise from your quantum cognition model.
   c) Propose a future research direction that combines insights from your model with another scientific discipline.

Ensure your response demonstrates a deep understanding of both quantum mechanics and cognitive science. Use technical terminology appropriately and provide explanations where necessary. Be creative in your model design while maintaining scientific plausibility. Your total response should be between 1150-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both quantum mechanics and cognitive science",
            "The proposed quantum cognition model is creative, well-structured, and incorporates the given quantum concept and cognitive process",
            "The theoretical framework and model description are scientifically plausible and well-explained",
            "The predictions and implications of the model are logical and distinguish it from classical cognitive models",
            "The experimental design is well-thought-out and could feasibly test the model's predictions",
            "Interdisciplinary connections and potential applications are insightfully discussed",
            "The response is well-organized and adheres to the specified word counts for each section"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
