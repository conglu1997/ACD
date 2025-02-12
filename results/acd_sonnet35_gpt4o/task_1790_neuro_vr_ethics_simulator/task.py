import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "interface_type": "Non-invasive EEG headset",
                "vr_application": "Educational simulations",
                "ethical_focus": "Privacy and data security",
                "data_rate": "500 Hz",
                "spatial_resolution": "5 mm"
            },
            {
                "interface_type": "Invasive neural implant",
                "vr_application": "Therapeutic interventions",
                "ethical_focus": "Informed consent and autonomy",
                "data_rate": "10 kHz",
                "spatial_resolution": "0.1 mm"
            },
            {
                "interface_type": "Hybrid optical-electrical interface",
                "vr_application": "Enhanced social interactions",
                "ethical_focus": "Identity and authenticity",
                "data_rate": "2 kHz",
                "spatial_resolution": "1 mm"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical brain-computer interface (BCI) for immersive virtual reality experiences, focusing on a {t['interface_type']} for {t['vr_application']}. Then, analyze its ethical implications and potential societal impacts, with a particular emphasis on {t['ethical_focus']}. Your BCI should have a data rate of {t['data_rate']} and a spatial resolution of {t['spatial_resolution']}. Your response should include the following sections:

1. BCI System Design (300-350 words):
   a) Describe the key components and functioning of your {t['interface_type']}.
   b) Explain how it interfaces with the brain to create immersive VR experiences for {t['vr_application']}.
   c) Discuss any novel features or technologies incorporated into your design.
   d) Include a brief diagram or flowchart description of your BCI system.
   e) Explain how your system achieves the specified data rate and spatial resolution, and discuss the implications of these parameters.

2. Neuroscientific Principles (250-300 words):
   a) Explain the neuroscientific principles underlying your BCI design.
   b) Discuss how your system interacts with specific brain regions or neural processes.
   c) Address any potential neuroplasticity considerations or long-term effects on the brain.
   d) Provide a quantitative analysis of the neural signal processing requirements given the data rate and spatial resolution.

3. VR Experience Design (200-250 words):
   a) Describe the key features of the VR experiences enabled by your BCI for {t['vr_application']}.
   b) Explain how the BCI enhances immersion or functionality compared to traditional VR systems.
   c) Provide a specific example scenario of how your system would be used.
   d) Discuss how the data rate and spatial resolution affect the VR experience quality.

4. Ethical Analysis (250-300 words):
   a) Analyze the ethical implications of your BCI system, focusing on {t['ethical_focus']}.
   b) Discuss potential risks or misuses of the technology.
   c) Propose ethical guidelines or safeguards for the development and use of your BCI system.
   d) Consider the ethical implications of the high-resolution brain data collected by your system.

5. Societal Impact (200-250 words):
   a) Predict potential societal changes that could result from widespread adoption of your BCI system.
   b) Discuss how it might affect social interactions, education, or work environments.
   c) Consider any potential legal or regulatory challenges that might arise.
   d) Analyze the potential economic impact of your technology.

6. Future Developments and Challenges (150-200 words):
   a) Propose potential future advancements or iterations of your BCI system.
   b) Discuss technical or ethical challenges that need to be overcome.
   c) Suggest areas for further research or development.
   d) Predict how improvements in data rate and spatial resolution might affect future versions of your system.

Ensure your response demonstrates a deep understanding of neuroscience, virtual reality technology, and ethical reasoning. Use appropriate terminology and provide clear explanations for complex concepts. Be creative and innovative while maintaining scientific and ethical plausibility.

Format your response with clear headings for each section and use bullet points or numbered lists where appropriate. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['interface_type']} technology and its application in {t['vr_application']}",
            f"The ethical analysis thoroughly addresses the implications related to {t['ethical_focus']}",
            "The design is innovative yet scientifically plausible",
            "The societal impact analysis is comprehensive and well-reasoned",
            f"The response correctly incorporates the specified data rate of {t['data_rate']} and spatial resolution of {t['spatial_resolution']}",
            "The quantitative analysis of neural signal processing requirements is accurate and well-explained",
            "The response demonstrates interdisciplinary knowledge integration across neuroscience, VR technology, ethics, and societal impact analysis"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
