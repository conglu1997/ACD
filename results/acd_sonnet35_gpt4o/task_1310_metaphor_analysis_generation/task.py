import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        metaphor_types = [
            {
                "type": "Structural",
                "description": "One concept is metaphorically structured in terms of another",
                "example": "Life is a journey"
            },
            {
                "type": "Orientational",
                "description": "Organizes a whole system of concepts with respect to one another",
                "example": "Happy is up; sad is down"
            },
            {
                "type": "Ontological",
                "description": "Physical object, substance, or container metaphors",
                "example": "The mind is a machine"
            }
        ]
        
        domains = [
            "Technology", "Nature", "Emotions", "Economics", "Art"
        ]
        
        return {
            "1": {
                "metaphor_type": random.choice(metaphor_types),
                "source_domain": random.choice(domains),
                "target_domain": random.choice(domains)
            },
            "2": {
                "metaphor_type": random.choice(metaphor_types),
                "source_domain": random.choice(domains),
                "target_domain": random.choice(domains)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a system for analyzing existing metaphors and generating novel ones, focusing on {t['metaphor_type']['type']} metaphors. Your system should be able to analyze metaphors that map concepts from the domain of {t['source_domain']} to the domain of {t['target_domain']}. Then, use this system to generate new metaphors of the same type and domains.\n\n1. System Design (250-300 words):\n   a) Describe the key components of your metaphor analysis and generation system.\n   b) Explain how your system incorporates principles from cognitive linguistics, psychology, and artificial intelligence.\n   c) Discuss how your system would identify and represent conceptual mappings between domains.\n\n2. Metaphor Analysis (200-250 words):\n   a) Describe how your system would analyze the given example metaphor: '{t['metaphor_type']['example']}'.\n   b) Explain how it would identify the source and target domains, and the mappings between them.\n   c) Discuss how your system would evaluate the metaphor's effectiveness or novelty.\n\n3. Novel Metaphor Generation (200-250 words):\n   a) Explain the process your system would use to generate novel {t['metaphor_type']['type']} metaphors mapping concepts from {t['source_domain']} to {t['target_domain']}.\n   b) Provide two examples of metaphors your system might generate, and explain the conceptual mappings involved.\n   c) Discuss how your system ensures the generated metaphors are both novel and meaningful.\n\n4. Cognitive Plausibility (150-200 words):\n   a) Analyze how well your system aligns with current theories of human metaphor comprehension and generation.\n   b) Discuss any simplifications or abstractions in your model and their potential impact.\n   c) Propose an experiment to test the cognitive plausibility of your system.\n\n5. Applications and Implications (150-200 words):\n   a) Suggest two potential applications of your metaphor analysis and generation system.\n   b) Discuss the implications of such a system for our understanding of human cognition and creativity.\n   c) Explore any ethical considerations related to automated metaphor generation.\n\nEnsure your response demonstrates a deep understanding of metaphor theory, natural language processing, and cognitive science. Be innovative in your approach while maintaining scientific plausibility."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of metaphor theory and cognitive linguistics.",
            "The system design effectively integrates principles from linguistics, psychology, and AI.",
            "The metaphor analysis process is clearly explained and theoretically sound.",
            "The novel metaphor generation process is creative, well-reasoned, and produces meaningful results.",
            "The discussion of cognitive plausibility shows critical thinking and awareness of current theories.",
            "The proposed applications and implications are insightful and demonstrate interdisciplinary thinking."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
