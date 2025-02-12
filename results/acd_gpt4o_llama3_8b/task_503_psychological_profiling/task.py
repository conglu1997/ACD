class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "John is a meticulous and organized person. He likes to plan everything in advance and often makes detailed to-do lists. He feels uneasy when things don't go as planned and prefers a structured environment."},
            "2": {"description": "Emma is an outgoing and social individual. She enjoys meeting new people and often takes the lead in social gatherings. She is spontaneous and loves trying new things, often making decisions on the fly."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following description and infer the personality traits and psychological profile of the described individual. Your analysis should include the main personality traits, potential strengths and weaknesses, and any psychological insights you can infer from the description. Submit your analysis as a plain text string in the following format:

Personality Traits: [Your analysis here]

Description:
{t['description']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The analysis should accurately infer the main personality traits from the description.", "The analysis should include potential strengths and weaknesses of the described individual.", "The analysis should provide insightful psychological observations based on the text.", "The analysis should be clear, well-structured, and demonstrate understanding of psychological concepts."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0