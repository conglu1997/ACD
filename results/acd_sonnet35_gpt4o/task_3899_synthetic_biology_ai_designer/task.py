import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environmental_issues = [
            'oil spill cleanup',
            'heavy metal contamination',
            'plastic pollution',
            'atmospheric carbon dioxide reduction'
        ]
        organism_types = [
            'bacteria',
            'algae',
            'fungi',
            'synthetic hybrid'
        ]
        tasks = [
            {
                'environmental_issue': random.choice(environmental_issues),
                'organism_type': random.choice(organism_types)
            },
            {
                'environmental_issue': random.choice(environmental_issues),
                'organism_type': random.choice(organism_types)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of creating and optimizing synthetic organisms for environmental remediation, focusing on {t['environmental_issue']} using {t['organism_type']}. Then, analyze its output and propose experiments to validate its designs. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for synthetic biology design.
   b) Explain how it integrates knowledge from biology, genetics, and environmental science.
   c) Detail the mechanisms for designing and optimizing synthetic organisms.
   d) Include a simple diagram or flowchart of your system architecture using ASCII art or Unicode characters.

2. Organism Design Process (200-250 words):
   a) Explain the steps your system takes to design synthetic organisms for {t['environmental_issue']}.
   b) Describe how your system ensures the viability and safety of the designed organisms.
   c) Discuss how your system optimizes the organisms for efficiency in their intended function.

3. Environmental Impact Analysis (200-250 words):
   a) Detail how your AI system predicts and analyzes the potential environmental impact of the designed organisms.
   b) Explain how it balances remediation efficiency with ecological safety.
   c) Describe any built-in safeguards or control mechanisms in the organism designs.

4. Output Analysis (200-250 words):
   a) Provide a detailed example of a synthetic {t['organism_type']} your system might design for {t['environmental_issue']}.
   b) Analyze its predicted effectiveness and potential limitations.
   c) Discuss any novel or unexpected features in the organism design.

5. Validation Experiments (200-250 words):
   a) Propose a series of experiments to validate the safety and efficacy of the designed organism.
   b) Describe the methodology, including containment procedures and measurement techniques.
   c) Explain how you would assess both the remediation effectiveness and ecological impact.

6. Ethical Considerations (150-200 words):
   a) Discuss the ethical implications of using AI-designed synthetic organisms for environmental remediation.
   b) Address concerns about unintended ecological consequences.
   c) Propose guidelines for responsible development and deployment of such organisms.

7. Future Directions (100-150 words):
   a) Suggest two potential improvements or extensions to your AI system.
   b) Propose a research question that could further explore the intersection of AI, synthetic biology, and environmental science.

Ensure your response demonstrates a deep understanding of synthetic biology, environmental science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your answer with clear headings for each section, numbered as above. Your total response should be between 1300-1650 words.

For the system architecture diagram, use ASCII art or Unicode characters to create a clear and informative representation. The diagram should be no larger than 20 lines by 80 characters."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of synthetic biology, environmental science, and artificial intelligence.",
            "The AI system design is innovative, plausible, and well-explained, integrating concepts from multiple disciplines.",
            "The organism design process and environmental impact analysis are thorough and scientifically sound.",
            "The proposed validation experiments are well-designed and address both efficacy and safety concerns.",
            "The response adequately addresses ethical considerations and future directions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
