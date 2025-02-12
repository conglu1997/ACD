import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"ai_type": "Transformer-based language model", "key_feature": "Attention mechanism"},
            "2": {"ai_type": "Recurrent Neural Network (RNN)", "key_feature": "Sequential processing"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel writing system that reflects how an {t['ai_type']} might internally represent and process language, focusing on its {t['key_feature']}. Your writing system should:

1. Include a set of basic symbols or components (at least 10) that represent fundamental units of language processing for the AI.

2. Explain how these symbols can be combined or modified to represent more complex linguistic structures (e.g., words, phrases, sentences).

3. Describe how the writing system incorporates or reflects the {t['key_feature']} of the {t['ai_type']}.

4. Provide an example of a simple sentence written in your AI writing system, along with an explanation of how it represents the sentence's meaning and structure.

5. Discuss how your writing system might handle ambiguity or uncertainty in language processing.

6. Compare your AI writing system to human writing systems, highlighting at least two similarities and two differences.

7. Explain how this writing system could potentially aid in understanding or visualizing the AI's internal language processing.

Ensure your response is creative, coherent, and grounded in an understanding of both linguistics and AI systems. Your total response should be between 400-600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of the specified AI type and its key feature.",
            "The writing system is novel, coherent, and reflects the AI's internal language processing.",
            "The response addresses all seven points in the instructions comprehensively.",
            "The explanation is creative while remaining grounded in linguistic and AI principles."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
