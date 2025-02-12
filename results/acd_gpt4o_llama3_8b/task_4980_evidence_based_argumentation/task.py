class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "premise": "Climate change is a significant threat to biodiversity.",
                "evidence": [
                    "A recent study found that rising temperatures have caused shifts in the habitats of various species.",
                    "Increased frequency of extreme weather events has led to habitat destruction and loss of life.",
                    "Ocean acidification has negatively impacted marine life, particularly coral reefs.",
                    "Changes in precipitation patterns have altered the availability of water resources, affecting both plant and animal life."
                ]
            },
            "2": {
                "premise": "Remote work should be adopted as a permanent option by companies.",
                "evidence": [
                    "Studies have shown that remote work can increase employee productivity and job satisfaction.",
                    "Remote work reduces the need for commuting, which lowers carbon emissions and traffic congestion.",
                    "Companies can save on overhead costs such as office space and utilities.",
                    "Flexible work arrangements can attract a wider talent pool and improve work-life balance for employees."
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Evaluate the following premise and form a coherent argument based on the given evidence. Your argument should be logically structured and clearly support the premise provided.

Premise:
{t['premise']}

Evidence:
- {t['evidence'][0]}
- {t['evidence'][1]}
- {t['evidence'][2]}
- {t['evidence'][3]}

Ensure that your argument is well-reasoned and uses the evidence effectively to support the premise. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The argument should be logically structured and clearly support the premise.",
            "The argument should effectively use the given evidence.",
            "The argument should be coherent and well-reasoned."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
