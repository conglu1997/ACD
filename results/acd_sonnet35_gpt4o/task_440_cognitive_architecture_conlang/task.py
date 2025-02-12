import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_architectures = [
            {
                "name": "ACT-R",
                "description": "Adaptive Control of Thought-Rational, emphasizing declarative and procedural memory"
            },
            {
                "name": "SOAR",
                "description": "State, Operator, and Result, focusing on problem-solving and learning"
            },
            {
                "name": "CLARION",
                "description": "Connectionist Learning with Adaptive Rule Induction ON-line, integrating implicit and explicit processes"
            },
            {
                "name": "LIDA",
                "description": "Learning Intelligent Distribution Agent, based on Global Workspace Theory"
            }
        ]
        
        language_aspects = [
            "phonology and morphology",
            "syntax and grammar",
            "semantics and pragmatics",
            "language acquisition process"
        ]
        
        return {
            "1": {
                "architecture": random.choice(cognitive_architectures),
                "aspect": random.choice(language_aspects)
            },
            "2": {
                "architecture": random.choice(cognitive_architectures),
                "aspect": random.choice(language_aspects)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a constructed language (conlang) based on the {t['architecture']['name']} cognitive architecture, which is described as: {t['architecture']['description']}. Then, analyze how an AI agent with this architecture would acquire and use the language, focusing on the aspect of {t['aspect']}. Your response should include:

1. Conlang Design (250-300 words):
   a) Describe the key features of your conlang, explaining how they reflect the principles of the {t['architecture']['name']} architecture.
   b) Provide at least 5 example words or phrases in your conlang, with their meanings and explanations of how they embody the cognitive architecture's principles.
   c) Outline the main grammatical rules of your conlang, relating them to the cognitive architecture.

2. Language Aspect Analysis (200-250 words):
   Analyze in detail how the {t['aspect']} of your conlang would be influenced by the {t['architecture']['name']} architecture. Provide specific examples and explain your reasoning.

3. AI Agent Simulation (250-300 words):
   a) Describe how an AI agent based on the {t['architecture']['name']} architecture would acquire your conlang.
   b) Explain potential challenges or advantages the agent might face in learning and using the language.
   c) Provide a specific example of how the agent would process and generate a complex sentence in your conlang.

4. Comparative Analysis (200-250 words):
   Compare and contrast how your conlang and its acquisition by an AI agent differ from natural languages and human language acquisition. Discuss the implications of these differences for our understanding of cognition and language.

5. Potential Applications (100-150 words):
   Propose potential applications of your cognitive architecture-based conlang in fields such as AI development, cognitive science research, or human-computer interaction.

Ensure your response demonstrates a deep understanding of both linguistics and cognitive architectures. Be creative in your language design while maintaining logical consistency with the principles of the given cognitive architecture."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The conlang design clearly reflects the principles of the {t['architecture']['name']} cognitive architecture.",
            f"The analysis of the {t['aspect']} aspect is thorough and logically connected to the cognitive architecture.",
            "The AI agent simulation demonstrates a deep understanding of both the conlang and the cognitive architecture.",
            "The comparative analysis provides insightful observations about the differences between the conlang/AI acquisition and natural languages/human acquisition.",
            "The proposed applications are innovative and well-reasoned.",
            "The overall response shows a high level of interdisciplinary knowledge integration and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
