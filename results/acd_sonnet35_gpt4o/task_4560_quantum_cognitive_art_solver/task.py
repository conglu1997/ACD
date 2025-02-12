import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = ['superposition', 'entanglement', 'interference']
        cognitive_processes = ['divergent thinking', 'conceptual blending', 'analogical reasoning']
        art_styles = ['abstract expressionism', 'surrealism', 'minimalism']
        artistic_challenges = ['expressing complex emotions', 'visualizing scientific concepts', 'creating optical illusions']
        
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "cognitive_process": random.choice(cognitive_processes),
                "art_style": random.choice(art_styles),
                "artistic_challenge": random.choice(artistic_challenges)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "cognitive_process": random.choice(cognitive_processes),
                "art_style": random.choice(art_styles),
                "artistic_challenge": random.choice(artistic_challenges)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired cognitive model for creative problem-solving in visual arts, focusing on the quantum principle of {t['quantum_principle']}, the cognitive process of {t['cognitive_process']}, and the art style of {t['art_style']}. Then, apply your model to analyze and generate solutions for the artistic challenge of {t['artistic_challenge']}. Your response should include:

1. Quantum-Cognitive Model (300-350 words):
   a) Explain how your model incorporates the quantum principle and cognitive process.
   b) Describe how it simulates creative thinking in the context of visual arts.
   c) Detail any novel algorithms or techniques used in your model.
   d) Provide a diagram or pseudocode (in text format) illustrating a key aspect of your model.

2. Artistic Style Integration (200-250 words):
   a) Explain how your model incorporates principles from the given art style.
   b) Discuss how the quantum-cognitive approach enhances or reinterprets this style.
   c) Provide an example of how your model might generate a novel artistic technique within this style.

3. Problem Analysis (200-250 words):
   a) Analyze the given artistic challenge using your quantum-cognitive model.
   b) Explain how the model breaks down the challenge into quantum-inspired components.
   c) Describe the cognitive processes your model simulates to approach the challenge.

4. Solution Generation (250-300 words):
   a) Detail how your model generates potential solutions to the artistic challenge.
   b) Provide at least two distinct solution concepts derived from your model.
   c) Explain how these solutions incorporate aspects of the quantum principle, cognitive process, and art style.
   d) Describe how an artist might interpret and implement these solution concepts.

5. Comparative Analysis (150-200 words):
   a) Compare your quantum-cognitive approach to traditional methods of artistic problem-solving.
   b) Discuss potential advantages and limitations of your model.
   c) Explain how your approach might lead to novel artistic discoveries or techniques.

6. Ethical and Philosophical Implications (150-200 words):
   a) Discuss the potential impact of quantum-cognitive models on the nature of creativity and artistic expression.
   b) Consider ethical implications of using AI-generated solutions in art.
   c) Explore how this technology might influence our understanding of consciousness and creative cognition.

Ensure your response demonstrates a deep understanding of quantum principles, cognitive science, and art theory. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and artistic plausibility.

Cite relevant sources or provide specific examples to support your arguments where appropriate. This will help demonstrate the depth of your understanding and the validity of your proposed model.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words.

Note on scoring: Your response will be evaluated based on how effectively you address all the points mentioned above. To receive a full score, you must meet all the evaluation criteria. These include incorporating the given quantum principle, cognitive process, and art style in your model design, applying the model to the artistic challenge, providing clear and consistent explanations, demonstrating creativity in your solutions, and offering thoughtful comparative analysis and ethical discussion."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively incorporates the quantum principle of {t['quantum_principle']}, the cognitive process of {t['cognitive_process']}, and the art style of {t['art_style']} in the model design.",
            f"The model is applied to analyze and generate solutions for the artistic challenge of {t['artistic_challenge']}.",
            "The quantum-cognitive model for creative problem-solving is clearly explained and logically consistent.",
            "The response demonstrates a deep understanding of quantum principles, cognitive science, and art theory.",
            "The solution generation process and example solutions are creative and well-aligned with the model's principles.",
            "The comparative analysis and ethical implications are thoughtfully discussed.",
            "The overall response is innovative while maintaining scientific and artistic plausibility.",
            "Relevant sources are cited or specific examples are provided to support arguments."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
