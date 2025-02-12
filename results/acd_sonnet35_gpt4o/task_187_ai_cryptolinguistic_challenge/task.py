import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "scenario": "Secure AI-to-AI communication in a multi-agent system",
                "constraints": [
                    "Must be resistant to quantum computing attacks",
                    "Should incorporate elements of natural language to improve AI comprehension",
                    "Must have a mechanism for evolving the encryption over time"
                ],
                "puzzle": "Decrypt the following message encoded in your system: [PLACEHOLDER]"
            },
            {
                "scenario": "Steganographic communication between AI agents in a public forum",
                "constraints": [
                    "Must hide messages within seemingly normal text",
                    "Should be adaptable to different languages and writing styles",
                    "Must include a method for verifying message authenticity"
                ],
                "puzzle": "Encode the following message using your system: [PLACEHOLDER]"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a cryptolinguistic system for {t['scenario']} with the following constraints:\n\n" + \
               "\n".join(f"- {constraint}" for constraint in t['constraints']) + \
               f"\n\nProvide your response in the following format:\n\n" + \
               "1. System Overview (3-4 sentences)\n" + \
               "2. Encryption Method (3-4 sentences)\n" + \
               "3. Decryption Process (2-3 sentences)\n" + \
               "4. Security Analysis (3-4 sentences)\n" + \
               "5. AI Comprehension Features (2-3 sentences)\n" + \
               "6. Evolution Mechanism (2-3 sentences)\n" + \
               f"7. {t['puzzle']}\n\n" + \
               "Ensure your cryptolinguistic system is innovative, addresses all given constraints, and demonstrates a deep understanding of linguistics, cryptography, and AI language models."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The cryptolinguistic system is innovative and unique, while being theoretically feasible.",
            "The system effectively addresses all given constraints.",
            "The response demonstrates a strong understanding of linguistics, cryptography, and AI language models.",
            "The encryption and decryption methods are well-explained and logically consistent.",
            "The security analysis is thorough and considers potential vulnerabilities.",
            "The AI comprehension features are well-integrated and enhance the system's effectiveness.",
            "The evolution mechanism is clearly explained and provides long-term security benefits.",
            "The puzzle solution (encoding or decoding) is correct and consistent with the described system."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
