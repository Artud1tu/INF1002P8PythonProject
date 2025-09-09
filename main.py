# whitelist
SAFE_DOMAINS = ["example.com", "myschool.edu"]

def safe_domain(sender_email: str) -> bool:
    domain = sender_email.split("@")[-1].lower()
    return domain in SAFE_DOMAINS

def main():
    test_email = {"from": "test@g00gle.com", "subject": "Urgent! Verify your account"}

    print("Checking email:", test_email)
    if safe_domain(test_email["from"]):
        print("Safe Email")
    else:
        print("Suspicious Email")

if __name__ == "__main__":
    main()
