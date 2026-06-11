import csv

#class that strcutures a single Contact record
class PhoneContact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"Contact: {self.name}:{self.phone}"
    

class Phone:
    def __init__(self):
        self.contacts = []
    
    #Method that lists all contacts data
    def show(self):
        print("List of Contacts: ")
        for contact in self.contacts:
            print(contact)

    #Method that reads Contacts from the initial CSV 
    def import_contacts_from_csv(self, file):
        print("Import Contacts")
        with open(file, newline="") as csvfile:
            fieldnames = ["Name", "Phone"]
            reader = csv.DictReader(csvfile, fieldnames)

            for row in reader:
                self.contacts.append(PhoneContact(row["Name"],
                                                  row["Phone"]))
        print("Import was successful")

    #Method that writes read Contacts into new CSV file
    def export_contacts_to_csv(self, file):
        print("Export Contacts")
        with open(file, "w", newline="") as csvfile:
            writer = csv.writer(
                csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
            )

            for contact in self.contacts:
                writer.writerow([contact.name, contact.phone])
        print("Import was successful")

    #Method that searches for the specific Contact in the read file
    def search_contacts(self):
        phrase = input("Search Contact: ")
        print("Search Contacts by phrase: ")
        count = 0
        for contact in self.contacts:
            if phrase.lower() in contact.name.lower() or phrase in contact.phone:
                print(f"Contact found: {contact.name} {contact.phone}")
                count += 1
        if count == 0:
            print("Contact not found")

def main():
    phone = Phone()
    phone.import_contacts_from_csv("contacts.csv")
    phone.show()
    phone.search_contacts()
    phone.export_contacts_to_csv("exported_contacts.csv")

if __name__ == "__main__":
    main()
