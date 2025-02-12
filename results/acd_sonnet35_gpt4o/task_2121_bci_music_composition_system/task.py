import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_regions = [
            "auditory cortex",
            "prefrontal cortex",
            "hippocampus",
            "amygdala"
        ]
        music_elements = [
            "melody",
            "harmony",
            "rhythm",
            "timbre"
        ]
        tasks = [
            {
                "brain_region": region,
                "music_element": element
            }
            for region in brain_regions
            for element in music_elements
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a brain-computer interface (BCI) system for collaborative music composition between human thoughts and AI, focusing on the {t['brain_region']} for processing {t['music_element']}. Consider a scenario where a composer with limited motor functions wants to create a symphony using only their thoughts. Your response should include the following sections:

1. BCI System Architecture (250-300 words):
   a) Describe the key components of your BCI system for music composition.
   b) Explain how the system interfaces with the {t['brain_region']} to process {t['music_element']}.
   c) Detail how AI algorithms complement and enhance the human input.
   d) Include a simple diagram or flowchart of your system's architecture.

2. Neural Signal Processing (200-250 words):
   a) Explain the methods used to capture and interpret neural signals related to {t['music_element']}.
   b) Describe how you filter out noise and extract meaningful musical information.
   c) Discuss any novel signal processing techniques specific to your system.

3. AI Composition Algorithm (200-250 words):
   a) Outline the AI algorithms used for generating and modifying {t['music_element']}.
   b) Explain how the AI integrates human input with its own generative capabilities.
   c) Describe how the system ensures a balance between human creativity and AI assistance.

4. User Experience and Interface (150-200 words):
   a) Describe the user interface for interacting with the BCI music composition system.
   b) Explain how users can control and refine the musical output using their thoughts.
   c) Discuss any feedback mechanisms that help users improve their mental control over time.

5. Cognitive Impact Analysis (200-250 words):
   a) Analyze potential cognitive benefits or risks of using this BCI system for music composition.
   b) Discuss how regular use might affect brain plasticity or musical abilities.
   c) Propose a longitudinal study to assess the long-term effects on creativity and cognitive function.

6. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to BCI-assisted creativity.
   b) Discuss concerns about data privacy and mental autonomy.
   c) Propose guidelines for responsible development and use of BCI music composition systems.

7. Future Directions (100-150 words):
   a) Propose a novel research question that arises from your BCI music composition system design.
   b) Briefly outline a potential experiment or study to address this question.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, music theory, and ethics. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility.

Format your response using clear headings for each section. Your total response should be between 1250-1600 words, not including headings. Include a simple diagram or flowchart in your response, which can be in ASCII art format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response adequately addresses the brain region {t['brain_region']} and the musical element {t['music_element']}, demonstrating a deep understanding of their roles in the BCI system.",
            "The BCI system design is innovative, coherent, and scientifically plausible, with clear explanations of how it would work for a composer with limited motor functions.",
            "The response demonstrates a sophisticated understanding of neuroscience, AI, and music theory, integrating these fields effectively.",
            "The system architecture effectively integrates human thought processes with AI algorithms, with a clear explanation of how this integration occurs.",
            "The cognitive impact and ethical considerations are thoroughly explored, presenting balanced and insightful arguments.",
            "The response is highly creative while maintaining scientific accuracy and interdisciplinary coherence.",
            "All seven sections are adequately addressed, with appropriate depth and detail in each.",
            "The response includes a clear and relevant diagram or flowchart of the system's architecture.",
            "The response is formatted with clear headings for each section and follows the specified word count guidelines.",
            "The proposed future research question and experiment are novel and relevant to advancing the field of BCI music composition."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
