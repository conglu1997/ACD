class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "ecosystem": "Coral reef",
                "challenges": "Coral bleaching due to climate change, overfishing, and pollution"
            },
            "2": {
                "ecosystem": "Temperate forest",
                "challenges": "Deforestation, invasive species, and habitat fragmentation"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a detailed ecological restoration plan for the following ecosystem:

Ecosystem: {t['ecosystem']}
Challenges: {t['challenges']}

Your plan should address the following components:
1. Ecosystem Description: A detailed description of the ecosystem, including key species and ecological functions.
2. Challenges Analysis: An analysis of the challenges facing the ecosystem and their causes.
3. Restoration Techniques: A comprehensive list of techniques and strategies to restore the ecosystem, including any specific interventions.
4. Implementation Plan: A step-by-step plan for implementing the restoration techniques, including timelines and resource requirements.
5. Monitoring and Evaluation: A plan for monitoring the progress of the restoration and evaluating its success.

Submit your response as a plain text string in the following format:
Ecosystem Description: [Your ecosystem description]
Challenges Analysis: [Your challenges analysis]
Restoration Techniques: [Your restoration techniques]
Implementation Plan: [Your implementation plan]
Monitoring and Evaluation: [Your monitoring and evaluation plan]

Ensure that each component is comprehensive, logically structured, and demonstrates a deep understanding of ecological principles. Your plan should be feasible and address the specific challenges mentioned."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The ecosystem description should be detailed and include key species and ecological functions.",
            "The challenges analysis should provide insights into the causes and impacts of the challenges.",
            "The restoration techniques should be comprehensive and relevant to the ecosystem.",
            "The implementation plan should be thorough, with clear timelines and resource requirements.",
            "The monitoring and evaluation plan should outline methods for assessing progress and success.",
            "The entire plan should demonstrate a deep understanding of ecological principles and be feasible."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
