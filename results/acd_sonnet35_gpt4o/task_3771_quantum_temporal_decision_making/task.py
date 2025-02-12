import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        decision_contexts = [
            {
                "context": "Career planning",
                "time_scales": ["immediate", "short-term", "long-term"],
                "linguistic_aspect": "future tense constructions"
            },
            {
                "context": "Climate change mitigation",
                "time_scales": ["daily", "yearly", "generational"],
                "linguistic_aspect": "conditional statements"
            },
            {
                "context": "Financial investment",
                "time_scales": ["hourly", "monthly", "decade-long"],
                "linguistic_aspect": "probabilistic language"
            },
            {
                "context": "Health and wellness",
                "time_scales": ["daily", "seasonal", "lifetime"],
                "linguistic_aspect": "imperative mood"
            }
        ]
        return {
            "1": random.choice(decision_contexts),
            "2": random.choice(decision_contexts)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired cognitive framework for temporal decision-making in the context of {t['context']}. Your framework should integrate principles from quantum computing, linguistics, and cognitive science to model and optimize decision processes across the following time scales: {', '.join(t['time_scales'])}. Pay special attention to the linguistic aspect of {t['linguistic_aspect']}. Your response should include:

1. Framework Overview (300-350 words):
   a) Describe the key components of your quantum-inspired cognitive framework for temporal decision-making.
   b) Explain how it incorporates quantum principles, linguistic elements, and cognitive science concepts.
   c) Discuss how your framework addresses decision-making across the specified time scales.
   d) Include a high-level diagram or pseudocode representing the framework's structure (describe it textually).

2. Quantum-Cognitive Mapping (250-300 words):
   a) Explain how quantum states or processes in your framework correspond to cognitive elements or decision-making processes.
   b) Describe how your framework models the temporal aspects of decision-making using quantum-inspired concepts.
   c) Discuss how the specified linguistic aspect is integrated into the quantum-cognitive model.

3. Decision Process Modeling (250-300 words):
   a) Detail how your framework models the decision-making process in the given context.
   b) Explain how it handles the different time scales specified.
   c) Provide an example of how a specific decision might be represented and processed in your framework.

4. Mathematical Representation (150-200 words):
   a) Provide a mathematical formalization of your framework, using equations to represent key concepts and processes.
   b) Explain the significance of each term in your equations and how they relate to the quantum-cognitive-linguistic integration.

5. Optimization and Learning (200-250 words):
   a) Describe how your framework optimizes decision-making processes over time.
   b) Explain any learning mechanisms that allow the framework to adapt to new information or changing circumstances.
   c) Discuss how the framework balances short-term and long-term considerations in decision-making.

6. Linguistic Integration (200-250 words):
   a) Explain in detail how your framework incorporates the specified linguistic aspect.
   b) Discuss how this linguistic integration enhances the temporal decision-making process.
   c) Provide an example of how linguistic features influence the quantum-cognitive representation of a decision.

7. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical implications of using this framework for decision-making in the given context.
   b) Address any limitations or potential biases in your approach.
   c) Propose guidelines for responsible development and use of quantum-inspired cognitive decision-making systems.

Ensure your response demonstrates a deep understanding of quantum computing principles, cognitive science, linguistics, and decision theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Adhere strictly to the word count for each section. Your total response should be between 1500-1850 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing principles, cognitive science, linguistics, and decision theory.",
            "The framework effectively integrates quantum-inspired concepts with cognitive and linguistic elements.",
            "The design addresses temporal decision-making across the specified time scales in the given context.",
            "The framework incorporates the specified linguistic aspect in a meaningful way.",
            "The response includes innovative ideas while maintaining scientific plausibility.",
            "The mathematical representation accurately formalizes key concepts of the framework.",
            "Ethical considerations and limitations are thoughtfully addressed.",
            "The response adheres to the specified word count for each section and overall."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
