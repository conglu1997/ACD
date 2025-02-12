import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            "Climate Change",
            "Artificial Intelligence",
            "Quantum Physics",
            "Economic Inequality",
            "Neuroscience",
            "Cybersecurity"
        ]
        cognitive_processes = [
            "Analogical Mapping",
            "Conceptual Blending",
            "Image Schema Activation",
            "Embodied Simulation"
        ]
        return {
            "1": {
                "domain": random.choice(domains),
                "cognitive_process": random.choice(cognitive_processes)
            },
            "2": {
                "domain": random.choice(domains),
                "cognitive_process": random.choice(cognitive_processes)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models the cognitive process of {t['cognitive_process']} in metaphor comprehension and generation, then apply it to create and analyze novel metaphors in the domain of {t['domain']}. Your response should include:

1. Cognitive Model (250-300 words):
   a) Explain the key features of {t['cognitive_process']} and its role in metaphor processing.
   b) Describe how you would model this cognitive process in an AI system.
   c) Discuss how your model integrates insights from cognitive science and linguistics.

2. AI System Architecture (250-300 words):
   a) Outline the key components of your AI metaphor system.
   b) Explain how your system implements the cognitive model of {t['cognitive_process']}.
   c) Describe the data sources and training approach for your system.

3. Metaphor Generation (200-250 words):
   a) Explain how your AI system would generate novel metaphors in the domain of {t['domain']}.
   b) Provide two examples of metaphors your system might create, with explanations.
   c) Discuss how the cognitive process of {t['cognitive_process']} influences the generation process.

4. Metaphor Analysis (200-250 words):
   a) Describe how your system would analyze and interpret metaphors in the {t['domain']} domain.
   b) Explain how it would identify the underlying conceptual mappings and inferences.
   c) Discuss potential challenges in metaphor analysis and how your system addresses them.

5. Evaluation and Implications (200-250 words):
   a) Propose methods for evaluating the quality and novelty of the generated metaphors.
   b) Discuss potential applications of your system in fields such as creative writing, science communication, or AI research.
   c) Analyze how your approach might contribute to our understanding of human cognition and creativity.

6. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to AI-generated metaphors and their interpretation.
   b) Discuss the implications of using AI to model human cognitive processes.
   c) Propose guidelines for the responsible development and use of metaphor-generating AI systems.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately explains and models the cognitive process of {t['cognitive_process']} in metaphor comprehension and generation.",
            f"The AI system architecture is well-designed and effectively implements the cognitive model for the domain of {t['domain']}.",
            "The generated metaphors are novel, relevant to the given domain, and demonstrate a clear understanding of the cognitive process involved.",
            "The metaphor analysis approach is comprehensive and grounded in cognitive science and linguistics.",
            "The evaluation methods and potential applications are well-reasoned and insightful.",
            "The ethical considerations are thoughtful and address important issues in AI-generated metaphors.",
            "The response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence.",
            "The writing is clear, well-structured, and adheres to the specified format and word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
