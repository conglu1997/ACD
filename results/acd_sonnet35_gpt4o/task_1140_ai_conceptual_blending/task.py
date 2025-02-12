import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "concept1": "Time",
                "concept2": "River",
                "domain": "Philosophy"
            },
            "2": {
                "concept1": "Quantum Computing",
                "concept2": "Neural Networks",
                "domain": "Technology"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are an AI system capable of advanced conceptual blending and linguistic analysis. Your task is to generate and analyze a novel conceptual blend based on the given concepts and domain, then evaluate its cognitive and linguistic implications. Follow these steps:

1. Conceptual Blend Generation (200-250 words):
   a) Create a novel conceptual blend combining {t['concept1']} and {t['concept2']} within the domain of {t['domain']}.
   b) Describe the key features and structure of your conceptual blend.
   c) Explain how elements from both input concepts contribute to the blend.
   d) Discuss any emergent properties or novel insights arising from the blend.

2. Linguistic Analysis (200-250 words):
   a) Analyze the linguistic implications of your conceptual blend.
   b) Propose 3-5 new terms or phrases that emerge from this blend, explaining their meanings and formation.
   c) Discuss how existing vocabulary might be repurposed or modified to express ideas within this blended concept.
   d) Consider potential challenges in articulating ideas related to this blend using current language.

3. Cognitive Implications (200-250 words):
   a) Evaluate how this conceptual blend might influence human thought processes or problem-solving approaches in the given domain.
   b) Discuss potential applications of this blend in advancing understanding or creativity in the field.
   c) Analyze any cognitive biases or limitations that might arise from thinking in terms of this blended concept.

4. AI and Human Creativity Comparison (150-200 words):
   a) Compare the process you used to generate this blend with hypothetical human cognitive processes.
   b) Discuss any advantages or limitations of AI-generated conceptual blends compared to human-generated ones.
   c) Propose an experiment to test whether humans can distinguish between AI and human-generated conceptual blends in this domain.

5. Ethical and Societal Considerations (150-200 words):
   a) Discuss potential ethical implications or societal impacts of introducing this conceptual blend.
   b) Consider how this blend might influence public understanding or discourse in the given domain.
   c) Propose guidelines for responsible development and application of AI-generated conceptual blends.

Ensure your response demonstrates deep understanding of conceptual blending theory, linguistics, cognitive science, and the specific domain. Be creative while maintaining scientific and philosophical rigor. Your total response should be between 900-1150 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a novel and coherent conceptual blend of the given concepts.",
            "The linguistic analysis provides new terms and discusses language implications.",
            "Cognitive implications of the blend are thoroughly explored.",
            "AI and human creativity are compared in the context of conceptual blending.",
            "Ethical and societal considerations of the blend are discussed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
