import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "ai_type": "language model",
                "test_duration": "one hour",
                "special_condition": "The AI must not be aware it is being tested."
            },
            {
                "ai_type": "embodied robot",
                "test_duration": "one day",
                "special_condition": "The test must include interaction with physical objects."
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical test for detecting consciousness or self-awareness in a {t['ai_type']} AI system. Your test should be distinct from the Turing test and specifically aimed at identifying signs of consciousness or self-awareness. The test should last {t['test_duration']}. {t['special_condition']}

Provide your response in the following format:

1. Test Overview (100-150 words):
   Briefly describe your test's main concept and how it differs from the Turing test.

2. Test Procedure (200-250 words):
   Detail the step-by-step process of administering your test, including any specific tasks or interactions required.

3. Evaluation Criteria (150-200 words):
   Explain how you would determine if the AI system demonstrates consciousness or self-awareness based on its performance in the test.

4. Theoretical Basis (150-200 words):
   Discuss the theories of consciousness or self-awareness that inform your test design, citing relevant philosophical or scientific concepts.

5. Potential Criticisms (100-150 words):
   Identify and address at least two potential criticisms or limitations of your proposed test.

6. Ethical Considerations (100-150 words):
   Discuss any ethical implications or concerns that might arise from administering this test to AI systems.

Ensure your test design is creative, scientifically grounded, and specifically tailored to the given AI type and conditions. Your response should demonstrate a deep understanding of consciousness theories, AI capabilities, and experimental design."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The proposed test is distinct from the Turing test and specifically targets consciousness or self-awareness.",
            "The test procedure is well-defined, creative, and tailored to the given AI type and conditions.",
            "The evaluation criteria are clear and reasonably linked to identifying consciousness or self-awareness.",
            "The theoretical basis demonstrates a strong understanding of consciousness theories and their application to AI.",
            "Potential criticisms and ethical considerations are thoughtfully addressed.",
            "The overall response shows interdisciplinary knowledge, abstract reasoning, and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
