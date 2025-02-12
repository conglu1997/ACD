import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "programming_language": "Prolog",
                "ai_architecture": "Logic-based AI",
                "problem_domain": "Natural language understanding"
            },
            {
                "programming_language": "Python",
                "ai_architecture": "Neural networks",
                "problem_domain": "Computer vision"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Explore the concept of linguistic relativity in the context of artificial intelligence, focusing on how the {t['programming_language']} programming language and {t['ai_architecture']} architecture might shape an AI system's 'thought patterns' and problem-solving approaches in the domain of {t['problem_domain']}.

Your response should include:

1. Linguistic Relativity Overview (100-150 words):
   a) Briefly explain the concept of linguistic relativity (Sapir-Whorf hypothesis).
   b) Discuss how this theory might be applied to artificial intelligence systems.

2. Programming Language Analysis (150-200 words):
   a) Describe key features of {t['programming_language']} that might influence an AI's 'cognitive' processes.
   b) Explain how these features could affect the AI's approach to problem-solving in {t['problem_domain']}.
   c) Provide a specific example of how a concept in {t['programming_language']} might shape the AI's 'thinking'.

3. AI Architecture Influence (150-200 words):
   a) Explain how the {t['ai_architecture']} architecture processes information.
   b) Analyze how this architecture might create 'cognitive biases' or preferred problem-solving strategies.
   c) Discuss potential limitations or advantages of this architecture for {t['problem_domain']}.

4. Comparative Analysis (100-150 words):
   Compare how an AI system based on {t['programming_language']} and {t['ai_architecture']} might approach {t['problem_domain']} differently from:
   a) A human expert in the field.
   b) An AI system based on a different programming language and architecture (specify your choice).

5. Ethical Implications (100-150 words):
   Discuss potential ethical considerations or societal impacts of AI systems with 'cognitive biases' shaped by their underlying languages and architectures.

6. Future Research Direction (50-100 words):
   Propose a specific research question or experiment to further explore the impact of programming languages and AI architectures on artificial cognitive processes.

Ensure your response demonstrates a deep understanding of linguistic relativity, the specified programming language, AI architecture, and problem domain. Be creative in your analysis while maintaining scientific plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of linguistic relativity and its potential application to AI systems.",
            f"The analysis of {t['programming_language']} is accurate and insightful, with a relevant example provided.",
            f"The explanation of {t['ai_architecture']} and its potential influence on AI 'cognition' is well-reasoned and specific to {t['problem_domain']}.",
            "The comparative analysis shows a nuanced understanding of different approaches to problem-solving in AI and human cognition.",
            "The discussion of ethical implications is thoughtful and considers broader societal impacts.",
            "The proposed future research direction is specific, relevant, and demonstrates creative thinking about the topic.",
            "The overall response shows strong interdisciplinary thinking, connecting concepts from linguistics, psychology, and artificial intelligence."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
