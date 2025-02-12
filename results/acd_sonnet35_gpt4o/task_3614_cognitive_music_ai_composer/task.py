import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_styles = [
            {
                'style': 'Jazz',
                'description': 'A music genre characterized by improvisation, syncopation, and swing rhythm'
            },
            {
                'style': 'Classical',
                'description': 'A genre of Western art music with complex harmonies and formal structures'
            }
        ]
        
        cognitive_principles = [
            {
                'principle': 'Expectation and surprise',
                'description': 'The cognitive processes involved in anticipating musical events and the emotional responses to unexpected elements'
            },
            {
                'principle': 'Gestalt principles in music perception',
                'description': 'How the brain organizes musical elements into coherent patterns and structures'
            }
        ]
        
        tasks = [
            {
                'musical_style': musical_styles[0],
                'cognitive_principle': cognitive_principles[0]
            },
            {
                'musical_style': musical_styles[1],
                'cognitive_principle': cognitive_principles[1]
            }
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system for music composition that incorporates principles from music theory, cognitive science of music perception, and computational creativity. Your system should focus on composing in the {t['musical_style']['style']} style and incorporate the cognitive principle of {t['cognitive_principle']['principle']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the main components of your AI music composition system and how they interact.
   b) Explain how your system incorporates music theory principles specific to {t['musical_style']['style']}.
   c) Detail how the system implements the cognitive principle of {t['cognitive_principle']['principle']}.
   d) Include a simple ASCII diagram or flowchart of your system architecture.

2. Composition Process (250-300 words):
   a) Explain how your AI system generates musical ideas and develops them into full compositions.
   b) Provide examples of specific techniques used to create {t['musical_style']['style']} compositions.
   c) Describe how the system evaluates and refines its compositions based on musical and cognitive principles.

3. Cognitive Model Integration (200-250 words):
   a) Discuss how your system models human music perception and cognition, particularly {t['cognitive_principle']['principle']}.
   b) Explain how this cognitive modeling influences the composition process.
   c) Propose a method to evaluate whether the system's compositions effectively implement the chosen cognitive principle.

4. Creative Decision-Making (200-250 words):
   a) Describe how your system makes creative decisions during the composition process.
   b) Explain how it balances adherence to {t['musical_style']['style']} conventions with novel and unexpected elements.
   c) Discuss any mechanisms for generating and evaluating original musical ideas.

5. Emotional Expression (150-200 words):
   a) Explain how your system incorporates emotional expression into its compositions.
   b) Discuss how it maps cognitive and musical elements to emotional responses.
   c) Propose a method to evaluate the emotional impact of the AI-generated compositions.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss ethical implications of AI-generated music, including issues of authorship and creativity.
   b) Propose guidelines for responsible development and use of AI music composition systems.
   c) Suggest potential applications of your system beyond music composition.

Ensure your response demonstrates a deep understanding of music theory, cognitive science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility and musical authenticity.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['musical_style']['style']} music theory and how {t['cognitive_principle']['principle']} can be applied in music composition.",
            "The AI system design is innovative, coherent, and grounded in principles of music theory, cognitive science, and artificial intelligence.",
            "The proposed composition process is creative, specific, and likely to produce authentic {t['musical_style']['style']} music.",
            "The response thoroughly addresses the integration of cognitive models and creative decision-making in the AI system.",
            "The ethical considerations and future directions are well-considered and relevant to AI music composition."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
