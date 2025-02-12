import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        artifact_types = [
            {
                'type': 'Ancient pottery',
                'challenge': 'Fragile structure and surface degradation'
            },
            {
                'type': 'Medieval manuscript',
                'challenge': 'Ink fading and paper deterioration'
            }
        ]
        nano_techniques = [
            {
                'technique': 'Self-assembling nanocoatings',
                'description': 'Protective layers that form autonomously at the molecular level'
            },
            {
                'technique': 'Nanorobotic restoration',
                'description': 'Microscopic robots that repair damage at the cellular level'
            }
        ]
        ethical_concerns = [
            {
                'concern': 'Authenticity',
                'description': 'Ensuring nano-preservation doesn\'t alter the original nature of artifacts'
            },
            {
                'concern': 'Access equity',
                'description': 'Addressing disparities in access to advanced preservation technologies'
            }
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                'artifact': random.choice(artifact_types),
                'nanotechnique': random.choice(nano_techniques),
                'ethical_issue': random.choice(ethical_concerns)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a nanotechnology-based system for preserving and studying archaeological artifacts, focusing on {t['artifact']['type']} and addressing the challenge of {t['artifact']['challenge']}. Your system should incorporate the nanotechnology technique of {t['nanotechnique']['technique']} ({t['nanotechnique']['description']}). Then, analyze its potential impact on historical research and cultural heritage preservation, particularly addressing the ethical concern of {t['ethical_issue']['concern']} ({t['ethical_issue']['description']}). Your response should include:

1. System Design (300-350 words):
   a) Describe the key components and processes of your nanoarchaeology preservation system.
   b) Explain how it addresses the specific challenges associated with {t['artifact']['type']}.
   c) Detail how your system incorporates {t['nanotechnique']['technique']} and why this technique is particularly suitable.
   d) Discuss any novel elements in your design that enable more effective preservation or study of artifacts.
   e) Include a diagram or flowchart of your system's architecture (describe it textually).

2. Nanotechnology-Archaeology Interface (200-250 words):
   a) Explain how your system bridges nanotechnology with traditional archaeological methods.
   b) Discuss potential challenges in applying nanotechnology to archaeological artifacts and how your system addresses them.
   c) Describe how your system might reveal new information about artifacts that traditional methods cannot access.

3. Preservation and Analysis Process (250-300 words):
   a) Provide a step-by-step explanation of how an artifact would be processed and preserved using your system.
   b) Describe how your system allows for ongoing study and analysis of the artifact post-preservation.
   c) Explain how your system ensures the long-term stability and integrity of the preserved artifact.
   d) Discuss any limitations or potential risks associated with your preservation method.

4. Historical Research Impact (200-250 words):
   a) Analyze how your nanoarchaeology system could advance our understanding of past civilizations.
   b) Provide specific examples of research questions that could be answered using your system.
   c) Discuss how your system might change archaeological fieldwork and laboratory practices.

5. Cultural Heritage Implications (200-250 words):
   a) Examine the potential impact of your system on cultural heritage preservation efforts.
   b) Discuss how it might affect museum exhibitions and public engagement with historical artifacts.
   c) Address any cultural or religious sensitivities that might arise from using nanotechnology on sacred or culturally significant objects.

6. Ethical Analysis (200-250 words):
   a) Analyze the ethical implications of your system, focusing on {t['ethical_issue']['concern']}.
   b) Discuss how your system might exacerbate or mitigate this ethical concern.
   c) Propose guidelines or safeguards to ensure the ethical use of nanotechnology in archaeology.
   d) Consider any potential unintended consequences of widespread adoption of your system.

7. Future Developments (150-200 words):
   a) Suggest potential enhancements or extensions to your nanoarchaeology preservation system.
   b) Propose a specific experiment or case study to further validate your system's effectiveness.
   c) Speculate on how this technology might influence the field of archaeology in the next few decades.

Ensure your response demonstrates a deep understanding of nanotechnology, archaeology, and materials science. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The System Design effectively incorporates {t['nanotechnique']['technique']} and addresses the challenges of preserving {t['artifact']['type']}.",
            "The Nanotechnology-Archaeology Interface demonstrates a deep understanding of both fields and their potential synergies.",
            "The Preservation and Analysis Process provides a clear and scientifically plausible methodology.",
            "The Historical Research Impact analysis offers compelling examples of how the system could advance archaeological knowledge.",
            "The Cultural Heritage Implications section thoughtfully considers the broader impacts on society and culture.",
            f"The Ethical Analysis thoroughly addresses the concern of {t['ethical_issue']['concern']} and proposes meaningful guidelines.",
            "The Future Developments section offers innovative and relevant ideas for advancing the technology.",
            "The response demonstrates interdisciplinary knowledge integration and creative problem-solving throughout.",
            "The ideas presented are scientifically plausible and well-explained.",
            "The response follows the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
