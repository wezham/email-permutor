import dns.resolver
import socket
import smtplib

class EmailPermutor:

    def __init__(self, name, company_name, company_url):
        self.company_url = company_url;
        self.name = name;
        self.company_name = "@" + company_name;
        self.emails = []
        self.permute_over_names()
        #self.print_emails()

    def permute_over_names(self):
        split_names = self.name.split()
        #try:
        first_name = split_names[0].lower()
        last_name = split_names[1].lower()
        self.mix_and_match(first_name, last_name)

        self.dns_resolver()
        print(host)
        #except:
        #    print("Name not formatted correctly. Try 'FIRSTNAME LASTNAME'")

    def dns_resolver(self):
        host = socket.gethostname()
        server = smtplib.SMTP()
        server.set_debuglevel(6)
        records = dns.resolver.query(self.company_url, 'MX')
        mxRecord = records[0].exchange
        mxRecord = str(mxRecord)
        print(f"MxRecord {mxRecord}")
        server.connect(mxRecord)
        print(f"Connected to {mxRecord}")
        server.helo("188.166.177.208")
        for email in self.emails:
            print(f"Trying {email}")
            server.mail(email)
            code, message = server.rcpt(str(addressToVerify))
            print(code)
            print(message)
        server.quit()

    def mix_and_match(self, first_name, last_name):
        self.appender(first_name, '',last_name)
        self.appender(last_name, '',first_name)
        self.appender(first_name, ".", last_name)
        self.appender(last_name, ".", first_name)
        self.appender(first_name)
        self.appender(last_name)
        self.appender(first_name[:1], ".", last_name)
        self.appender(first_name[:1], '', last_name)
        self.appender(last_name,  '',first_name[:1])
        self.appender(last_name, '.', first_name[:1])
        self.print_emails()

    def appender(self, half1, joiner="", half2=""):
        self.emails.append(half1+joiner+half2+self.company_name + ".com")

    def print_emails(self):
        print("Trying to permute over:")
        for email in self.emails:
            print(email)

EmailPermutor("Wez Ham", "gmail", "gmail.com")
