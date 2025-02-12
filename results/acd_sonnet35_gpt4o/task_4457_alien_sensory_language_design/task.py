import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        alien_species = [
            {
                'name': 'Luminavores',
                'primary_sense': 'Photon polarization detection',
                'secondary_sense': 'Quantum entanglement perception',
                'environment': 'Gas giant upper atmosphere',
                'concept': 'Time dilation'
            },
            {
                'name': 'Gravitons',
                'primary_sense': 'Gravitational wave detection',
                'secondary_sense': 'Magnetic field manipulation',
                'environment': 'Neutron star surface',
                'concept': 'Information entropy'
            },
            {
                'name': 'Neutrinians',
                'primary_sense': 'Neutrino flavor oscillation detection',
                'secondary_sense': 'Dark matter density perception',
                'environment': 'Interstellar void',
                'concept': 'Quantum superposition'
            },
            {
                'name': 'Chronosapiens',
                'primary_sense': 'Temporal flux detection',
                'secondary_sense': 'Probability wave manipulation',
                'environment': 'Event horizon boundary',
                'concept': 'Causal loops'
            }
        ]
        return {str(i+1): species for i, species in enumerate(random.sample(alien_species, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a communication system for the {t['name']}, a hypothetical alien species with unique sensory capabilities, then use it to express a complex abstract concept. The {t['name']} have the following characteristics:

1. Primary sensory capability: {t['primary_sense']}
2. Secondary sensory capability: {t['secondary_sense']}
3. Native environment: {t['environment']}
4. Abstract concept to be expressed: {t['concept']}

Your task includes the following steps:

1. Sensory-Based Communication System (300-350 words):
   a) Describe the fundamental principles of the communication system based on the alien species' sensory capabilities.
   b) Explain how the primary and secondary senses are utilized in the communication process.
   c) Detail the 'phonology' or basic units of the communication system (e.g., modulations of gravitational waves, patterns of neutrino oscillations).
   d) Discuss how the native environment influences the communication system's development and use.

2. Grammar and Syntax (250-300 words):
   a) Outline the basic grammatical structures of the communication system.
   b) Explain how complex ideas are constructed from simpler elements.
   c) Describe any unique features of the syntax that reflect the aliens' sensory experiences or environment.
   d) Provide examples of how temporal or spatial relationships are expressed in this system.

3. Lexicon Development (200-250 words):
   a) Explain the principles behind the creation of 'words' or basic meaningful units in this communication system.
   b) Describe how abstract concepts are represented.
   c) Provide 3-5 example 'words' with their meanings and explain how they reflect the aliens' sensory experiences.

4. Expressing the Abstract Concept (250-300 words):
   a) Use your designed communication system to express the given abstract concept: {t['concept']}.
   b) Provide a detailed 'translation' of this expression, explaining how each component contributes to the overall meaning.
   c) Discuss any challenges in expressing this concept in the alien communication system and how you addressed them.

5. Cognitive Implications (200-250 words):
   a) Analyze how this communication system might influence the thought patterns and worldview of the {t['name']}.
   b) Discuss how their unique sensory capabilities and environment might lead to different conceptualizations of reality compared to humans.
   c) Speculate on potential areas of knowledge or understanding where the {t['name']} might excel due to their communication system.

6. Comparative Analysis (200-250 words):
   a) Compare and contrast your designed communication system with human language.
   b) Discuss any potential universal properties of communication that emerge from this exercise.
   c) Reflect on what this alien communication system reveals about the nature of language and thought in general.

Ensure your response demonstrates a deep understanding of linguistics, sensory biology, cognitive science, and the specified scientific concept. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The communication system effectively utilizes the {t['name']}'s primary sense of {t['primary_sense']} and secondary sense of {t['secondary_sense']}.",
            f"The design considers the influence of the {t['environment']} environment on the communication system.",
            f"The response successfully expresses the concept of {t['concept']} using the designed communication system.",
            "The grammar, syntax, and lexicon of the communication system are well-developed and internally consistent.",
            "The response demonstrates creativity and innovation while maintaining scientific plausibility.",
            "The analysis of cognitive implications and comparison with human language is insightful and well-reasoned.",
            "The response is well-structured, clear, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
