import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        evolutionary_constraints = [
            {
                "constraint": "Extreme temperature fluctuations",
                "description": "The alien planet experiences rapid and extreme temperature changes, ranging from -100°C to +200°C within a single day-night cycle."
            },
            {
                "constraint": "Silicon-based biochemistry",
                "description": "The alien life forms have evolved using silicon as the basis for their biochemistry instead of carbon."
            }
        ]
        return {
            "1": random.choice(evolutionary_constraints),
            "2": random.choice(evolutionary_constraints)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical evolutionary mechanism for alien life forms, considering the following environmental constraint: {t['constraint']}. {t['description']}

Your task is to create an innovative evolutionary mechanism that addresses this constraint. Your response should include:

1. Mechanism Description (250-300 words):
   a) Name and describe your proposed evolutionary mechanism.
   b) Explain how it functions at the genetic, organismal, and population levels.
   c) Describe how this mechanism specifically addresses the given environmental constraint.

2. Comparative Analysis (200-250 words):
   a) Compare your proposed mechanism to known evolutionary processes on Earth.
   b) Discuss similarities and differences, highlighting the novel aspects of your mechanism.
   c) Explain why this mechanism might not have evolved on Earth.

3. Ecological Implications (200-250 words):
   a) Describe how your evolutionary mechanism might influence ecosystem dynamics on the alien planet.
   b) Discuss potential patterns of speciation or adaptation that could result from this mechanism.
   c) Propose a hypothetical example of how two species might co-evolve under this mechanism.

4. Theoretical Challenges (150-200 words):
   a) Identify potential theoretical challenges or limitations of your proposed mechanism.
   b) Discuss how these challenges might be addressed or investigated.
   c) Propose an experiment or observation that could test the validity of your mechanism.

5. Astrobiological Significance (150-200 words):
   a) Explain how your mechanism could influence the search for extraterrestrial life.
   b) Discuss what biosignatures might result from this evolutionary process.
   c) Describe how this mechanism might change our understanding of the potential for life in the universe.

Ensure your response demonstrates a deep understanding of evolutionary biology, creative application of scientific principles, and logical reasoning. Use appropriate scientific terminology and provide clear explanations of complex ideas. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 950-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The proposed evolutionary mechanism is innovative and plausibly addresses the given environmental constraint.",
            "The explanation demonstrates a deep understanding of evolutionary biology and applies scientific principles creatively.",
            "The comparative analysis shows clear reasoning about the differences between the proposed mechanism and Earth's evolutionary processes.",
            "The ecological implications are well-thought-out and logically derived from the proposed mechanism.",
            "The response identifies relevant theoretical challenges and proposes reasonable ways to address them.",
            "The discussion of astrobiological significance demonstrates an understanding of the broader implications for the search for extraterrestrial life.",
            "The overall response is well-structured, scientifically plausible, and demonstrates interdisciplinary thinking."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
