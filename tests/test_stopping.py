from ubr.stopping import decide

CONFIG = {
    "cycle": {"iterations_per_checkpoint": 3},
    "stopping": {
        "sota_weighted_min": 4.3,
        "sota_criterion_min": 4.0,
        "plateau_delta": 0.1,
        "plateau_window": 2,
        "min_verified_sources_ratio": 0.9,
        "min_coverage": 1.0,
        "regression_alert": -0.2,
    },
}


def entry(n, weighted, delta, min_criterion=None, coverage=1.0, verified=0.95, critical=0):
    return {
        "iteration": n,
        "weighted": weighted,
        "delta": delta,
        "min_criterion": weighted if min_criterion is None else min_criterion,
        "open_critical": critical,
        "metrics": {"coverage": coverage, "verified_ratio": verified},
    }


def test_improving_plan_continues():
    history = [entry(1, 3.0, None), entry(2, 3.4, 0.4)]
    assert decide(history, CONFIG, last_checkpoint=0).outcome == "continue"


def test_checkpoint_after_configured_number_of_iterations():
    history = [entry(1, 3.0, None), entry(2, 3.4, 0.4), entry(3, 3.8, 0.4)]
    assert decide(history, CONFIG, last_checkpoint=0).outcome == "checkpoint"
    assert decide(history, CONFIG, last_checkpoint=2).outcome == "continue"


def test_regression_stops_immediately():
    history = [entry(1, 3.5, None), entry(2, 3.2, -0.3)]
    decision = decide(history, CONFIG, last_checkpoint=0)
    assert decision.outcome == "regression"
    assert any("-0.3" in r for r in decision.reasons)


def test_sota_candidate_requires_all_gates_and_plateau():
    history = [entry(1, 4.2, None), entry(2, 4.40, 0.2), entry(3, 4.45, 0.05), entry(4, 4.50, 0.05)]
    assert decide(history, CONFIG, last_checkpoint=3).outcome == "sota-candidate"


def test_high_score_without_plateau_continues():
    history = [entry(1, 4.0, None), entry(2, 4.4, 0.4)]
    assert decide(history, CONFIG, last_checkpoint=0).outcome == "continue"


def test_open_critical_issue_blocks_sota():
    history = [entry(1, 4.4, None), entry(2, 4.45, 0.05), entry(3, 4.5, 0.05, critical=1)]
    decision = decide(history, CONFIG, last_checkpoint=2)
    assert decision.outcome == "plateau"
    assert any("critical" in r for r in decision.reasons)


def test_low_coverage_or_unverified_sources_block_sota():
    base = [entry(1, 4.4, None), entry(2, 4.45, 0.05)]
    low_cov = base + [entry(3, 4.5, 0.05, coverage=0.9)]
    low_ver = base + [entry(3, 4.5, 0.05, verified=0.5)]
    assert decide(low_cov, CONFIG, last_checkpoint=2).outcome == "plateau"
    assert decide(low_ver, CONFIG, last_checkpoint=2).outcome == "plateau"


def test_weak_criterion_blocks_sota():
    history = [entry(1, 4.4, None), entry(2, 4.45, 0.05), entry(3, 4.5, 0.05, min_criterion=3.5)]
    assert decide(history, CONFIG, last_checkpoint=2).outcome == "plateau"


def test_plateau_below_sota_asks_for_human_help():
    history = [entry(1, 3.0, None), entry(2, 3.05, 0.05), entry(3, 3.08, 0.03)]
    assert decide(history, CONFIG, last_checkpoint=2).outcome == "plateau"


def test_regression_takes_precedence_over_checkpoint():
    history = [entry(1, 3.5, None), entry(2, 3.6, 0.1), entry(3, 3.2, -0.4)]
    assert decide(history, CONFIG, last_checkpoint=0).outcome == "regression"
