from patient_class import Patient

person = Patient("097-21-1003", "08/13/92", "7001294103", "Ima", "Person", "606 6th St.")

print(person.fullName)
print(person.address)

person.address = "32 Mulberry St."

print(person.address)