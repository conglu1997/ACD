class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task": "develop_project_plan",
                "project": "Design and construct a sustainable city block with residential, commercial, and green spaces."
            },
            "2": {
                "task": "develop_project_plan",
                "project": "Create a new high-speed rail network connecting three major cities in a country."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Develop a detailed project plan for the following engineering project: {t['project']}. Your plan should include the following sections: 1. Project Scope 2. Objectives 3. Required Resources (materials, personnel, technology, etc.) 4. Timeline (phases and milestones) 5. Potential Challenges and Mitigations. Ensure your plan is comprehensive, logically structured, and demonstrates a deep understanding of the engineering principles and practical considerations involved. Submit your project plan as a plain text string in the following format: 'Project Scope: [Your project scope] Objectives: [Your objectives] Required Resources: [Your required resources] Timeline: [Your timeline] Potential Challenges and Mitigations: [Your potential challenges and mitigations]'."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The plan should include all required sections: Project Scope, Objectives, Required Resources, Timeline, Potential Challenges and Mitigations.",
            "The plan should be comprehensive and logically structured.",
            "The plan should demonstrate a deep understanding of the engineering principles and practical considerations involved.",
            "The plan should be in the correct format: 'Project Scope: [Your project scope] Objectives: [Your objectives] Required Resources: [Your required resources] Timeline: [Your timeline] Potential Challenges and Mitigations: [Your potential challenges and mitigations]'."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
