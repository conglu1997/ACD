import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        sensory_modalities = [
            "visual",
            "auditory",
            "olfactory",
            "gustatory",
            "tactile"
        ]
        art_forms = [
            "painting",
            "music composition",
            "sculpture",
            "interactive installation",
            "virtual reality experience"
        ]
        applications = [
            "art therapy",
            "neurodivergent education",
            "human-computer interaction",
            "sensory augmentation",
            "cross-cultural communication"
        ]
        
        tasks = {
            "1": {
                "input_modality": random.choice(sensory_modalities),
                "output_art_form": random.choice(art_forms),
                "application": random.choice(applications)
            },
            "2": {
                "input_modality": random.choice(sensory_modalities),
                "output_art_form": random.choice(art_forms),
                "application": random.choice(applications)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that generates synesthetic art by translating {t['input_modality']} input into a {t['output_art_form']}. Then, apply this system to create a unique artwork and explore its potential applications in {t['application']}. Your response should include the following sections:

1. Synesthetic System Design (300-350 words):
   a) Describe the key components of your synesthetic art generation system.
   b) Explain how your system translates {t['input_modality']} input into {t['output_art_form']}.
   c) Discuss the cognitive and neurological principles underlying your system's design.
   d) Provide a simple diagram or flowchart of your system (describe it textually).

2. Artwork Generation (250-300 words):
   a) Use your system to generate a unique artwork based on a specific {t['input_modality']} input of your choice.
   b) Describe the resulting {t['output_art_form']} in detail, including its sensory characteristics and emotional impact.
   c) Explain how the generated artwork reflects the principles of synesthesia.

3. Cognitive and Artistic Analysis (200-250 words):
   a) Analyze the cognitive processes involved in perceiving and interpreting your generated artwork.
   b) Discuss how your artwork challenges or extends traditional artistic conventions.
   c) Explore potential cognitive or perceptual effects on viewers/participants.

4. Application in {t['application']} (200-250 words):
   a) Propose a specific application of your synesthetic art generation system in the field of {t['application']}.
   b) Describe how this application could benefit users or advance the field.
   c) Discuss any challenges or ethical considerations in implementing this application.

5. Technical Implementation (150-200 words):
   a) Outline the key algorithms or computational methods needed to implement your system.
   b) Discuss any hardware requirements or constraints for your system.
   c) Propose a method for evaluating the effectiveness of your system in generating synesthetic art.

6. Future Directions and Implications (100-150 words):
   a) Suggest two potential extensions or improvements to your synesthetic art generation system.
   b) Discuss broader implications of your system for our understanding of perception, creativity, and consciousness.

Ensure your response demonstrates a deep understanding of neuroscience, art theory, and computational creativity. Use technical terminology appropriately and provide explanations where necessary. Be innovative in your approach while maintaining scientific and artistic plausibility.

Format your response with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a comprehensive explanation of how {t['input_modality']} input is translated into {t['output_art_form']}",
            "The system design demonstrates a clear understanding of synesthesia and relevant cognitive principles",
            "The generated artwork is described in detail and reflects synesthetic principles",
            f"The proposed application in {t['application']} is well-explained and plausible",
            "The technical implementation section outlines feasible computational methods and evaluation strategies",
            "The response demonstrates creativity and innovation while maintaining scientific and artistic plausibility",
            "The analysis shows a deep understanding of the cognitive processes involved in creating and perceiving synesthetic art",
            "The future directions and implications section provides insightful suggestions and discusses broader impacts"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
