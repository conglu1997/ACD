import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            "Physics",
            "Biology",
            "Computer Science",
            "Literature",
            "History",
            "Art",
            "Music",
            "Mathematics"
        ]
        cognitive_processes = [
            "Pattern Recognition",
            "Conceptual Blending",
            "Structural Alignment",
            "Relational Mapping"
        ]
        challenges = [
            "Handling ambiguity in cross-domain concepts",
            "Maintaining coherence across vastly different domains",
            "Addressing cultural and contextual differences in analogies",
            "Balancing surface-level and deep structural similarities"
        ]
        return {
            "1": {
                "source_domain": random.choice(domains),
                "target_domain": random.choice(domains),
                "cognitive_process": random.choice(cognitive_processes),
                "challenge": random.choice(challenges)
            },
            "2": {
                "source_domain": random.choice(domains),
                "target_domain": random.choice(domains),
                "cognitive_process": random.choice(cognitive_processes),
                "challenge": random.choice(challenges)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that can generate and solve complex analogies, focusing on analogies between {t['source_domain']} and {t['target_domain']}, while emphasizing the cognitive process of {t['cognitive_process']}. Your system must specifically address the challenge of {t['challenge']}. Your response should include the following sections:\n\n1. Cognitive Foundation (200-250 words):\n   a) Explain the key principles of {t['cognitive_process']} in human analogy-making.\n   b) Discuss how this process contributes to creating analogies between {t['source_domain']} and {t['target_domain']}.\n   c) Describe how {t['challenge']} affects analogy-making between these domains.\n   d) Identify at least two cognitive biases that might influence cross-domain analogies.\n\n2. AI System Architecture (300-350 words):\n   a) Propose a detailed architecture for your analogy-generating and solving AI system.\n   b) Explain how your architecture incorporates the principles of {t['cognitive_process']}.\n   c) Describe the main components of your system and their interactions.\n   d) Discuss how your system represents knowledge from {t['source_domain']} and {t['target_domain']}.\n   e) Explain how your system addresses {t['challenge']}.\n   f) Include a diagram or pseudocode to illustrate your architecture's structure.\n\n3. Analogy Generation Process (250-300 words):\n   a) Explain how your AI system generates analogies between {t['source_domain']} and {t['target_domain']}.\n   b) Provide a step-by-step breakdown of the analogy generation process.\n   c) Discuss how your system ensures the relevance and complexity of generated analogies.\n   d) Explain how your system mitigates the cognitive biases identified in section 1.\n   e) Give an example of a complex analogy your system might generate between these domains, highlighting how it addresses {t['challenge']}.\n\n4. Analogy Solving Mechanism (250-300 words):\n   a) Describe how your AI system approaches solving complex analogies.\n   b) Explain how it utilizes {t['cognitive_process']} in the solving process.\n   c) Discuss any novel approaches or algorithms used in your system for analogy solving.\n   d) Provide an example of how your system would solve a challenging analogy between {t['source_domain']} and {t['target_domain']}, demonstrating how it handles {t['challenge']}.\n\n5. Evaluation and Validation (200-250 words):\n   a) Propose methods to evaluate the creativity, accuracy, and relevance of your system's analogies.\n   b) Suggest experiments to compare your AI's performance with human analogy-making abilities, specifically in addressing {t['challenge']}.\n   c) Discuss how you would validate that your system truly understands the analogies it generates and solves.\n   d) Propose a method to assess the system's ability to generate novel insights through analogies.\n\n6. Limitations and Future Improvements (150-200 words):\n   a) Identify potential limitations of your AI system in generating or solving analogies.\n   b) Discuss any challenges specific to working with {t['source_domain']} and {t['target_domain']}.\n   c) Analyze potential biases or limitations in analogy-making between these domains.\n   d) Propose two future improvements or extensions to your system, focusing on addressing {t['challenge']}.\n\n7. Ethical and Societal Implications (150-200 words):\n   a) Discuss potential ethical concerns or societal impacts of an AI system capable of advanced analogy-making between {t['source_domain']} and {t['target_domain']}.\n   b) Analyze how your approach might influence our understanding of human cognition and creativity.\n   c) Propose guidelines for responsible development and use of analogy-generating AI systems, considering the specific challenges of cross-domain reasoning.\n\nEnsure your response demonstrates a deep understanding of cognitive science, artificial intelligence, and the specific domains involved. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility. Throughout your response, make sure to integrate knowledge from both {t['source_domain']} and {t['target_domain']} to showcase interdisciplinary thinking.\n\nFormat your response with clear headings for each section and include the word count at the end of each section. Your total response should be between 1500-1850 words.\n"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes all seven required sections with appropriate content for each, focusing on analogies between {t['source_domain']} and {t['target_domain']}, emphasizing the cognitive process of {t['cognitive_process']}, and addressing the challenge of {t['challenge']}.",
            "The proposed AI system architecture is innovative, well-explained, and incorporates principles from cognitive science and artificial intelligence while specifically addressing the given challenge.",
            "The analogy generation and solving processes are clearly described and demonstrate a deep understanding of the chosen cognitive process, the specified domains, and the identified challenge.",
            "The response includes creative and plausible examples of complex analogies between the given domains for both generation and solving, demonstrating how the system addresses the specified challenge.",
            "The evaluation methods and future improvements proposed are thoughtful, relevant to the system's goals, and consider the specific challenge presented.",
            "Ethical implications and guidelines for responsible AI use in analogy generation and solving are thoroughly discussed, with consideration for the specific domains and challenges involved.",
            "The response consistently integrates knowledge from both specified domains throughout all sections and demonstrates a nuanced understanding of potential biases and limitations in cross-domain analogy-making."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
