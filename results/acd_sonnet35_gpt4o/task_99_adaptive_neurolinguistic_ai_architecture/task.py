class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "language_aspect": "Syntax parsing, semantic processing, and pragmatics",
                "brain_region": "Broca's area, Wernicke's area, and prefrontal cortex",
                "cognitive_process": "Working memory, attention switching, and cognitive flexibility",
                "simulated_environment": "Real-time multilingual crisis negotiation with unexpected cultural misunderstandings",
                "adaptive_challenge": "Sudden change in communication medium (e.g., from verbal to text-based)"
            },
            "2": {
                "language_aspect": "Discourse analysis, metaphor comprehension, and emotional language processing",
                "brain_region": "Right hemisphere, limbic system, and anterior cingulate cortex",
                "cognitive_process": "Theory of mind, context integration, and emotional regulation",
                "simulated_environment": "Cross-cultural diplomatic communication with time pressure and shifting alliances",
                "adaptive_challenge": "Unexpected introduction of a new stakeholder with conflicting interests"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You have 35 minutes to complete this task. Design an adaptive cognitive architecture for AI language processing inspired by neurolinguistic models of human language processing, and analyze its performance in a complex, time-constrained, and dynamically changing simulated environment. Focus on the following aspects:

1. Language Aspects: {t['language_aspect']}
2. Brain Regions: {t['brain_region']}
3. Cognitive Processes: {t['cognitive_process']}
4. Simulated Environment: {t['simulated_environment']}
5. Adaptive Challenge: {t['adaptive_challenge']}

Your response should include:

1. Adaptive Architecture Overview (300-350 words):
   - Describe the main components of your cognitive architecture.
   - Explain how these components interact to process language efficiently under time constraints and adapt to unexpected changes.
   - Highlight how your design is inspired by the specified brain regions and cognitive processes, emphasizing adaptability.

2. Neurolinguistic Basis (250-300 words):
   - Explain the roles of the specified brain regions in human language processing, particularly in adaptive contexts.
   - Describe how the cognitive processes contribute to language comprehension, production, and adaptation to new situations.
   - Discuss how your architecture mimics or adapts these neurological and cognitive features for efficient and flexible processing.

3. AI Implementation (300-350 words):
   - Propose specific AI techniques or algorithms that could be used to implement your adaptive architecture.
   - Explain how these techniques relate to the neurolinguistic inspiration of your design and enable real-time adaptation.
   - Discuss any novel approaches or combinations of existing methods in your implementation to handle the complex, time-constrained, and dynamically changing environment.

4. Adaptive Mechanism (250-300 words):
   - Describe in detail how your architecture would handle the specified adaptive challenge.
   - Explain the decision-making process and the reconfiguration of the system in response to unexpected changes.
   - Discuss how the adaptive mechanism maintains performance in language processing while adjusting to new conditions.

5. Data Flow Diagram:
   - Create a detailed diagram (using ASCII art) illustrating the flow of information through your adaptive architecture.
   - Label each component and show how data moves between them, highlighting adaptive pathways and feedback loops.

6. Performance Analysis (250-300 words):
   - Describe how your architecture would perform in the specified complex, time-constrained, and dynamically changing simulated environment.
   - Identify potential strengths and weaknesses of your design in this context, particularly regarding speed, accuracy, and adaptability trade-offs.
   - Propose metrics to evaluate the performance of your architecture in the given environment, considering linguistic accuracy, time efficiency, and adaptive capability.

7. Limitations and Future Directions (200-250 words):
   - Identify potential limitations of your proposed adaptive architecture, especially in handling unforeseen challenges.
   - Suggest areas for future research or improvement to enhance performance and adaptability.
   - Discuss how your architecture could be extended to other aspects of language processing or adapted for even more complex, real-world scenarios with multiple simultaneous adaptive challenges.

Ensure your response demonstrates a deep understanding of neurolinguistics, cognitive science, and artificial intelligence, with a focus on efficient processing and adaptation under dynamic conditions. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility and addressing the challenges of the complex, time-constrained, and unpredictable environment."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response provides a detailed and coherent description of an adaptive cognitive architecture for AI language processing, clearly inspired by neurolinguistic models and optimized for efficient processing and real-time adaptation.",
            "The architecture effectively incorporates the specified language aspects, brain regions, and cognitive processes, with a focus on handling time constraints and unexpected changes.",
            "The neurolinguistic basis is accurately explained and well-integrated into the proposed AI implementation, considering the challenges of rapid processing and adaptation.",
            "The AI implementation suggests specific, relevant techniques and explains their relationship to the neurolinguistic inspiration, with a focus on efficiency, adaptability, and handling complex, dynamic environments.",
            "The adaptive mechanism is clearly described and demonstrates how the architecture would handle the specified challenge, including decision-making processes and system reconfiguration.",
            "A clear, detailed, and informative data flow diagram is provided using ASCII art, highlighting adaptive pathways and feedback loops.",
            "The performance analysis thoroughly examines the architecture's behavior in the specified complex, time-constrained, and dynamically changing simulated environment, including strengths, weaknesses, and evaluation metrics that consider accuracy, speed, and adaptability.",
            "Limitations and future directions are thoughtfully discussed, with a focus on improving performance and adaptability in complex, unpredictable scenarios.",
            "The response demonstrates a sophisticated understanding of neurolinguistics, cognitive science, and artificial intelligence, using technical terminology appropriately and addressing the challenges of efficient processing and adaptation in dynamic environments.",
            "The proposed architecture is creative and innovative in its approach to handling time constraints, complex environments, and unexpected changes while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
