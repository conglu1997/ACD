import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "musical_style": "Baroque",
                "linguistic_concept": "Phrase structure grammar",
                "compositional_element": "Counterpoint"
            },
            {
                "musical_style": "Jazz",
                "linguistic_concept": "Generative grammar",
                "compositional_element": "Improvisation"
            },
            {
                "musical_style": "Minimalism",
                "linguistic_concept": "Finite state grammar",
                "compositional_element": "Repetition"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze and generate a musical phrase using principles from computational linguistics and music theory. Your task has three parts:

1. Analysis (200-250 words):
   a) Explain how the linguistic concept of {t['linguistic_concept']} can be applied to music theory, particularly in the context of {t['musical_style']} style.
   b) Discuss how this linguistic approach might provide new insights into the compositional element of {t['compositional_element']}.
   c) Provide an example of how a musical phrase in {t['musical_style']} style could be represented using {t['linguistic_concept']}.

2. Generation (200-250 words):
   a) Describe a method for generating a musical phrase in {t['musical_style']} style using {t['linguistic_concept']}.
   b) Explain how your method incorporates the compositional element of {t['compositional_element']}.
   c) Provide a step-by-step description of how your method would create a short musical phrase.

3. Notation and Analysis (200-250 words):
   a) Present a generated musical phrase using standard music notation (you may use ASCII art or text-based representation).
   b) Analyze the generated phrase, explaining how it reflects {t['musical_style']} style, incorporates {t['compositional_element']}, and demonstrates the application of {t['linguistic_concept']}.
   c) Discuss any limitations or potential improvements to your generation method.

Ensure your response demonstrates a deep understanding of both music theory and computational linguistics. Be creative in your approach while maintaining musical and linguistic accuracy."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include an analysis of how {t['linguistic_concept']} can be applied to music theory in the context of {t['musical_style']} style",
            f"The response should describe a method for generating a musical phrase in {t['musical_style']} style using {t['linguistic_concept']}",
            f"The response should present a generated musical phrase using some form of notation",
            f"The response should analyze the generated phrase, explaining how it reflects {t['musical_style']} style, incorporates {t['compositional_element']}, and demonstrates the application of {t['linguistic_concept']}",
            "The response should demonstrate a deep understanding of both music theory and computational linguistics"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
