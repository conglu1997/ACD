import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = [
            "quantum coherence",
            "quantum entanglement",
            "quantum tunneling"
        ]
        biological_processes = [
            "light harvesting",
            "electron transport",
            "energy transfer"
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "quantum_effect": random.choice(quantum_effects),
                "biological_process": random.choice(biological_processes)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum biological system that enhances photosynthetic efficiency through quantum information processing, focusing on the quantum effect of {t['quantum_effect']} in the biological process of {t['biological_process']}. Your response should include:

1. System Design (300-350 words):
   a) Describe the key components of your quantum biological system.
   b) Explain how it incorporates the specified quantum effect.
   c) Detail how the system enhances the given biological process.
   d) Provide a diagram or schematic representation of your system. (Describe this in words, as if you were explaining a visual representation)

2. Quantum Analysis (250-300 words):
   a) Analyze how quantum information is processed in your system.
   b) Explain any quantum advantages or phenomena that arise.
   c) Discuss how classical models would be insufficient to describe your system.

3. Biological Implications (250-300 words):
   a) Explore how your system could impact overall photosynthetic efficiency.
   b) Discuss potential evolutionary implications of such a system.
   c) Compare your system to known natural photosynthetic processes.

4. Information Theory Application (200-250 words):
   a) Apply information theory concepts to analyze your quantum biological system.
   b) Propose a novel metric for quantifying quantum information in biological processes.
   c) Discuss how information flow in your system differs from classical biological systems.

5. Experimental Approach (250-300 words):
   a) Propose an experimental setup to test or validate your quantum biological system.
   b) Discuss the technical challenges and limitations of implementing such an experiment.
   c) Suggest how advances in quantum technologies might enable future testing of your ideas.

6. Broader Implications (150-200 words):
   a) Discuss potential applications of your quantum biological system beyond photosynthesis.
   b) Explore how your ideas might impact our understanding of quantum effects in other biological processes.
   c) Consider any ethical implications or potential risks associated with engineering quantum biological systems.

Ensure your response demonstrates a deep understanding of quantum mechanics, biology, and information theory. Use appropriate terminology and provide clear explanations for complex concepts. Be creative and original in your approach while maintaining scientific rigor.

Cite at least three relevant scientific papers or sources to support your design and analysis. Include these citations in-text and provide a brief reference list at the end of your response.

Format your response with clear headings for each section, numbered subsections, and a brief conclusion summarizing the key points of your design and its potential impact. Your total response should be between 1400-1700 words, excluding references."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed design of a quantum biological system specifically incorporating {t['quantum_effect']} in the process of {t['biological_process']}",
            "The response provides a thorough quantum analysis of the system, explaining quantum advantages and limitations of classical models",
            "The response discusses biological implications, including impacts on photosynthetic efficiency and evolutionary considerations",
            "The response applies information theory concepts to the quantum biological system and proposes a novel metric for quantifying quantum information",
            "The response proposes a specific experimental approach to test the system, including technical challenges and potential future advancements",
            "The response explores broader implications and potential applications beyond photosynthesis",
            "The response demonstrates a deep understanding of quantum mechanics, biology, and information theory, using appropriate terminology",
            "The response includes at least three relevant scientific citations and a brief reference list",
            "The response is well-structured with clear headings, numbered subsections, and falls within the specified word count range"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
