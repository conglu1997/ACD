import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'quantum_principle': 'superposition',
                'cognitive_theory': 'parallel distributed processing',
                'ai_application': 'natural language processing'
            },
            {
                'quantum_principle': 'entanglement',
                'cognitive_theory': 'predictive coding',
                'ai_application': 'computer vision'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel cognitive architecture for AI systems inspired by the quantum mechanics principle of {t['quantum_principle']} and the cognitive science theory of {t['cognitive_theory']}. Apply this architecture to the AI domain of {t['ai_application']}.

Your response should include:

1. Theoretical Foundation (150-200 words):
   Explain the key concepts of the quantum principle and cognitive theory, and how they might be relevant to AI systems.

2. Architecture Design (250-300 words):
   Describe your proposed cognitive architecture, including:
   - How it incorporates the quantum principle and cognitive theory
   - The main components and their interactions
   - How the architecture processes information
   Provide a high-level diagram or pseudocode to illustrate your architecture.

3. Application to AI (200-250 words):
   Explain how your architecture could be applied to {t['ai_application']}. Include:
   - Potential advantages over traditional approaches
   - Specific tasks or problems it might excel at
   - Possible challenges in implementation

4. Implications and Future Directions (150-200 words):
   Discuss the broader implications of your architecture for:
   - AI and cognitive science
   - Our understanding of human cognition
   - Potential applications in other domains
   Propose two directions for future research based on your architecture.

Ensure your response demonstrates a deep understanding of quantum mechanics, cognitive science, and AI principles. Be creative in your design while maintaining scientific plausibility. Use technical terminology appropriately and provide explanations where necessary."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of the quantum principle of {t['quantum_principle']} and the cognitive theory of {t['cognitive_theory']}",
            "The proposed architecture creatively integrates concepts from quantum mechanics and cognitive science",
            f"The application to {t['ai_application']} is well-explained and plausible",
            "The response shows depth of knowledge in quantum mechanics, cognitive science, and AI",
            "The implications and future directions are insightful and well-reasoned"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
