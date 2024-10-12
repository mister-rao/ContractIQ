# tools
from utils import TextDocumentGenerator

EA_TEMPLATE = "templates/employee_agreement.jinja"


def save_employee_agreement(
    day: str,
    month: str,
    year: str,
    company_name: str,
    company_address: str,
    employee_name: str,
    parent_spouse_name: str,
    employee_age: str,
    employee_address: str,
    employee_position: str,
    probation_period_days: int,
    probation_period_text: str,
    employee_responsibilities: str,
    salary_amount: str,
    casual_leave_days: int,
    sick_leave_days: int,
    public_holidays: str,
    competing_business_restriction_period: str,
    termination_notice_period: str,
    resignation_notice_period: str,
    governing_law: str,
    jurisdiction: str,
    employee_designation: str,
) -> None:
    """
    Updates an Employee Agreement template with the given values for placeholders.

    Args:
        day: str: The day when the agreement is created.
        month: str: The month when the agreement is created.
        year: str: The year when the agreement is created.
        company_name: str: The name of the company.
        company_address: str: The address of the company.
        employee_name: str: The name of the employee.
        parent_spouse_name: str: The name of the employee's parent or spouse.
        employee_age: str: The age of the employee.
        employee_address: str: The address of the employee.
        employee_position: str: The position of the employee in the company.
        probation_period_days: int: The number of days in the probation period.
        probation_period_text: str: The description of the probation period.
        employee_responsibilities: str: The responsibilities of the employee.
        salary_amount: str: The employee's salary.
        casual_leave_days: int: The number of casual leave days.
        sick_leave_days: int: The number of sick leave days.
        public_holidays: str: The public holidays list or description.
        competing_business_restriction_period: str: The time restriction for competing businesses.
        termination_notice_period: str: The termination notice period.
        resignation_notice_period: str: The resignation notice period.
        governing_law: str: The governing law for the agreement.
        jurisdiction: str: The jurisdiction for the agreement.
        employee_designation: str: The designation of the employee.
    """

    employee_agreement = TextDocumentGenerator(EA_TEMPLATE)

    data = {
        "day": day,
        "month": month,
        "year": year,
        "company_name": company_name,
        "company_address": company_address,
        "employee_name": employee_name,
        "parent_spouse_name": parent_spouse_name,
        "employee_age": employee_age,
        "employee_address": employee_address,
        "employee_position": employee_position,
        "probation_period_days": str(probation_period_days),
        "probation_period_text": probation_period_text,
        "employee_responsibilities": employee_responsibilities,
        "salary_amount": salary_amount,
        "casual_leave_days": str(casual_leave_days),
        "sick_leave_days": str(sick_leave_days),
        "public_holidays": public_holidays,
        "competing_business_restriction_period": competing_business_restriction_period,
        "termination_notice_period": termination_notice_period,
        "resignation_notice_period": resignation_notice_period,
        "governing_law": governing_law,
        "jurisdiction": jurisdiction,
        "employee_designation": employee_designation,
    }

    employee_agreement.update(data)
    employee_agreement.generate_pdf("employee_agreement")


tools = [save_employee_agreement]
