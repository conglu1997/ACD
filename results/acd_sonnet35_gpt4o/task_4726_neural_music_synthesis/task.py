import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_regions = [
            "auditory cortex",
            "prefrontal cortex",
            "amygdala",
            "hippocampus",
            "cerebellum"
        ]
        musical_elements = [
            "melody",
            "harmony",
            "rhythm",
            "timbre",
            "dynamics"
        ]
        emotional_states = [
            "joy",
            "sadness",
            "anger",
            "fear",
            "serenity"
        ]
        return {
            "1": {
                "brain_region": random.choice(brain_regions),
                "musical_element": random.choice(musical_elements),
                "emotional_state": random.choice(emotional_states)
            },
            "2": {
                "brain_region": random.choice(brain_regions),
                "musical_element": random.choice(musical_elements),
                "emotional_state": random.choice(emotional_states)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that translates neural activity patterns into musical compositions, focusing on the {t['brain_region']} for neural input, {t['musical_element']} as the primary musical element to manipulate, and {t['emotional_state']} as the target emotional state to evoke. Then, analyze the implications of this system for neuroscience, AI, and artistic expression.

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for neural-to-music translation.
   b) Explain how your system processes neural signals from the {t['brain_region']}.
   c) Detail the algorithms used to translate neural patterns into musical elements, especially {t['musical_element']}.
   d) Discuss how your system incorporates the target emotional state of {t['emotional_state']} into the composition process.
   e) Include a diagram or flowchart illustrating the system's architecture.

2. Neuroscientific Basis (250-300 words):
   a) Explain the role of the {t['brain_region']} in musical perception and emotion.
   b) Describe how your system models the relationship between neural activity in this region and musical features.
   c) Discuss any novel hypotheses about brain function that your system design suggests.
   d) Address potential limitations in our current understanding of the neural basis of music perception and emotion.

3. AI and Machine Learning Techniques (250-300 words):
   a) Detail the specific AI and machine learning techniques used in your system.
   b) Explain how these techniques are adapted for the unique challenges of neural-to-music translation.
   c) Discuss how your system handles the temporal aspects of both neural signals and music.
   d) Describe how your AI learns to generate music that evokes the target emotional state of {t['emotional_state']}.

4. Musical Composition Process (200-250 words):
   a) Explain how your system generates {t['musical_element']} based on neural input.
   b) Describe how other musical elements are incorporated to support the primary element.
   c) Discuss how your system ensures musical coherence and aesthetic quality.
   d) Provide a short example of how a specific neural pattern might be translated into a musical phrase.

5. Artistic and Emotional Expression (200-250 words):
   a) Analyze how well your system captures and expresses the emotional state of {t['emotional_state']}.
   b) Discuss the artistic implications of AI-generated music based on neural activity.
   c) Consider how this technology might impact our understanding of creativity and emotional expression.
   d) Address potential criticisms regarding the authenticity of AI-generated emotional music.

6. Ethical Considerations (150-200 words):
   a) Identify potential ethical concerns related to translating neural activity into music.
   b) Discuss privacy implications of using personal neural data for artistic expression.
   c) Consider the potential therapeutic applications and associated ethical challenges.
   d) Propose guidelines for the responsible development and use of neural music synthesis technology.

7. Future Directions and Interdisciplinary Impact (200-250 words):
   a) Propose two potential advancements or applications of your neural music synthesis technology.
   b) Discuss how this technology might contribute to our understanding of consciousness and subjective experience.
   c) Explain how your system might be adapted for other forms of artistic expression beyond music.
   d) Describe potential collaborations between neuroscientists, AI researchers, and musicians to further develop this technology.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and music theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1550-1900 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the {t['brain_region']} and its role in musical perception and emotion.",
            f"The system effectively translates neural activity into {t['musical_element']} while evoking the emotional state of {t['emotional_state']}.",
            "The AI and machine learning techniques are well-explained and appropriate for the task.",
            "The musical composition process is clearly described and takes into account both neural input and musical coherence.",
            "The response thoughtfully addresses ethical considerations and future directions for the technology.",
            "The answer is creative and innovative while maintaining scientific plausibility.",
            "The response effectively integrates knowledge from neuroscience, AI, and music theory throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
