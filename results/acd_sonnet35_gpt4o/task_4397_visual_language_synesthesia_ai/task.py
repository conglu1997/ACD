import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "linguistic_feature": "Phonological structure",
                "visual_element": "Color and shape",
                "cognitive_process": "Metaphor comprehension"
            },
            {
                "linguistic_feature": "Syntactic complexity",
                "visual_element": "Spatial arrangement and texture",
                "cognitive_process": "Abstract reasoning"
            },
            {
                "linguistic_feature": "Semantic networks",
                "visual_element": "Interconnected patterns and gradients",
                "cognitive_process": "Conceptual blending"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can generate and interpret abstract visual representations of language, simulating a form of artificial synesthesia between language and visual perception. Your system should focus on the linguistic feature of {t['linguistic_feature']}, utilize {t['visual_element']} as the primary visual elements, and demonstrate its application in the cognitive process of {t['cognitive_process']}. Your response should include:

1. Conceptual Framework (250-300 words):
   a) Explain the principles of synesthesia and how they relate to language and visual perception.
   b) Describe how the specified linguistic feature can be mapped to visual elements.
   c) Discuss the potential insights this mapping might provide into the chosen cognitive process.

2. AI System Architecture (300-350 words):
   a) Design an AI architecture capable of generating and interpreting these visual-linguistic representations.
   b) Explain how your system integrates language processing and visual generation components.
   c) Describe any novel algorithms or techniques used in your system.
   d) Include a high-level diagram of your architecture (described in text).

3. Visual-Linguistic Mapping (250-300 words):
   a) Detail the specific rules or algorithms for mapping the linguistic feature to visual elements.
   b) Provide an example of how a complex linguistic structure would be visually represented.
   c) Explain how your system handles ambiguity or context in these mappings.

4. Interpretation and Analysis (200-250 words):
   a) Describe how your AI system interprets and analyzes the visual representations it generates.
   b) Explain how this interpretation relates to the specified cognitive process.
   c) Discuss any insights your system might provide about human language processing or synesthesia.

5. Training and Data Requirements (150-200 words):
   a) Outline the types of data needed to train your AI system.
   b) Describe any unique challenges in obtaining or creating this data.
   c) Propose a method for validating the system's visual-linguistic mappings.

6. Potential Applications and Implications (200-250 words):
   a) Suggest practical applications of your system in fields such as education, art, or cognitive therapy.
   b) Discuss how this technology might enhance our understanding of language and perception.
   c) Consider potential implications for AI development and human-AI interaction.

7. Ethical Considerations and Limitations (150-200 words):
   a) Identify potential ethical concerns or misuses of this technology.
   b) Discuss limitations of your approach and potential biases in the system.
   c) Propose guidelines for responsible development and use of visual-linguistic AI systems.

Ensure your response demonstrates a deep understanding of linguistics, visual perception, cognitive science, and AI architectures. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should focus on the linguistic feature of {t['linguistic_feature']}",
            f"The system should utilize {t['visual_element']} as the primary visual elements",
            f"The application in the cognitive process of {t['cognitive_process']} should be clearly demonstrated",
            "The AI system architecture should be well-designed and explained",
            "The visual-linguistic mapping should be detailed and provide a concrete example",
            "The response should demonstrate interdisciplinary knowledge and creativity"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
