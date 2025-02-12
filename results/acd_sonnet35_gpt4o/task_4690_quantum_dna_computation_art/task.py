import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        art_styles = [
            "Cubism",
            "Surrealism"
        ]
        optimization_problems = [
            "Color harmony optimization using complementary DNA base pairs",
            "Geometric pattern optimization based on DNA helical structures"
        ]
        return {
            str(i+1): {
                'art_style': style,
                'optimization_problem': problem
            } for i, (style, problem) in enumerate(zip(art_styles, optimization_problems))
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system that uses DNA-based qubits to generate and analyze abstract art in the style of {t['art_style']}, then use it to solve the complex optimization problem of {t['optimization_problem']} in artistic style transfer. Your response should include the following sections:

1. Quantum DNA Computing System Architecture (300-350 words):
   a) Describe the key components of your quantum DNA computing system for art generation and analysis.
   b) Explain how DNA-based qubits are implemented using specific nucleotide sequences and how they are manipulated in your system.
   c) Detail how quantum operations (e.g., superposition, entanglement) are performed on these DNA qubits.
   d) Discuss how your system integrates quantum computing with artistic style generation.
   e) Include a high-level diagram or pseudocode representing your system's architecture (described in words).

2. DNA-Qubit Art Generation Process (250-300 words):
   a) Explain the step-by-step process of generating abstract art using your DNA-qubit system.
   b) Describe how quantum superposition and entanglement are utilized in the art creation process.
   c) Detail how your system ensures the generated art adheres to the principles of {t['art_style']}.
   d) Discuss any novel quantum algorithms developed for this artistic application.
   e) Provide a brief description or example of the type of art your system would generate.

3. Quantum Art Analysis (200-250 words):
   a) Describe how your system analyzes the generated art using quantum computing principles.
   b) Explain how this analysis differs from classical computer vision techniques.
   c) Discuss how quantum analysis could provide insights not possible with classical methods.

4. Optimization Problem Solution (250-300 words):
   a) Detail your approach to solving the {t['optimization_problem']} problem using your quantum DNA art system.
   b) Explain how quantum computing provides an advantage in this optimization task.
   c) Describe the expected output or result of this optimization process.
   d) Discuss any challenges specific to this optimization problem and how your system addresses them.

5. Practical Implementation and Challenges (200-250 words):
   a) Identify key technical challenges in implementing your system with current technology.
   b) Propose potential solutions or workarounds for these challenges.
   c) Discuss the scalability of your approach as quantum and DNA computing technologies advance.

6. Ethical and Artistic Implications (150-200 words):
   a) Analyze potential ethical concerns related to using quantum DNA computing for art creation.
   b) Discuss how this technology might impact the art world and human artists.
   c) Consider the question of authorship and creativity in quantum-generated art.

7. Future Applications and Extensions (150-200 words):
   a) Suggest two potential applications of your quantum DNA art system beyond abstract art generation.
   b) Propose an experiment to further explore the capabilities of your system.
   c) Speculate on how this technology might evolve in the next decade.

Ensure your response demonstrates a deep understanding of quantum computing, DNA manipulation, and art theory. Use appropriate technical terminology from all relevant fields and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of quantum computing principles, DNA-based qubits (including specific nucleotide sequences), and their application to art generation and analysis in the style of {t['art_style']}",
            f"The system architecture and art generation process are well-explained, scientifically plausible, and include a brief description or example of the generated art",
            f"The approach to solving the {t['optimization_problem']} problem using the quantum DNA art system is innovative, well-reasoned, and clearly explains the quantum advantage",
            "The submission addresses practical implementation challenges and ethical implications thoughtfully",
            "The response showcases interdisciplinary knowledge integration and creative problem-solving throughout all sections",
            "The proposed future applications and extensions are innovative and demonstrate a deep understanding of the technology's potential"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
