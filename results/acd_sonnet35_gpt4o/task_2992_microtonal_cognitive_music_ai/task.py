import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_states = [
            "Flow state",
            "Meditative trance",
            "Heightened alertness",
            "Emotional catharsis",
            "Dream-like reverie"
        ]
        cultural_contexts = [
            "Traditional Indian classical",
            "Middle Eastern maqam",
            "Indonesian gamelan",
            "Western avant-garde",
            "African polyrhythmic"
        ]
        microtonal_systems = [
            "22 Shruti",
            "31 equal temperament",
            "Just intonation",
            "Bohlen-Pierce scale",
            "Wendy Carlos' alpha scale"
        ]
        
        tasks = {}
        for i in range(2):
            state = random.choice(cognitive_states)
            context = random.choice(cultural_contexts)
            system = random.choice(microtonal_systems)
            
            tasks[str(i+1)] = {
                "cognitive_state": state,
                "cultural_context": context,
                "microtonal_system": system
            }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can generate and analyze microtonal music based on different cognitive states and cultural contexts. Your system should focus on the cognitive state of {t['cognitive_state']}, draw inspiration from the {t['cultural_context']} tradition, and utilize the {t['microtonal_system']} for pitch organization.

Your response should include the following sections:

1. Theoretical Framework (250-300 words):
   a) Explain the key principles from cognitive science related to the {t['cognitive_state']}.
   b) Describe how the {t['cultural_context']} tradition influences microtonal music composition and perception.
   c) Discuss the characteristics and challenges of the {t['microtonal_system']}.

2. System Architecture (300-350 words):
   a) Outline the main components of your AI system and their functions.
   b) Explain how your system integrates cognitive state information, cultural context, and microtonal theory.
   c) Describe any novel algorithms or techniques your system uses for music generation and analysis.
   d) Discuss how your system ensures musical coherence while adhering to microtonal principles.

3. Cognitive-Musical Mapping (200-250 words):
   a) Provide a detailed explanation of how your system maps the {t['cognitive_state']} to specific aspects of microtonal music.
   b) Include at least one concrete example of a musical pattern or structure your system might generate, using appropriate notation or a clear textual description.
   c) Explain the rationale behind this mapping, citing relevant research in music cognition or ethnomusicology.

4. Cultural Integration and Adaptation (200-250 words):
   a) Describe how your system incorporates elements from the {t['cultural_context']} tradition.
   b) Explain how the AI adapts its output to maintain cultural authenticity while exploring microtonal possibilities.
   c) Discuss any challenges in creating a system that can generalize across different cultural contexts and microtonal systems.

5. Analysis and Interpretation (150-200 words):
   a) Explain how your AI system analyzes and interprets the microtonal music it generates.
   b) Describe the criteria the system uses to evaluate the effectiveness of a composition in expressing the intended cognitive state and cultural context.
   c) Discuss how the system might handle the subjective nature of music perception across different cultures.

6. Ethical Considerations and Applications (150-200 words):
   a) Identify potential ethical concerns related to an AI system that generates culturally-inspired microtonal music.
   b) Propose guidelines for responsible development and use of such a system, considering cultural appropriation and intellectual property issues.
   c) Suggest two potential applications of your system in fields such as music therapy, cross-cultural communication, or music education.

Ensure your response demonstrates a deep understanding of cognitive science, ethnomusicology, microtonal music theory, and AI technologies. Be creative in your approach while maintaining scientific and cultural plausibility. Use appropriate terminology and provide explanations where necessary.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of the cognitive state {t['cognitive_state']}, the {t['cultural_context']} musical tradition, and the {t['microtonal_system']}.",
            "The system architecture integrates cognitive science, ethnomusicology, and microtonal music theory in a novel and plausible manner.",
            "The cognitive-musical mapping is well-explained and justified with relevant research.",
            "The approach to cultural integration and adaptation is thoughtful and addresses potential challenges.",
            "The analysis and interpretation methods are clearly described and consider cultural differences in music perception.",
            "Ethical considerations are thoroughly addressed, with particular attention to cultural sensitivity.",
            "The response is creative and innovative while maintaining scientific and cultural plausibility.",
            "The writing is clear, well-organized, and adheres to the specified format and word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
