import check50
import check50.c

@check50.check()
def exists():
    """stack.c exists"""
    check50.exists("stack.c")

@check50.check(exists)
def compiles():
    """stack.c compiles"""
    check50.c.compile("stack.c", lcs50=True)

@check50.check(compiles)
def raises_error_with_no_emails_1():
    """raises an error when trying to print no emails"""
    from re import match
    expected = "--> Printing all emails from newest to oldest.\nError: Inbox is empty.\n"
    actual = check50.run("./stack").stdin("print").stdout()
    if not match(expected, actual):
        raise check50.Mismatch(expected, actual)

@check50.check(compiles)
def raises_error_with_no_emails_2():
    """raises an error when trying to print no emails after one push and one pop"""
    from re import match
    expected = "--> Printing all emails from newest to oldest.\nError: Inbox is empty.\n"
    actual = check50.run("./stack").stdin("push").stdin("1").stdin("pop").stdin("print").stdout()
    if not match(expected, actual):
        raise check50.Mismatch(expected, actual)

@check50.check(compiles)
def pushes_and_prints_one_email():
    """pushes and prints email with 'Hello, world' as subject"""
    from re import match
    expected = "--> Printing all emails from newest to oldest.\nHello, world\n"
    actual = check50.run("./stack").stdin("push").stdin("Hello, world").stdin("print").stdout()
    if not match(expected, actual):
        raise check50.Mismatch(expected, actual)
 
@check50.check(compiles)
def pushes_and_prints_three_emails():
    """pushes and prints emails with 'Hello, world', 'Are you there', and 'Seriously' as subjects"""
    from re import match
    expected = "--> Printing all emails from newest to oldest.\nSeriously\nAre you there\nHello, world\n"
    actual = check50.run("./stack").stdin("push").stdin("Hello, world").stdin("push").stdin("Are you there").stdin("push").stdin("Seriously").stdin("print").stdout()
    if not match(expected, actual):
        raise check50.Mismatch(expected, actual)

@check50.check(compiles)
def pushes_and_prints_five_emails():
    """pushes and prints emails with 'Hello, world', 'Are you there', 'Seriously', 'C'mon', and 'Sad face' as subjects"""
    from re import match
    expected = "--> Printing all emails from newest to oldest.\nSad face\nC'mon\nSeriously\nAre you there\nHello, world\n"
    actual = check50.run("./stack").stdin("push").stdin("Hello, world").stdin("push").stdin("Are you there").stdin("push").stdin("Seriously").stdin("push").stdin("C'mon").stdin("push").stdin("Sad face").stdin("print").stdout()
    if not match(expected, actual):
        raise check50.Mismatch(expected, actual)

@check50.check(compiles)
def rejects_sixth_email():
    """does not push or print a sixth email"""
    from re import match
    expected = "--> Printing all emails from newest to oldest.\n5\n4\n3\n2\n1\n"
    actual = check50.run("./stack").stdin("push").stdin("1").stdin("push").stdin("2").stdin("push").stdin("3").stdin("push").stdin("4").stdin("push").stdin("5").stdin("push").stdin("6").stdin("print").stdout()
    if not match(expected, actual):
        raise check50.Mismatch(expected, actual)

@check50.check(compiles)
def pushes_2_pops_1_and_prints():
    """pushes 2 emails, pops 1 email, and then prints"""
    from re import match
    expected = "--> Printing all emails from newest to oldest.\nOhai\n"
    actual = check50.run("./stack").stdin("push").stdin("Ohai").stdin("push").stdin("Rly").stdin("pop").stdin("print").stdout()
    if not match(expected, actual):
        raise check50.Mismatch(expected, actual)

@check50.check(compiles)
def pushes_2_pops_1_pushes_1_and_prints():
    """pushes 2 emails, pops 1 email, pushes another email, and then prints"""
    from re import match
    expected = "--> Printing all emails from newest to oldest.\nKbye\nOhai\n"
    actual = check50.run("./stack").stdin("push").stdin("Ohai").stdin("push").stdin("Rly").stdin("pop").stdin("push").stdin("Kbye").stdin("print").stdout()
    if not match(expected, actual):
        raise check50.Mismatch(expected, actual)
