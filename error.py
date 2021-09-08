# @purpose Shortcut the dummy-proofing


# Checks to see if the response is empty literal
def empty_string(string):
    if not string:
        return True
    return False


# Runs loop while answer is empty literal
def empty_literal(empty_response, question, answer):
    while empty_response:
        answer = input(question)
        empty_response = empty_string(answer)
    return answer
