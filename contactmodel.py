class ContactForm:
    def __init__(self):
        self.submissions = []

    def add_submission(self, name, email, phone, message):
        submission = {
            'name': name,
            'email': email,
            'phone': phone,
            'message': message
        }
        self.submissions.append(submission)

    def get_submissions(self):
        return self.submissions

# Example usage
contact_form = ContactForm()
