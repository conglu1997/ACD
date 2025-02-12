import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            "emergency response coordination",
            "academic research collaboration",
            "intercultural diplomatic negotiations",
            "technical support for complex systems",
            "creative storytelling in virtual reality"
        ]
        cognitive_constraints = [
            "working memory limitations",
            "attention span in high-stress situations",
            "cross-linguistic conceptual mapping",
            "cognitive load in multitasking environments",
            "emotional state influence on information processing"
        ]
        compression_techniques = [
            "hierarchical concept clustering",
            "metaphor-based information encoding",
            "context-dependent semantic pruning",
            "multi-modal information fusion",
            "adaptive redundancy management"
        ]
        
        tasks = {
            "1": {
                "domain": random.choice(domains),
                "cognitive_constraint": random.choice(cognitive_constraints),
                "compression_technique": random.choice(compression_techniques)
            },
            "2": {
                "domain": random.choice(domains),
                "cognitive_constraint": random.choice(cognitive_constraints),
                "compression_technique": random.choice(compression_techniques)
            }
        }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel communication system based on semantic compression principles and cognitive load optimization for the domain of {t['domain']}. Your system should address the cognitive constraint of {t['cognitive_constraint']} and incorporate the compression technique of {t['compression_technique']}. Your response should include the following sections:

1. System Overview (250-300 words):
   a) Describe the key features and components of your communication system.
   b) Explain how it addresses the specified cognitive constraint.
   c) Detail how it incorporates the given compression technique.

2. Semantic Compression Mechanism (200-250 words):
   a) Explain the theoretical basis for your semantic compression approach.
   b) Describe how your system compresses and decompresses information.
   c) Provide an example of how a complex message would be compressed and transmitted.

3. Cognitive Load Optimization (200-250 words):
   a) Discuss how your system optimizes cognitive load for users.
   b) Explain any novel techniques used to enhance information processing and retention.
   c) Describe how your system adapts to individual users' cognitive capacities.

4. Implementation and Interface (150-200 words):
   a) Propose a user interface design for your communication system.
   b) Explain how the interface reflects the principles of semantic compression and cognitive load optimization.
   c) Discuss any challenges in implementing this system and how you would address them.

5. Comparative Analysis (200-250 words):
   a) Compare your system to traditional communication methods in the specified domain.
   b) Discuss the potential advantages and limitations of your approach.
   c) Explain how your system might perform in high-stakes or time-sensitive situations.

6. Ethical Considerations and Societal Impact (150-200 words):
   a) Identify potential ethical issues arising from the use of your communication system.
   b) Discuss how your system might influence social dynamics or power structures in the given domain.
   c) Propose guidelines for responsible development and use of semantic compression technologies.

7. Future Directions and Extensions (150-200 words):
   a) Suggest how your system could be adapted for other domains or use cases.
   b) Propose an experiment to evaluate the effectiveness of your communication system.
   c) Discuss potential implications for AI-human interaction and natural language processing.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and information theory. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1300-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a detailed description of a novel communication system based on semantic compression and cognitive load optimization.",
            f"The system effectively addresses the cognitive constraint of {t['cognitive_constraint']}.",
            f"The system incorporates the compression technique of {t['compression_technique']}.",
            f"The design is appropriate for the domain of {t['domain']}.",
            "The response demonstrates a deep understanding of linguistics, cognitive science, and information theory.",
            "The proposed system is innovative while maintaining scientific plausibility.",
            "The response addresses all required sections with appropriate depth and clarity."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
