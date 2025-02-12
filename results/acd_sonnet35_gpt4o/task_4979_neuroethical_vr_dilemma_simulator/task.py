import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        dilemmas = [
            {
                "name": "Autonomous Vehicle Dilemma",
                "description": "An autonomous vehicle must choose between swerving to hit a group of pedestrians or staying on course to hit a single pedestrian.",
                "brain_region": "prefrontal cortex"
            },
            {
                "name": "Medical Resource Allocation",
                "description": "A hospital must decide whether to allocate a limited life-saving resource to a young patient or an elderly patient with dependents.",
                "brain_region": "anterior cingulate cortex"
            }
        ]
        return {
            "1": random.choice(dilemmas),
            "2": random.choice(dilemmas)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a virtual reality system that simulates complex ethical dilemmas while monitoring and analyzing participants' neurological responses, then use this data to develop an AI model for predicting and understanding moral decision-making processes. Focus on the following ethical dilemma and brain region:

Dilemma: {t['name']}
{t['description']}
Brain Region of Interest: {t['brain_region']}

Your response should include the following sections:

1. VR Simulation Design (250-300 words):
   a) Describe the key components and features of your VR ethical dilemma simulator.
   b) Explain how you would create an immersive and realistic experience for the given dilemma.
   c) Discuss any novel VR techniques used to enhance the emotional impact and decision-making pressure.

2. Neurological Monitoring System (200-250 words):
   a) Describe the neuroimaging or monitoring technologies you would use.
   b) Explain how you would specifically track activity in the given brain region.
   c) Discuss any challenges in integrating this monitoring with the VR system and how you'd address them.

3. Data Collection and Analysis (200-250 words):
   a) Outline your approach to collecting and preprocessing neurological and behavioral data.
   b) Describe the key features or patterns you would look for in the data.
   c) Explain any novel data analysis techniques you would employ.

4. AI Model Development (250-300 words):
   a) Describe the architecture of your AI model for predicting moral decision-making.
   b) Explain how your model incorporates both neurological and behavioral data.
   c) Discuss how you would train and validate your model.
   d) Include a brief pseudocode snippet (5-10 lines) illustrating a key aspect of your model.

5. Ethical Considerations (200-250 words):
   a) Discuss potential ethical issues in using this system for research or other applications.
   b) Propose guidelines for responsible use of this technology.
   c) Explore potential societal implications of being able to predict moral decision-making.

6. Future Applications and Research Directions (150-200 words):
   a) Suggest two potential applications of your system beyond ethical research.
   b) Propose a follow-up study that builds on this technology.

Ensure your response demonstrates a deep understanding of virtual reality technology, neuroscience, ethical philosophy, and AI modeling. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.

Format your response with clear headings for each section and subsections labeled a, b, c, d as appropriate. Your total response should be between 1250-1550 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of virtual reality technology, neuroscience, ethical philosophy, and AI modeling.",
            "The proposed system is innovative and scientifically plausible.",
            "The response addresses all required sections and subsections comprehensively.",
            "The ethical considerations are thoughtfully explored and guidelines for responsible use are proposed.",
            "The response uses appropriate terminology from all relevant fields and provides clear explanations for complex concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
