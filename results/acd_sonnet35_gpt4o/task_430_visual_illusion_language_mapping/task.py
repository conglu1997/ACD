import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        illusions = [
            {
                "name": "Café Wall Illusion",
                "type": "geometric",
                "effect": "parallel lines appear to be sloped"
            },
            {
                "name": "Ebbinghaus Illusion",
                "type": "size perception",
                "effect": "surrounding context affects perceived size of central object"
            }
        ]
        return {str(i+1): illusion for i, illusion in enumerate(illusions)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that maps visual illusions to linguistic descriptions, and use it to analyze and generate new illusions. Focus on the {t['name']} as an example of a {t['type']} illusion where {t['effect']}. Your response should include the following sections:

1. Illusion Analysis (200-250 words):
   a) Describe the key visual elements and perceptual mechanisms involved in the {t['name']}.
   b) Explain how these elements create the illusion effect, referencing relevant principles of visual perception.
   c) Discuss any cultural or individual differences that might affect the perception of this illusion.

2. Linguistic Mapping System (250-300 words):
   a) Design a system to map visual illusions to linguistic descriptions. Explain its key components and how they interact.
   b) Describe how your system would represent the {t['name']} linguistically, including syntax, semantics, and any special notation.
   c) Explain how your system accounts for the perceptual mechanisms and effects identified in the analysis.
   d) Discuss how your system could be generalized to other types of visual illusions.

3. New Illusion Generation (200-250 words):
   a) Use your linguistic mapping system to generate a new visual illusion concept.
   b) Provide a detailed linguistic description of this new illusion using your system.
   c) Explain the predicted perceptual effects and the underlying mechanisms of your new illusion.
   d) Discuss potential applications or implications of this new illusion in fields such as psychology, art, or user interface design.

4. Cognitive Implications (150-200 words):
   a) Discuss how your linguistic mapping system might inform our understanding of the relationship between language and visual perception.
   b) Speculate on how an AI trained on such linguistic descriptions might 'perceive' or 'imagine' visual illusions without actually seeing them.
   c) Consider potential implications for theories of mental imagery and visual processing in humans.

5. Ethical Considerations (100-150 words):
   a) Identify potential ethical concerns or misuses of a system that can generate visual illusions through linguistic descriptions.
   b) Propose guidelines for the responsible development and use of such systems in various contexts (e.g., research, entertainment, therapy).

Ensure your response demonstrates a deep understanding of visual perception, linguistics, and cognitive science. Be creative in your approach while maintaining scientific plausibility and rigor."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The Illusion Analysis section must accurately describe the perceptual mechanisms of the {t['name']}.",
            "The Linguistic Mapping System must be clearly explained and demonstrate how it could be applied to various illusions.",
            "The New Illusion Generation must present a novel and plausible visual illusion concept with a detailed linguistic description.",
            "The Cognitive Implications section should discuss at least two distinct implications for our understanding of visual perception and language.",
            "The Ethical Considerations section must identify at least two potential ethical concerns and propose specific guidelines.",
            "The overall response must demonstrate interdisciplinary knowledge, creativity, and critical thinking in the domains of visual perception, linguistics, and cognitive science."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
