
class Atom:
    """
    Atom represents a single first-order logic literal:
    a predicate applied to a fixed number of arguments.

    What it models
    --------------
    Think of an Atom as:   predicate(arg1, arg2, ..., argN)

    Examples of *ground* facts (no variables):
        Atom('parent', ('anna', 'eva'))
        Atom('likes', ('alice', 'pizza'))
        Atom('edge', ('A', 'B'))
        Atom('color', ('house1', 'red'))
        Atom('age', ('bob', 42))

    Examples of *patterns* (for rules; variables start with '?'):
        Atom('parent', ('?x', '?y'))              # “?x is a parent of ?y”
        Atom('grandparent', ('?g', '?c'))         # “?g is a grandparent of ?c”
        Atom('between', ('?a', '?b', '?c'))       # example of 3 arguments

    Design notes
    ------------
    - Arguments are stored as a tuple to make the Atom hashable and safe to put
      in sets or use as dictionary keys (facts are typically stored in a set).
    - Each argument should itself be hashable (e.g., str, int). If you use
      variables, the common convention is strings beginning with '?'.
    - Two Atoms are equal if both their predicate and all arguments (in order)
      are equal. This enables reliable de-duplication of facts.

    Doctest-style examples
    ----------------------
    >>> a1 = Atom('parent', ('anna', 'eva'))
    >>> a2 = Atom('parent', ('anna', 'eva'))
    >>> a3 = Atom('parent', ('john', 'eva'))
    >>> a1 == a2
    True
    >>> a1 == a3
    False
    >>> len({a1, a2, a3})   # a1 and a2 are duplicates
    2
    >>> repr(a1)
    "parent('anna', 'eva')"
    """
    def __init__(self, predicate, args):
        """
        Initialize an Atom.

        Parameters
        ----------
        predicate : str
            The predicate name (e.g., 'parent', 'likes', 'edge').
        args : sequence
            The ordered arguments of the atom. These are converted to a tuple
            to ensure immutability and hashability.

        Notes
        -----
        - Arguments should be hashable (e.g., str, int).
        - For rule patterns, use variables as strings starting with '?',
          e.g., '?x', '?y'. For ground facts, use concrete values only.
        """
        # TODO - BLOCK START
        # TASK#2
        pass
        # TODO - BLOCK END

    def __eq__(self, other):
        """
        Structural equality.

        Returns True if:
          - 'other' is an Atom, and
          - both atoms have the same predicate string, and
          - their argument tuples are equal (same length, same items in order).

        This allows Atoms to be compared meaningfully and de-duplicated.

        Example
        -------
        >>> Atom('likes', ('alice', 'pizza')) == Atom('likes', ('alice', 'pizza'))
        True
        >>> Atom('likes', ('alice', 'sushi')) == Atom('likes', ('alice', 'pizza'))
        False
        """
        # TODO - BLOCK START
        # TASK#3
        pass
        # TODO - BLOCK END

    def __hash__(self):
        """
        Hash consistent with equality.

        The hash is derived from (predicate, args). This lets Atoms be used as:
          - elements of a set (e.g., a fact base), or
          - keys in a dictionary (e.g., indexing facts by Atom).

        Contract
        --------
        If a == b then hash(a) == hash(b). Since __eq__ compares both
        predicate and args, we mirror that here.

        Example
        -------
        >>> a = Atom('edge', ('A', 'B'))
        >>> s = {a}
        >>> Atom('edge', ('A', 'B')) in s
        True
        """
        # TODO - BLOCK START
        # TASK#4
        pass
        # TODO - BLOCK END

    def __repr__(self):
        """
        Unambiguous string representation.

        Produces a canonical form like:
            predicate('arg1', 'arg2', 3)

        - Each argument is rendered using Python's repr(), so strings are quoted
          and numbers appear as-is.
        - Helpful for debugging, logging, or inspecting derived facts.

        Example
        -------
        >>> repr(Atom('color', ('house1', 'red')))
        "color('house1', 'red')"
        """
        # TODO - BLOCK START
        # TASK#5
        pass
        # TODO - BLOCK END

