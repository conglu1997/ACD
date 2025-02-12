class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"domain": "medicine", "task": "Write a detailed patient case report for a patient with Type 2 Diabetes Mellitus."},
            "2": {"domain": "engineering", "task": "Write a technical specification for a new bridge design, including materials, load calculations, and safety protocols."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to generate technical documentation in the specified domain. Ensure that your documentation is clear, accurate, and adheres to domain-specific conventions.

Domain: {t['domain']}

Task: {t['task']}

Provide your documentation in plain text format, ensuring it is well-structured and comprehensive.

Example (for domain 'medicine'):

Patient Case Report:

Patient Information:
- Name: John Doe
- Age: 55
- Gender: Male

Medical History:
- Type 2 Diabetes Mellitus diagnosed 5 years ago
- Hypertension
- Hyperlipidemia

Current Medications:
- Metformin
- Lisinopril
- Atorvastatin

Clinical Presentation:
- Complaints of increased thirst, frequent urination, and fatigue
- Blood glucose levels: 200 mg/dL

Diagnosis:
- Uncontrolled Type 2 Diabetes Mellitus

Treatment Plan:
- Adjust medication dosage
- Implement lifestyle changes (diet and exercise)
- Regular follow-up appointments

Example (for domain 'engineering'):

Technical Specification for Bridge Design:

Project Title: New Suspension Bridge

Materials:
- Steel cables
- Reinforced concrete
- Asphalt

Load Calculations:
- Maximum load capacity: 20,000 tonnes
- Safety factor: 1.5

Safety Protocols:
- Regular inspections every 6 months
- Load testing every year
- Emergency response plan for structural failures

Ensure your documentation is similarly detailed and follows the conventions of the specified domain."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The documentation should be clear and well-structured.",
            "The content should be accurate and adhere to domain-specific conventions.",
            "The documentation should be comprehensive and cover all necessary aspects of the task."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0