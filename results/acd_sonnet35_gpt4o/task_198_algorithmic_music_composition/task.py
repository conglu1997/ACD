import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'musical_style': 'Minimalism',
                'mathematical_concept': 'Fibonacci sequence',
                'ai_technique': 'Generative Adversarial Networks (GANs)'
            },
            {
                'musical_style': 'Serialism',
                'mathematical_concept': 'Group theory',
                'ai_technique': 'Recurrent Neural Networks (RNNs)'
            },
            {
                'musical_style': 'Aleatoric music',
                'mathematical_concept': 'Chaos theory',
                'ai_technique': 'Reinforcement Learning'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an algorithmic music composition system that combines the following elements:

1. Musical Style: {t['musical_style']}
2. Mathematical Concept: {t['mathematical_concept']}
3. AI Technique: {t['ai_technique']}

Your task is to create a detailed proposal for this system, including:

1. System Architecture (200-250 words):
   - Describe the overall structure of your composition system.
   - Explain how it incorporates the given musical style, mathematical concept, and AI technique.
   - Detail the main components and their interactions.
   - Include a high-level diagram or pseudocode representing the system's workflow.

2. Mathematical Implementation (150-200 words):
   - Explain how you will use the given mathematical concept in your composition process.
   - Provide at least one specific formula or algorithm that will be central to your system.
   - Describe how this mathematical concept influences the musical output.

3. AI Integration (150-200 words):
   - Describe how the specified AI technique will be used in your system.
   - Explain its role in the composition process and how it interacts with other components.
   - Discuss the training process and data requirements for your AI model.

4. Musical Output (100-150 words):
   - Describe the expected characteristics of the music produced by your system.
   - Explain how these align with the given musical style.
   - Provide a brief example of how a short musical phrase might be generated (use text to describe notes, rhythm, or other musical elements).

5. Evaluation Method (100-150 words):
   - Propose a method to evaluate the quality and style-adherence of the compositions.
   - Include both quantitative and qualitative aspects in your evaluation approach.
   - Suggest at least one specific metric or test to assess the system's output.

6. Potential Applications and Ethical Considerations (100-150 words):
   - Suggest two potential real-world applications for your system.
   - Explain how each application could benefit from this algorithmic approach to music composition.
   - Discuss any ethical implications or potential misuse of your system.

Ensure your response demonstrates a deep understanding of music theory, the specified mathematical concept, and AI techniques. Be creative in your approach while maintaining scientific and artistic rigor. Use appropriate terminology from all relevant fields and provide explanations where necessary.

Format your response using clear headings for each section (e.g., '1. System Architecture', '2. Mathematical Implementation', etc.). Your total response should be between 900-1100 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified musical style, mathematical concept, and AI technique.",
            "The system architecture is well-designed, clearly incorporates all required elements, and includes a high-level diagram or pseudocode.",
            "The mathematical implementation is sound, relevant to the composition process, and includes at least one specific formula or algorithm.",
            "The AI integration is well-explained, appropriately applied to the task, and includes discussion of training and data requirements.",
            "The description of the musical output aligns with the given musical style and includes a brief example of a generated musical phrase.",
            "The proposed evaluation method includes both quantitative and qualitative aspects, with at least one specific metric or test.",
            "The potential applications are innovative, well-justified, and include consideration of ethical implications.",
            "The response follows the specified format with clear headings for each section.",
            "The total word count is between 900-1100 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
