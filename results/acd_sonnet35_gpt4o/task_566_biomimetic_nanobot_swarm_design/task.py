import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'biological_system': 'Ant colonies',
                'target_application': 'Environmental cleanup',
                'ethical_concern': 'Unintended ecological impact'
            },
            {
                'biological_system': 'Immune system',
                'target_application': 'Targeted drug delivery',
                'ethical_concern': 'Privacy and bodily autonomy'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""In the rapidly evolving field of nanotechnology, biomimicry offers innovative solutions to complex challenges. Your task is to design a swarm of nanobots inspired by the biological system of {t['biological_system']}, targeting the application of {t['target_application']}. Then, analyze the potential implications of this technology, with a focus on the ethical concern of {t['ethical_concern']}.

Your response should include:

1. Biomimetic Design (250-300 words):
   a) Describe the key features of the chosen biological system relevant to swarm behavior.
   b) Explain how these features are translated into the nanobot swarm design.
   c) Provide a schematic or detailed description of an individual nanobot in your swarm.
   d) Describe how the swarm communicates and coordinates its actions.

2. Functional Mechanisms (200-250 words):
   a) Explain the primary mechanisms by which the nanobot swarm operates.
   b) Describe how these mechanisms enable the swarm to perform its target application.
   c) Discuss any novel capabilities that emerge from the swarm behavior.
   d) Provide at least one quantitative example or calculation to demonstrate a key aspect of the swarm's functionality.

3. Target Application Analysis (200-250 words):
   a) Provide a detailed explanation of how the nanobot swarm would be used in the target application.
   b) Discuss the potential advantages of this approach compared to existing solutions.
   c) Identify any technical challenges that would need to be overcome.
   d) Propose a specific scenario or case study where your nanobot swarm would be particularly effective.

4. Ethical Implications (200-250 words):
   a) Analyze the specified ethical concern in depth.
   b) Discuss any additional ethical considerations that might arise from this technology.
   c) Propose guidelines or safeguards to address these ethical issues.
   d) Provide a balanced argument considering both the potential benefits and risks of the technology.

5. Broader Impacts (150-200 words):
   a) Speculate on how this technology might affect society, industry, or scientific research.
   b) Discuss any potential dual-use concerns or unintended consequences.
   c) Propose two potential spin-off applications or research directions.

6. Technical Challenges and Future Development (150-200 words):
   a) Identify the main technical hurdles in developing and deploying this nanobot swarm.
   b) Suggest approaches to overcome these challenges.
   c) Outline a roadmap for future development and testing of the technology.
   d) Propose a specific experiment or trial to validate a key aspect of your nanobot swarm design.

Ensure your response demonstrates a deep understanding of both the biological system and nanotechnology principles. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility.

Format your response with clear headings for each section and subsections labeled a, b, c, d as appropriate. Your total response should be between 1200-1500 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified biological system and its relevance to swarm behavior, with clear explanations of key features.",
            "The nanobot swarm design clearly incorporates biomimetic principles derived from the given biological system, with a detailed description or schematic of an individual nanobot.",
            "The functional mechanisms of the nanobot swarm are well-explained, scientifically plausible, and include at least one quantitative example or calculation.",
            "The target application analysis is thorough, considers both advantages and challenges, and includes a specific scenario or case study.",
            "The ethical implications, including the specified concern, are analyzed in depth with thoughtful guidelines proposed and a balanced argument presented.",
            "The broader impacts of the technology are considered, including potential unintended consequences and specific spin-off applications.",
            "Technical challenges are identified and addressed with plausible approaches for future development, including a proposed experiment or trial.",
            "The response demonstrates creativity and innovation while maintaining scientific plausibility throughout all sections.",
            "The submission effectively synthesizes knowledge from biology, engineering, and nanotechnology, using appropriate technical terminology.",
            "The response is well-structured, following the specified format with clear headings and subsections, and adheres to the 1200-1500 word count guideline."
        ]
        score = sum(1 for criterion in criteria if eval_with_llm_judge(instructions, submission, [criterion])) / len(criteria)
        return score
