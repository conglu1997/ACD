import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_theories = [
            {
                "theory": "Conceptual Metaphor Theory",
                "description": "Proposes that metaphors are not just linguistic expressions but fundamental cognitive mechanisms"
            },
            {
                "theory": "Conceptual Blending Theory",
                "description": "Suggests that new concepts emerge from the integration of existing mental spaces"
            }
        ]
        
        target_domains = [
            "Artificial Intelligence",
            "Climate Change",
            "Social Media",
            "Quantum Computing"
        ]
        
        return {
            "1": {"cognitive_theory": random.choice(cognitive_theories), "target_domain": random.choice(target_domains)},
            "2": {"cognitive_theory": random.choice(cognitive_theories), "target_domain": random.choice(target_domains)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of understanding and generating novel metaphors based on the principles of {t['cognitive_theory']['theory']}. Your system should be able to create and interpret metaphors related to {t['target_domain']}. Provide your response in the following format:

1. Theoretical Framework (250-300 words):
   a) Explain the key principles of {t['cognitive_theory']['theory']} and how they relate to metaphor comprehension and generation.
   b) Describe how your AI system incorporates these principles in its design.
   c) Discuss the relevance of {t['target_domain']} as a target domain for metaphor generation.
   d) Explain how your system would handle the abstraction and mapping required for metaphor processing.

2. System Architecture (300-350 words):
   a) Provide a detailed description of your AI system's architecture.
   b) Explain how each component contributes to metaphor understanding and generation.
   c) Describe the computational models or algorithms used in your system.
   d) Include a diagram or flowchart of your system architecture (use ASCII art or a clear textual description).
   e) Explain how your system integrates linguistic knowledge with domain-specific knowledge about {t['target_domain']}.

3. Metaphor Comprehension Process (200-250 words):
   a) Describe the step-by-step process of how your system interprets a given metaphor.
   b) Explain how it handles the specific challenges related to {t['target_domain']}.
   c) Provide an example of how your system would interpret a novel metaphor in this domain.

4. Metaphor Generation Mechanism (200-250 words):
   a) Explain how your system generates novel metaphors based on its knowledge and the given domain.
   b) Describe the creative processes involved in your system's metaphor generation.
   c) Provide an example of a metaphor your system might generate for {t['target_domain']}.
   d) Discuss how your system ensures the generated metaphors are both novel and meaningful.

5. Evaluation and Benchmarking (150-200 words):
   a) Propose methods for evaluating your system's metaphor comprehension and generation capabilities.
   b) Suggest benchmarks or tests that could compare its performance to human metaphor processing.
   c) Discuss potential limitations of your evaluation approach.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Address ethical implications of developing AI systems that can understand and generate metaphors.
   b) Discuss potential applications of your system in fields such as education, creative writing, or marketing.
   c) Suggest areas for future research or improvement of your system.

Ensure your response demonstrates a deep understanding of cognitive linguistics, conceptual blending theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a comprehensive understanding of {t['cognitive_theory']['theory']} and its application to metaphor processing.",
            f"The proposed AI system architecture is well-designed and integrates linguistic knowledge with domain-specific knowledge about {t['target_domain']}.",
            "The metaphor comprehension and generation processes are clearly explained and plausible.",
            "The system demonstrates creativity in metaphor generation while ensuring meaningfulness.",
            "Ethical considerations are thoroughly addressed, including potential applications and future directions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
