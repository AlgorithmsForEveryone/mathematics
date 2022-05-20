# TODO: create flags to config the functions ex: when an event is equiprobable -e, with repetitions -r or withour -wr.


# Probability of an event
# # set must be finite and all the events are equiprobable
from numpy import NaN
from sympy import re


def without_repetition(stage, result_set):
    if(stage >= 0):
        return result_set * without_repetition(stage-1, result_set-1)
    else:
        return 1


def with_repetition(stage, result_set):
    if(stage >= 0):
        return result_set * with_repetition(stage-1, result_set)
    else:
        return 1


def probability_of_event(stage, result_set, repetition):
    event_cardinality = 0
    omega_cardinality = result_set**stage
    if(repetition == 1):
        event_cardinality = with_repetition(stage, result_set)
    else:
        event_cardinality = without_repetition(stage, result_set)
    return event_cardinality / omega_cardinality
