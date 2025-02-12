import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_regions = ['prefrontal cortex', 'auditory cortex', 'amygdala', 'hippocampus']
        music_elements = ['rhythm', 'melody', 'harmony', 'timbre']
        ai_techniques = ['spiking neural networks', 'reservoir computing', 'neuroevolution']
        music_genres = ['classical', 'jazz', 'electronic', 'world music']
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                'brain_region': random.choice(brain_regions),
                'music_element': random.choice(music_elements),
                'ai_technique': random.choice(ai_techniques),
                'target_genre': random.choice(music_genres)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that synthesizes music based on real-time brain activity, incorporating principles from neuroscience, music theory, and neuromorphic computing. Your system should focus on the {t['brain_region']} for brain activity input, primarily control the {t['music_element']} of the generated music, utilize {t['ai_technique']} as the core AI technique, and aim to produce music in the {t['target_genre']} genre.

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the overall structure of your neuromorphic music synthesis system.
   b) Explain how your system interfaces with brain activity data from the {t['brain_region']}.
   c) Detail how you incorporate {t['ai_technique']} into your design.
   d) Discuss how your system translates neural signals into musical {t['music_element']}.
   e) Explain how your system ensures the output adheres to the {t['target_genre']} genre.

2. Neuroscience-Music Mapping (250-300 words):
   a) Explain the theoretical basis for mapping activity in the {t['brain_region']} to musical {t['music_element']}.
   b) Describe any novel approaches or hypotheses your system employs in this mapping.
   c) Discuss how your system accounts for individual differences in brain activity and musical perception.

3. Real-time Processing and Adaptation (200-250 words):
   a) Explain how your system processes brain activity data in real-time.
   b) Describe how the system adapts to changes in neural activity during a music generation session.
   c) Discuss any techniques used to minimize latency between brain activity and musical output.

4. Music Theory Integration (200-250 words):
   a) Describe how your system incorporates music theory principles, especially those relevant to {t['music_element']} and {t['target_genre']}.
   b) Explain how the system balances adherence to music theory with the spontaneity of brain-derived input.
   c) Discuss any novel music theory concepts or rules that emerge from your brain-to-music mapping approach.

5. Ethical Considerations and Potential Applications (150-200 words):
   a) Discuss ethical implications of a system that translates thought into music, including privacy concerns and potential misuse.
   b) Propose guidelines for the responsible development and use of neuromorphic music synthesis technology.
   c) Suggest two potential applications of your system beyond artistic expression (e.g., in therapy, cognitive science research, or human-computer interaction).

6. Evaluation and Future Work (150-200 words):
   a) Propose a method for evaluating the quality and faithfulness of the brain-to-music translation.
   b) Suggest two specific areas for future research or improvement of your system.
   c) Discuss potential long-term impacts of this technology on our understanding of creativity and consciousness.

Ensure your response demonstrates a deep understanding of neuroscience, music theory, and AI technologies. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a comprehensive understanding of neuroscience, music theory, and AI technologies, particularly {t['ai_technique']}.",
            f"The system architecture effectively integrates brain activity data from the {t['brain_region']} with music generation, focusing on {t['music_element']}.",
            f"The neuroscience-music mapping is well-explained and plausible, with novel approaches or hypotheses presented.",
            "The real-time processing and adaptation of the system is clearly described and accounts for challenges in brain-to-music translation.",
            f"Music theory principles, especially those relevant to {t['music_element']} and {t['target_genre']}, are effectively incorporated into the system design.",
            "Ethical considerations are thoroughly discussed with responsible guidelines proposed.",
            "The evaluation method and future work suggestions are well-reasoned and demonstrate forward-thinking in the field.",
            "The response is well-structured, addressing all required points comprehensively within the specified word count ranges."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
