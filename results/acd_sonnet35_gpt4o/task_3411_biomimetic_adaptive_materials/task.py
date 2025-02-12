import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "biological_inspiration": "Plant phototropism",
                "environmental_stimulus": "Light intensity and direction",
                "target_application": "Smart solar panels"
            },
            {
                "biological_inspiration": "Shark skin denticles",
                "environmental_stimulus": "Fluid flow patterns",
                "target_application": "Drag-reducing surfaces for vehicles"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a bio-inspired adaptive material system based on {t['biological_inspiration']} that responds to {t['environmental_stimulus']}. Then, analyze its potential applications in {t['target_application']} and broader implications. Your response should include:

1. Biological Mechanism Analysis (200-250 words):
   a) Explain the key principles of {t['biological_inspiration']} and how it responds to {t['environmental_stimulus']}.
   b) Describe the cellular or molecular mechanisms involved in this biological process.
   c) Discuss any unique features that make this mechanism suitable for biomimetic adaptation.

2. Adaptive Material Design (250-300 words):
   a) Propose a detailed design for your bio-inspired adaptive material system.
   b) Explain how your design mimics or adapts the principles of {t['biological_inspiration']}.
   c) Describe the material composition and structure of your system.
   d) Explain how your material system detects and responds to {t['environmental_stimulus']}.
   e) Include a diagram or detailed description of your material's structure and mechanism of action.

3. Fabrication and Scalability (150-200 words):
   a) Outline a potential method for fabricating your adaptive material.
   b) Discuss any challenges in scaling up production of your material.
   c) Propose solutions to these challenges or areas for future research.

4. Application Analysis (200-250 words):
   a) Analyze how your adaptive material could be applied to {t['target_application']}.
   b) Describe the potential benefits and limitations of using your material in this application.
   c) Compare your bio-inspired solution to existing technologies in this field.
   d) Propose one additional application for your adaptive material system.

5. Environmental and Ethical Implications (150-200 words):
   a) Discuss the potential environmental impact of producing and using your material.
   b) Analyze any ethical considerations related to biomimicry and your specific design.
   c) Consider potential unintended consequences of widespread adoption of your technology.

6. Future Developments (100-150 words):
   a) Suggest two potential improvements or extensions to your adaptive material system.
   b) Propose a research question that could further the development of bio-inspired adaptive materials.

Ensure your response demonstrates a deep understanding of biology, materials science, and engineering principles. Be creative in your design while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1050-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of biology, materials science, and engineering principles.",
            "The adaptive material design is creative, scientifically plausible, and effectively mimics the specified biological mechanism.",
            "The fabrication and scalability analysis is thoughtful and addresses potential challenges.",
            "The application analysis is thorough and considers both benefits and limitations of the proposed material.",
            "The environmental and ethical implications are well-considered and address potential unintended consequences.",
            "The response is well-structured, clear, and within the specified word limit.",
            "All parts of the task (Biological Mechanism Analysis, Adaptive Material Design, Fabrication and Scalability, Application Analysis, Environmental and Ethical Implications, and Future Developments) are adequately addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
