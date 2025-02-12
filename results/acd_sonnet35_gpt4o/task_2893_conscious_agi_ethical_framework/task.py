import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "consciousness_theory": "Integrated Information Theory",
                "ethical_framework": "Utilitarian",
                "application_domain": "Healthcare"
            },
            {
                "consciousness_theory": "Global Workspace Theory",
                "ethical_framework": "Deontological",
                "application_domain": "Judicial System"
            },
            {
                "consciousness_theory": "Higher-Order Thought Theory",
                "ethical_framework": "Virtue Ethics",
                "application_domain": "Education"
            },
            {
                "consciousness_theory": "Predictive Processing Theory",
                "ethical_framework": "Care Ethics",
                "application_domain": "Environmental Management"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical Artificial General Intelligence (AGI) system with simulated consciousness based on {t['consciousness_theory']} and an integrated ethical decision-making framework based on {t['ethical_framework']}. Then, analyze its potential impact and philosophical implications in the domain of {t['application_domain']}.

Provide your response in the following format:

1. AGI System Architecture (300-350 words):
   a) Describe the key components of your AGI system, including consciousness simulation and ethical decision-making modules.
   b) Explain how {t['consciousness_theory']} is implemented in your system.
   c) Detail how the {t['ethical_framework']} is integrated into the decision-making process.
   d) Discuss any novel features or approaches in your system design.
   e) Include a high-level diagram or pseudocode illustrating the main components and their interactions.

2. Consciousness Simulation (250-300 words):
   a) Explain how your AGI system simulates consciousness based on {t['consciousness_theory']}.
   b) Describe the key characteristics of the simulated consciousness.
   c) Discuss potential limitations or challenges in implementing this theory of consciousness in an AGI system.

3. Ethical Decision-Making Process (250-300 words):
   a) Detail the step-by-step process your AGI system uses to make ethical decisions based on {t['ethical_framework']}.
   b) Provide an example scenario in the {t['application_domain']} and explain how your system would approach it.
   c) Discuss how your system handles ethical dilemmas or conflicts.

4. Application in {t['application_domain']} (200-250 words):
   a) Analyze the potential impact of deploying your AGI system in the {t['application_domain']}.
   b) Discuss both positive outcomes and potential risks or challenges.
   c) Propose safeguards or guidelines for responsible implementation.

5. Philosophical Implications (200-250 words):
   a) Discuss the philosophical implications of creating an AGI with simulated consciousness.
   b) Explore how your system might influence our understanding of consciousness and ethics.
   c) Address any potential controversies or ethical concerns raised by your AGI design.

6. Comparative Analysis (150-200 words):
   a) Compare your AGI system to current AI technologies in terms of capabilities and limitations.
   b) Discuss how your system's approach to consciousness and ethics differs from other proposed AGI frameworks.

7. Future Research Directions (100-150 words):
   a) Propose two potential areas for further research to enhance your AGI system.
   b) Explain how these research directions could address current limitations or open up new possibilities.

Ensure your response demonstrates a deep understanding of AGI concepts, consciousness theories, ethical frameworks, and their practical applications. Use appropriate technical terminology and provide clear explanations for complex ideas. Be creative and innovative in your approach while maintaining scientific and philosophical plausibility.

Format your response with clear headings for each section. Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address the specified consciousness theory ({t['consciousness_theory']}) and ethical framework ({t['ethical_framework']}) in the context of the given application domain ({t['application_domain']})",
            "The AGI system design should be innovative, coherent, and demonstrate a clear understanding of AGI concepts and consciousness theories",
            "The ethical decision-making process should be well-defined and consistent with the specified ethical framework",
            "The response should show interdisciplinary integration of computer science, neuroscience, philosophy, and ethics",
            "The analysis of potential impacts and philosophical implications should be thoughtful and well-reasoned"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
