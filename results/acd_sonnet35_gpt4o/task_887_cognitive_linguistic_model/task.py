import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "scenario": "Second Language Acquisition in Adults",
                "context": "Analyzing the cognitive processes involved in adults learning a new language"
            },
            {
                "scenario": "Bilingual Language Development in Children",
                "context": "Examining how children acquire and process two languages simultaneously from birth"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel cognitive model of language acquisition and processing, and apply it to analyze the scenario of {t['scenario']}. Your response should include the following sections:

1. Theoretical Foundation (200-250 words):
   a) Briefly discuss key theories in cognitive linguistics and language acquisition relevant to your model.
   b) Explain how your model integrates or challenges existing theories.

2. Model Architecture (250-300 words):
   a) Describe the main components of your cognitive linguistic model.
   b) Explain how these components interact to facilitate language acquisition and processing.
   c) Include a simple ASCII art diagram illustrating your model's architecture.

3. Cognitive Processes (200-250 words):
   a) Detail the specific cognitive processes involved in your model.
   b) Explain how these processes contribute to language learning and use.

4. Neural Basis (150-200 words):
   a) Propose a potential neural basis for your model.
   b) Discuss how specific brain regions might be involved in the processes you've described.

5. Application to {t['scenario']} (250-300 words):
   a) Apply your model to analyze the given scenario: {t['context']}.
   b) Explain how your model accounts for the unique aspects of this scenario.
   c) Predict potential outcomes or challenges based on your model.

6. Testable Hypotheses (100-150 words):
   a) Propose two testable hypotheses derived from your model.
   b) Briefly outline experimental designs to test these hypotheses.

7. Limitations and Future Directions (100-150 words):
   a) Discuss potential limitations of your model.
   b) Suggest areas for future research or expansion of the model.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and neuroscience. Be creative in your model design while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1250-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive science, linguistics, and neuroscience principles.",
            "The proposed model is novel, coherent, and scientifically plausible.",
            "The model is clearly explained and effectively illustrated with an ASCII art diagram.",
            "The application of the model to the given scenario is thorough and insightful.",
            "The proposed hypotheses and experimental designs are logical and relevant to the model.",
            "The response shows creativity and interdisciplinary thinking in addressing the task."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
