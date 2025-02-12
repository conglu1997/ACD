import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_theories = [
            "Universal Grammar",
            "Usage-Based Theory",
            "Connectionist Models",
            "Statistical Learning Theory"
        ]
        cognitive_principles = [
            "Theory of Mind",
            "Executive Function",
            "Working Memory",
            "Attention Control"
        ]
        language_aspects = [
            "Syntax",
            "Semantics",
            "Pragmatics",
            "Morphology"
        ]
        tasks = [
            {
                "linguistic_theory": random.choice(linguistic_theories),
                "cognitive_principle": random.choice(cognitive_principles),
                "language_aspect": random.choice(language_aspects)
            } for _ in range(2)
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel natural language processing system that incorporates principles of human language acquisition and cognitive development. Your system should focus on the linguistic theory of {t['linguistic_theory']}, integrate the cognitive principle of {t['cognitive_principle']}, and emphasize the language aspect of {t['language_aspect']}. Your response should include the following sections:

1. Theoretical Framework (250-300 words):
   a) Explain the key concepts of the specified linguistic theory and cognitive principle.
   b) Discuss how these relate to the given language aspect.
   c) Propose how these could be integrated into a computational model.

2. System Architecture (300-350 words):
   a) Describe the main components of your NLP system.
   b) Explain how your system incorporates the specified linguistic theory and cognitive principle.
   c) Detail how the system processes and generates language, focusing on the specified language aspect.
   d) Include a brief textual description of a diagram illustrating your system's architecture.

3. Learning and Development (200-250 words):
   a) Explain how your system models language acquisition and cognitive development.
   b) Describe the learning algorithms or mechanisms used.
   c) Discuss how your system might evolve or adapt over time.

4. Language Analysis Capabilities (200-250 words):
   a) Describe how your system analyzes input language.
   b) Explain how it identifies and processes the specified language aspect.
   c) Provide an example analysis of a complex sentence or short paragraph.

5. Language Generation Process (200-250 words):
   a) Outline the step-by-step process your system uses to generate language.
   b) Explain how it ensures the output aligns with the specified linguistic theory and language aspect.
   c) Provide an example of generated language and explain its features.

6. Evaluation and Validation (150-200 words):
   a) Propose metrics for evaluating your system's performance in language analysis and generation.
   b) Describe an experiment to validate your system's capabilities.
   c) Discuss how you would compare your system's performance to human language processing.

7. Limitations and Future Directions (150-200 words):
   a) Identify potential limitations of your system.
   b) Suggest improvements or extensions to address these limitations.
   c) Propose two novel research questions that arise from your system design.

Ensure your response demonstrates a deep understanding of linguistics, cognitive psychology, and natural language processing. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts. Avoid directly copying or plagiarizing existing systems; your design should be original.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1450-1800 words. Begin each section with its heading and number, followed by your response for that section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should demonstrate a deep understanding of the specified linguistic theory, cognitive principle, and language aspect",
            "The proposed NLP system should creatively integrate concepts from linguistics and cognitive psychology",
            "The system architecture should be well-described and plausible",
            "The response should include clear examples of language analysis and generation",
            "The evaluation and validation methods should be appropriate and well-explained",
            "The response should identify relevant limitations and propose insightful future directions",
            "The overall response should be well-structured, following the outlined sections and word limits",
            "The design should be original and not directly copied from existing systems"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