class Rule:
    """
    Horn clause (rule) in first-order logic.

    Shape
    -----
        head :- body1, body2, ..., bodyK

    - head : Atom
        The conclusion that can be inferred when all body atoms hold.
    - body : list[Atom]
        The premises (a conjunction). If the body is empty, the rule is a
        *fact* (a unit clause): `head :-` which is logically just `head`.

    Intuition
    ---------
    Read `grandparent(?g, ?c) :- parent(?g, ?p), parent(?p, ?c)` as:
        “?g is a grandparent of ?c if ?g is a parent of ?p and ?p is a parent of ?c.”

    Variables
    ---------
    - Use strings that start with '?' for variables, e.g., '?x', '?y'.
    - Ground rules (no variables) are unusual, but allowed.
    - For safety/range restriction in forward chaining, every variable that
      appears in the head should also appear somewhere in the body.

    Examples
    --------
    Grandparent rule:
        Rule(
            head=Atom('grandparent', ('?g', '?c')),
            body=[
                Atom('parent', ('?g', '?p')),
                Atom('parent', ('?p', '?c')),
            ]
        )

    Sibling rule (simple version):
        Rule(
            head=Atom('sibling', ('?a', '?b')),
            body=[
                Atom('parent', ('?p', '?a')),
                Atom('parent', ('?p', '?b')),
                Atom('neq', ('?a', '?b')),  # custom predicate to enforce ?a != ?b
            ]
        )

    Ancestor (recursive) rules:
        # Base case: every parent is an ancestor
        Rule(
            head=Atom('ancestor', ('?a', '?b')),
            body=[
                Atom('parent', ('?a', '?b')),
            ]
        )
        # Recursive case: if a is ancestor of p and p is parent of b, then a is ancestor of b
        Rule(
            head=Atom('ancestor', ('?a', '?b')),
            body=[
                Atom('ancestor', ('?a', '?p')),
                Atom('parent', ('?p', '?b')),
            ]
        )

    Sets & Maps
    -----------
    Rules are made hashable and comparable (by structure) so they can be used
    in sets/dicts to avoid duplicates and cache them.

    Doctest-style checks
    --------------------
    >>> r1 = Rule(Atom('grandparent', ('?g','?c')),
    ...           [Atom('parent', ('?g','?p')), Atom('parent', ('?p','?c'))])
    >>> r2 = Rule(Atom('grandparent', ('?g','?c')),
    ...           [Atom('parent', ('?g','?p')), Atom('parent', ('?p','?c'))])
    >>> r1 == r2
    True
    >>> len({r1, r2})  # de-duplicated
    1
    >>> repr(r1)
    "grandparent('?g', '?c') :- parent('?g', '?p'), parent('?p', '?c')"
    """

    def __init__(self, head, body):
        """
        Initialize a rule.

        Parameters
        ----------
        head : Atom
            The rule head (conclusion).
        body : sequence of Atom
            The rule body (premises). Converted to a list internally.

        Notes
        -----
        - An empty body means the rule is a fact (unit clause).
        - For forward chaining, prefer range-restricted rules:
          every variable appearing in 'head' should appear in 'body'.
        """
        # TODO - BLOCK START
        # TASK#6
        pass
        # TODO - BLOCK END

    def __eq__(self, other):
        """
        Structural equality: same head and same body (same order and atoms).

        Example
        -------
        >>> Rule(Atom('p', ('?x',)), [Atom('q', ('?x',))]) == \
        ... Rule(Atom('p', ('?x',)), [Atom('q', ('?x',))])
        True
        """
        # TODO - BLOCK START
        # TASK#7
        pass
        # TODO - BLOCK END

    def __hash__(self):
        """
        Hash consistent with equality, based on (head, tuple(body)).

        This allows rules to be placed in sets or used as dictionary keys.
        """
        # TODO - BLOCK START
        # TASK#8
        pass
        # TODO - BLOCK END

    def __repr__(self):
        """
        Unambiguous string representation.

        Examples
        --------
        >>> repr(Rule(Atom('p', ('a',)), []))
        "p('a')"
        >>> repr(Rule(Atom('r', ('?x','?y')),
        ...           [Atom('p', ('?x',)), Atom('q', ('?x','?y'))]))
        "r('?x', '?y') :- p('?x'), q('?x', '?y')"
        """
        # TODO - BLOCK START
        # TASK#9
        pass
        # TODO - BLOCK END

