import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "artist": "Vincent van Gogh",
                "style": "Post-Impressionism",
                "target_style": "Cubism"
            },
            {
                "artist": "Leonardo da Vinci",
                "style": "High Renaissance",
                "target_style": "Surrealism"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that analyzes the cognitive processes involved in perceiving the artistic style of {t['artist']} ({t['style']}) and uses this analysis to recreate artworks in the style of {t['target_style']}. Your response should include:

1. Cognitive Analysis (250-300 words):
   a) Describe the key cognitive processes involved in perceiving and understanding {t['artist']}'s style.
   b) Explain how these processes differ from those involved in perceiving {t['target_style']}.
   c) Discuss any relevant neuroscientific findings that inform your analysis.

2. AI System Design (300-350 words):
   a) Outline the architecture of your AI system, including its main components and their functions.
   b) Explain how your system models the cognitive processes identified in the analysis.
   c) Describe the algorithms or techniques your system uses to transform artworks from {t['style']} to {t['target_style']}.
   d) Discuss how your system ensures that the output maintains the essence of the original artwork while adopting the new style.

3. Training and Data (200-250 words):
   a) Describe the type and amount of data your system would need for training.
   b) Explain your approach to data collection and preprocessing.
   c) Discuss any potential biases in your training data and how you would address them.

4. Evaluation Metrics (150-200 words):
   a) Propose at least three quantitative metrics to evaluate your system's performance.
   b) Describe a qualitative evaluation method involving human experts or viewers.
   c) Explain how these metrics relate to both cognitive fidelity and artistic quality.

5. Ethical Considerations (150-200 words):
   a) Discuss potential ethical issues related to authorship and originality in AI-generated art.
   b) Address concerns about the impact of such systems on human artists and the art world.
   c) Propose guidelines for the responsible use of your system.

6. Future Applications (150-200 words):
   a) Suggest two novel applications of your system beyond art recreation.
   b) Discuss how your approach could contribute to our understanding of human creativity and cognition.
   c) Propose an experiment that could validate your system's cognitive model.

Ensure your response demonstrates a deep understanding of cognitive science, art history, and artificial intelligence. Be innovative in your approach while maintaining scientific and artistic plausibility. Use appropriate terminology from all relevant fields.

Format your response with clear headings for each section and subsections labeled a, b, c as appropriate. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the cognitive processes involved in perceiving {t['artist']}'s style and {t['target_style']}.",
            "The AI system design is innovative, well-explained, and grounded in cognitive science principles.",
            "The training and data section addresses potential biases and challenges in data collection.",
            "The evaluation metrics are comprehensive and relate to both cognitive fidelity and artistic quality.",
            "Ethical considerations are thoughtfully addressed with proposed guidelines.",
            "Future applications and experiments are creative and scientifically plausible.",
            "The response shows a strong interdisciplinary approach, integrating knowledge from cognitive science, art history, and artificial intelligence."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
