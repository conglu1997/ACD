import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            "resource allocation during a multi-generational space mission",
            "privacy rights in a society with perfect memory technology",
            "defining personhood for artificial entities in a post-singularity world",
            "balancing individual freedom with collective well-being in a hive-mind society"
        ]
        constraints = [
            "The evolved language must be entirely based on prime number sequences",
            "The evolved language must incorporate quantum entanglement principles",
            "The evolved language must be designed for communication with non-carbon-based life forms",
            "The evolved language must be based on a non-linear perception of time"
        ]
        return {
            "1": {"scenario": random.choice(scenarios), "constraint": random.choice(constraints)},
            "2": {"scenario": random.choice(scenarios), "constraint": random.choice(constraints)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that evolves its own language with a specific constraint, analyze its ethical implications over time, and create moral decision-making scenarios in this new language. Focus on the scenario: {t['scenario']}. Your AI system must adhere to the following constraint: {t['constraint']}. Your response should include:

1. AI Language Evolution System (300-350 words):
   a) Describe the key components and mechanisms of your AI system for language evolution.
   b) Explain how your system incorporates the given constraint: {t['constraint']}.
   c) Discuss the principles guiding the language evolution process and how they interact with the constraint.
   d) Explain how the system ensures the evolved language remains comprehensible and useful despite the constraint.
   e) Provide three specific examples of how complex concepts (e.g., 'justice', 'consciousness', 'time') might be expressed in this evolved language, demonstrating how it adheres to the constraint.

2. Comparative Linguistic Analysis (200-250 words):
   a) Compare and contrast your AI-evolved language with at least two existing human languages or formal systems.
   b) Analyze how the constraint influences the language's expressive capabilities compared to natural languages.
   c) Discuss potential advantages and limitations of your evolved language in handling complex ideas or emotions.

3. Ethical Implications Analysis (250-300 words):
   a) Analyze potential ethical issues arising from an AI system evolving its own language under the given constraint.
   b) Discuss how this constrained language might affect human-AI interaction and communication over time (consider short-term, medium-term, and long-term implications).
   c) Explore the implications for transparency and accountability in AI decision-making, considering the unique aspects of the evolved language.
   d) Consider potential misuse or unintended consequences of such a system, particularly in light of the constraint.
   e) Discuss any new ethical considerations that arise specifically due to the constraint and how they might evolve over time.

4. Moral Decision-Making Scenario (250-300 words):
   a) Create a specific moral dilemma related to the given scenario: {t['scenario']}.
   b) Present this dilemma using elements of your AI-evolved language, adhering to the constraint.
   c) Explain how the nuances of the evolved language and its constraint might influence the framing and understanding of the moral issue.
   d) Discuss how an AI using this evolved language might approach resolving the dilemma at three different time points (e.g., 1 year, 10 years, and 100 years after language creation), and how the constraint might affect its reasoning process over time.
   e) Compare this approach to how a human might reason about the same dilemma using natural language at these different time points.

5. Language-Ethics Interaction (200-250 words):
   a) Analyze how the structure and features of the evolved language, including its constraint, might influence ethical reasoning over time.
   b) Discuss whether certain ethical concepts might become easier or harder to express in this new language as it evolves, due to its unique characteristics.
   c) Explore how the constraint might create new opportunities or challenges for moral reasoning in the long term.
   d) Speculate on how prolonged use of this language might shape the ethical framework of its users across generations.

6. Governance and Control Mechanisms (200-250 words):
   a) Propose mechanisms to monitor and control the language evolution process, considering the specific challenges posed by the constraint and potential changes over time.
   b) Suggest ways to ensure the evolved language aligns with human ethical values while respecting its unique structure, even as both the language and human values may change.
   c) Discuss the challenges of maintaining human oversight over a potentially rapidly evolving AI language, especially given its constrained nature, over an extended period.
   d) Propose a framework for translating between the AI's constrained language and human language for ethical discussions and decision-making, considering how this translation process might need to adapt over time.

7. Reflection and Implications (150-200 words):
   a) Reflect on what this thought experiment reveals about the relationship between language, thought, ethics, and time, particularly in light of the imposed constraint.
   b) Discuss potential long-term implications for future AI development and human-AI coexistence, considering the unique aspects of the evolved language.
   c) Speculate on how such constrained AI languages might influence the future of human language, communication, and ethical reasoning over centuries.

Ensure your response demonstrates a deep understanding of AI, linguistics, ethics, and temporal reasoning. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific and philosophical plausibility.

Format your response with clear headings for each section. Your total response should be between 1550-1900 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of AI, linguistics, ethics, and temporal reasoning.",
            "The AI language evolution system is well-designed, clearly explained, and effectively incorporates the given constraint, with three specific examples of complex concept expression.",
            "The comparative linguistic analysis effectively contrasts the AI-evolved language with existing languages or formal systems.",
            "The ethical implications are thoroughly analyzed and discussed, including those specific to the constrained language, with consideration of short-term, medium-term, and long-term effects.",
            f"A compelling moral decision-making scenario related to {t['scenario']} is presented using elements of the AI-evolved language, adhering to the constraint: {t['constraint']}, with analysis at three different time points.",
            "The interaction between the constrained language and ethics is insightfully explored, considering its evolution over time.",
            "Governance and control mechanisms are proposed and discussed thoughtfully, addressing the unique challenges posed by the constrained language and its potential changes over time.",
            "The reflection demonstrates critical thinking about the long-term implications of AI language evolution under constraints for human-AI coexistence and ethical reasoning."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