class KnowledgeBase:
    """
    A minimal, in-memory knowledge base that stores ground facts and Horn rules.

    What it holds
    -------------
    - facts : set of Atom
        Each fact is an Atom with *concrete* arguments only (no variables),
        e.g. Atom('parent', ('anna', 'ewa')). Using a set automatically
        de-duplicates repeated insertions of the same fact.

    - rules : list of Rule
        Each rule is a Horn clause of the form:
            head :- body1, body2, ...
        where head and body elements are Atoms that may contain variables
        (arguments starting with '?' such as '?x', '?y').

    Responsibilities
    ----------------
    This class **only** stores knowledge (facts + rules) and offers a simple
    pattern-based query over the *materialized facts*. It does not derive
    new facts by itself. Forward-chaining / rule application is handled by
    a separate component (e.g., an InferenceEngine) that reads and writes
    to this knowledge base.

    Example
    -------
    >>> kb = KnowledgeBase()
    >>> kb.add_fact('parent', 'anna', 'ewa')
    >>> kb.add_fact('parent', 'ewa', 'ola')
    >>> kb.add_rule(
    ...     Atom('grandparent', ('?x', '?z')),
    ...     [Atom('parent', ('?x','?y')), Atom('parent', ('?y','?z'))]
    ... )
    # A forward-chaining engine could now derive:
    #   grandparent('anna','ola')
    # and insert it back as a fact.
    """

    def __init__(self):
        """
        Construct an empty knowledge base.

        Attributes
        ----------
        facts : set of Atom
            Ground facts (contain only constants; no variables). Stored in a
            set to avoid duplicates and to allow fast membership checks.
        rules : list of Rule
            Horn clauses (may contain variables). Kept in insertion order,
            which can be useful for deterministic forward-chaining strategies
            and priority/weight handling.
        """
        # TODO - BLOCK START
        # TASK#10
        pass
        # TODO - BLOCK END

    def __repr__(self):
        """
        Return a compact, unambiguous string useful for debugging.

        Format
        ------
        "KnowledgeBase(facts=<count>, rules=<count>)"

        Notes
        -----
        - We intentionally show only counts, not full contents. This keeps the
          representation stable and readable even for large knowledge bases.
        """
        # TODO - BLOCK START
        # TASK#11
        pass
        # TODO - BLOCK END

    def add_fact(self, predicate, *args):
        """
        Add a single *ground* fact to the knowledge base.

        Parameters
        ----------
        predicate : str
            The predicate name, e.g. 'parent', 'likes', 'color_of'.
        *args : tuple
            The concrete arguments of the fact. These should be ground (no variables),
            e.g. ('anna', 'ewa') or ('house1', 'green').

        Behavior
        --------
        - The fact is wrapped in an Atom and inserted into the `facts` set.
        - Because `facts` is a set, attempting to add the same fact again is a no-op.

        Examples
        --------
        >>> kb.add_fact('parent', 'anna', 'ewa')
        >>> kb.add_fact('color_of', 'house1', 'green')
        """
        # TODO - BLOCK START
        # TASK#12
        pass
        # TODO - BLOCK END

    def add_rule(self, head_atom, body_atoms):
        """
        Add a Horn rule to the knowledge base.

        Parameters
        ----------
        head_atom : Atom
            The rule's conclusion (may contain variables), e.g.:
                Atom('grandparent', ('?x','?z'))
        body_atoms : list[Atom]
            The rule's premises (a conjunction), each may contain variables, e.g.:
                [Atom('parent', ('?x','?y')), Atom('parent', ('?y','?z'))]

        Behavior
        --------
        - Appends the Rule(head_atom, body_atoms) to the `rules` list.
        - The knowledge base does not attempt to validate variable safety;
          any inference engine that uses the rules should handle that.

        Example
        -------
        >>> kb.add_rule(
        ...     Atom('grandparent', ('?x','?z')),
        ...     [Atom('parent', ('?x','?y')), Atom('parent', ('?y','?z'))]
        ... )
        """
        # TODO - BLOCK START
        # TASK#13
        pass
        # TODO - BLOCK END

    def query(self, predicate, *args):
        """
        Retrieve tuples of arguments of all facts that match the given pattern.

        This is a *direct lookup* over the stored `facts` only.
        It does not apply rules. If you want inferred facts, run a forward
        (or backward) chaining engine first to populate `facts`.

        Matching rules
        --------------
        - The predicate must match exactly.
        - The arity (number of arguments) must match.
        - Each argument is matched positionally:
            * If the pattern argument is a concrete value (e.g., 'anna'),
              it must equal the fact's argument at that position.
            * If the pattern argument is `None`, it acts as a wildcard
              and matches any value at that position.

        Returns
        -------
        list of tuples
            Each tuple is the full argument tuple of a matching fact.

        Examples
        --------
        Suppose the KB contains:
            parent('anna','ewa'), parent('ewa','ola'), color_of('house1','green')

        >>> kb.query('parent', None, None)
        [('anna', 'ewa'), ('ewa', 'ola')]

        >>> kb.query('parent', 'anna', None)
        [('anna', 'ewa')]

        >>> kb.query('parent', None, 'ola')
        [('ewa', 'ola')]

        >>> kb.query('color_of', 'house1', None)
        [('house1', 'green')]

        Tips
        ----
        - This method is intentionally simple: it does not understand variables
          like '?x'. Use `None` for “any value”. Variables are meaningful inside
          rules and are used by the inference engine during unification.
        """
        # TODO - BLOCK START
        # TASK#14
        pass
        # TODO - BLOCK END

class StudentID:
    """
    Utility class for identifying the student.

    Each student must replace the placeholder return value
    in the `get_ID` method with their own unique student ID.
    """

    @staticmethod
    def get_ID():
        """
        Return the student ID as a string.

        Returns
        -------
        str
            The student ID. Each student must replace "student_ID" with their own ID.

        Examples
        --------
        >>> StudentID.get_ID()
        '123456'
        """
        # TODO - BLOCK START
        # TASK#1
        return "student_ID"
        # TODO - BLOCK END