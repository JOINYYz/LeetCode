class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        correct_emails = []
        for email in emails:
            if email.find('+') < email.find('@'):
                email = email.replace(email[email.find('+'):email.find('@')],'')
            if email.find('.') < email.find('@'):
                email = email.replace('.','')
            correct_emails.append(email)
        return (len(set(correct_emails)))
