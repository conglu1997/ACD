class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "biological_problem": "Detect and respond to environmental toxins",
                "host_organism": "Escherichia coli",
                "constraint": "Minimize metabolic burden on the host"
            },
            "2": {
                "biological_problem": "Regulate insulin production in response to glucose levels",
                "host_organism": "Saccharomyces cerevisiae",
                "constraint": "Ensure rapid response time (<5 minutes)"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a synthetic genetic circuit to {t['biological_problem']} in {t['host_organism']}, while adhering to the following constraint: {t['constraint']}. Your response should include:

1. Circuit Design (300-350 words):
   a) Describe the overall architecture of your genetic circuit.
   b) Explain the function of each genetic component (e.g., promoters, genes, regulatory elements).
   c) Provide a detailed diagram or schematic of your circuit, including all relevant genetic elements.
   d) Explain how your circuit addresses the specified biological problem and constraint.

2. Molecular Mechanisms (250-300 words):
   a) Describe the molecular interactions that enable your circuit to function.
   b) Explain how your circuit detects the relevant stimuli and produces the desired response.
   c) Discuss any feedback mechanisms or regulatory controls in your design.

3. Host Integration and Optimization (200-250 words):
   a) Explain how your circuit integrates with the host organism's existing systems.
   b) Describe any modifications needed to optimize the circuit for the chosen host.
   c) Discuss potential impacts on the host's fitness and strategies to mitigate negative effects.

4. Performance Analysis (200-250 words):
   a) Propose methods to quantitatively measure your circuit's performance.
   b) Describe expected behavior under different conditions or stimuli.
   c) Discuss potential failure modes and how you would address them.

5. Ethical and Biosafety Considerations (150-200 words):
   a) Identify potential ethical issues related to your genetic circuit.
   b) Discuss biosafety measures necessary for developing and implementing your design.
   c) Consider potential unintended consequences and how to mitigate them.

6. Future Improvements (100-150 words):
   a) Suggest two potential enhancements to your circuit for future development.
   b) Discuss how these improvements could expand the circuit's capabilities or applications.

Ensure your response demonstrates a deep understanding of synthetic biology, genetic engineering principles, and systems biology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of synthetic biology, genetic engineering, and systems biology principles.",
            f"The genetic circuit design effectively addresses the specified biological problem: {t['biological_problem']}.",
            f"The design is optimized for the given host organism: {t['host_organism']}.",
            f"The circuit design adheres to the specified constraint: {t['constraint']}.",
            "The response includes a clear and detailed diagram or schematic of the genetic circuit.",
            "The analysis of ethical and biosafety considerations is thorough and well-reasoned.",
            "The response is innovative while maintaining scientific plausibility.",
            "The response adheres to the specified word count guidelines for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
