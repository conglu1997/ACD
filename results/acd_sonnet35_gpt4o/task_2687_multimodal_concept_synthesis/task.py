import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        modalities = ['visual', 'auditory', 'linguistic', 'tactile', 'olfactory']
        abstract_concepts = ['time', 'justice', 'beauty', 'consciousness', 'infinity']
        problem_domains = ['climate change', 'space exploration', 'social inequality', 'artificial general intelligence', 'human longevity']
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                'modalities': random.sample(modalities, 3),
                'abstract_concept': random.choice(abstract_concepts),
                'problem_domain': random.choice(problem_domains)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system capable of synthesizing and manipulating the abstract concept of {t['abstract_concept']} across the modalities of {', '.join(t['modalities'])} to generate novel solutions in the problem domain of {t['problem_domain']}. Your response should include:\n\n1. Conceptual Framework (250-300 words):\n   a) Explain how your AI system represents and processes the abstract concept of {t['abstract_concept']} across different modalities.\n   b) Describe the mechanisms for translating and synthesizing information between modalities.\n   c) Discuss how your system maintains conceptual coherence across modalities.\n\n2. System Architecture (200-250 words):\n   a) Provide a high-level overview of your AI system's architecture.\n   b) Explain how different components work together to perform multimodal concept synthesis.\n   c) Describe any novel or unique features of your system.\n\n3. Concept Synthesis Process (250-300 words):\n   a) Detail the step-by-step process your AI system would follow to synthesize the concept of {t['abstract_concept']} across {', '.join(t['modalities'])}.\n   b) Explain how this synthesis process generates novel ideas or solutions.\n   c) Provide an example of a potential output from your system, describing its multimodal nature.\n\n4. Application to Problem Domain (200-250 words):\n   a) Apply your AI system to generate a novel solution or approach to {t['problem_domain']}.\n   b) Explain how the multimodal synthesis of {t['abstract_concept']} contributes to this solution.\n   c) Discuss the potential advantages of your approach compared to traditional problem-solving methods.\n\n5. Cognitive Science Foundations (150-200 words):\n   a) Discuss the cognitive science theories or principles that inform your AI system's design.\n   b) Explain how your system's approach to concept synthesis relates to human cognitive processes.\n\n6. Ethical Considerations and Limitations (150-200 words):\n   a) Identify potential ethical implications or challenges of using AI for multimodal concept synthesis.\n   b) Discuss any limitations of your proposed system and suggest areas for future research or improvement.\n\nEnsure your response demonstrates a deep understanding of cognitive science, artificial intelligence, and the specific modalities and problem domain. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.\n\nFormat your response with clear headings for each section. Your total response should be between 1200-1500 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of cognitive science and AI principles in relation to multimodal concept synthesis",
            f"The proposed AI system presents a plausible and creative approach to synthesizing the concept of {t['abstract_concept']} across {', '.join(t['modalities'])}",
            f"The application to {t['problem_domain']} is innovative and well-reasoned",
            "The response shows strong interdisciplinary knowledge integration and creative problem-solving",
            "Ethical considerations and limitations are thoroughly discussed"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
