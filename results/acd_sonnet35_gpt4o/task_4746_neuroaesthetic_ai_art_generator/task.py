import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_regions = ['prefrontal cortex', 'amygdala', 'insula', 'anterior cingulate cortex']
        art_mediums = ['painting', 'sculpture', 'music', 'dance']
        aesthetic_experiences = ['beauty', 'sublimity', 'disgust', 'awe']
        artistic_movements = ['surrealism', 'abstract expressionism', 'minimalism', 'romanticism']

        return {
            "1": {
                "brain_region": random.choice(brain_regions),
                "art_medium": random.choice(art_mediums),
                "aesthetic_experience": random.choice(aesthetic_experiences),
                "artistic_movement": random.choice(artistic_movements)
            },
            "2": {
                "brain_region": random.choice(brain_regions),
                "art_medium": random.choice(art_mediums),
                "aesthetic_experience": random.choice(aesthetic_experiences),
                "artistic_movement": random.choice(artistic_movements)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that analyzes brain activity in the {t['brain_region']} associated with the aesthetic experience of {t['aesthetic_experience']}, and uses this information to generate and evaluate {t['art_medium']} in the style of {t['artistic_movement']}. Your response should include:

1. Neuroscientific Framework (250-300 words):
   a) Explain the role of the {t['brain_region']} in processing the aesthetic experience of {t['aesthetic_experience']}.
   b) Describe how you would collect and analyze brain activity data related to this aesthetic experience.
   c) Discuss any challenges in isolating and interpreting the relevant neural signals.

2. AI System Architecture (300-350 words):
   a) Outline the key components of your AI system for analyzing brain activity and generating art.
   b) Explain how your system translates neural data into artistic parameters or rules.
   c) Describe the algorithms or models used for art generation in the specified medium and style.
   d) Discuss how your system evaluates the generated art based on the analyzed brain activity patterns.

3. Artistic Integration (250-300 words):
   a) Explain how your AI system incorporates principles of {t['artistic_movement']} in generating {t['art_medium']}.
   b) Describe how the system ensures the generated art evokes the intended aesthetic experience of {t['aesthetic_experience']}.
   c) Discuss any novel approaches to bridging neuroscience and art theory in your system design.

4. Example Generation (200-250 words):
   a) Provide a detailed description of an artwork your AI system might generate based on the given parameters.
   b) Explain how this artwork reflects both the neural data and the artistic style.
   c) Discuss how the artwork might evoke the intended aesthetic experience in viewers.

5. Ethical and Philosophical Implications (200-250 words):
   a) Discuss the ethical considerations of using brain data to generate art.
   b) Explore the philosophical implications of AI-generated art based on human neural responses.
   c) Consider how this technology might impact our understanding of creativity and artistic expression.

6. Evaluation and Future Directions (200-250 words):
   a) Propose methods for evaluating the effectiveness and artistic merit of your AI system's creations.
   b) Discuss potential applications of this technology in fields such as art therapy, entertainment, or neuroscience research.
   c) Suggest areas for future research or improvement in neuroaesthetic AI art generation.

Ensure your response demonstrates a deep understanding of neuroscience, art theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the role of the {t['brain_region']} in processing the aesthetic experience of {t['aesthetic_experience']}.",
            f"The AI system architecture effectively translates neural data into artistic parameters for generating {t['art_medium']}.",
            f"The system incorporates principles of {t['artistic_movement']} and aims to evoke the aesthetic experience of {t['aesthetic_experience']}.",
            "The example artwork generation is detailed and reflects both neural data and artistic style.",
            "The response thoughtfully discusses ethical and philosophical implications of neuroaesthetic AI art generation.",
            "The proposed evaluation methods and future directions are insightful and relevant.",
            "The overall response demonstrates creativity, interdisciplinary knowledge integration, and scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
