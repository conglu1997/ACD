import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_regions = [
            "auditory cortex",
            "prefrontal cortex",
            "hippocampus",
            "amygdala",
            "cerebellum"
        ]
        music_genres = [
            "classical",
            "jazz",
            "electronic",
            "world music",
            "avant-garde"
        ]
        neural_recording_methods = [
            "EEG",
            "fMRI",
            "single-neuron recording",
            "MEG",
            "intracranial EEG"
        ]
        
        tasks = {
            "1": {
                "brain_region": random.choice(brain_regions),
                "music_genre": random.choice(music_genres),
                "recording_method": random.choice(neural_recording_methods)
            },
            "2": {
                "brain_region": random.choice(brain_regions),
                "music_genre": random.choice(music_genres),
                "recording_method": random.choice(neural_recording_methods)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that composes music in the {t['music_genre']} genre by interpreting real-time neural activity from the {t['brain_region']} using {t['recording_method']}. Then, analyze its implications for our understanding of creativity, consciousness, and the nature of artistic expression. Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your neuromusical AI composer.
   b) Explain how the system processes neural signals from the {t['brain_region']}.
   c) Detail how the AI translates neural activity into musical elements.
   d) Discuss any novel machine learning techniques employed in your design.
   e) Provide a high-level diagram or flowchart of your system architecture (describe it textually).

2. Neural-Musical Mapping (200-250 words):
   a) Explain how specific neural patterns are mapped to musical elements (e.g., rhythm, melody, harmony).
   b) Describe how the system captures and interprets emotional or cognitive states from neural activity.
   c) Discuss how the AI ensures the composed music adheres to the principles of {t['music_genre']}.
   d) Address any challenges in maintaining musical coherence and structure.

3. Creative Process Analysis (200-250 words):
   a) Analyze how your system's composition process compares to human creativity.
   b) Discuss the role of consciousness and intentionality in your AI's musical creation.
   c) Explore the philosophical implications of machine-generated art based on human neural activity.
   d) Consider whether the resulting music should be attributed to the human subject, the AI, or both.

4. Ethical Considerations (150-200 words):
   a) Identify potential ethical concerns related to privacy, mental autonomy, and artistic integrity.
   b) Discuss the implications of commodifying or commercializing music generated from personal neural data.
   c) Consider the potential psychological effects on individuals whose brain activity is used for composition.
   d) Propose guidelines for the ethical development and use of neuromusical AI technology.

5. Experimental Design (200-250 words):
   a) Propose an experiment to test the effectiveness and artistic quality of your neuromusical AI composer.
   b) Describe the methodology, including participant selection, control conditions, and evaluation criteria.
   c) Explain how you would measure both the technical accuracy and the artistic merit of the composed music.
   d) Discuss how you would assess the system's impact on listeners' emotional and cognitive states.

6. Implications for Neuroscience and Musicology (150-200 words):
   a) Discuss how this technology might advance our understanding of the neural basis of music perception and creation.
   b) Explore potential applications in music therapy or treatment of neurological disorders.
   c) Consider how this technology might influence music education and the development of musical skills.

7. Future Directions (100-150 words):
   a) Propose two potential enhancements or extensions to your neuromusical AI composer.
   b) Speculate on how this technology might evolve in the next decade and its potential societal impacts.

Ensure your response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and addressing the ethical and philosophical questions raised by this technology.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1250-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a comprehensive explanation of how neural activity from the {t['brain_region']} is translated into {t['music_genre']} music",
            "The system design demonstrates a clear understanding of neuroscience, music theory, and AI principles",
            "The creative process analysis provides insightful discussion on the nature of creativity and consciousness",
            "The ethical considerations are thorough and address key issues related to privacy and artistic integrity",
            "The experimental design is well-thought-out and addresses both technical and artistic aspects of evaluation",
            "The response demonstrates creativity and innovation while maintaining scientific plausibility",
            "The analysis shows a deep understanding of the implications for neuroscience and musicology",
            "The future directions provide insightful suggestions and discuss broader impacts"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
