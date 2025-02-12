import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "context": "resource allocation in a post-scarcity society",
                "behavioral_bias": "status quo bias",
                "social_factor": "group identity"
            },
            {
                "context": "interspecies negotiation in a galactic federation",
                "behavioral_bias": "hyperbolic discounting",
                "social_factor": "cultural relativism"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel decision-making framework that integrates concepts from game theory, behavioral economics, and social psychology. Your framework should address the context of {t['context']}, incorporate the behavioral bias of {t['behavioral_bias']}, and consider the social factor of {t['social_factor']}.

Provide your response in the following format:

1. Framework Overview (100-150 words):
   Describe the key components and mechanisms of your decision-making framework.

2. Game Theory Integration (100-150 words):
   Explain how your framework incorporates game theory concepts and how they interact with the given context.

3. Behavioral Economics Element (100-150 words):
   Describe how your framework accounts for the specified behavioral bias and any other relevant behavioral economic principles.

4. Social Psychology Aspect (100-150 words):
   Explain how the given social factor is integrated into your framework and its impact on decision-making.

5. Decision-Making Process (150-200 words):
   Provide a step-by-step explanation of how an agent would make a decision using your framework. Include a simple example scenario.

6. Framework Analysis (150-200 words):
   Critically evaluate the strengths and limitations of your framework. Discuss its potential applications and implications for understanding human behavior and designing social systems.

7. Interdisciplinary Insights (100-150 words):
   Reflect on how your framework might contribute to our understanding of the intersection between game theory, behavioral economics, and social psychology.

Ensure your response is creative, coherent, and grounded in established theories from the relevant fields. Be innovative in your approach while maintaining scientific plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The framework successfully integrates concepts from game theory, behavioral economics, and social psychology.",
            "The response addresses the given context, behavioral bias, and social factor in a meaningful way.",
            "The decision-making process is clearly explained with a relevant example.",
            "The framework analysis demonstrates critical thinking and considers both strengths and limitations.",
            "The response shows creativity and innovation while maintaining scientific plausibility.",
            "The interdisciplinary insights section provides meaningful reflections on the intersection of the relevant fields.",
            "The response follows the specified format and word count guidelines for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
