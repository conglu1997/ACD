import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_principles = [
            "conceptual metaphor",
            "image schemas",
            "mental spaces",
            "cognitive grammar"
        ]
        computational_problems = [
            "sorting algorithm",
            "pathfinding in a graph",
            "pattern matching in strings",
            "matrix multiplication"
        ]
        return {
            "1": {"principle": random.choice(cognitive_principles), "problem": random.choice(computational_problems)},
            "2": {"principle": random.choice(cognitive_principles), "problem": random.choice(computational_problems)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a programming language based on the cognitive linguistics principle of {t['principle']}, then use it to solve the computational problem of {t['problem']}. Your response should include:

1. Language Design (250-300 words):
   a) Explain the chosen cognitive linguistics principle and its relevance to language processing.
   b) Describe the key features and syntax of your programming language, showing how they incorporate the cognitive principle.
   c) Provide examples of basic programming constructs (e.g., variables, loops, functions) in your language.
   d) Explain how your language might influence or reflect cognitive processes in programming.

2. Cognitive Analysis (200-250 words):
   a) Analyze how your language design might affect problem-solving approaches in programming.
   b) Discuss potential cognitive benefits or challenges for programmers using your language.
   c) Compare your language's cognitive aspects to those of existing programming paradigms (e.g., imperative, functional, object-oriented).

3. Problem Implementation (250-300 words):
   a) Present a solution to the given computational problem using your designed language.
   b) Explain your implementation, highlighting how it leverages the cognitive principle in your language design.
   c) Discuss any unique aspects of solving this problem in your language compared to traditional programming languages.

4. Code Snippet:
   Provide a small code snippet (10-15 lines) in your designed language that demonstrates a key aspect of the problem solution.

5. Evaluation (150-200 words):
   a) Assess the strengths and limitations of your language for solving the given problem.
   b) Propose a method for empirically testing the cognitive effects of programming in your language.
   c) Suggest potential applications or domains where your language might be particularly effective.

6. Reflection and Extension (150-200 words):
   a) Reflect on how this exercise provides insights into the relationship between language, cognition, and computation.
   b) Propose an extension or variation of your language that incorporates an additional cognitive linguistics principle.

Ensure your response demonstrates a deep understanding of cognitive linguistics, programming language design, and computer science concepts. Be creative in your language design while maintaining scientific and computational plausibility. Use appropriate terminology and provide clear explanations for complex concepts."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should clearly incorporate the cognitive linguistics principle of {t['principle']} into the programming language design.",
            f"The language should be used to solve the computational problem of {t['problem']}.",
            "The proposed language should be novel and creative while remaining computationally plausible.",
            "The response should demonstrate a deep understanding of cognitive linguistics, programming language design, and computer science concepts.",
            "All six requested sections should be present and adequately addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
