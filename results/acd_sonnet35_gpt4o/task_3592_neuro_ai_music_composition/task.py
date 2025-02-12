import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = ['joy', 'sadness', 'anger', 'fear', 'surprise', 'disgust']
        musical_elements = ['melody', 'harmony', 'rhythm', 'timbre', 'dynamics']
        brain_regions = ['amygdala', 'hippocampus', 'prefrontal cortex', 'auditory cortex', 'nucleus accumbens']
        
        task1 = {
            'emotion': random.choice(emotions),
            'musical_element': random.choice(musical_elements),
            'brain_region': random.choice(brain_regions)
        }
        
        task2 = {
            'emotion': random.choice(emotions),
            'musical_element': random.choice(musical_elements),
            'brain_region': random.choice(brain_regions)
        }
        
        return {
            "1": task1,
            "2": task2
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neural-inspired AI system for composing music that evokes the emotion of {t['emotion']}, focusing on the musical element of {t['musical_element']} and incorporating insights from the {t['brain_region']}. Your response should include the following sections:

1. Neuroscientific Foundation (250-300 words):
   a) Explain the role of the {t['brain_region']} in processing emotions and music.
   b) Describe how this brain region might influence the perception of {t['musical_element']}.
   c) Discuss any relevant neuroscientific theories or studies related to {t['emotion']} and music processing.
   d) Cite at least two relevant scientific studies to support your explanations.

2. AI System Architecture (300-350 words):
   a) Propose a detailed architecture for your neural-inspired AI music composition system.
   b) Explain how your system incorporates insights from the {t['brain_region']} and music theory.
   c) Describe the key components and their interactions within your system.
   d) Include a simple diagram or flowchart of your system architecture using ASCII art or Unicode characters (minimum 10 lines, maximum 20 lines).
   e) Propose at least one novel musical feature or technique in your system design.

3. Music Generation Process (250-300 words):
   a) Detail how your AI system generates music to evoke {t['emotion']}.
   b) Explain how the system manipulates {t['musical_element']} to achieve the desired emotional response.
   c) Describe any novel algorithms or techniques used in the composition process.

4. Emotional Response Modeling (200-250 words):
   a) Explain how your system models and predicts emotional responses to generated music.
   b) Discuss any feedback mechanisms or learning processes that allow the system to improve its ability to evoke {t['emotion']}.
   c) Address potential challenges in accurately modeling subjective emotional experiences.

5. Evaluation and Validation (200-250 words):
   a) Propose methods to evaluate the effectiveness of your system in evoking {t['emotion']}.
   b) Suggest experiments to validate the influence of {t['musical_element']} on emotional responses.
   c) Discuss how you would measure the system's success in mimicking human-like creativity in music composition.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Address potential ethical implications of using AI for emotional manipulation through music.
   b) Discuss the impact of this technology on human creativity and the music industry.
   c) Propose two potential future research directions to enhance your system's capabilities.

Ensure your response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Include a word count at the end of each section and a total word count at the end of your response. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified brain region and its role in emotion and music processing.",
            "The proposed AI system architecture is innovative and clearly incorporates insights from neuroscience and music theory.",
            "The music generation process is well-explained and shows a clear connection to evoking the specified emotion.",
            "The approach to manipulating the given musical element is creative and well-reasoned.",
            "The emotional response modeling is sophisticated and addresses the challenges of subjective experiences.",
            "The evaluation and validation methods are well-designed and relevant to the system's goals.",
            "Ethical considerations are thoughtfully addressed, and future research directions are insightful.",
            "The response is well-structured, clear, and within the specified word count range.",
            "At least two relevant scientific studies are cited in the Neuroscientific Foundation section.",
            "The ASCII art or Unicode diagram of the system architecture is provided and meets the specified line count requirements.",
            "At least one novel musical feature or technique is proposed in the system design.",
            "Word counts are provided for each section and the total response."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
