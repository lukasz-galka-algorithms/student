from knowledge_base import KnowledgeBase, Atom
from inference_engine import InferenceEngine

class Experiment:
    """
    A class to run experiments.
    """

    @staticmethod
    def run_inference(kb, eng, max_iterations=10000):
        """
        Run forward-chaining on an existing knowledge base.

        Parameters
        ----------
        kb : KnowledgeBase
            Prepared KB (facts + rules).
        eng : InferenceEngine
            InferenceEngine instance.
        max_iterations : int
            Safety cap for forward chaining.

        Returns
        -------
        int
            Number of *new* facts added by the engine.
        """
        # TODO - BLOCK START
        # TASK#20
        pass
        # TODO - BLOCK END

    @staticmethod
    def prepare_grandparents_knowledgebase():
        """
        Build the KB for the grandparents scenario and return it WITHOUT inference.
        Facts:
          parent(anna, eva)
          parent(john, eva)
          parent(eva,  ola)
          parent(adam, peter)
          parent(peter, mark)

        Rule:
          grandparent(X,Z) :- parent(X,Y), parent(Y,Z)
        """
        # TODO - BLOCK START
        # TASK#21
        pass
        # TODO - BLOCK END

    @staticmethod
    def answer_grandparents_queries(kb):
        """
        Execute three queries on a KB *after* inference. Here, (X, Z) denotes
        **all matches** (i.e., all variable bindings) such that the atom holds.

        - "all_grandparents":    list of (X, Z) where grandparent(X, Z) holds.
        - "grandparents_of_ola": list of (X, 'ola') where grandparent(X, 'ola') holds.
        - "is_anna_grandparent_of_ola": bool, True if grandparent('anna', 'ola') holds.

        Returns a dict with those keys and values.
        """
        # TODO - BLOCK START
        # TASK#22
        return {
            "all_grandparents": None,
            "grandparents_of_ola": None,
            "is_anna_grandparent_of_ola": None,
        }
        # TODO - BLOCK END

    @staticmethod
    def experiment_grandparents(eng):
        """
        Orchestrated run:
          - prepare KB
          - run inference
          - answer queries
          - return {'added': ..., <answers...>}
        """
        kb = Experiment.prepare_grandparents_knowledgebase()
        added = Experiment.run_inference(kb, eng=eng)
        out = {"added": added}
        out.update(Experiment.answer_grandparents_queries(kb))
        return out

    @staticmethod
    def prepare_ancestors_knowledgebase():
        """
        Build the KB for recursive ancestors and return it WITHOUT inference.
        Facts:
          parent(anna, eva)
          parent(eva, ola)
          parent(ola, iza)

        Rules:
          ancestor(X,Z) :- parent(X,Z).
          ancestor(X,Z) :- parent(X,Y), ancestor(Y,Z).
        """
        # TODO - BLOCK START
        # TASK#23
        pass
        # TODO - BLOCK END

    @staticmethod
    def answer_ancestors_queries(kb):
        """
        Execute two queries on a KB *after* inference. Here, (X) denotes
        **all matches** (i.e., all variable bindings) such that the atom holds.

        - "ancestors_of_iza":         list of (X, 'iza') where ancestor(X, 'iza') holds.
        - "anna_is_ancestor_of_iza":  bool, True if ancestor('anna', 'iza') holds.

        Returns a dict with those keys and values.
        """
        # TODO - BLOCK START
        # TASK#24
        return {
            "ancestors_of_iza": None,
            "anna_is_ancestor_of_iza": None,
        }
        # TODO - BLOCK END

    @staticmethod
    def experiment_ancestors(eng):
        """
        Orchestrated run:
          - prepare KB
          - run inference
          - answer queries
          - return {'added': ..., <answers...>}
        """
        kb = Experiment.prepare_ancestors_knowledgebase()
        added = Experiment.run_inference(kb, eng=eng)
        out = {"added": added}
        out.update(Experiment.answer_ancestors_queries(kb))
        return out

    @staticmethod
    def prepare_graph_paths_knowledgebase():
        """
        Build the KB for path reachability and return it WITHOUT inference.
        Facts (directed edges):
          edge(a,b)
          edge(b,c)
          edge(c,d)
          edge(a,e)
          edge(e,f)

        Rules:
          path(X,Y) :- edge(X,Y).
          path(X,Z) :- edge(X,Y), path(Y,Z).
        """
        # TODO - BLOCK START
        # TASK#25
        pass
        # TODO - BLOCK END

    @staticmethod
    def answer_graph_paths_queries(kb):
        """
        Execute three queries on a KB *after* inference. Here, (X, Y) denotes
        **all matches** (i.e., all variable bindings) such that the atom holds.

        - "all_paths":     list of (X, Y) where path(X, Y) holds (the full reachability set).
        - "paths_from_a":  list of ('a', Y) where path('a', Y) holds (all nodes reachable from 'a').
        - "path_a_to_d":   bool, True if path('a', 'd') holds.

        Returns a dict with those keys and values.
        """
        # TODO - BLOCK START
        # TASK#26
        return {
            "all_paths": None,
            "paths_from_a": None,
            "path_a_to_d": None,
        }
        # TODO - BLOCK END

    @staticmethod
    def experiment_graph_paths(eng):
        """
        Orchestrated run:
          - prepare KB
          - run inference
          - answer queries
          - return {'added': ..., <answers...>}
        """
        kb = Experiment.prepare_graph_paths_knowledgebase()
        added = Experiment.run_inference(kb, eng=eng)
        out = {"added": added}
        out.update(Experiment.answer_graph_paths_queries(kb))
        return out

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