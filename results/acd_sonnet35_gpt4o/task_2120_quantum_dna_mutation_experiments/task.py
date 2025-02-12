import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = [
            "Quantum tunneling",
            "Quantum coherence",
            "Quantum entanglement",
            "Superposition"
        ]
        dna_processes = [
            "Base pair substitution",
            "Nucleotide excision repair",
            "Mismatch repair",
            "Double-strand break repair"
        ]
        research_applications = [
            "Cancer treatment",
            "Genetic disease prevention",
            "Evolutionary biology theories",
            "Synthetic biology"
        ]
        
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "quantum_effect": random.choice(quantum_effects),
                "dna_process": random.choice(dna_processes),
                "application": random.choice(research_applications)
            }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical experiment to investigate the role of {t['quantum_effect']} in the DNA process of {t['dna_process']}, and analyze its potential implications for {t['application']}. Your response should include:

1. Theoretical Framework (250-300 words):
   a) Explain the chosen quantum effect and its potential relevance to the specified DNA process.
   b) Describe the current understanding of the DNA process and where quantum effects might play a role.
   c) Propose a hypothesis for how the quantum effect could influence the DNA process.
   d) Cite at least two relevant scientific papers to support your theoretical framework.

2. Experimental Design (300-350 words):
   a) Outline a detailed experimental setup to test your hypothesis.
   b) Describe the equipment, techniques, and methodologies you would use.
   c) Explain how you would isolate and measure the quantum effect in the context of the DNA process.
   d) Discuss potential challenges in the experimental design and how you would address them.
   e) Provide a visual representation or diagram of your experimental setup (describe it textually).

3. Data Analysis and Interpretation (200-250 words):
   a) Describe the expected results if your hypothesis is correct.
   b) Explain how you would analyze the data to confirm or refute the presence of quantum effects.
   c) Discuss potential alternative explanations for your results and how you would rule them out.
   d) Cite at least one relevant paper on data analysis techniques in quantum biology.

4. Implications and Applications (200-250 words):
   a) Analyze the potential implications of your findings for the specified application area.
   b) Discuss how your results might influence current theories or practices in this field.
   c) Propose potential future research directions based on your findings.
   d) Cite at least one review paper discussing the implications of quantum effects in biology.

5. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to your research and its applications.
   b) Discuss how these ethical concerns might be addressed or mitigated.
   c) Propose guidelines for responsible conduct of research in this area.
   d) Reference at least one paper or guideline on ethics in advanced biological research.

Ensure your response demonstrates a deep understanding of both quantum mechanics and molecular biology. Use appropriate scientific terminology and provide clear explanations where necessary. Be creative and speculative in your approach while maintaining scientific plausibility and rigor.

Format your response with clear headings for each section. Your total response should be between 1100-1350 words. Include a word count at the end of your response.

Cite all references using APA format. Include a 'References' section at the end of your response (not counted in the word limit) with full citations for all papers mentioned."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both quantum mechanics and molecular biology",
            "The experimental design is well-thought-out, addresses potential challenges, and includes a clear description of a visual representation",
            "The implications and applications are thoroughly analyzed and supported by relevant citations",
            "Ethical considerations are thoughtfully discussed with reference to existing guidelines",
            "The response is creative and speculative while maintaining scientific plausibility",
            "The response includes appropriate citations throughout and a properly formatted References section",
            "The response adheres to the specified word count and formatting requirements"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
