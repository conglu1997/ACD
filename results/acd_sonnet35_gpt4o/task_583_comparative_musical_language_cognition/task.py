import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_elements = [
            {
                "element1": "pitch",
                "element2": "rhythm",
                "cognitive_aspect": "spatial-temporal reasoning"
            },
            {
                "element1": "harmony",
                "element2": "timbre",
                "cognitive_aspect": "emotional-auditory processing"
            }
        ]
        return {str(i+1): element for i, element in enumerate(musical_elements)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design two contrasting musical language systems: one primarily using {t['element1']} and another using {t['element2']} as their core linguistic features. Then, analyze and compare their potential effects on {t['cognitive_aspect']}. Your response should include the following sections:

1. Musical Language Designs (300-350 words):
   a) Describe the key features of both musical languages, focusing on how they utilize {t['element1']} and {t['element2']} respectively to convey meaning.
   b) Explain the basic grammar and syntax of each language, providing examples of how ideas are expressed in both.
   c) Discuss how each language incorporates other musical elements to enhance or modify meaning.

2. Comparative Cognitive Impact Analysis (250-300 words):
   a) Analyze how regular use of each musical language might differently affect speakers'/listeners' {t['cognitive_aspect']}.
   b) Compare and contrast the potential benefits and drawbacks of each language system on cognitive processes.
   c) Discuss how these effects might differ from those of natural spoken languages.

3. Learning and Acquisition Comparison (200-250 words):
   a) Describe and compare the processes of learning or acquiring fluency in each musical language.
   b) Discuss the unique challenges in learning each language compared to natural languages and to each other.
   c) Propose methods to facilitate the learning process for each language, considering different learning styles and abilities.

4. Comparative Practical Applications (250-300 words):
   a) Suggest at least two practical applications for each musical language in fields such as education, therapy, or communication.
   b) Compare how these applications leverage the unique features of each language and its cognitive effects.
   c) Discuss any limitations or potential negative consequences of using each language in these contexts.

5. Experimental Design (200-250 words):
   a) Propose an experiment to compare the effects of both musical languages on {t['cognitive_aspect']}.
   b) Describe the methodology, including participant selection, experimental procedure, and data analysis methods.
   c) Discuss potential confounding factors and how you would control for them.

Ensure your response demonstrates a deep understanding of linguistics, music theory, and cognitive science. Be creative in your language designs and analysis while maintaining scientific plausibility and logical consistency. Highlight the contrasts between the two language systems throughout your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The Musical Language Designs section must clearly explain how {t['element1']} and {t['element2']} are used as primary linguistic features in two distinct language systems.",
            f"The Comparative Cognitive Impact Analysis must provide a plausible discussion of how each language might differently affect {t['cognitive_aspect']}.",
            "The Learning and Acquisition Comparison section should address unique challenges of learning each musical language and compare them.",
            "The Comparative Practical Applications section must suggest at least two realistic and innovative uses for each musical language and compare them.",
            f"The Experimental Design must propose a valid method to compare the effects of both musical languages on {t['cognitive_aspect']}.",
            "The overall response must demonstrate interdisciplinary knowledge, creativity, critical thinking, and comparative analysis in the domains of linguistics, music theory, and cognitive science."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
