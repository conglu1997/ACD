import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        embodied_concepts = [
            {
                'concept': 'time',
                'physical_experience': 'movement through space',
                'example': 'We\'re approaching the deadline.'
            },
            {
                'concept': 'importance',
                'physical_experience': 'weight',
                'example': 'This is a heavy decision.'
            },
            {
                'concept': 'affection',
                'physical_experience': 'warmth',
                'example': 'She gave me a warm welcome.'
            },
            {
                'concept': 'understanding',
                'physical_experience': 'grasping objects',
                'example': 'I can\'t quite grasp that idea.'
            }
        ]
        
        return {str(i+1): random.choice(embodied_concepts) for i in range(2)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a conceptual language model that incorporates the principles of embodied cognition, focusing on how the physical experience of {t['physical_experience']} shapes our understanding and use of language related to the concept of {t['concept']}. Your response should include:

1. Theoretical Framework (200-250 words):
   a) Explain the key principles of embodied cognition relevant to this task.
   b) Describe how the physical experience of {t['physical_experience']} relates to the concept of {t['concept']}.
   c) Discuss any relevant research or theories that support this embodied understanding.
   d) Propose a novel hypothesis about how this embodied experience might influence language processing in ways not yet explored in current literature.

2. Model Architecture (250-300 words):
   a) Propose a high-level architecture for your language model that incorporates embodied cognition principles.
   b) Explain how your model would represent and process the relationship between {t['physical_experience']} and {t['concept']}.
   c) Describe any novel components or mechanisms in your model that differ from traditional language models.
   d) Discuss how your model might handle cross-linguistic variations in embodied metaphors related to {t['concept']}.

3. Language Processing Example (200-250 words):
   a) Using the example phrase \"{t['example']}\", walk through how your model would process and understand this expression.
   b) Explain how the embodied experience influences the model's interpretation or generation of such phrases.
   c) Contrast this with how a traditional, non-embodied language model might process the same phrase.
   d) Provide an example of how your model might generate a novel metaphor based on the embodied understanding of {t['concept']}.

4. Potential Applications and Ethical Considerations (200-250 words):
   a) Propose two potential applications of your embodied language model in fields such as AI, human-computer interaction, or cognitive science.
   b) Explain how these applications could advance our understanding of language or improve existing technologies.
   c) Discuss potential ethical implications or misuses of an AI system with embodied understanding of concepts.
   d) Suggest safeguards or guidelines for responsible development and use of such systems.

5. Limitations and Future Directions (150-200 words):
   a) Discuss potential limitations or challenges of your proposed model.
   b) Suggest areas for future research or development in embodied language models.
   c) Propose an experiment that could empirically test the effectiveness of your model compared to traditional language models.

Ensure your response demonstrates a deep understanding of embodied cognition, linguistics, and artificial intelligence. Use appropriate terminology and provide clear explanations for complex ideas. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a thorough understanding of embodied cognition principles and their application to language processing, including a novel hypothesis.",
            "The proposed model architecture is innovative, coherently incorporates embodied cognition into language processing, and addresses cross-linguistic variations.",
            f"The explanation of how the model processes the example phrase \"{t['example']}\" is clear and demonstrates the integration of embodied experiences, including the generation of a novel metaphor.",
            "The potential applications are creative and well-reasoned, showing a deep understanding of the model's implications, and ethical considerations are thoroughly addressed.",
            "The discussion of limitations and future directions shows critical thinking, awareness of the field's challenges, and includes a proposed empirical experiment.",
            "The response follows the required format and word count guidelines, and demonstrates originality and depth of thought throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
