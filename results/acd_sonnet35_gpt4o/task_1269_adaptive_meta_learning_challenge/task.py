import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            "mathematics",
            "logic",
            "linguistics",
            "computer science",
            "physics",
            "biology",
            "psychology",
            "economics"
        ]
        
        complexity_levels = [1, 2, 3]
        
        tasks = {}
        for i in range(1, 3):
            selected_domains = random.sample(domains, 3)
            tasks[str(i)] = {
                "domains": selected_domains,
                "complexity_levels": complexity_levels
            }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        problem_examples = {
            "mathematics": ["Solve: 2x + 3 = 7", "Find the derivative of f(x) = x^3 + 2x", "Prove the Pythagorean theorem"],
            "logic": ["If A implies B, and B implies C, what can we conclude?", "Construct a truth table for (P ∨ Q) ∧ ¬R", "Prove the validity of modus ponens using natural deduction"],
            "linguistics": ["Identify the subject and predicate in 'The cat sat on the mat'", "Explain the difference between descriptive and prescriptive grammar", "Analyze the syntactic structure of 'The old man the boat'"],
            "computer science": ["Write a function to check if a number is prime", "Implement a binary search algorithm", "Design a neural network architecture for image classification"],
            "physics": ["Calculate the force of gravity between two objects", "Derive the equation for the period of a simple pendulum", "Explain the concept of quantum entanglement"],
            "biology": ["Describe the process of mitosis", "Explain the central dogma of molecular biology", "Analyze the evolutionary implications of punctuated equilibrium"],
            "psychology": ["Define classical conditioning", "Explain the difference between short-term and long-term memory", "Critique Freud's psychoanalytic theory"],
            "economics": ["Define supply and demand", "Explain the concept of opportunity cost", "Analyze the effects of quantitative easing on inflation"]
        }

        instructions = f"""You are participating in an Adaptive Meta-Learning Challenge. Your task is to solve a series of increasingly complex problems across three diverse domains: {', '.join(t['domains'])}. Each domain will present problems at three levels of complexity. Your goal is to demonstrate adaptive learning by applying strategies from earlier problems to solve later, more complex ones.

Instructions:
1. For each domain, you will be presented with three problems of increasing complexity (levels 1-3).
2. Solve each problem to the best of your ability.
3. After solving each problem, briefly explain your problem-solving approach and any strategies you used.
4. As you progress, try to identify patterns or strategies that can be applied across different domains or complexity levels.
5. For the final problem in each domain, explain how you adapted strategies from earlier problems or other domains to solve it.

Here are examples of the types of problems you might encounter for each domain and complexity level:

"""

        for domain in t['domains']:
            instructions += f"{domain.capitalize()}:\n"
            for i, example in enumerate(problem_examples[domain], 1):
                instructions += f"Level {i}: {example}\n"
            instructions += "\n"

        instructions += """Provide your response in the following format for each domain:

[Domain Name]
Problem 1 (Level 1):
[Your solution]
Explanation: [Your problem-solving approach and strategies]

Problem 2 (Level 2):
[Your solution]
Explanation: [Your problem-solving approach and strategies]

Problem 3 (Level 3):
[Your solution]
Explanation: [Your problem-solving approach and strategies, including how you adapted strategies from earlier problems or other domains]

Remember, the key to success in this challenge is not just solving individual problems, but demonstrating your ability to learn, adapt, and transfer knowledge across diverse domains and complexity levels.

Are you ready to begin the challenge?"""

        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes solutions and explanations for all three complexity levels in each of the three domains: {', '.join(t['domains'])}.",
            "The solutions demonstrate increasing complexity and depth of understanding across the three levels in each domain.",
            "The explanations for each problem clearly articulate the problem-solving approach and strategies used.",
            "There is evidence of strategy transfer and adaptation across problems and domains, especially in the level 3 problems.",
            "The response demonstrates creativity and flexibility in applying knowledge across diverse domains.",
            "The overall submission shows clear progression in problem-solving abilities and meta-learning skills across the challenge."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
