class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'task_type': 'interpretation', 'medical_text': 'The patient presents with symptoms of dyspnea, tachycardia, and lower extremity edema. The differential diagnosis includes congestive heart failure, chronic obstructive pulmonary disease, pulmonary embolism, and renal failure. Further diagnostic testing, including echocardiogram, spirometry, and D-dimer levels, is required to confirm the diagnosis and guide treatment.'},
            '2': {'task_type': 'generation', 'context': 'A patient has been diagnosed with Type 2 diabetes. Provide a detailed explanation of the condition, including its pathophysiology, risk factors, common symptoms, and management strategies. Ensure your explanation is suitable for a layperson.'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'interpretation':
            return f"""Your task is to interpret the following medical text and provide a clear and concise summary in layman's terms. Ensure that your summary is accurate and easily understandable by a non-medical audience.

Medical Text: {t['medical_text']}

Your response should be in plain text format and no longer than 150 words."""
        elif t['task_type'] == 'generation':
            return f"""Your task is to generate a detailed explanation of the medical condition described below. Ensure that your explanation is accurate, comprehensive, and easily understandable by a non-medical audience.

Context: {t['context']}

Your response should be in plain text format and no longer than 300 words."""
        else:
            return "Unknown task type."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'interpretation':
            criteria = [
                'The summary should accurately reflect the medical text.',
                'The summary should be easily understandable by a non-medical audience.',
                'The summary should be no longer than 150 words.'
            ]
        elif t['task_type'] == 'generation':
            criteria = [
                'The explanation should be accurate and comprehensive.',
                'The explanation should be easily understandable by a non-medical audience.',
                'The explanation should be no longer than 300 words.'
            ]
        else:
            return 0.0
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
