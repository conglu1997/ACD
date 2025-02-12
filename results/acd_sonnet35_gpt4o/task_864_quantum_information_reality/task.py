import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            "Quantum Entanglement",
            "Quantum Superposition",
            "Quantum Tunneling",
            "Quantum Decoherence"
        ]
        philosophical_questions = [
            "The nature of free will",
            "The existence of objective reality",
            "The emergence of consciousness",
            "The concept of personal identity"
        ]
        return {
            "1": {"concept": random.choice(quantum_concepts), "question": random.choice(philosophical_questions)},
            "2": {"concept": random.choice(quantum_concepts), "question": random.choice(philosophical_questions)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Create a thought experiment that explores the implications of {t['concept']} on {t['question']}. Your response should include:\n\n1. Thought Experiment Design (200-250 words):\n   a) Describe a scenario that illustrates how {t['concept']} might influence or relate to {t['question']}.\n   b) Explain the key components and assumptions of your thought experiment.\n   c) Provide a clear, step-by-step description of how the thought experiment unfolds.\n\n2. Quantum Mechanics Analysis (150-200 words):\n   a) Explain the relevant principles of {t['concept']} in the context of your thought experiment.\n   b) Discuss how quantum information theory applies to or informs your scenario.\n   c) Address any potential misconceptions or common misunderstandings about the quantum concept.\n\n3. Philosophical Implications (200-250 words):\n   a) Analyze how your thought experiment sheds new light on {t['question']}.\n   b) Discuss potential challenges to existing philosophical views based on your experiment.\n   c) Propose at least one novel philosophical insight arising from your thought experiment.\n\n4. Interdisciplinary Connections (150-200 words):\n   a) Explore how your thought experiment might relate to other scientific disciplines (e.g., neuroscience, computer science, or cosmology).\n   b) Discuss potential technological applications or research directions inspired by your thought experiment.\n\n5. Critical Evaluation (100-150 words):\n   a) Identify potential limitations or criticisms of your thought experiment.\n   b) Propose how these limitations might be addressed in future iterations or experiments.\n\nEnsure your response demonstrates a deep understanding of both quantum mechanics and philosophical concepts. Be creative and rigorous in your approach, and use appropriate terminology from both fields. Your total response should be between 800-1050 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The thought experiment is creative, coherent, and effectively combines quantum mechanics with philosophical questions.",
            "The response demonstrates a clear understanding of the specified quantum concept and its implications.",
            "The philosophical analysis is insightful and well-reasoned, offering novel perspectives on the given question.",
            "The interdisciplinary connections are relevant and thought-provoking.",
            "The critical evaluation shows awareness of potential limitations and proposes reasonable solutions.",
            "The overall response is well-structured, scientifically accurate, and demonstrates high-level abstract reasoning."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
