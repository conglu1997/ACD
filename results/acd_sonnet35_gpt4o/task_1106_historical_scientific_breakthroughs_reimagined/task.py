import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "breakthrough": "Newton's laws of motion",
                "alt_context": "quantum computing era"
            },
            "2": {
                "breakthrough": "Darwin's theory of evolution",
                "alt_context": "interplanetary colonization"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Reimagine the historical scientific breakthrough of {t['breakthrough']} as if it were discovered in the context of {t['alt_context']}. Your task is to:

1. Briefly explain the original breakthrough and its historical context (2-3 sentences).

2. Describe how this breakthrough might have occurred in the alternative technological context, considering the tools, knowledge, and challenges of that era (150-200 words).

3. Outline the key principles or components of your reimagined breakthrough, explaining how they differ from or build upon the original (200-250 words).

4. Analyze the potential scientific and technological implications of this reimagined breakthrough in its new context (150-200 words).

5. Discuss how this alternative discovery might have altered the course of scientific progress and societal development (150-200 words).

6. Propose a specific experiment or technological application that could result from this reimagined breakthrough (100-150 words).

7. Reflect on what this exercise reveals about the nature of scientific discovery and the role of context in shaping our understanding of the natural world (100-150 words).

Ensure your response is well-reasoned, creative, and grounded in scientific principles. Use appropriate scientific terminology and provide explanations where necessary. Organize your answer using clear headings for each section, numbered as above.

Your total response should be between 900-1200 words. Each section should be within the specified word count range.

Your response will be evaluated based on the accuracy of the original breakthrough explanation, the creativity and scientific plausibility of the reimagined breakthrough, the depth of analysis of its implications, and the overall coherence and organization of your answer."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response explains the original {t['breakthrough']} and its historical context",
            f"The breakthrough is creatively reimagined in the context of {t['alt_context']}",
            "Key principles of the reimagined breakthrough are outlined and compared to the original",
            "Potential scientific and technological implications are analyzed",
            "The impact on scientific progress and societal development is discussed",
            "A specific experiment or application is proposed",
            "The response reflects on the nature of scientific discovery and the role of context",
            "The answer demonstrates understanding of relevant scientific principles",
            "The response is well-organized with clear headings for each numbered section",
            "The total response is between 900-1200 words, with each section within its specified range"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
