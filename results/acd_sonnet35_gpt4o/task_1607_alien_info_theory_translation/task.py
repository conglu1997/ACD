import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        alien_bases = [
            {
                'base': 'Silicon',
                'environment': 'High-pressure gas giant'
            },
            {
                'base': 'Ammonia',
                'environment': 'Cryogenic liquid methane ocean'
            }
        ]
        info_structures = [
            {
                'structure': 'Quantum spin networks',
                'description': 'Information encoded in the quantum states of entangled particles'
            },
            {
                'structure': 'Gravitational waves',
                'description': 'Information encoded in the modulation of spacetime curvature'
            }
        ]
        tasks = []
        for ab in alien_bases:
            for is_ in info_structures:
                tasks.append({
                    'alien_base': ab['base'],
                    'alien_environment': ab['environment'],
                    'info_structure': is_['structure'],
                    'info_description': is_['description']
                })
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system to translate and interpret alien information structures based on hypothetical non-carbon-based life forms, incorporating principles from astrobiology, information theory, and speculative physics. Your task involves creating a translation system for {t['alien_base']}-based life forms living in a {t['alien_environment']}, who use {t['info_structure']} ({t['info_description']}) as their primary method of information storage and communication. Your response should include the following sections:

1. Theoretical Framework (250-300 words):
   a) Explain how {t['alien_base']}-based life might evolve in a {t['alien_environment']}.
   b) Describe the physical properties and constraints of {t['info_structure']} as an information carrier.
   c) Discuss how these alien life forms might perceive and interact with their environment using this information structure.

2. Translation System Design (300-350 words):
   a) Describe the key components of your translation system.
   b) Explain how your system would detect and capture {t['info_structure']}.
   c) Detail the process of converting {t['info_structure']} into a form interpretable by humans.
   d) Discuss any novel algorithms or technologies required for this translation process.

3. Information Theory Analysis (200-250 words):
   a) Analyze the information capacity and efficiency of {t['info_structure']} compared to conventional human information systems.
   b) Discuss potential noise sources and error correction mechanisms in this alien information system.
   c) Propose a method for quantifying the semantic content of messages encoded in {t['info_structure']}.

4. Speculative Physics (200-250 words):
   a) Propose a theoretical model explaining how {t['alien_base']}-based life forms could manipulate {t['info_structure']}.
   b) Discuss any implications this model might have for our current understanding of physics.
   c) Suggest an experiment that could potentially validate aspects of your model.

5. Potential Applications (150-200 words):
   a) Propose two potential applications of your translation system beyond communicating with alien life.
   b) Discuss how insights from this alien information system might advance human information technology.

6. Ethical and Philosophical Implications (150-200 words):
   a) Discuss the potential impact of successfully translating alien information structures on human philosophy and worldviews.
   b) Address ethical considerations in attempting to communicate with or interpret information from alien life forms.

7. Limitations and Future Directions (150-200 words):
   a) Discuss potential limitations of your translation system.
   b) Propose areas for future research or improvement of your system.
   c) Suggest how this work might inform the search for extraterrestrial intelligence (SETI).

Ensure your response demonstrates a deep understanding of astrobiology, information theory, and theoretical physics. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1400-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['alien_base']}-based life, {t['alien_environment']} environments, and {t['info_structure']} as an information carrier.",
            "The proposed translation system is innovative, scientifically plausible, and thoroughly explained.",
            "The information theory analysis is insightful and well-reasoned.",
            "The speculative physics section proposes novel ideas while maintaining scientific credibility.",
            "The response addresses ethical and philosophical implications thoughtfully.",
            "The writing is clear, well-structured, and uses appropriate technical terminology from multiple disciplines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
