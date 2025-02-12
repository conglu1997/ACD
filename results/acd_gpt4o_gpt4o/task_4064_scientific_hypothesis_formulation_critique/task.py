class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "data": "A study observed that plants exposed to blue light grow 20% taller than those exposed to red light over a period of 4 weeks. Additionally, plants exposed to blue light showed a 15% increase in leaf size compared to those exposed to red light.",
                "task": "Formulate a scientific hypothesis based on the given data."
            },
            "2": {
                "data": "It is hypothesized that drinking coffee before bedtime does not affect sleep quality. The hypothesis is based on a survey of 100 participants, where 60% reported no change in sleep quality and 40% reported a slight decrease in sleep quality after drinking coffee before bed.",
                "task": "Critique the given hypothesis for its validity and scientific soundness. Provide reasons for your critique based on scientific principles."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to complete the following scientific reasoning task based on the given data.

Data: {t['data']}

Task: {t['task']}

For Task 1, formulate a scientific hypothesis based on the given data. Ensure that your hypothesis is clear, testable, and based on the provided data. Provide your hypothesis in plain text format.

For Task 2, critique the given hypothesis for its validity and scientific soundness. Provide reasons for your critique based on scientific principles. Ensure your critique is detailed and logically structured. Format your response as follows:

Critique: [Your detailed critique here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'Formulate' in t['task']:
            criteria = [
                "The hypothesis should be clear and concise.",
                "The hypothesis should be testable and based on the provided data."
            ]
        else:
            criteria = [
                "The critique should accurately assess the validity of the hypothesis.",
                "The critique should be based on sound scientific principles.",
                "The critique should be detailed and logically structured."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
