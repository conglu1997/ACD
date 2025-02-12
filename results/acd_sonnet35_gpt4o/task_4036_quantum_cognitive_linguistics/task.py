import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            "Superposition",
            "Entanglement",
            "Interference",
            "Contextuality"
        ]
        linguistic_processes = [
            "Semantic ambiguity resolution",
            "Syntactic parsing",
            "Pragmatic inference",
            "Metaphor comprehension"
        ]
        social_scenarios = [
            "Negotiation in a multicultural business setting",
            "Political debate on a contentious issue",
            "Conflict resolution in a diverse community",
            "Cross-cultural communication in diplomacy"
        ]
        tasks = {
            "1": {
                "quantum_concept": random.choice(quantum_concepts),
                "linguistic_process": random.choice(linguistic_processes),
                "social_scenario": random.choice(social_scenarios)
            },
            "2": {
                "quantum_concept": random.choice(quantum_concepts),
                "linguistic_process": random.choice(linguistic_processes),
                "social_scenario": random.choice(social_scenarios)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum cognitive model of language processing and decision-making, focusing on the quantum concept of {t['quantum_concept']} and its application to the linguistic process of {t['linguistic_process']}. Then, apply your model to analyze and predict linguistic behavior in the following social scenario: {t['social_scenario']}.

        Your response should include the following sections:

        1. Quantum Cognitive Model (300-350 words):
           a) Explain how the quantum concept of {t['quantum_concept']} can be applied to model the linguistic process of {t['linguistic_process']}.
           b) Describe the key components and mechanisms of your quantum cognitive model.
           c) Discuss how your model differs from classical cognitive models of language processing.
           d) Include a simple diagram or mathematical formulation of your model using ASCII characters.

        2. Linguistic Process Analysis (250-300 words):
           a) Analyze how your quantum cognitive model represents and processes {t['linguistic_process']}.
           b) Explain any novel insights or predictions that emerge from your quantum approach.
           c) Discuss potential limitations or challenges in applying quantum concepts to this linguistic process.

        3. Social Scenario Application (300-350 words):
           a) Apply your quantum cognitive model to analyze linguistic behavior in the scenario: {t['social_scenario']}.
           b) Provide specific predictions or explanations for linguistic phenomena in this scenario based on your model.
           c) Discuss how the quantum nature of your model contributes to a deeper understanding of the complex social dynamics involved.

        4. Experimental Design (200-250 words):
           a) Propose an experiment to test the predictions of your quantum cognitive model in the given social scenario.
           b) Describe the methodology, including participant selection, procedure, and data collection.
           c) Explain how you would analyze the results to validate or refine your model.

        5. Interdisciplinary Implications (150-200 words):
           a) Discuss the potential implications of your quantum cognitive model for other fields (e.g., artificial intelligence, neuroscience, social psychology).
           b) Propose a novel research question that combines quantum cognition, linguistics, and another discipline of your choice.

        6. Ethical Considerations (150-200 words):
           a) Analyze potential ethical implications of using quantum cognitive models to predict and influence linguistic behavior in social scenarios.
           b) Propose guidelines for the responsible development and application of such models in real-world contexts.

        Ensure your response demonstrates a deep understanding of quantum theory, cognitive science, and linguistics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and coherence across all sections of your response.

        Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum theory, cognitive science, and linguistics.",
            "The quantum cognitive model is well-explained and coherently applies the specified quantum concept to the given linguistic process.",
            "The application to the social scenario is insightful and demonstrates how the quantum model provides novel understanding.",
            "The experimental design is well-thought-out and appropriate for testing the model's predictions.",
            "Interdisciplinary implications and ethical considerations are thoroughly discussed.",
            "The response is creative and innovative while maintaining scientific plausibility.",
            "The response is well-structured, clear, and within the specified word limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
