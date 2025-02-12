import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "target_emotion": "nostalgia",
                "musical_element": "harmony",
                "brain_region": "hippocampus"
            },
            {
                "target_emotion": "awe",
                "musical_element": "dynamics",
                "brain_region": "anterior insula"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neural network-based AI system that can compose music to elicit the emotion of {t['target_emotion']}, focusing on the musical element of {t['musical_element']} and considering the role of the {t['brain_region']} in emotional processing. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for emotion-based music composition.
   b) Explain how your system incorporates neuroscientific principles of music perception and emotional processing.
   c) Detail how the system specifically targets the {t['brain_region']} to evoke {t['target_emotion']}.
   d) Discuss how your system manipulates {t['musical_element']} to achieve the desired emotional response.

2. Neural Network Design (200-250 words):
   a) Outline the structure of your neural network, including types of layers and their functions.
   b) Explain how the network processes musical input and generates compositions.
   c) Describe any novel or unique features in your network architecture that address the challenge of emotion-based composition.

3. Training Process (200-250 words):
   a) Describe the data you would use to train your AI system.
   b) Explain your training methodology, including any specific techniques or algorithms.
   c) Discuss how you would validate the emotional impact of the generated music during training.

4. Composition Generation (200-250 words):
   a) Provide a step-by-step explanation of how your system would generate a composition to evoke {t['target_emotion']}.
   b) Explain how the system ensures the prominence of {t['musical_element']} in the composition.
   c) Describe any post-processing or refinement steps applied to the generated music.

5. Evaluation Metrics (150-200 words):
   a) Propose specific metrics to evaluate the effectiveness of your system in evoking {t['target_emotion']}.
   b) Describe how you would measure the system's manipulation of {t['musical_element']}.
   c) Discuss potential challenges in evaluating emotion-based AI music composition.

6. Ethical Considerations (100-150 words):
   a) Discuss ethical implications of using AI to compose emotion-evoking music.
   b) Address potential concerns about emotional manipulation through AI-generated music.
   c) Propose guidelines for responsible use of your system.

7. Future Developments (100-150 words):
   a) Suggest two potential improvements or extensions to your system.
   b) Discuss how your system could be adapted to study or treat emotional or neurological disorders.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and music theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1200-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of how the {t['brain_region']} is involved in processing the emotion of {t['target_emotion']}.",
            f"The system design clearly explains how it manipulates the musical element of {t['musical_element']} to evoke the target emotion.",
            "The neural network design and training process are well-explained and scientifically plausible.",
            "The composition generation process is clearly described and logically sound.",
            "The proposed evaluation metrics are specific and relevant to measuring emotional responses to music.",
            "Ethical considerations are thoughtfully discussed with proposed guidelines for responsible use.",
            "The response demonstrates creativity and innovation while maintaining scientific accuracy."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
