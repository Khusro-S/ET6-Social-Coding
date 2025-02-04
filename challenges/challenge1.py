# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:30:30 2025

@author: somai
Challenge 1: Detecting Suspicious Login Attempts
Objective:
The goal of this challenge is to practice Boolean algebra simplification. Students will write a Python program to simplify a
given Boolean expressions using Boolean Algebra’s law, helping them understand how to optimize logical expressions in
programming.
Scenario:
A cybersecurity team is investigating an authentication system that occasionally flags legitimate login attempts as
suspicious. The system checks multiple conditions to determine if a login attempt should be blocked.
One of the core checks involves the following rule:
¬(A∧(B∨¬B))
where:
A: The user has provided the correct login credentials.
B: The login attempt is from a trusted device.
The security team suspects that the system might be blocking users incorrectly due to redundant logic checks. Your task is
to simplify the logic to understand what the system is actually doing and determine if the rule is valid or needs
modification.

Task:
Analyze the given Boolean expression.
Apply Boolean law to simplify it.
Interpret what the final expression means in the context of allowing or blocking a login attempt.

"""


def access(a: bool, b: bool) -> bool:
    """
    Evaluates the given Boolean rule:
      ¬(A ∧ (B ∨ ¬B)) simplifies to ¬A.

    Parameters:
      a (bool): True if the user has provided correct credentials, False otherwise.
      b (bool): True if the login attempt is from a trusted device, False otherwise.

      Returns:
      bool: True if the login attempt should be blocked, False otherwise.

    Raises:
      valueError if simplified rule is not equal to the given rule

    >>> access(true, true)
    false

    >>> access(false, true)
    true

    >>> access(false, false)
    true
    """
    given_rule = not (a and (b or not b))
    simplified_rule = not a

    if given_rule != simplified_rule:
        raise ValueError("Simplification error!")
    return simplified_rule


test_cases = [
    (False, False),
    (False, True),
    (True, False),
    (True, True),
]
print("\nGiven approach")
print("a     |   b    |    result")
for a, b in test_cases:
    result = access(a, b)
    print(a, "   ", b, "   ", result)


def better_access(a: bool, b: bool) -> bool:
    """
    Determines whether the login should be allowed or denied
      both the inputs (correct credentials and attempt from trusted device) should return true (login allowed)

    Parameters:
      a (bool): True if the user has provided correct credentials, False otherwise.
      b (bool): True if the login attempt is from a trusted device, False otherwise.

      Returns:
      bool: True if the login attempt should be blocked, False otherwise.

    >>> access(true, true)
    true

    >>> access(false, true)
    false

    >>> access(false, false)
    false
    """
    return a and b


test_cases_2 = [
    (False, False),
    (False, True),
    (True, False),
    (True, True),
]
print("\nModified approach")
print("a     |   b    |    result")
for a, b in test_cases_2:
    result = better_access(a, b)
    print(a, "   ", b, "   ", result)
