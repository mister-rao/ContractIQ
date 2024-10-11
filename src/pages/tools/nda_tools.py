# tools
from utils import TextDocumentGenerator

NDA_TEMPLATE = "../templates/nda.md"


template = TextDocumentGenerator(NDA_TEMPLATE)


def update_nda_template(
    day: str,
    month: str,
    year: str,
    role: str,
    company_name: str,
    survival_period: int,
    post_binding_agreement_period: int,
    governing_laws: str,
    jurisdiction_city: str,
    arbitration_act: str,
    arbitration_city: str,
    arbitration_language: str,
    authorized_signatory_name: str,
    authorized_signatory_date: str,
    employee_name: str,
    employee_date: str,
) -> str:
    """
    Updates a Non-Disclosure Agreement (NDA) template with the given values for placeholders.

    Args:
        day: str: The day of the month when the agreement is created.
        month: str: The month when the agreement is created.
        year: str: The year when the agreement is created.
        role: str: The role or title of the employee (e.g., "Intern").
        company_name: str: The name of the company entering into the NDA.
        survival_period: int: The period (in years) for which the NDA remains in effect after termination.
        post_binding_agreement_period: int: The period (in years) after the binding agreement is terminated or expires.
        governing_laws: str: The set of laws governing the NDA (e.g., "India").
        jurisdiction_city: str: The city in which legal jurisdiction is established for the NDA (e.g., "Bangalore").
        arbitration_act: str: The specific arbitration act applicable to the NDA (e.g., "Indian Arbitration & Conciliation Act, 1996").
        arbitration_city: str: The city where arbitration proceedings will take place.
        arbitration_language: str: The language in which the arbitration proceedings will be conducted.
        authorized_signatory_name: str: The name of the company's authorized signatory.
        authorized_signatory_date: str: The date when the authorized signatory signs the agreement.
        employee_name: str: The name of the employee signing the NDA.
        employee_date: str: The date when the employee signs the NDA.
    """
    data = {
        "day": day,
        "month": month,
        "year": year,
        "role": role,
        "company_name": company_name,
        "survival_period": str(survival_period),
        "post_binding_agreement_period": str(post_binding_agreement_period),
        "governing_laws": governing_laws,
        "jurisdiction_city": jurisdiction_city,
        "arbitration_act": arbitration_act,
        "arbitration_city": arbitration_city,
        "arbitration_language": arbitration_language,
        "authorized_signatory_name": authorized_signatory_name,
        "authorized_signatory_date": authorized_signatory_date,
        "employee_name": employee_name,
        "employee_date": employee_date,
    }

    template.update(data)


def save_nda_as_pdf() -> None:
    """Save NDA as a PDF document"""
    template.generate_pdf()


tools = [update_nda_template, save_nda_as_pdf]
