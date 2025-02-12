import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'cognitive_theory': 'Usage-based theory',
                'linguistic_focus': 'Syntactic development',
                'ai_technique': 'Reinforcement learning'
            },
            {
                'cognitive_theory': 'Connectionist models',
                'linguistic_focus': 'Phonological acquisition',
                'ai_technique': 'Neural networks'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a cognitive system for language acquisition and generation inspired by theories of child language development. Your system should incorporate principles from neuroscience, linguistics, and artificial intelligence, focusing on the cognitive theory of {t['cognitive_theory']}, the linguistic area of {t['linguistic_focus']}, and utilizing the AI technique of {t['ai_technique']}. Your response should include the following sections:

1. Theoretical Framework (250-300 words):
   a) Explain the key principles of {t['cognitive_theory']} and how they relate to language acquisition.
   b) Describe how your system incorporates these principles in its design.
   c) Discuss the relevance of {t['linguistic_focus']} in child language development.
   d) Briefly explain the basics of {t['ai_technique']} and its relevance to this task.
   e) Provide a concrete example illustrating how these elements interact in your system.

2. System Architecture (300-350 words):
   a) Provide a detailed description of your cognitive system's architecture.
   b) Explain how each component contributes to language acquisition and generation.
   c) Describe how you integrate {t['ai_technique']} into your system.
   d) Include a diagram or flowchart of your system architecture (use ASCII art or a clear textual description).
   e) Give an example scenario demonstrating how information flows through your system.

3. Language Acquisition Process (250-300 words):
   a) Describe the step-by-step process of how your system acquires language.
   b) Explain how it handles the specific challenges related to {t['linguistic_focus']}.
   c) Discuss how your system's approach differs from traditional AI language models.
   d) Provide an example of how your system would learn a specific linguistic feature.

4. Language Generation Mechanism (200-250 words):
   a) Explain how your system generates language based on its acquired knowledge.
   b) Provide an example of how it would generate a simple sentence or phrase.
   c) Discuss how the system ensures grammatical correctness and semantic coherence.
   d) Describe a scenario where your system adapts its language generation based on context.

5. Learning and Adaptation (200-250 words):
   a) Describe how your system learns and adapts over time.
   b) Explain how it handles errors and incorporates feedback.
   c) Discuss any mechanisms for generalizing learned patterns to new contexts.
   d) Provide an example of how your system would adapt to a novel linguistic input.

6. Evaluation and Benchmarking (150-200 words):
   a) Propose methods for evaluating your system's language acquisition and generation capabilities.
   b) Suggest benchmarks or tests that could compare its performance to human language learners.
   c) Discuss potential limitations of your evaluation approach.

7. Comparative Analysis (150-200 words):
   a) Compare your proposed system to existing approaches in language acquisition and generation.
   b) Discuss the potential advantages and limitations of your system.
   c) Explain how your system addresses challenges that current approaches struggle with.

8. Challenges and Limitations (150-200 words):
   a) Identify and discuss potential challenges in implementing your proposed system.
   b) Analyze any limitations or constraints of your approach.
   c) Suggest possible solutions or areas for future research to address these challenges.

9. Ethical Considerations and Future Directions (150-200 words):
   a) Address ethical implications of developing AI systems that mimic child language acquisition.
   b) Discuss potential applications of your system in education or clinical settings.
   c) Suggest areas for future research or improvement of your system.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1800-2250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed design of a cognitive system for language acquisition and generation, incorporating {t['cognitive_theory']}, focusing on {t['linguistic_focus']}, and utilizing {t['ai_technique']}.",
            "The theoretical framework is thoroughly explained, linking the chosen cognitive theory to language acquisition principles and briefly explaining the basics of the specified AI technique.",
            "The system architecture is clearly described with all components and their interactions explained, including a diagram or flowchart and an example scenario.",
            "The language acquisition process is detailed, addressing specific challenges related to the given linguistic focus and providing an example of learning a specific linguistic feature.",
            "The language generation mechanism is explained with a concrete example of sentence or phrase generation and a scenario demonstrating context-based adaptation.",
            "Learning and adaptation processes are described, including error handling, generalization mechanisms, and an example of adapting to novel linguistic input.",
            "Evaluation methods and benchmarks are proposed, with a discussion of potential limitations.",
            "A comparative analysis of the proposed system with existing approaches is provided, discussing advantages and limitations.",
            "Potential challenges and limitations of the proposed system are identified and analyzed, with suggestions for future research.",
            "Ethical considerations and future research directions are addressed.",
            "The response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence, using appropriate technical terminology.",
            "The proposed system is innovative while maintaining scientific plausibility.",
            "Concrete examples and scenarios are provided throughout the response to illustrate key concepts and system functionality.",
            "The response adheres to the specified word count limits for each section and the overall word count range of 1800-2250 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
