import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        global_issues = [
            {
                "issue": "Climate Change",
                "context": "Rising global temperatures and extreme weather events"
            },
            {
                "issue": "Food Security",
                "context": "Increasing global population and limited agricultural resources"
            },
            {
                "issue": "Antibiotic Resistance",
                "context": "Emergence of drug-resistant bacteria and limited new antibiotics"
            },
            {
                "issue": "Water Scarcity",
                "context": "Depleting freshwater resources and increasing water pollution"
            }
        ]
        return {
            "1": random.choice(global_issues),
            "2": random.choice(global_issues)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical biotechnology solution to address the global issue of {t['issue']} in the context of {t['context']}. Then, analyze its potential impacts and ethical implications. Complete the following tasks:

1. Solution Design (200-250 words):
   a) Describe your proposed biotechnology solution.
   b) Explain the key scientific principles behind your solution.
   c) Outline how your solution would be implemented.
   d) Cite at least one relevant scientific study or paper to support your proposed solution.
   e) Suggest a method for measuring the effectiveness of your solution.

2. Potential Impacts (200-250 words):
   a) Discuss two potential positive impacts of your solution.
   b) Analyze two possible negative consequences or risks, including unintended effects.
   c) Consider both short-term and long-term effects.

3. Ethical Analysis (200-250 words):
   a) Identify three major ethical concerns raised by your solution.
   b) Analyze these concerns using one ethical framework (e.g., utilitarianism, deontology, virtue ethics).
   c) Discuss how to address one of the ethical concerns.

4. Regulatory Considerations (150-200 words):
   a) Propose a framework for regulating the development and use of your biotechnology solution.
   b) Discuss two challenges in implementing such regulations on a global scale.

5. Alternative Approach (150-200 words):
   a) Describe one alternative (non-biotech) approach to addressing the same global issue.
   b) Compare this alternative to your biotech solution in terms of potential effectiveness and ethical implications.

Ensure your response demonstrates understanding of biotechnology, ethical reasoning, and global issues. Be creative while maintaining scientific plausibility.

Format your response using the following structure:

1. Solution Design
   [Your response here]

2. Potential Impacts
   [Your response here]

3. Ethical Analysis
   [Your response here]

4. Regulatory Considerations
   [Your response here]

5. Alternative Approach
   [Your response here]

Your entire response should not exceed 1200 words.

Example (partial, for Solution Design only):
1. Solution Design
Our proposed biotechnology solution to address climate change is the development of enhanced photosynthetic algae. These genetically modified algae would be designed to capture carbon dioxide more efficiently than natural algae, potentially reducing atmospheric CO2 levels. The key scientific principle involves..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The proposed biotechnology solution is relevant to the given global issue and scientifically plausible.",
            "The solution design cites at least one relevant scientific study or paper.",
            "The impact analysis considers both positive and negative consequences.",
            "The ethical analysis identifies at least three major concerns and applies an ethical framework.",
            "The regulatory considerations propose a framework and address challenges of implementation.",
            "The alternative approach is compared to the biotech solution in terms of effectiveness and ethics.",
            "The response follows the specified format and does not exceed 1200 words."
        ]
        return float(sum(eval_with_llm_judge(instructions, submission, [criterion]) for criterion in criteria) / len(criteria))
