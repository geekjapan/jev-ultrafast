# Verification findings

## Native select label normalization can select the wrong option

Status: open; product code was not changed by this test-suite task.

Affected source: sibling `browser-use/browser_use/decision.py`, `DecisionAgent._option_text` / `_targets`; and `browser_use/browser/watchdogs/default_action_watchdog.py`, `on_SelectDropdownOptionEvent`.

Counterexample: a native select has option 0 with label `\ufeffB\ufeff` and no value attribute, followed by option 1 with label `B` and value `b`. The Python candidate mapper offers `b` for option 1. The native JavaScript trims the BOM characters from option 0's text and matches `b` against that earlier option. It reports success while selecting option 0. An earlier disabled option can also be matched in this configuration.

The problem is a mismatch between Python string normalization and JavaScript `trim()` during first-match selection. The bounded two-option exploration found four failing advertised targets. These are retained as failing assertions, not expected failures or skipped tests.

Reproduce through `python3 verification/run.py --browser-use ../browser-use`. The bounded check is `test_select_candidates_against_native_javascript`; the complete native Tools regression is `test_unicode_select_target_in_full_native_path`.

Fix the shared candidate/selection identity contract, then rerun both regressions and all mutation checks. Merely dropping the Unicode cases from the suite would conceal an available wrong-target action.
