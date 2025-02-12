class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "type": "generation",
                "domains": ["Science", "History", "Art"],
                "prompt": "Create a short story that integrates concepts from science (e.g., the theory of evolution), historical events (e.g., the Industrial Revolution), and art (e.g., Impressionism). The story should be coherent and demonstrate a deep understanding of each domain."
            },
            "2": {
                "type": "analysis",
                "content": "In the Renaissance period, scientific discoveries were often depicted in art. For example, Leonardo da Vinci's Vitruvian Man illustrates the blend of art and science, reflecting the Renaissance belief in the harmony between human proportions and the universe. In this context, analyze the impact of such interdisciplinary works on the cultural and intellectual landscape of the time. Discuss the influence of these works on subsequent scientific and artistic developments."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['type'] == 'generation':
            return f"""Generate a short story that synthesizes information from the following domains:

Domains: {', '.join(t['domains'])}

Prompt: {t['prompt']}

Ensure that the story is coherent, engaging, and demonstrates a deep understanding of each domain. Submit your response as a plain text string in the following format:

Story:
[Your story here]"""
        else:
            return f"""Analyze the following content and provide a detailed discussion on the impact of interdisciplinary works on the cultural and intellectual landscape of the time. Discuss the influence of these works on subsequent scientific and artistic developments:

Content:
{t['content']}

Submit your response as a plain text string in the following format:

Analysis:
[Your analysis here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['type'] == 'generation':
            validation_criteria = [
                "The story should integrate concepts from science, history, and art.",
                "The story should be coherent and engaging.",
                "The story should demonstrate a deep understanding of each domain.",
                "The story should reflect creativity and originality."
            ]
        else:
            validation_criteria = [
                "The analysis should accurately reflect the interdisciplinary nature of the content.",
                "The analysis should be detailed and coherent.",
                "The analysis should demonstrate an understanding of the cultural and intellectual impact.",
                "The analysis should discuss the influence on subsequent scientific and artistic developments."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
