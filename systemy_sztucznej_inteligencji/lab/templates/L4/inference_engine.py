from knowledge_base import Atom, Rule, KnowledgeBase

class InferenceEngine:
    """
    Forward-chaining inference engine for a simple first-order (Horn) rule system.

    Conventions
    -----------
    - Variables are strings that start with '?' (e.g., '?x', '?y').
    - Facts in the knowledge base are assumed to be *ground* (no variables).
    - Rules are Horn clauses:  head :- body1, body2, ...
      where `head` and each `body` item is an `Atom`. The body is a conjunction.

    Workflow
    --------
    1. For each rule, try to *unify* (match) its body atoms with existing facts.
    2. Each successful match yields a substitution (mapping variables → constants).
    3. Apply the substitution to the rule head to form a *new* ground fact.
    4. Insert all new facts; repeat until no new facts are produced (saturation).
    """

    @staticmethod
    def is_var(x):
        """
        Return True if `x` is a logic variable according to our convention.

        Parameters
        ----------
        x : any
            Candidate value to check.

        Returns
        -------
        bool
            True if `x` is a string beginning with '?'.

        Examples
        --------
        >>> InferenceEngine.is_var('?x')
        True
        >>> InferenceEngine.is_var('alice')
        False
        >>> InferenceEngine.is_var(42)
        False
        """
        # TODO - BLOCK START
        # TASK#15
        pass
        # TODO - BLOCK END

    def unify_atoms(self, pattern_atom, fact_atom, subst):
        """
        Try to unify a (possibly variable-containing) `pattern_atom` with a
        *ground* `fact_atom` under the current substitution `subst`.

        Parameters
        ----------
        pattern_atom : Atom
            The atom that may contain variables (e.g., parent('?x','?y')).
        fact_atom : Atom
            The ground atom from the KB (no variables).
        subst : dict
            Current variable→constant bindings accumulated so far.

        Returns
        -------
        dict or None
            - A *new* substitution dict (extends `subst`) if unification succeeds.
            - None if unification fails.

        Notes
        -----
        - This simplified unifier binds variables only to constants (no var↔var).
        - Since `fact_atom` is ground, an occurs check is unnecessary.
        - Predicate name and arity must match exactly.

        Examples
        --------
        Unify parent('?x', 'bob') with parent('alice','bob'):
        → {'?x': 'alice'}

        Unify parent('?x', 'bob') with parent('alice','carol'):
        → None (second argument mismatch)
        """
        # TODO - BLOCK START
        # TASK#16
        pass
        # TODO - BLOCK END

    def substitute(self, atom, subst):
        """
        Apply a substitution map `subst` to an `atom` and return a NEW `Atom`.

        Parameters
        ----------
        atom : Atom
            The (possibly variable-containing) atom to instantiate.
        subst : dict
            Variable→constant bindings, e.g., {'?x': 'alice'}.

        Returns
        -------
        Atom
            A new atom with variables replaced where possible. Any variables
            not present in `subst` remain as-is (though in this engine, heads
            are generated only when all body vars are bound).

        Examples
        --------
        >>> a = Atom('parent', ('?x', 'bob'))
        >>> eng = InferenceEngine()
        >>> eng.substitute(a, {'?x': 'alice'})
        parent('alice', 'bob')
        """
        # TODO - BLOCK START
        # TASK#17
        pass
        # TODO - BLOCK END

    def match_body(self, facts, body_atoms):
        """
        Enumerate all substitutions that satisfy the conjunction `body_atoms`
        against the given set of ground `facts`.

        Parameters
        ----------
        facts : iterable[Atom]
            Ground facts available in the KB.
        body_atoms : list[Atom]
            Premises (each may contain variables). Interpreted as a conjunction.

        Returns
        -------
        list[dict]
            A list of substitutions (variable→constant dicts). If empty, the
            conjunction is unsatisfied by the current facts.

        How it works
        ------------
        - Start with a single empty substitution [{}].
        - For each body atom, try to extend each partial substitution by unifying
          with *every* fact. Collect all successful extensions.
        - If any step produces no extensions, the whole conjunction fails.

        # Example 1: chaining through a shared variable (?y)
        >>> facts = {
        ...     Atom('parent', ('anna', 'bob')),
        ...     Atom('parent', ('bob', 'carol')),
        ...     Atom('parent', ('bob', 'dave')),
        ...     Atom('parent', ('eve', 'frank')),
        ... }
        >>> body = [
        ...     Atom('parent', ('?x', '?y')),
        ...     Atom('parent', ('?y', '?z')),
        ... ]
        >>> eng.match_body(facts, body)
        [{'?x': 'anna', '?y': 'bob', '?z': 'carol'},
         {'?x': 'anna', '?y': 'bob', '?z': 'dave'}]
        """
        # TODO - BLOCK START
        # TASK#18
        pass
        # TODO - BLOCK END

    def forward_chain(self, kb, max_iterations=10000):
        """
        Perform forward chaining until saturation (no new facts) or until
        `max_iterations` passes over the rule set.

        Parameters
        ----------
        kb : KnowledgeBase
            The knowledge base holding ground facts and Horn rules.
        max_iterations : int, optional
            Safety cap to prevent infinite loops in pathological inputs.

        Returns
        -------
        int
            Total number of *new* facts added during the run.

        Examples
        --------
        Basic derivation (grandparent):
        >>> kb = KnowledgeBase()
        >>> kb.add_fact('parent', 'anna', 'bob')
        >>> kb.add_fact('parent', 'bob', 'carol')
        >>> # grandparent(X,Z) :- parent(X,Y), parent(Y,Z)
        >>> kb.add_rule(
        ...     Atom('grandparent', ('?x', '?z')),
        ...     [Atom('parent', ('?x','?y')), Atom('parent', ('?y','?z'))]
        ... )
        >>> eng = InferenceEngine()
        >>> eng.forward_chain(kb)
        1
        >>> kb.query('grandparent', None, None)
        [('anna', 'carol')]
        >>> # Running again adds nothing:
        >>> eng.forward_chain(kb)
        0
        """
        # TODO - BLOCK START
        # TASK#19
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