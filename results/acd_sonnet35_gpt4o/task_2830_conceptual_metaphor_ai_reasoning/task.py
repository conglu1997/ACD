import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        source_domains = [
            "Physical Space",
            "Journey",
            "Container",
            "Force",
            "Balance"
        ]
        target_domains = [
            "Economic Systems",
            "Emotional States",
            "Social Relationships",
            "Time",
            "Argumentation"
        ]
        problem_areas = [
            "Climate Change Mitigation",
            "Healthcare Resource Allocation",
            "Educational Equity",
            "Technological Ethics",
            "Cultural Integration"
        ]
        
        return {
            "1": {
                "source_domain": random.choice(source_domains),
                "target_domain": random.choice(target_domains),
                "problem_area": random.choice(problem_areas)
            },
            "2": {
                "source_domain": random.choice(source_domains),
                "target_domain": random.choice(target_domains),
                "problem_area": random.choice(problem_areas)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that uses conceptual metaphors as a fundamental reasoning mechanism, focusing on the metaphor '{t['target_domain']} IS {t['source_domain']}'. Then, apply this system to address challenges in {t['problem_area']}. Your response should include:\n\n1. Conceptual Metaphor Analysis (200-250 words):\n   a) Explain the chosen conceptual metaphor and its cognitive implications.\n   b) Discuss how this metaphor shapes human understanding and reasoning about {t['target_domain']}.\n   c) Provide examples of linguistic expressions that reflect this conceptual metaphor.\n\n2. AI System Architecture (250-300 words):\n   a) Describe the key components of your AI system that implements metaphor-based reasoning.\n   b) Explain how your system represents and processes conceptual metaphors.\n   c) Detail how the system maps knowledge from the source domain to the target domain.\n   d) Discuss any novel techniques or approaches used in your design.\n\n3. Reasoning Mechanism (200-250 words):\n   a) Explain how your AI system uses the conceptual metaphor to reason about {t['target_domain']}.\n   b) Describe the inference processes and knowledge structures involved.\n   c) Discuss how your system handles potential limitations or inconsistencies in the metaphorical mapping.\n\n4. Application to {t['problem_area']} (250-300 words):\n   a) Apply your AI system to address a specific challenge in {t['problem_area']}.\n   b) Explain how the metaphor-based reasoning leads to novel insights or solutions.\n   c) Compare your system's approach to traditional problem-solving methods in this domain.\n\n5. Evaluation and Implications (200-250 words):\n   a) Propose metrics to evaluate your system's effectiveness in reasoning and problem-solving.\n   b) Discuss potential biases or limitations introduced by the chosen conceptual metaphor.\n   c) Explore the broader implications of metaphor-based AI systems for cognitive science and AI research.\n\n6. Ethical Considerations (150-200 words):\n   a) Discuss ethical implications of using metaphor-based reasoning in AI decision-making.\n   b) Address potential risks of anthropomorphizing complex systems through metaphorical thinking.\n   c) Propose guidelines for responsible development and use of such AI systems.\n\nEnsure your response demonstrates a deep understanding of conceptual metaphor theory, AI architectures, and the chosen problem domain. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1250-1550 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of conceptual metaphor theory and its application to AI reasoning.",
            "The proposed AI system architecture is innovative, well-explained, and scientifically plausible.",
            "The application of the system to the given problem area is creative, insightful, and demonstrates clear benefits of metaphor-based reasoning.",
            "The response addresses potential limitations, biases, and ethical considerations of the approach.",
            "The writing is clear, well-structured, and effectively uses technical terminology from cognitive science, linguistics, and AI."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
