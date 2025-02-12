import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "thought_experiment": "The Chinese Room",
                "philosophical_problem": "The nature of consciousness and understanding"
            },
            {
                "thought_experiment": "The Ship of Theseus",
                "philosophical_problem": "Personal identity and the persistence of objects over time"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neural network architecture to simulate and analyze the philosophical thought experiment '{t['thought_experiment']}', then apply it to explore the philosophical problem of {t['philosophical_problem']}. Your response should include:

1. Neural Architecture Design (250-300 words):
   a) Describe the key components and structure of your neural network architecture.
   b) Explain how your architecture models the essential elements of the thought experiment.
   c) Discuss how your design incorporates relevant neuroscientific principles.
   d) Include a simple diagram or pseudocode snippet illustrating a key aspect of your architecture.

2. Philosophical Mapping (200-250 words):
   a) Explain how you map the philosophical concepts and relationships in the thought experiment to your neural network.
   b) Describe any novel techniques used to represent abstract philosophical ideas in a neural format.
   c) Discuss potential challenges in accurately representing the thought experiment in a neural network.

3. Simulation Process (250-300 words):
   a) Detail how your neural network simulates the thought experiment.
   b) Provide a step-by-step description of the simulation process, including input, processing, and output.
   c) Explain how the simulation helps explore or analyze the specified philosophical problem.
   d) Discuss any emergent behaviors or unexpected results from your simulation.

4. Analysis and Insights (200-250 words):
   a) Analyze the results of your simulation in the context of the philosophical problem.
   b) Discuss any new insights or perspectives gained from this neural approach to philosophy.
   c) Compare your approach to traditional philosophical methods of analyzing thought experiments.

5. Implications and Limitations (150-200 words):
   a) Discuss the potential implications of your neural philosophy simulator for AI ethics and consciousness research.
   b) Address limitations of your approach and potential objections from philosophers or neuroscientists.
   c) Propose guidelines for the responsible development and use of AI systems that engage with philosophical concepts.

6. Future Directions (150-200 words):
   a) Suggest two potential extensions or improvements to your neural philosophy simulator.
   b) Propose an experiment to further explore the relationship between neural networks and philosophical reasoning.
   c) Speculate on how this research might influence our understanding of machine consciousness or artificial general intelligence.

Ensure your response demonstrates a deep understanding of neural network architectures, philosophical concepts, and their potential interactions. Use technical terminology appropriately and provide explanations where necessary. Be creative and innovative in your approach while maintaining scientific and philosophical plausibility.

Format your response with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a detailed description of the neural network architecture that appropriately models the thought experiment",
            "The philosophical mapping is well-explained and addresses the challenges of representing abstract ideas in a neural format",
            "The simulation process is clearly described and demonstrates how it explores the philosophical problem",
            "The analysis provides novel insights or perspectives on the philosophical problem",
            "Implications and limitations are thoroughly discussed with proposed guidelines",
            "Future research directions are innovative and well-reasoned",
            "The response demonstrates a deep understanding of neural networks, philosophy, and their potential interactions",
            "The approach is creative and innovative while maintaining scientific and philosophical plausibility",
            "Appropriate technical terminology is used throughout the response",
            "The response is well-structured with clear headings for each section"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
