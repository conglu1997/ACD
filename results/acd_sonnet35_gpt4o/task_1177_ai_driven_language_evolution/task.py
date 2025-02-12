import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        communication_goals = [
            "Maximizing information density in limited-bandwidth environments",
            "Facilitating cross-cultural understanding and reducing misinterpretations",
            "Optimizing for rapid learning and adoption by both humans and AI systems",
            "Enhancing emotional expression and empathy in digital communication"
        ]
        existing_systems = [
            "Emoji-based communication",
            "Esperanto",
            "Programming languages",
            "Sign languages"
        ]
        return {
            "1": {"goal": random.choice(communication_goals), "existing_system": random.choice(existing_systems)},
            "2": {"goal": random.choice(communication_goals), "existing_system": random.choice(existing_systems)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can evolve a new language optimized for the following communication goal: {t['goal']}

Your response should include the following sections:

1. AI System Architecture (250-300 words):
   a) Describe the key components of your AI system for language evolution.
   b) Explain the algorithms or techniques used for generating and evaluating language features.
   c) Discuss how your system incorporates feedback and iterative improvement.

2. Language Design Principles (200-250 words):
   a) Outline the core principles guiding the language evolution process.
   b) Explain how these principles address the given communication goal.
   c) Describe any novel linguistic features your system might develop.
   d) Provide a concrete example of a specific language feature your AI system might generate, including its structure and function.

3. Evolution Process (200-250 words):
   a) Detail the steps involved in evolving the new language.
   b) Explain how the system balances innovation with usability.
   c) Discuss how the system might handle trade-offs between different language features.

4. Human-AI Interaction (150-200 words):
   a) Describe how humans would interact with and influence the language evolution process.
   b) Discuss potential challenges in human adoption of the evolved language.
   c) Propose methods for teaching the new language to humans and AI systems.

5. Implications and Ethics (200-250 words):
   a) Analyze potential impacts on linguistic diversity and human languages.
   b) Discuss ethical considerations related to AI-driven language evolution.
   c) Consider long-term consequences of widespread adoption of AI-evolved languages.

6. Evaluation and Refinement (150-200 words):
   a) Propose methods for evaluating the effectiveness of the evolved language.
   b) Describe how the system could be refined based on real-world performance.
   c) Suggest potential applications or domains for your AI-evolved language.

7. Comparison with Existing Systems (150-200 words):
   a) Compare your AI-evolved language to the following existing system: {t['existing_system']}
   b) Discuss similarities and differences in approach and effectiveness.
   c) Explain how your system improves upon or complements the existing system.

Ensure your response demonstrates a deep understanding of linguistics, AI systems, and the ethical implications of language evolution. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide explanations where necessary.

Format your response with clear headings for each section, numbered as above. Use subheadings (a, b, c) for each point within a section. Your total response should be between 1300-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics and AI systems.",
            "The proposed AI system is innovative and plausible for evolving a new language.",
            "The design principles and evolution process effectively address the given communication goal.",
            "A concrete example of a specific language feature is provided and well-explained.",
            "The response thoroughly considers human-AI interaction and ethical implications.",
            "The evaluation and refinement methods are well-thought-out and practical.",
            "The comparison with the existing system is insightful and demonstrates understanding of both approaches.",
            "The response follows the required format with clear headings and subheadings."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
