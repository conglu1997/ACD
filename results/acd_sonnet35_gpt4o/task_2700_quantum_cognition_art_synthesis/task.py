import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "superposition",
            "entanglement",
            "interference",
            "contextuality"
        ]
        art_forms = [
            "visual art",
            "music",
            "interactive installation",
            "performance art"
        ]
        cognitive_domains = [
            "decision making",
            "memory",
            "perception",
            "language processing"
        ]
        traditional_theories = [
            "cognitive dissonance theory",
            "dual-process theory",
            "connectionist models",
            "schema theory"
        ]
        tasks = {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "art_form": random.choice(art_forms),
                "cognitive_domain": random.choice(cognitive_domains),
                "traditional_theory": random.choice(traditional_theories)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "art_form": random.choice(art_forms),
                "cognitive_domain": random.choice(cognitive_domains),
                "traditional_theory": random.choice(traditional_theories)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Quantum cognition theory applies quantum physics principles to explain cognitive phenomena, challenging classical probability-based models of cognition. Your task is to design and analyze an artistic piece based on the quantum cognition principle of {t['quantum_principle']}, expressed through the medium of {t['art_form']}, focusing on the cognitive domain of {t['cognitive_domain']}. Then, propose an experiment to test its cognitive effects on viewers. Your response should include:

1. Artistic Concept (250-300 words):
   a) Describe your proposed artistic piece in detail, explaining how it incorporates the quantum cognition principle.
   b) Explain how the chosen art form is used to express the quantum principle and explore the cognitive domain.
   c) Discuss the potential cognitive effects you aim to elicit in viewers.
   d) Address potential criticisms or limitations of your artistic approach.

2. Quantum Cognition Analysis (200-250 words):
   a) Analyze how your artistic piece embodies the chosen quantum cognition principle.
   b) Explain the theoretical connections between the quantum principle, the art form, and the cognitive domain.
   c) Discuss how this integration might challenge or extend current understanding of quantum cognition theory.
   d) Compare your quantum cognition approach to the traditional cognitive theory of {t['traditional_theory']} in this context.

3. Cognitive Impact Hypothesis (150-200 words):
   a) Formulate a specific hypothesis about how experiencing your artistic piece might influence cognition in the chosen domain.
   b) Explain the reasoning behind your hypothesis, grounded in quantum cognition theory.
   c) Discuss potential implications for our understanding of human cognition if your hypothesis is supported.

4. Experimental Design (250-300 words):
   a) Propose a detailed experiment to test the cognitive effects of your artistic piece on viewers.
   b) Describe the methodology, including participant selection, experimental conditions, and control measures.
   c) Explain how you will measure and analyze the cognitive effects related to your chosen domain.
   d) Address potential confounding variables and how you plan to control for them.
   e) Discuss potential limitations of your experimental design and how they might be addressed in future studies.

5. Interdisciplinary Implications (150-200 words):
   a) Discuss the potential impact of your work on the fields of quantum cognition, art theory, and cognitive science.
   b) Explore how this approach might lead to new research directions or artistic practices.
   c) Consider any ethical implications of using art to influence cognition based on quantum principles.
   d) Reflect on the broader implications of applying quantum principles to human cognition and artistic expression.

Ensure your response demonstrates a deep understanding of quantum cognition theory, artistic principles, and experimental design in cognitive science. Be creative and innovative while maintaining scientific rigor and plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1000-1250 words. Adhere to the specified word count ranges for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates an exceptional understanding of quantum cognition theory, artistic principles, and cognitive science.",
            "The artistic concept creatively and coherently integrates the specified quantum principle, art form, and cognitive domain.",
            "The quantum cognition analysis provides profound insights and connections between the artistic piece and theoretical principles.",
            "The cognitive impact hypothesis is well-reasoned, grounded in quantum cognition theory, and offers novel predictions.",
            "The experimental design is detailed, scientifically rigorous, innovative, and appropriate for testing the stated hypothesis.",
            "The discussion of interdisciplinary implications is insightful and considers far-reaching impacts across multiple fields.",
            "The response effectively compares the quantum cognition approach to the specified traditional cognitive theory.",
            "The overall response is highly creative, scientifically plausible, well-structured, and addresses potential limitations and criticisms.",
            "The response adheres to the specified word count ranges for each section and the overall word count limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
