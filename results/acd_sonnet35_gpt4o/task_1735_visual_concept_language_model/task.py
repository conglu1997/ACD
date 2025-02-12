import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            "Time",
            "Justice",
            "Evolution",
            "Consciousness",
            "Entropy",
            "Democracy",
            "Emergence",
            "Infinity",
            "Paradox",
            "Synergy"
        ]
        visual_elements = [
            "Color",
            "Shape",
            "Texture",
            "Composition",
            "Perspective"
        ]
        cognitive_principles = [
            "Metaphorical mapping",
            "Conceptual blending",
            "Gestalt principles",
            "Embodied cognition",
            "Cognitive load theory"
        ]
        
        tasks = {}
        for i in range(2):
            concept = random.choice(concepts)
            visual_element = random.choice(visual_elements)
            cognitive_principle = random.choice(cognitive_principles)
            
            tasks[str(i+1)] = {
                "concept": concept,
                "visual_element": visual_element,
                "cognitive_principle": cognitive_principle
            }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI language model capable of generating and interpreting abstract visual representations of complex concepts. Your model should focus on the concept of {t['concept']}, emphasizing the visual element of {t['visual_element']}, and incorporating the cognitive principle of {t['cognitive_principle']}. Provide your response in the following format:

1. Model Architecture (250-300 words):
   a) Describe the overall structure of your AI model, including its main components and how they interact.
   b) Explain how your model integrates natural language processing with visual representation generation and interpretation.
   c) Detail how the model incorporates the specified cognitive principle in its design and function.

2. Concept-to-Visual Mapping (200-250 words):
   a) Explain how your model would translate the concept of {t['concept']} into an abstract visual representation.
   b) Describe how the model utilizes {t['visual_element']} in this representation.
   c) Provide a textual description of what the generated visual representation might look like.

3. Visual-to-Concept Interpretation (200-250 words):
   a) Describe how your model would interpret an abstract visual representation of {t['concept']}.
   b) Explain the process of translating visual elements back into natural language descriptions.
   c) Discuss how the model handles ambiguity or multiple interpretations.

4. Training and Data Requirements (150-200 words):
   a) Outline the types of data needed to train your AI model.
   b) Describe any novel data collection or generation methods required for this task.
   c) Discuss potential challenges in creating a dataset that links abstract concepts to visual representations.

5. Evaluation Methods (150-200 words):
   a) Propose metrics or methods to evaluate the performance of your AI model in both generation and interpretation tasks.
   b) Describe how you would assess the model's understanding of the cognitive principle {t['cognitive_principle']}.
   c) Suggest an experiment to test the model's ability to generalize to new concepts or visual elements.

6. Potential Applications and Implications (150-200 words):
   a) Discuss two potential applications of your visual concept language model in fields such as education, art, or communication.
   b) Analyze how this type of AI model might influence human understanding of abstract concepts or visual communication.
   c) Consider any ethical implications or potential misuses of this technology.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, artificial intelligence, and visual arts. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and technological plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cognitive science, artificial intelligence, and visual arts",
            "The proposed AI model effectively integrates natural language processing with visual representation generation and interpretation",
            "The concept-to-visual mapping and visual-to-concept interpretation processes are clearly explained and incorporate the specified cognitive principle",
            "The training data requirements and evaluation methods are well-thought-out and appropriate for the task",
            "The potential applications and implications of the model are insightfully discussed"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
