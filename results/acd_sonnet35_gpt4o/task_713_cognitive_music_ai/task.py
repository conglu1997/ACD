import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_states = [
            {
                'state': 'flow',
                'emotion': 'contentment',
                'musical_style': 'ambient'
            },
            {
                'state': 'anxiety',
                'emotion': 'fear',
                'musical_style': 'atonal'
            }
        ]
        return {str(i+1): state for i, state in enumerate(random.sample(cognitive_states, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates music based on cognitive and emotional states, then analyze and modify a musical piece using this system. Your task has the following components:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI music generation system.
   b) Explain how it incorporates cognitive state '{t['state']}' and emotion '{t['emotion']}' into the music generation process.
   c) Discuss how your system integrates principles from music theory, cognitive science, and AI.

2. Musical Representation (200-250 words):
   a) Propose a novel way to represent music that reflects cognitive and emotional states.
   b) Explain how this representation system differs from traditional musical notation.
   c) Provide an example of how a simple melody would be represented in your system.

3. Generation Process (200-250 words):
   a) Describe the step-by-step process your AI system would use to generate music in the '{t['musical_style']}' style.
   b) Explain how the cognitive state and emotion influence each step of the generation process.
   c) Discuss any challenges or unique features of generating music in this style.

4. Analysis and Modification (250-300 words):
   a) Choose a well-known piece of music in the '{t['musical_style']}' style.
   b) Analyze this piece using your AI system, explaining how it would interpret the cognitive and emotional content.
   c) Describe how your system would modify the piece to shift it towards the cognitive state '{t['state']}' and emotion '{t['emotion']}'.
   d) Explain the specific changes your system would make and why.

5. Evaluation and Implications (200-250 words):
   a) Propose a method to evaluate the effectiveness of your AI system in capturing and generating appropriate cognitive and emotional musical content.
   b) Discuss potential applications of your system in fields such as music therapy, entertainment, or cognitive science.
   c) Address any ethical considerations related to AI-generated music and emotional manipulation.

Ensure your response demonstrates a deep understanding of music theory, cognitive science, and AI principles. Use appropriate technical terminology and provide explanations where necessary. Be creative in your approach while maintaining scientific and artistic plausibility. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the cognitive state '{t['state']}' and emotion '{t['emotion']}' in the context of music generation.",
            f"The proposed AI system effectively incorporates principles from music theory, cognitive science, and AI to generate music in the '{t['musical_style']}' style.",
            "The musical representation system is novel and coherently reflects cognitive and emotional states.",
            "The analysis and modification of an existing piece of music is detailed and aligns with the given cognitive state and emotion.",
            "The response shows critical thinking about the evaluation, applications, and ethical considerations of the proposed system."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
