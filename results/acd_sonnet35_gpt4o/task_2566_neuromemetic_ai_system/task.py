import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "memory_type": "episodic memory",
                "brain_region": "hippocampus",
                "ai_application": "improved data retention in deep learning models",
                "neurotransmitter": "acetylcholine",
                "synaptic_mechanism": "long-term potentiation"
            },
            {
                "memory_type": "semantic memory",
                "brain_region": "neocortex",
                "ai_application": "enhanced knowledge representation in natural language processing",
                "neurotransmitter": "glutamate",
                "synaptic_mechanism": "spike-timing-dependent plasticity"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that mimics human {t['memory_type']} formation and retrieval processes based on neuroscientific principles of the {t['brain_region']}, and apply it to {t['ai_application']}. Your response should include:

1. Neuroscientific Foundation (200-250 words):
   a) Explain the key processes involved in {t['memory_type']} formation and retrieval in the human brain, focusing on the {t['brain_region']}.
   b) Discuss the role of {t['synaptic_mechanism']} and the neurotransmitter {t['neurotransmitter']} in these processes.
   c) Describe how these processes contribute to learning and adaptive behavior.

2. AI System Architecture (250-300 words):
   a) Design the main components of your AI system that mimic the neuroscientific processes you described.
   b) Explain how each component corresponds to specific brain functions or structures.
   c) Describe how these components interact to form and retrieve memories.
   d) Include a simple ASCII diagram illustrating your system's architecture.

3. Memory Formation and Retrieval Algorithm (200-250 words):
   a) Outline the key steps in your algorithm for memory formation and retrieval.
   b) Explain how your algorithm incorporates principles of {t['synaptic_mechanism']} and neural network dynamics.
   c) Provide a brief pseudocode (8-10 lines) for a critical part of your algorithm.
   d) Include a mathematical formula that represents a key aspect of your algorithm (e.g., weight update rule, activation function).

4. Application to {t['ai_application']} (250-300 words):
   a) Describe how your neuromemetic AI system can be applied to {t['ai_application']}.
   b) Explain the potential advantages of your approach compared to traditional methods.
   c) Discuss any challenges in implementing your system and how you would address them.
   d) Provide a specific example of how your system would improve performance in this application, including a hypothetical quantitative improvement (e.g., percentage increase in accuracy or efficiency).

5. Comparative Analysis (150-200 words):
   a) Compare your neuromemetic approach to existing AI methods for memory and learning.
   b) Discuss the strengths and limitations of your approach.
   c) Explain how your system might be combined with other AI techniques for optimal performance.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss potential ethical implications of developing AI systems that closely mimic human brain functions.
   b) Propose guidelines for responsible development and use of neuromemetic AI systems.
   c) Suggest future research directions or potential applications of your system beyond the current scope.

Ensure your response demonstrates a deep understanding of both neuroscience and artificial intelligence. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section and include a word count at the end. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience and artificial intelligence principles, specifically addressing {t['memory_type']}, {t['brain_region']}, {t['synaptic_mechanism']}, and {t['neurotransmitter']}.",
            "The AI system design effectively mimics the specified human memory processes and includes a clear ASCII diagram.",
            "The memory formation and retrieval algorithm is well-explained, including pseudocode and a relevant mathematical formula.",
            "The application to {t['ai_application']} is well-explained, plausible, and includes a specific example with a hypothetical quantitative improvement.",
            "The comparative analysis shows critical thinking about the strengths and limitations of the approach.",
            "Ethical considerations are thoughtfully addressed with specific guidelines proposed.",
            "The response is creative while maintaining scientific plausibility.",
            "Appropriate technical terminology is used throughout with clear explanations provided.",
            "The response follows the specified format and word count requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
