import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        artifacts = [
            {
                "name": "Antikythera Mechanism",
                "origin": "Ancient Greece",
                "purpose": "Astronomical calculator"
            },
            {
                "name": "Baghdad Battery",
                "origin": "Parthian or Sassanid era",
                "purpose": "Possible electrical device"
            }
        ]
        return {
            "1": random.choice(artifacts),
            "2": random.choice(artifacts)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the {t['name']} from {t['origin']}, originally used as a {t['purpose']}, using AI techniques, and then extrapolate its potential future evolution and applications. Your response should include:

1. Archaeological Analysis (200-250 words):
   a) Describe the artifact's known features and functions.
   b) Explain its historical and cultural significance.
   c) Discuss any mysteries or debates surrounding the artifact.

2. AI-Enhanced Investigation (250-300 words):
   a) Propose three AI techniques that could be used to further analyze the artifact.
   b) Explain how each technique would work and what new information it might reveal.
   c) Describe how these AI techniques relate to the specific features or mysteries of the artifact.
   d) Describe a hypothetical AI-driven discovery about the artifact and its implications.

3. Futuristic Extrapolation (250-300 words):
   a) Based on the artifact's original purpose and your AI analysis, propose an advanced future version of this technology.
   b) Describe its potential applications in various fields (e.g., science, medicine, space exploration).
   c) Explain how it might impact society and human development.
   d) Provide a simple diagram or schematic representation of your proposed future technology.

4. Ethical and Philosophical Considerations (150-200 words):
   a) Discuss potential ethical issues arising from the development and use of your proposed future technology.
   b) Explore how this technology might change our understanding of the relationship between past, present, and future.

5. Interdisciplinary Connections (150-200 words):
   Explain how your analysis and extrapolation connect archaeology, AI, and futurism, and discuss the potential benefits of this interdisciplinary approach.

Ensure your response demonstrates a deep understanding of the historical context, current AI capabilities, and potential future technological developments. Be creative in your extrapolations while maintaining scientific plausibility. Use appropriate terminology from archaeology, AI, and futurism.

Format your response with clear headings for each section (e.g., '1. Archaeological Analysis', '2. AI-Enhanced Investigation', etc.). Your total response should be between 1000-1250 words, not including the diagram."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a clear understanding of the {t['name']} and its historical context.",
            "The AI techniques proposed for analysis should be relevant, well-explained, and related to the artifact's specific features.",
            "The futuristic extrapolation should be creative yet scientifically plausible, and include a diagram or schematic representation.",
            "The ethical and philosophical considerations should be thoughtful and well-reasoned.",
            "The interdisciplinary connections should be clearly articulated and insightful.",
            "The overall response should be well-structured, coherent, and demonstrate strong analytical and creative thinking.",
            "The response should adhere to the specified word count (1000-1250 words) and include all required sections."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
