from __future__ import annotations

import collections, collections.abc
for _name in ("Mapping", "MutableMapping", "Sequence"):
    if not hasattr(collections, _name):
        setattr(collections, _name, getattr(collections.abc, _name))

from experta import KnowledgeEngine, Fact, Rule, DefFacts
from typing import Dict, List, Set, Tuple, Optional

class Assign(Fact):
    """Fact capturing a concrete assignment.

    Attributes
    ----------
    attr : str
        Attribute name (one of: ``color``, ``nation``, ``drink``, ``cigar``, ``pet``).
    value : str
        Assigned value (e.g., ``"red"``, ``"German"``).
    house : int
        House index in ``{1,2,3,4,5}``.
    """
    pass


class Rel(Fact):
    """Neighbour/ordering relation between house indices.

    Attributes
    ----------
    type : {"left_of", "right_of", "next_to"}
        Relation type.
    a : int
        First house index the relation refers to.
    b : int
        Second house index the relation refers to.
    """
    pass


class EinsteinPuzzleEngine(KnowledgeEngine):
    """Rule engine that models the Einstein riddle.

    The engine maintains *domains* (possible values) for each (attribute, house)
    cell, applies clue constraints to prune these domains, enforces per-attribute
    uniqueness, and optionally performs a small **CSP backtracking** step to
    finish the solution.

    Notes
    -----
    **CSP backtracking** is a depth‑first search that incrementally assigns
    variables and enforces constraints; on conflict it *backtracks* and tries
    alternatives, until a complete assignment satisfying all constraints is
    found. Here it is used only as a *last mile* after rule propagation.
    """

    # -------------------------- Problem constants -------------------------- #
    HOUSES = [1, 2, 3, 4, 5]

    # TODO - BLOCK START
    # TASK#2
    COLORS  = []
    NATIONS = []
    DRINKS  = []
    CIGARS  = []
    PETS    = []
    # TODO - BLOCK END

    ATTRS: Dict[str, List[str]] = {
        "color": COLORS,
        "nation": NATIONS,
        "drink": DRINKS,
        "cigar": CIGARS,
        "pet": PETS,
    }

    # ------------------------------ Lifecycle ------------------------------ #
    def __init__(self, verbose: bool = True):
        """Initialize engine state.

        Parameters
        ----------
        verbose : bool, default=True
            If ``True``, record fine-grained domain-edit events in ``event_log``.
        """
        super().__init__()
        self._in_bootstrap: bool = False
        self.verbose: bool = verbose
        # domains[attr][house] -> set of currently-possible values
        self.domains: Dict[str, Dict[int, Set[str]]] = {
            a: {h: set(vals) for h in EinsteinPuzzleEngine.HOUSES} for a, vals in EinsteinPuzzleEngine.ATTRS.items()
        }
        # rule-level and event-level logs
        self.rules_log: List[str] = []
        self.event_log: List[str] = []

    # ------------------------------- Logging ------------------------------- #
    def _log_rule(self, name: str) -> None:
        """Append a high-level log entry (e.g., which clue applied).

        Parameters
        ----------
        name : str
            A short label for the rule/phase that fired.
        """
        self.rules_log.append(name)

    def _log_event(self, msg: str) -> None:
        """Append a low-level domain-edit log entry if ``verbose`` is enabled.

        Parameters
        ----------
        msg : str
            Human-readable description of a domain edit.
        """
        if self.verbose:
            self.event_log.append(msg)

    # -------------------------- Snapshots & checks ------------------------- #
    def _snapshot(self) -> Dict[str, Dict[int, Set[str]]]:
        """Return a deep copy of current domains (used by CSP backtracking).

        Returns
        -------
        dict[str, dict[int, set[str]]]
            A deep copy of the domains structure.
        """
        # TODO - BLOCK START
        # TASK#3
        pass
        # TODO - BLOCK END

    def _restore(self, snap: Dict[str, Dict[int, Set[str]]]) -> None:
        """Restore domains from a snapshot created by :meth:`_snapshot`.

        Parameters
        ----------
        snap : dict[str, dict[int, set[str]]]
            A snapshot previously returned by :meth:`_snapshot`.
        """
        # TODO - BLOCK START
        # TASK#4
        pass
        # TODO - BLOCK END

    def _is_consistent(self) -> bool:
        """Check that every value remains placeable in at least one house.

        Returns
        -------
        bool
            ``True`` iff no value has been globally ruled out for its attribute.
        """
        # TODO - BLOCK START
        # TASK#5
        pass
        # TODO - BLOCK END

    # -------------------------- Domain primitives -------------------------- #
    def discard_value_with_reason(self, attr: str, house: int, value: str, reason: str) -> bool:
        """Remove a candidate value from a cell and log the reason.

        Parameters
        ----------
        attr : str
            Attribute row name (e.g., ``"color"``).
        house : int
            House index in ``{1,2,3,4,5}``.
        value : str
            Candidate value to remove.
        reason : str
            Human-readable reason (used for logging/tracing).

        Returns
        -------
        bool
            ``True`` if anything changed (the value was present and removed).
        """
        # TODO - BLOCK START
        # TASK#6
        pass
        # TODO - BLOCK END

    def set_singleton_with_reason(self, attr: str, house: int, value: str, reason: str) -> bool:
        """Force a cell's domain to a single value and log removals.

        Parameters
        ----------
        attr : str
            Attribute row name (e.g., ``"color"``).
        house : int
            House index in ``{1,2,3,4,5}``.
        value : str
            The single value to keep.
        reason : str
            Human-readable reason (used for logging/tracing).

        Returns
        -------
        bool
            ``True`` if the domain changed (i.e., became a different singleton).
        """
        # TODO - BLOCK START
        # TASK#7
        pass
        # TODO - BLOCK END

    def assign_singleton_with_uniqueness(self, attr: str, value: str, house: int, source: str = "", record_fact: Optional[bool] = None) -> bool:
        """Assign a singleton and enforce per-attribute uniqueness.

        Parameters
        ----------
        attr : str
            Attribute row name.
        value : str
            Value to assign.
        house : int
            House index in ``{1,2,3,4,5}``.
        source : str, optional
            A short label describing why/how the assignment happened (for logs).
        record_fact : bool or None, optional
            If ``True``, declare an :class:`Assign` fact in the engine agenda.
            If ``None``, this is automatically disabled during bootstrap.

        Returns
        -------
        bool
            ``True`` if any domain changed.
        """
        # TODO - BLOCK START
        # TASK#8
        pass
        # TODO - BLOCK END

    def enforce_global_uniqueness_closure(self) -> bool:
        """Iteratively assign any value that has exactly one possible house left.

        Returns
        -------
        bool
            ``True`` if new assignments were made during closure.
        """
        changed = False
        progress = True
        while progress:
            progress = False
            for attr, vals in EinsteinPuzzleEngine.ATTRS.items():
                for v in vals:
                    possible = [h for h in EinsteinPuzzleEngine.HOUSES if v in self.domains[attr][h]]
                    if len(possible) == 1:
                        if self.assign_singleton_with_uniqueness(attr, v, possible[0], source=f"unique({attr}:{v})"):
                            progress = True; changed = True
        return changed

    # ----------------------------- Constraints ----------------------------- #
    def enforce_left_of_constraint(self, attr: str, left_value: str, right_value: str, clue: str) -> bool:
        """Apply a "left-of" ordering within a *single* attribute row.

        Parameters
        ----------
        attr : str
            Attribute row (e.g., ``"color"``).
        left_value : str
            Value that must be immediately to the left.
        right_value : str
            Value that must be immediately to the right.
        clue : str
            Label used in logs to trace which clue triggered the pruning.

        Returns
        -------
        bool
            ``True`` if any domain changed.
        """
        changed = False
        changed |= self.discard_value_with_reason(attr, 5, left_value,  f"{clue} edge")
        changed |= self.discard_value_with_reason(attr, 1, right_value, f"{clue} edge")
        for h in EinsteinPuzzleEngine.HOUSES:
            if left_value in self.domains[attr][h]:
                if h+1 not in EinsteinPuzzleEngine.HOUSES or right_value not in self.domains[attr][h+1]:
                    changed |= self.discard_value_with_reason(attr, h, left_value,  f"{clue} pair")
            if right_value in self.domains[attr][h]:
                if h-1 not in EinsteinPuzzleEngine.HOUSES or left_value not in self.domains[attr][h-1]:
                    changed |= self.discard_value_with_reason(attr, h, right_value, f"{clue} pair")
        return changed

    def enforce_same_house_equivalence(self, a1: str, v1: str, a2: str, v2: str, clue: str) -> bool:
        """Link two attributes by equivalence within the same house.

        Encodes: ``(a1=v1) ⇔ (a2=v2)``.

        Parameters
        ----------
        a1, a2 : str
            Attribute names to link.
        v1, v2 : str
            Values that must co-occur in the same house.
        clue : str
            Label used in logs.

        Returns
        -------
        bool
            ``True`` if any domain changed.
        """
        changed = False
        for h in EinsteinPuzzleEngine.HOUSES:
            d1, d2 = self.domains[a1][h], self.domains[a2][h]
            if v1 not in d1 and v2 in d2:
                changed |= self.discard_value_with_reason(a2, h, v2, f"{clue} link")
            if v2 not in d2 and v1 in d1:
                changed |= self.discard_value_with_reason(a1, h, v1, f"{clue} link")
            if d1 == {v1} and d2 != {v2}:
                if self.set_singleton_with_reason(a2, h, v2, reason=f"{clue} enforce"): changed = True
            if d2 == {v2} and d1 != {v1}:
                if self.set_singleton_with_reason(a1, h, v1, reason=f"{clue} enforce"): changed = True
        return changed

    def enforce_cross_attribute_adjacency(self, a1: str, v1: str, a2: str, v2: str, clue: str) -> bool:
        """Link two attributes by *adjacency* across neighbouring houses.

        Encodes: ``|pos(a1=v1) - pos(a2=v2)| = 1``.

        Parameters
        ----------
        a1, a2 : str
            Attribute names to link across neighbours.
        v1, v2 : str
            Values that must be placed next to each other (in either order).
        clue : str
            Label used in logs.

        Returns
        -------
        bool
            ``True`` if any domain changed.
        """
        changed = False
        for h in EinsteinPuzzleEngine.HOUSES:
            if v1 in self.domains[a1][h]:
                neigh = [n for n in (h-1, h+1) if n in EinsteinPuzzleEngine.HOUSES]
                if not any(v2 in self.domains[a2][n] for n in neigh):
                    changed |= self.discard_value_with_reason(a1, h, v1, f"{clue} no-neighbour")
            if v2 in self.domains[a2][h]:
                neigh = [n for n in (h-1, h+1) if n in EinsteinPuzzleEngine.HOUSES]
                if not any(v1 in self.domains[a1][n] for n in neigh):
                    changed |= self.discard_value_with_reason(a2, h, v2, f"{clue} no-neighbour")
        return changed

    # --------------------------- Individual clues --------------------------- #
    def apply_clue_01_brit_lives_in_red_house(self) -> bool:
        """(1) *The Brit lives in the red house.*

        Returns
        -------
        bool
            ``True`` if the domains were pruned.
        """
        # TODO - BLOCK START
        # TASK#9
        pass
        # TODO - BLOCK END

    def apply_clue_02_swede_keeps_dogs(self) -> bool:
        """(2) *The Swede keeps dogs.*"""
        # TODO - BLOCK START
        # TASK#10
        pass
        # TODO - BLOCK END

    def apply_clue_03_dane_drinks_tea(self) -> bool:
        """(3) *The Dane drinks tea.*"""
        # TODO - BLOCK START
        # TASK#11
        pass
        # TODO - BLOCK END

    def apply_clue_04_green_left_of_white(self) -> bool:
        """(4) *The green house is immediately to the left of the white house.*"""
        # TODO - BLOCK START
        # TASK#12
        pass
        # TODO - BLOCK END

    def apply_clue_05_green_house_drinks_coffee(self) -> bool:
        """(5) *The green house’s owner drinks coffee.*"""
        # TODO - BLOCK START
        # TASK#13
        pass
        # TODO - BLOCK END

    def apply_clue_06_pallmall_smoker_rears_birds(self) -> bool:
        """(6) *The person who smokes Pall Mall rears birds.*"""
        # TODO - BLOCK START
        # TASK#14
        pass
        # TODO - BLOCK END

    def apply_clue_07_yellow_house_smokes_dunhill(self) -> bool:
        """(7) *The owner of the yellow house smokes Dunhill.*"""
        # TODO - BLOCK START
        # TASK#15
        pass
        # TODO - BLOCK END

    def apply_clue_08_middle_house_drinks_milk(self) -> bool:
        """(8) *Center house drinks milk.* Seeded in bootstrap (no-op here)."""
        return False

    def apply_clue_09_norwegian_lives_in_first_house(self) -> bool:
        """(9) *Norwegian lives in the first house.* Seeded in bootstrap (no-op)."""
        return False

    def apply_clue_10_blend_smoker_next_to_cats(self) -> bool:
        """(10) *The Blend smoker lives next to the one who keeps cats.*"""
        # TODO - BLOCK START
        # TASK#16
        pass
        # TODO - BLOCK END

    def apply_clue_11_horse_next_to_dunhill_smoker(self) -> bool:
        """(11) *The horse owner lives next to the man who smokes Dunhill.*"""
        # TODO - BLOCK START
        # TASK#17
        pass
        # TODO - BLOCK END

    def apply_clue_12_bluemaster_smoker_drinks_beer(self) -> bool:
        """(12) *The BlueMaster smoker drinks beer.*"""
        # TODO - BLOCK START
        # TASK#18
        pass
        # TODO - BLOCK END

    def apply_clue_13_german_smokes_prince(self) -> bool:
        """(13) *The German smokes Prince.*"""
        # TODO - BLOCK START
        # TASK#19
        pass
        # TODO - BLOCK END

    def apply_clue_14_norwegian_next_to_blue_house(self) -> bool:
        """(14) *The Norwegian lives next to the blue house.*"""
        # TODO - BLOCK START
        # TASK#20
        pass
        # TODO - BLOCK END

    def apply_clue_15_blend_smoker_next_to_water(self) -> bool:
        """(15) *The Blend smoker has a neighbour who drinks water.*"""
        # TODO - BLOCK START
        # TASK#21
        pass
        # TODO - BLOCK END

    # -------------------- One pass over clues + uniqueness ------------------ #
    def apply_all_clues_once(self) -> bool:
        """Apply all clues once and then run uniqueness closure.

        Returns
        -------
        bool
            ``True`` if any domain changed due to clues or closure.
        """
        changed = False
        for name, fn in [
            ("clue#01 brit→red", self.apply_clue_01_brit_lives_in_red_house),
            ("clue#02 swede→dogs", self.apply_clue_02_swede_keeps_dogs),
            ("clue#03 dane→tea", self.apply_clue_03_dane_drinks_tea),
            ("clue#04 green left of white", self.apply_clue_04_green_left_of_white),
            ("clue#05 green→coffee", self.apply_clue_05_green_house_drinks_coffee),
            ("clue#06 PallMall→birds", self.apply_clue_06_pallmall_smoker_rears_birds),
            ("clue#07 yellow→Dunhill", self.apply_clue_07_yellow_house_smokes_dunhill),
            ("clue#08 middle→milk", self.apply_clue_08_middle_house_drinks_milk),
            ("clue#09 Norwegian@1", self.apply_clue_09_norwegian_lives_in_first_house),
            ("clue#10 Blend next to cats", self.apply_clue_10_blend_smoker_next_to_cats),
            ("clue#11 horse next to Dunhill", self.apply_clue_11_horse_next_to_dunhill_smoker),
            ("clue#12 BlueMaster→beer", self.apply_clue_12_bluemaster_smoker_drinks_beer),
            ("clue#13 German→Prince", self.apply_clue_13_german_smokes_prince),
            ("clue#14 Norwegian next to blue", self.apply_clue_14_norwegian_next_to_blue_house),
            ("clue#15 Blend next to water", self.apply_clue_15_blend_smoker_next_to_water),
        ]:
            if fn():
                self._log_rule(name)
                changed = True
        if self.enforce_global_uniqueness_closure():
            self._log_rule("unique-closure")
            changed = True
        return changed

    # ------------------------------ Bootstrap ------------------------------ #
    @DefFacts()
    def _bootstrap(self):
        """Seed base facts and initial clues before the engine runs.

        Yields
        ------
        Fact
            - ``Fact(house=h)`` for ``h`` in 1..5
            - :class:`Rel` relations for left/right/next_to between house indices
            - ``Fact(initialized=True)`` at the end to trigger the rules

        Notes
        -----
        During bootstrap we *avoid* declaring :class:`Assign` facts to the engine
        (``self._in_bootstrap = True``). We assign two given clues directly:
        Norwegian@1 and milk@3 (center house). Then we run one pass of clues to
        propagate obvious consequences before regular rule execution.
        """
        for h in EinsteinPuzzleEngine.HOUSES:
            yield Fact(house=h)
        for a in EinsteinPuzzleEngine.HOUSES:
            if a < 5:
                yield Rel(type='left_of', a=a, b=a+1)
            if a > 1:
                yield Rel(type='right_of', a=a, b=a-1)
        for a in EinsteinPuzzleEngine.HOUSES:
            for b in EinsteinPuzzleEngine.HOUSES:
                if abs(a-b) == 1:
                    yield Rel(type='next_to', a=a, b=b)

        self._in_bootstrap = True
        self.assign_singleton_with_uniqueness("nation", "Norwegian", 1, source="clue#9")
        self.assign_singleton_with_uniqueness("drink", "milk", 3, source="clue#8")
        while self.apply_all_clues_once():
            pass
        self._in_bootstrap = False
        yield Fact(initialized=True)

    # ----------------------- Rule that runs the engine ---------------------- #
    @Rule(Fact(initialized=True))
    def run_all_clues_until_stable(self):
        """Keep applying clues + closure until no further change occurs."""
        while self.apply_all_clues_once():
            self._log_rule("iteration")

    # ------------------------------- Solving ------------------------------- #
    def solve(self) -> bool:
        """Run the engine and, if needed, finish with CSP backtracking.

        Returns
        -------
        bool
            ``True`` if a consistent assignment was found (it should be unique).
        """
        self.reset()
        self.run()
        if all(len(self.domains[attr][h]) == 1 for attr in EinsteinPuzzleEngine.ATTRS for h in EinsteinPuzzleEngine.HOUSES):
            return True
        return self._csp_backtracking_last_mile()

    def _choose_mrv_variable(self) -> Tuple[str, int] | None:
        """Choose the next variable using MRV (minimum remaining values) heuristic.

        Returns
        -------
        tuple[str, int] | None
            The pair ``(attr, house)`` to branch on, or ``None`` if all are fixed.
        """
        best = None; size = 10**9
        for attr in EinsteinPuzzleEngine.ATTRS:
            for h in EinsteinPuzzleEngine.HOUSES:
                d = self.domains[attr][h]
                if 1 < len(d) < size:
                    size = len(d); best = (attr, h)
        return best

    def _csp_backtracking_last_mile(self) -> bool:
        """Minimal backtracking to finish the puzzle if propagation alone stalls.

        Returns
        -------
        bool
            ``True`` if a consistent complete assignment is found.
        """
        if all(len(self.domains[attr][h]) == 1 for attr in EinsteinPuzzleEngine.ATTRS for h in EinsteinPuzzleEngine.HOUSES):
            return True
        var = self._choose_mrv_variable()
        if not var:
            return True
        attr, h = var
        for v in list(self.domains[attr][h]):
            snap = self._snapshot()
            self.assign_singleton_with_uniqueness(attr, v, h, source="CSP")
            while self.apply_all_clues_once():
                pass
            if self._is_consistent() and self._csp_backtracking_last_mile():
                return True
            self._restore(snap)
        return False

    # ------------------------------ Formatting ----------------------------- #
    def table(self) -> Dict[int, Dict[str, str]]:
        """Return a solved (or partial) table mapping ``house -> {attr: value}``.

        Any cell that is not yet a singleton is shown as ``"?"``.

        Returns
        -------
        dict[int, dict[str, str]]
            Human-readable table view of current assignments.
        """
        t = {h: {} for h in EinsteinPuzzleEngine.HOUSES}
        for attr in ("color","nation","drink","cigar","pet"):
            for h in EinsteinPuzzleEngine.HOUSES:
                vals = list(self.domains[attr][h])
                t[h][attr] = vals[0] if len(vals) == 1 else "?"
        return t

    def pretty_table(self) -> str:
        """Render the table using Unicode box-drawing characters.

        Returns
        -------
        str
            A multiline string containing the formatted table.
        """
        t = self.table()
        cols = ["color","nation","drink","cigar","pet"]
        widths = {c: max(len(c), max(len(t[h][c]) for h in EinsteinPuzzleEngine.HOUSES)) for c in cols}
        top =    "┌" + "┬".join("".ljust(widths[c]+2, "─") for c in cols) + "┐"
        header = "│ " + " │ ".join(c.upper().ljust(widths[c]) for c in cols) + " │"
        sep =    "├" + "┼".join("".ljust(widths[c]+2, "─") for c in cols) + "┤"
        lines = ["┌────────┬" + "".ljust(len(header)-2, "─") + "┐",
                 "│ HOUSE  │" + header[1:],
                 "├────────┼" + sep[1:]]
        for h in EinsteinPuzzleEngine.HOUSES:
            row = "│ {:>6} │ ".format(h) + " │ ".join(t[h][c].ljust(widths[c]) for c in cols) + " │"
            lines.append(row)
        lines.append("└────────┴" + top[1:])
        return "\n".join(lines)

    # ------------------------------- Q&A API ------------------------------- #
    def get_house_by(self, attr: str, value: str, return_candidates: bool = False) -> Optional[int] | List[int]:
        """Find the house where ``attr == value``.

        Parameters
        ----------
        attr : str
            Attribute name (``color``, ``nation``, ``drink``, ``cigar``, ``pet``).
        value : str
            Desired value (e.g., ``"water"``).
        return_candidates : bool, default=False
            If ``True`` and the position is not unique, return *all* candidate houses.

        Returns
        -------
        int or list[int] or None
            The unique house index, or (if requested) a list of candidates, or ``None``.
        """
        # TODO - BLOCK START
        # TASK#22
        pass
        # TODO - BLOCK END

    def get_value_at(self, house: int, attr: str, return_candidates: bool = False) -> Optional[str] | List[str]:
        """Read the value of an attribute in a given house.

        Parameters
        ----------
        house : int
            House index in ``{1,2,3,4,5}``.
        attr : str
            Attribute to inspect.
        return_candidates : bool, default=False
            If ``True`` and not fixed yet, return the list of candidates.

        Returns
        -------
        str or list[str] or None
            The unique value, a list of candidates, or ``None``.
        """
        # TODO - BLOCK START
        # TASK#23
        pass
        # TODO - BLOCK END

    def get_nation_in_house(self, house: int) -> Optional[str]:
        """Convenience: return the nation living in the given house (if known).

        Parameters
        ----------
        house : int
            House index.

        Returns
        -------
        str or None
            The nation if fixed, otherwise ``None``.
        """
        return self.get_value_at(house, "nation")

    def get_value_for_nation(self, nation: str, attr: str, return_candidates: bool = False) -> Optional[str] | List[str]:
        """Return the value of ``attr`` for the specified ``nation``.

        Parameters
        ----------
        nation : str
            One of ``British``, ``Swedish``, ``Danish``, ``Norwegian``, ``German``.
        attr : str
            Attribute name.
        return_candidates : bool, default=False
            If ``True`` and not fixed yet, return the candidate list.

        Returns
        -------
        str or list[str] or None
            The unique value, the candidate list, or ``None`` if the nation’s
            house is not yet uniquely identified.
        """
        h = self.get_house_by("nation", nation, return_candidates=False)
        if h is None:
            return [] if return_candidates else None
        return self.get_value_at(h, attr, return_candidates=return_candidates)

    # ---- WHO … ? ----------------------------------------------------------- #
    def quiz_who_drinks(self, drink: str) -> Optional[Tuple[int, str]]:
        """Return ``(house, nation)`` of the person who drinks ``drink`` (if unique).

        Parameters
        ----------
        drink : str
            One of :data:`DRINKS`.

        Returns
        -------
        tuple[int, str] or None
            House number and nation, or ``None`` if not uniquely determined.
        """
        h = self.get_house_by("drink", drink)
        return (h, self.get_nation_in_house(h)) if h else None

    def quiz_who_keeps(self, pet: str) -> Optional[Tuple[int, str]]:
        """Return ``(house, nation)`` of the person who keeps ``pet`` (if unique).

        Parameters
        ----------
        pet : str
            One of :data:`PETS`.
        """
        h = self.get_house_by("pet", pet)
        return (h, self.get_nation_in_house(h)) if h else None

    def quiz_who_smokes(self, cigar: str) -> Optional[Tuple[int, str]]:
        """Return ``(house, nation)`` of the person who smokes ``cigar`` (if unique).

        Parameters
        ----------
        cigar : str
            One of :data:`CIGARS`.
        """
        h = self.get_house_by("cigar", cigar)
        return (h, self.get_nation_in_house(h)) if h else None

    def quiz_who_lives_in_color(self, color: str) -> Optional[Tuple[int, str]]:
        """Return ``(house, nation)`` for the house with wall color ``color`` (if unique).

        Parameters
        ----------
        color : str
            One of :data:`COLORS`.
        """
        h = self.get_house_by("color", color)
        return (h, self.get_nation_in_house(h)) if h else None

    # ---- WHAT does a nation … ? ------------------------------------------- #
    def quiz_what_does_nation_drink(self, nation: str) -> Optional[str]:
        """Return the drink for ``nation`` (if determined)."""
        return self.get_value_for_nation(nation, "drink")

    def quiz_what_pet_does_nation_keep(self, nation: str) -> Optional[str]:
        """Return the pet for ``nation`` (if determined)."""
        return self.get_value_for_nation(nation, "pet")

    def quiz_what_cigar_does_nation_smoke(self, nation: str) -> Optional[str]:
        """Return the cigar brand for ``nation`` (if determined)."""
        return self.get_value_for_nation(nation, "cigar")

    def quiz_what_color_is_nations_house(self, nation: str) -> Optional[str]:
        """Return the house color for ``nation`` (if determined)."""
        return self.get_value_for_nation(nation, "color")

    # ---- Neighbours -------------------------------------------------------- #
    def quiz_neighbors_of_nation(self, nation: str) -> List[Tuple[int, Optional[str]]]:
        """Return neighbours of ``nation`` as ``[(house, nation_or_None), ...]``.

        Parameters
        ----------
        nation : str
            Nation whose neighbours should be reported.

        Returns
        -------
        list[tuple[int, str|None]]
            For each neighbouring house: its index and the neighbour’s nation if
            known (otherwise ``None``).
        """
        h = self.get_house_by("nation", nation)
        if not h:
            return []
        neigh = [n for n in (h-1, h+1) if n in EinsteinPuzzleEngine.HOUSES]
        return [(n, self.get_nation_in_house(n)) for n in neigh]

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