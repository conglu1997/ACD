class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "cognitive_architecture": "ACT-R (Adaptive Control of Thought-Rational)",
                "semantic_space_type": "Conceptual Spaces",
                "application_domain": "Automated metaphor generation"
            },
            "2": {
                "cognitive_architecture": "SOAR (State, Operator, and Result)",
                "semantic_space_type": "Word Embeddings",
                "application_domain": "Cross-lingual information retrieval"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a semantic space for the {t['cognitive_architecture']} cognitive architecture using the {t['semantic_space_type']} approach. Then, propose a novel application in {t['application_domain']}. Your response should include:

1. Cognitive Architecture Overview (200-250 words):
   - Explain the key principles and components of the given cognitive architecture.
   - Discuss how it models human cognition and its strengths in AI applications.

2. Semantic Space Design (250-300 words):
   - Describe the {t['semantic_space_type']} approach and its relevance to semantic representation.
   - Design a semantic space that integrates with the given cognitive architecture.
   - Explain how your design captures semantic relationships and supports cognitive processes.

3. Integration Analysis (200-250 words):
   - Analyze how your semantic space design integrates with the cognitive architecture.
   - Discuss potential challenges and advantages of this integration.
   - Explain how this integration enhances the architecture's capabilities.

4. Novel Application (250-300 words):
   - Propose an innovative application in {t['application_domain']} using your integrated semantic space and cognitive architecture.
   - Describe the application's functionality and potential impact.
   - Explain how it leverages the strengths of both the semantic space and the cognitive architecture.

5. Implementation Outline (150-200 words):
   - Provide a high-level outline of how your application could be implemented.
   - Discuss potential challenges and how they might be addressed.
   - Suggest evaluation methods for assessing the application's performance.

Ensure your response demonstrates a deep understanding of cognitive architectures, semantic spaces, and their applications in AI and NLP. Use technical terminology appropriately and provide explanations where necessary. Be creative in your semantic space design and proposed application while maintaining scientific rigor."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response provides a comprehensive and accurate explanation of the given cognitive architecture and semantic space type.",
            "The semantic space design is creative, well-integrated with the cognitive architecture, and clearly explained.",
            "The integration analysis thoroughly discusses challenges, advantages, and enhancements to the architecture's capabilities.",
            "The proposed novel application is innovative, feasible, and clearly demonstrates how it leverages both the semantic space and cognitive architecture.",
            "The implementation outline is practical, addresses potential challenges, and suggests appropriate evaluation methods.",
            "The response adheres to the specified word count ranges for each section and demonstrates a sophisticated understanding of cognitive science, AI, and NLP concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
