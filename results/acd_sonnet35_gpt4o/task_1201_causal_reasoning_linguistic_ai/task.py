import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        causal_structures = [
            {
                "language": "English",
                "causal_structure": "Because X, Y",
                "example": "Because it rained, the ground is wet."
            },
            {
                "language": "Japanese",
                "causal_structure": "Y, because X",
                "example": "地面が濡れている、雨が降ったから。 (The ground is wet, because it rained.)"
            },
            {
                "language": "Pirahã",
                "causal_structure": "Juxtaposition without explicit causative",
                "example": "It rained. The ground is wet."
            },
            {
                "language": "Mandarin Chinese",
                "causal_structure": "因为 (yīnwèi) X, 所以 (suǒyǐ) Y",
                "example": "因为下雨了，所以地面湿了。 (Because it rained, therefore the ground is wet.)"
            },
            {
                "language": "German",
                "causal_structure": "Weil X, Y",
                "example": "Weil es geregnet hat, ist der Boden nass. (Because it rained, the ground is wet.)"
            },
            {
                "language": "Turkish",
                "causal_structure": "X -diği için Y",
                "example": "Yağmur yağdığı için yer ıslak. (Because it rained, the ground is wet.)"
            }
        ]
        return {
            "1": random.choice(causal_structures),
            "2": random.choice(causal_structures)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze how the expression of causality in {t['language']} might influence causal reasoning in AI language models, focusing on the structure '{t['causal_structure']}'. Then, design experiments to test this hypothesis. Your response should include:

1. Linguistic Analysis (200-250 words):
   a) Explain the causal structure in {t['language']} and how it differs from other languages.
   b) Discuss how this structure might influence causal reasoning according to linguistic relativity.
   c) Provide an example of how this structure is used: {t['example']}

2. AI Language Model Implications (250-300 words):
   a) Analyze how this causal structure might affect an AI language model trained primarily on {t['language']}.
   b) Discuss potential biases or limitations in the AI's understanding or generation of causal relationships.
   c) Propose a hypothesis about how this causal structure might influence the AI's performance on causal reasoning tasks.

3. Experimental Design (300-350 words):
   a) Propose two experiments to test your hypothesis about the influence of {t['language']}'s causal structure on AI language models:
      - One experiment comparing AI models trained on different languages
      - One experiment examining the AI's performance across languages or tasks
   b) For each experiment, describe:
      - The methodology
      - The data or resources needed
      - The expected outcomes
      - How you would measure and analyze the results

4. Ethical Considerations (150-200 words):
   a) Discuss potential ethical implications of your findings for AI development and deployment.
   b) Consider how differences in causal reasoning might impact AI decision-making in critical applications.
   c) Propose guidelines to address these ethical concerns in AI research and applications.

5. Broader Implications (150-200 words):
   a) Discuss how understanding causal reasoning differences in AI could impact fields such as machine translation, cross-cultural communication, or AI ethics.
   b) Propose one novel application or research direction that could emerge from this line of inquiry.

Ensure your response demonstrates a deep understanding of linguistics, causal reasoning, AI language models, and experimental design. Use technical terminology appropriately and provide explanations where necessary. Be creative in your analysis and experimental designs while maintaining scientific plausibility.

Note: Manage your time wisely to address all sections comprehensively. Your total response should be between 1050-1300 words, with some flexibility in individual section lengths to allow for thorough exploration of complex ideas."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of the causal structure in {t['language']} and its potential cognitive implications.",
            "The analysis of AI language model implications is thorough and considers potential biases and limitations in causal reasoning.",
            "The experimental designs are well-thought-out, feasible, and directly address the proposed hypothesis about causal reasoning in AI models.",
            "The ethical considerations are relevant and thoughtfully discussed, particularly regarding AI decision-making.",
            "The broader implications and proposed novel application demonstrate creativity and insight in applying linguistic causal structures to AI development.",
            "The overall response shows a strong grasp of linguistics, cognitive science, and AI principles, applied in the context of causal reasoning."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
