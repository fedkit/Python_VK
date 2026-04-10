def find_contact(contacts, contact_key, value):
    value_lower = value.lower()
    answer = []
    for contact in contacts:
        if contact_key in contact and str(contact[contact_key]).lower() == value_lower:
            answer.append(contact)
    return answer