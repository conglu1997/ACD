import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_structures = [
            {
                "structure": "Subject-Object-Verb word order",
                "example_language": "Japanese",
                "cognitive_aspect": "Working memory load"
            },
            {
                "structure": "Tonal language system",
                "example_language": "Mandarin Chinese",
                "cognitive_aspect": "Auditory processing"
            }
        ]
        return {
            "1": random.choice(linguistic_structures),
            "2": random.choice(linguistic_structures)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an experiment to test how the linguistic structure of {t['structure']} (as found in {t['example_language']}) impacts the learning and processing capabilities of artificial neural networks, with a focus on the cognitive aspect of {t['cognitive_aspect']}. Your response should include:

1. Linguistic Analysis (200-250 words):
   a) Explain the key features of the given linguistic structure.
   b) Discuss how this structure might theoretically impact neural network processing, relating it to the specified cognitive aspect.
   c) Compare this structure to its counterpart in English or another widely-used language in AI training.

2. Hypothesis Formulation (150-200 words):
   a) Based on your analysis, propose a specific hypothesis about how this linguistic structure might affect a neural network's performance on a relevant language processing task.
   b) Explain the reasoning behind your hypothesis, linking it to principles of linguistics, cognitive science, and artificial neural networks.

3. Experimental Design (250-300 words):
   a) Design an experiment to test your hypothesis. Include:
      - Dataset creation or selection
      - Neural network architecture
      - Training procedure
      - Evaluation metrics
   b) Explain how your experiment isolates the impact of the specific linguistic structure.
   c) Describe any control conditions or comparative experiments you would include.

4. Implementation Considerations (150-200 words):
   a) Discuss potential challenges in implementing your experiment.
   b) Propose solutions or workarounds for these challenges.
   c) Suggest any novel techniques or tools you might need to develop for this experiment.

5. Analysis Plan (150-200 words):
   a) Describe how you would analyze the results of your experiment.
   b) Explain what patterns or outcomes would support or refute your hypothesis.
   c) Discuss how you would account for potential confounding variables in your analysis.

6. Broader Implications (200-250 words):
   a) Discuss the potential implications of your study for our understanding of linguistic structures in AI and human cognition.
   b) Propose how your findings could influence future AI model designs or training procedures.
   c) Speculate on potential applications of this research in fields such as natural language processing, machine translation, or cognitive modeling.

7. Ethical Considerations (100-150 words):
   a) Identify potential ethical issues in conducting this research or applying its findings.
   b) Propose measures to address these ethical concerns.
   c) Discuss the broader societal implications of this line of research.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial neural networks. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific rigor and plausibility.

Format your response using clear headings for each section. Your total response should be between 1200-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified linguistic structure and its potential impact on neural network processing.",
            "The hypothesis is well-formulated and logically connected to the linguistic analysis.",
            "The experimental design is comprehensive, well-thought-out, and specifically tailored to test the impact of the given linguistic structure.",
            "The analysis plan and discussion of broader implications show a nuanced understanding of both linguistics and artificial neural networks.",
            "The response addresses potential challenges, ethical considerations, and societal implications of the research.",
            "The overall response is creative, scientifically rigorous, and demonstrates strong interdisciplinary knowledge application."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
