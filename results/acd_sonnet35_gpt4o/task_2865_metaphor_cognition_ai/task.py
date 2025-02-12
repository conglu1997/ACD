import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_theories = [
            "Conceptual Metaphor Theory",
            "Blending Theory",
            "Structure-Mapping Theory"
        ]
        application_domains = [
            "Mental Health Counseling",
            "Science Education",
            "Business Strategy Communication",
            "Political Discourse Analysis"
        ]
        metaphor_types = [
            "Structural metaphors",
            "Ontological metaphors",
            "Orientational metaphors"
        ]
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                "cognitive_theory": random.choice(cognitive_theories),
                "application_domain": random.choice(application_domains),
                "metaphor_type": random.choice(metaphor_types)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can analyze and generate metaphorical language based on {t['cognitive_theory']}, focusing on {t['metaphor_type']}. Then, apply this system to enhance human-AI communication in the domain of {t['application_domain']}. Your response should include:

1. Theoretical Framework (250-300 words):
   a) Explain the key principles of {t['cognitive_theory']} and how they relate to metaphor processing.
   b) Describe how {t['metaphor_type']} function and their significance in cognitive linguistics.
   c) Discuss how these theories can be operationalized in an AI system.

2. AI System Architecture (300-350 words):
   a) Outline the main components of your AI system for metaphor analysis and generation.
   b) Explain how your system incorporates the principles of {t['cognitive_theory']}.
   c) Describe the mechanisms for identifying, interpreting, and generating {t['metaphor_type']}.
   d) Discuss any novel approaches or technologies used in your design.

3. Metaphor Processing Example (200-250 words):
   a) Provide an example of how your system would analyze a complex metaphor in the context of {t['application_domain']}.
   b) Demonstrate how your system would generate a novel, contextually appropriate metaphor for a concept in {t['application_domain']}.
   c) Explain how these processes reflect the underlying cognitive theory and metaphor type.

4. Application in {t['application_domain']} (250-300 words):
   a) Describe how your metaphor cognition AI system would be applied in {t['application_domain']}.
   b) Explain the potential benefits of using metaphor-aware AI in this domain.
   c) Discuss any challenges specific to this application and how your system addresses them.
   d) Provide a concrete example of how your system could enhance human-AI communication in this domain.

5. Evaluation and Validation (200-250 words):
   a) Propose methods for evaluating the performance of your metaphor cognition AI system.
   b) Describe how you would validate the system's understanding and generation of metaphors.
   c) Discuss potential metrics for assessing the system's impact on human-AI communication in {t['application_domain']}.

6. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to AI systems that process and generate metaphorical language.
   b) Discuss how these issues might specifically manifest in {t['application_domain']}.
   c) Propose guidelines for the responsible development and use of metaphor cognition AI.

7. Future Directions (100-150 words):
   a) Suggest two potential extensions or improvements to your metaphor cognition AI system.
   b) Discuss how these enhancements could further our understanding of human cognition or advance AI capabilities.

Ensure your response demonstrates a deep understanding of cognitive linguistics, artificial intelligence, and the specific application domain. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and ethical considerations.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive linguistics, artificial intelligence, and the specified application domain.",
            "The AI system architecture is well-designed and clearly incorporates the principles of the given cognitive theory.",
            "The metaphor processing example effectively illustrates the system's capabilities in analysis and generation.",
            "The application to the specified domain is well-explained and includes concrete examples of enhancing human-AI communication.",
            "The evaluation and validation methods are appropriate and comprehensive.",
            "Ethical considerations are thoroughly addressed and relevant to the specific application domain.",
            "Future directions are innovative and well-reasoned.",
            "The response is creative and demonstrates effective interdisciplinary knowledge integration.",
            "The response follows the required format, including section headings, and adheres to the word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
