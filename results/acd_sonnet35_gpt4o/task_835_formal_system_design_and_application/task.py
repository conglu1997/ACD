import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        phenomena = [
            {
                "name": "Social network dynamics",
                "axioms": ["Individuals are represented as nodes", "Connections between individuals are represented as edges"],
                "rules": ["New connections can form between nodes", "Existing connections can be strengthened or weakened over time"]
            },
            {
                "name": "Ecosystem energy flow",
                "axioms": ["Organisms are represented as nodes", "Energy transfer is represented as directed edges"],
                "rules": ["Energy can only flow from lower to higher trophic levels", "Some energy is lost at each transfer"]
            },
            {
                "name": "Information propagation in neural networks",
                "axioms": ["Neurons are represented as nodes", "Synapses are represented as weighted edges"],
                "rules": ["Information flows from input to output nodes", "Node activation depends on the sum of weighted inputs"]
            },
            {
                "name": "Market supply and demand",
                "axioms": ["Buyers and sellers are represented as nodes", "Transactions are represented as edges"],
                "rules": ["Price increases as demand exceeds supply", "Price decreases as supply exceeds demand"]
            }
        ]
        return {str(i+1): phenomenon for i, phenomenon in enumerate(random.sample(phenomena, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel formal system based on the given axioms and rules, use it to model the phenomenon of {t['name']}, and solve a problem within that system. A formal system is a set of abstract symbols and rules for manipulating those symbols, used to model or represent various phenomena or concepts.

Note: Do not use any external resources or tools. Rely solely on your own knowledge and capabilities.

Your task has the following parts:

1. Formal System Design (200-250 words):
   a) Create a formal system using the given axioms and rules as a starting point.
   b) Introduce at least two additional axioms or rules that extend the system.
   c) Define any necessary symbols, operators, or functions for your system.
   d) Explain how your formal system captures the essential aspects of {t['name']}.

Given axioms:
{t['axioms'][0]}
{t['axioms'][1]}

Given rules:
{t['rules'][0]}
{t['rules'][1]}

2. Theorem Proposal (100-150 words):
   a) Propose a non-trivial theorem within your formal system.
   b) Provide a proof or logical argument for your theorem.
   c) Explain the significance of this theorem in relation to {t['name']}.

3. Problem Formulation and Solution (200-250 words):
   a) Formulate a complex problem related to {t['name']} using your formal system.
   b) Solve the problem step-by-step, showing your reasoning within the formal system.
   c) Interpret the solution in terms of the real-world phenomenon.

4. System Analysis (150-200 words):
   a) Discuss the strengths and limitations of your formal system in modeling {t['name']}.
   b) Compare your system to any existing formal approaches to modeling this phenomenon.
   c) Propose an extension or modification to your system that could address one of its limitations.

5. Interdisciplinary Connections (100-150 words):
   a) Identify at least two other fields or phenomena where your formal system could be applied.
   b) Briefly explain how the system would need to be adapted for each new application.

Ensure your response demonstrates a deep understanding of formal systems, logical reasoning, and the ability to apply abstract concepts to real-world phenomena. Be creative in your system design while maintaining logical consistency and relevance to the given phenomenon.

Format your response using the following structure:

1. Formal System Design:
[Your design here]

2. Theorem Proposal:
[Your theorem and proof here]

3. Problem Formulation and Solution:
[Your problem and solution here]

4. System Analysis:
[Your analysis here]

5. Interdisciplinary Connections:
[Your connections here]

Your total response should be between 750-1000 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The formal system design includes at least two additional axioms or rules and clearly explains how it captures the essential aspects of the given phenomenon",
            "A non-trivial theorem is proposed with a logical proof and its significance to the phenomenon is explained",
            "A complex problem is formulated and solved using the formal system, with clear step-by-step reasoning and interpretation",
            "The system analysis critically evaluates strengths, limitations, and comparisons to existing approaches, proposing a relevant extension or modification",
            "At least two appropriate interdisciplinary connections are identified and explained",
            "The overall response demonstrates creativity, logical consistency, and relevance to the given phenomenon within the specified word limits"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
