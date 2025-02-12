import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_processes = [
            "memory formation and retrieval",
            "decision making",
            "attention allocation",
            "language comprehension",
            "spatial reasoning"
        ]
        geometric_concepts = [
            "hyperbolic spaces",
            "manifold learning",
            "graph neural networks",
            "simplicial complexes",
            "persistent homology"
        ]
        return {
            "1": {
                "cognitive_process": random.choice(cognitive_processes),
                "geometric_concept": random.choice(geometric_concepts)
            },
            "2": {
                "cognitive_process": random.choice(cognitive_processes),
                "geometric_concept": random.choice(geometric_concepts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a geometric deep learning model to simulate the human cognitive process of {t['cognitive_process']}, incorporating the geometric concept of {t['geometric_concept']}.

Geometric deep learning extends traditional deep learning to non-Euclidean domains, such as graphs and manifolds, allowing for more expressive representations of complex data structures.

Your response should include:

1. Theoretical Framework (250-300 words):
   a) Explain the chosen cognitive process and its key characteristics.
   b) Describe how the specified geometric concept can be applied to model this process.
   c) Discuss the potential advantages of using geometric deep learning for this application.

2. Model Architecture (300-350 words):
   a) Propose a detailed architecture for your geometric deep learning model.
   b) Explain how it incorporates the specified geometric concept.
   c) Describe the key components and their roles in simulating the cognitive process.
   d) Include at least one equation or formal representation of a critical component in your model.

3. Data Requirements and Processing (200-250 words):
   a) Specify the types of data needed to train and validate your model.
   b) Describe how you would preprocess and represent this data geometrically.
   c) Discuss any challenges in obtaining or preparing suitable data for this application.

4. Training and Optimization (200-250 words):
   a) Outline the training procedure for your model, including loss functions and optimization techniques.
   b) Explain how you would handle any unique challenges related to the geometric nature of your model.
   c) Discuss strategies for ensuring the model generalizes well to novel cognitive scenarios.

5. Evaluation and Validation (200-250 words):
   a) Propose methods to evaluate the performance and biological plausibility of your model.
   b) Describe key metrics or experiments that would validate your approach.
   c) Discuss how you would compare your model's performance to traditional non-geometric approaches.

6. Limitations and Challenges (150-200 words):
   a) Identify potential limitations of your proposed model.
   b) Discuss any challenges that might arise in implementing or scaling your model.
   c) Suggest possible ways to address these limitations and challenges.

7. Implications and Future Directions (150-200 words):
   a) Discuss the potential impact of your model on our understanding of human cognition.
   b) Explore possible applications of your model in cognitive science or AI research.
   c) Suggest two extensions or improvements to your model for future research.

Ensure your response demonstrates a deep understanding of cognitive science, geometric deep learning, and relevant mathematical concepts. Use technical terminology appropriately and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility. Your total response should be between 1450-1800 words, with each section adhering to the specified word limits."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both the specified cognitive process and geometric concept.",
            "The proposed model architecture is well-detailed and clearly incorporates the geometric concept in modeling the cognitive process.",
            "The data requirements, processing methods, and training procedures are thoroughly explained and appropriate for the task.",
            "The evaluation methods and metrics are well-designed and suitable for assessing the model's performance and biological plausibility.",
            "The limitations and challenges of the proposed model are thoughtfully discussed with potential solutions.",
            "The discussion of implications and future directions shows insight into the potential impact and applications of the model.",
            "The response is creative and innovative while maintaining scientific and mathematical rigor.",
            "The response adheres to the specified word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
