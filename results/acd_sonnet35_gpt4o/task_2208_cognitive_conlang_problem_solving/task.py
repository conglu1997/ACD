import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_principles = [
            "Embodied cognition",
            "Predictive processing",
            "Cognitive load theory",
            "Dual-process theory",
            "Conceptual metaphor theory"
        ]
        problem_domains = [
            "Climate change mitigation",
            "Interstellar communication",
            "Quantum computing algorithms",
            "Ethical decision-making in AI",
            "Modeling complex ecosystems"
        ]
        return {
            "1": {
                "principle": random.choice(cognitive_principles),
                "domain": random.choice(problem_domains)
            },
            "2": {
                "principle": random.choice(cognitive_principles),
                "domain": random.choice(problem_domains)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an artificial language (conlang) based on the cognitive principle of {t['principle']}, then use it to solve a complex problem in the domain of {t['domain']}. Your response should include:

1. Language Design (300-350 words):
   a) Describe the key features of your conlang, including its phonology, morphology, and syntax.
   b) Explain how your language incorporates the specified cognitive principle.
   c) Provide at least 3 example sentences in your conlang with translations and explanations.
   d) Discuss how your language differs from natural languages and other constructed languages.

2. Cognitive Foundations (200-250 words):
   a) Explain the cognitive science principles underlying your language design.
   b) Discuss how your language might influence or change thought processes.
   c) Address potential cognitive benefits and challenges of using your language.

3. Problem-Solving Application (250-300 words):
   a) Describe a complex problem in the specified domain that your language is particularly suited to address.
   b) Provide a high-level solution to this problem using your conlang.
   c) Explain how the cognitive principle-based features of your language contribute to solving the problem.

4. AI Integration (200-250 words):
   a) Propose how an AI system could be designed or trained to understand and generate your conlang.
   b) Discuss potential challenges in implementing this AI system and how you would address them.
   c) Explore how this AI system might be used in conjunction with your language for problem-solving.

5. Broader Implications (150-200 words):
   a) Discuss how your cognitive conlang might impact human-AI interaction and collaboration.
   b) Explore potential applications in fields such as education, therapy, or intercultural communication.
   c) Address any ethical considerations or potential misuses of your language and its associated AI system.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence principles. Be creative in your approach while maintaining scientific and technological plausibility. Use appropriate terminology and provide explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The conlang design effectively incorporates the cognitive principle of {t['principle']}.",
            f"The problem-solving application in the domain of {t['domain']} is well-explained and plausible.",
            "The response demonstrates a deep understanding of linguistics, cognitive science, and AI principles.",
            "The conlang examples are coherent and clearly explained.",
            "The AI integration proposal is innovative and addresses potential challenges.",
            "The broader implications and ethical considerations are thoughtfully discussed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
