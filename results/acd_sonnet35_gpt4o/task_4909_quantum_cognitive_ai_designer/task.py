import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            {
                "domain": "Climate change prediction",
                "cognitive_process": "Decision making under uncertainty"
            },
            {
                "domain": "Language translation",
                "cognitive_process": "Semantic understanding"
            },
            {
                "domain": "Drug discovery",
                "cognitive_process": "Pattern recognition"
            },
            {
                "domain": "Financial market analysis",
                "cognitive_process": "Complex system modeling"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(domains, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that leverages principles of quantum computing to model and enhance cognitive processes, then apply it to solve a complex problem in {t['domain']}. Your system should focus on enhancing the cognitive process of {t['cognitive_process']}. Your response should include:

1. Quantum-Cognitive Framework (300-350 words):
   a) Explain how your AI system integrates quantum computing principles with cognitive modeling.
   b) Describe the key quantum algorithms or techniques used in your system.
   c) Discuss how quantum principles enhance the modeling of {t['cognitive_process']}.
   d) Explain any novel approaches in your design that go beyond classical AI systems.

2. System Architecture (250-300 words):
   a) Provide an overview of your AI system's architecture.
   b) Explain how quantum and classical components interact in your system.
   c) Describe how your system processes information and makes decisions.
   d) Include a diagram or flowchart of your system architecture (describe it textually).

3. Cognitive Enhancement Mechanism (250-300 words):
   a) Detail how your system enhances {t['cognitive_process']}.
   b) Explain the advantages of your quantum-cognitive approach over classical methods.
   c) Discuss potential limitations or challenges in implementing this enhancement.

4. Application to {t['domain']} (300-350 words):
   a) Describe a specific problem in {t['domain']} that your system would address.
   b) Explain how your system would approach solving this problem.
   c) Discuss the potential impact of your system on {t['domain']}.
   d) Provide a hypothetical example of your system's output or decision-making process.

5. Ethical Considerations and Societal Impact (200-250 words):
   a) Discuss potential ethical implications of using quantum-cognitive AI in {t['domain']}.
   b) Address concerns about the 'black box' nature of quantum systems and explainability.
   c) Analyze possible societal impacts, both positive and negative, of widespread adoption.

6. Future Developments and Challenges (200-250 words):
   a) Identify key technical challenges in realizing your proposed system.
   b) Suggest areas for future research in quantum-cognitive AI.
   c) Discuss how advancements in quantum hardware might impact your system's capabilities.

7. Comparative Analysis (150-200 words):
   a) Compare your quantum-cognitive approach to current state-of-the-art classical AI systems in {t['domain']}.
   b) Discuss potential synergies between quantum and classical AI approaches.

Ensure your response demonstrates a deep understanding of quantum computing, cognitive science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1650-2000 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address the application of quantum-cognitive AI to {t['domain']}",
            f"The system design should demonstrate integration of quantum computing principles and {t['cognitive_process']}",
            "The response should include a detailed analysis of the system architecture and cognitive enhancement mechanisms",
            "The proposed application should be innovative and scientifically plausible",
            "The response should demonstrate a deep understanding of quantum computing, cognitive science, and AI"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
