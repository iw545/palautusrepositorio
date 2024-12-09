from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or

class QueryBuilder:
    def __init__(self, matcher = All()):
        self._matcher = matcher

    def build(self):
        return self._matcher

    def plays_in(self, name):
        return QueryBuilder(And(self._matcher, PlaysIn(name)))

    def has_at_least(self, value, name):
        return QueryBuilder(And(self._matcher, HasAtLeast(value, name)))

    def has_fewer_than(self, value, name):
        return QueryBuilder(And(self._matcher, HasFewerThan(value, name)))

    def one_of(self, first, second):
        return QueryBuilder(Or(first, second))
