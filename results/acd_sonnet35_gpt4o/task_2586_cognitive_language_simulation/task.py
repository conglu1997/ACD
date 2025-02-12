import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_processes = [
            "Working Memory",
            "Analogical Reasoning",
            "Conceptual Blending",
            "Metacognition"
        ]
        language_model_types = [
            "Transformer-based",
            "Recurrent Neural Network",
            "Graph Neural Network",
            "Neuro-symbolic"
        ]
        application_domains = [
            "Cognitive Psychology Research",
            "Educational Technology",
            "Human-AI Collaboration",
            "Mental Health Diagnostics"
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "cognitive_process": random.choice(cognitive_processes),
                "language_model_type": random.choice(language_model_types),
                "application_domain": random.choice(application_domains)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a cognitive language simulation system that models the cognitive process of {t['cognitive_process']} using a {t['language_model_type']} language model. Then, analyze its potential applications in {t['application_domain']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your cognitive language simulation system.
   b) Explain how you integrate the specified cognitive process into the language model architecture.
   c) Detail how your system simulates or models the given cognitive process.
   d) Discuss any novel features that distinguish your system from traditional language models.

2. Cognitive-Linguistic Mapping (250-300 words):
   a) Explain how linguistic features or processes in your model correspond to cognitive states or processes.
   b) Provide a specific example of how this mapping works for the given cognitive process.
   c) Discuss potential advantages of this approach over classical cognitive models.

3. Implementation and Training (200-250 words):
   a) Describe how your system would be implemented and trained.
   b) Explain any novel training techniques or data requirements.
   c) Discuss how you would validate the cognitive fidelity of your model.

4. Potential Applications (250-300 words):
   a) Propose three potential applications of your system in the specified domain.
   b) Explain how each application leverages the unique features of your cognitive language simulation.
   c) Discuss potential impacts and benefits of these applications.

5. Limitations and Ethical Considerations (200-250 words):
   a) Identify at least three potential limitations or challenges of your system.
   b) Discuss any ethical concerns that may arise from its development or application.
   c) Propose potential solutions or guidelines to address these issues.

6. Future Research Directions (150-200 words):
   a) Suggest two potential research projects that could further explore or validate your cognitive language simulation system.
   b) Describe how these projects could contribute to our understanding of human cognition or advance AI development.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must design a cognitive language simulation system that models {t['cognitive_process']} using a {t['language_model_type']} language model",
            f"The design should be creative and plausible, integrating principles from cognitive science, linguistics, and artificial intelligence",
            "The response should thoroughly analyze the application of the system to the specified domain",
            "The system architecture should be detailed and include novel or innovative elements",
            "Ethical considerations and limitations should be thoughtfully addressed",
            "The proposed future research directions should be relevant and well-described",
            "The overall response should demonstrate interdisciplinary thinking and creative problem-solving"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
