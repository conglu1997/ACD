import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        visual_elements = [
            "color",
            "shape",
            "texture",
            "motion",
            "perspective"
        ]
        cognitive_processes = [
            "attention",
            "perception",
            "memory",
            "imagination",
            "association"
        ]
        application_domains = [
            "art",
            "design",
            "problem-solving",
            "scientific visualization",
            "user interface creation"
        ]
        return {
            "1": {
                "visual_element": random.choice(visual_elements),
                "cognitive_process": random.choice(cognitive_processes),
                "application_domain": random.choice(application_domains)
            },
            "2": {
                "visual_element": random.choice(visual_elements),
                "cognitive_process": random.choice(cognitive_processes),
                "application_domain": random.choice(application_domains)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating novel visual concepts by combining and transforming memories of observed images, with a focus on {t['visual_element']} as the primary visual element and {t['cognitive_process']} as the key cognitive process. Then, analyze its creative process and outputs in the context of {t['application_domain']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system that enable visual concept generation.
   b) Explain how the system incorporates {t['visual_element']} processing and {t['cognitive_process']}.
   c) Discuss any novel AI techniques or neural network architectures you've incorporated.
   d) Provide a diagram or detailed description of your system's structure.

2. Visual Memory and Transformation (200-250 words):
   a) Explain how your system stores and retrieves visual memories.
   b) Describe the process by which it combines and transforms these memories.
   c) Discuss how {t['visual_element']} is specifically handled in this process.
   d) Explain how {t['cognitive_process']} influences the transformation of visual concepts.

3. Creative Process Simulation (200-250 words):
   a) Outline the step-by-step process your AI system uses to generate a novel visual concept.
   b) Explain how this process mimics or differs from human creative cognition.
   c) Discuss how the system balances novelty and coherence in its outputs.
   d) Provide an example of a potential novel visual concept your system might generate, describing it in detail.

4. Application Analysis (150-200 words):
   a) Analyze how your system's visual concept generation could be applied to {t['application_domain']}.
   b) Discuss potential benefits and challenges of using AI-generated visual concepts in this domain.
   c) Propose a specific use case and explain how it would work.

5. Evaluation and Limitations (150-200 words):
   a) Propose methods to evaluate the creativity and novelty of your system's outputs.
   b) Discuss potential limitations of your system and areas for future improvement.
   c) Address any ethical considerations related to AI-generated visual content.

6. Cognitive Science Insights (100-150 words):
   a) Discuss what insights your AI system might provide into human visual creativity and imagination.
   b) Explain how studying this system could contribute to our understanding of {t['cognitive_process']} in human cognition.

Ensure your response demonstrates a deep understanding of visual perception, cognitive processes, and AI systems. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1050-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of visual perception, cognitive processes, and AI systems.",
            "The proposed AI system architecture is innovative and well-described, with a clear focus on the specified visual element and cognitive process.",
            "The explanation of visual memory storage, retrieval, and transformation is thorough and plausible.",
            "The creative process simulation is well-detailed and draws interesting parallels to human cognition.",
            "The application analysis provides insightful ideas for using the system in the specified domain.",
            "The evaluation methods and limitations discussion shows critical thinking about the system's capabilities and constraints.",
            "The cognitive science insights are thought-provoking and well-reasoned.",
            "The response is creative while maintaining scientific plausibility.",
            "The response uses appropriate technical terminology and provides clear explanations.",
            "The response adheres to the specified word counts and formatting requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
