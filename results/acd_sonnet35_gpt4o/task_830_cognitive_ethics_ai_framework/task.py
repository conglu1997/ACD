import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_architectures = [
            {
                "name": "ACT-R (Adaptive Control of Thought-Rational)",
                "description": "A cognitive architecture that defines various types of memory and learning mechanisms."
            },
            {
                "name": "SOAR (State, Operator, and Result)",
                "description": "A cognitive architecture based on the idea of problem spaces and goal-directed behavior."
            },
            {
                "name": "CLARION (Connectionist Learning with Adaptive Rule Induction ON-line)",
                "description": "A cognitive architecture that integrates connectionist, symbolic, motivational, and metacognitive processes."
            },
            {
                "name": "LIDA (Learning Intelligent Distribution Agent)",
                "description": "A cognitive architecture based on the Global Workspace Theory of consciousness."
            }
        ]
        return {str(i+1): arch for i, arch in enumerate(random.sample(cognitive_architectures, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel ethical framework for AI systems based on the cognitive architecture {t['name']}. Then, apply this framework to analyze the ethical implications of deploying AI in a specific domain. Your response should include:

1. Ethical Framework Design (300-350 words):
   a) Briefly explain the key features of {t['name']}. {t['description']}
   b) Describe how you will adapt this cognitive architecture into an ethical framework for AI.
   c) Define 3-4 core ethical principles derived from this cognitive architecture-based approach.
   d) Explain how these principles differ from traditional ethical frameworks in AI.

2. Framework Application (250-300 words):
   Apply your ethical framework to analyze the implications of deploying AI in the domain of autonomous vehicles.
   a) Describe how each of your core ethical principles would guide decision-making in this domain.
   b) Provide a specific ethical dilemma in autonomous vehicles and explain how your framework would approach it.
   c) Compare the outcome of your framework to that of a traditional ethical approach (e.g., utilitarianism or deontology).

3. Implications for AI Development (200-250 words):
   a) Discuss how adopting your cognitive architecture-based ethical framework might influence AI development practices.
   b) Analyze potential challenges in implementing this framework in real-world AI systems.
   c) Propose one novel AI development methodology or tool that could help integrate your ethical framework into AI systems.

4. Critial Analysis (150-200 words):
   a) Identify potential limitations or weaknesses in your ethical framework.
   b) Suggest one way to empirically test the effectiveness of your framework in guiding ethical AI behavior.
   c) Discuss how your framework might need to be adapted for different types of AI systems (e.g., narrow AI vs. artificial general intelligence).

Ensure your response demonstrates a deep understanding of cognitive architectures, AI ethics, and the challenges of implementing ethical frameworks in AI systems. Be creative and rigorous in your approach while acknowledging the speculative nature of the task."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must include a well-defined ethical framework based on the {t['name']} cognitive architecture",
            "The framework should be applied to analyze ethical implications in the autonomous vehicles domain",
            "The response should demonstrate interdisciplinary knowledge of cognitive science, AI ethics, and autonomous systems",
            "The analysis should include critical reflection on the limitations and implications of the proposed framework"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0