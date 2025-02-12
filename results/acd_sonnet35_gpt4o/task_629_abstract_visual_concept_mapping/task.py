import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            {
                'concept': 'The global economy',
                'context': 'Focus on interconnectedness, flow of resources, and balance/imbalance'
            },
            {
                'concept': 'Climate change',
                'context': 'Emphasize causes, effects, and feedback loops'
            },
            {
                'concept': 'The human immune system',
                'context': 'Highlight defense mechanisms, adaptation, and systemic responses'
            },
            {
                'concept': 'Social media influence',
                'context': 'Consider information spread, network effects, and psychological impacts'
            }
        ]
        return {str(i+1): concept for i, concept in enumerate(random.sample(concepts, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create an abstract visual representation of the concept: {t['concept']}. Your task has two parts:

1. Visual Representation Design (250-300 words):
   a) Describe an abstract visual representation of the given concept, focusing on {t['context']}.
   b) Explain how different visual elements (shapes, colors, connections, etc.) represent key aspects of the concept.
   c) Discuss how your visual representation captures the complexity and interrelationships within the concept.
   d) Describe how your design would change or animate over time to represent dynamic aspects of the concept.

2. Interpretation and Analysis (200-250 words):
   a) Explain how someone would 'read' or interpret your visual representation.
   b) Discuss what insights or understanding your representation might provide that a textual description alone might not.
   c) Analyze potential limitations or ambiguities in your visual representation.
   d) Suggest how your representation could be used as a tool for further analysis or problem-solving related to the concept.

3. AI-Human Collaboration (150-200 words):
   a) Describe how an AI system and a human could collaborate to refine and iterate on this visual representation.
   b) Discuss the respective strengths that AI and humans might bring to this collaborative process.
   c) Propose a method for evaluating the effectiveness of the resulting visual representation.

Ensure your response demonstrates creative thinking, abstract reasoning, and an understanding of how visual elements can represent complex ideas. Use clear, precise language to describe visual concepts, and explain your reasoning throughout the process.

Format your response using the numbered structure provided above, with clear headings for each section. Your total response should be between 600-750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates creativity and abstract thinking in designing the visual representation.",
            "The visual elements and their relationships are clearly explained and relevant to the given concept.",
            "The interpretation and analysis show depth of understanding and insight into the concept and its visual representation.",
            "The AI-Human collaboration section provides thoughtful and plausible ideas for joint work and evaluation.",
            "The overall response is well-structured, coherent, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
