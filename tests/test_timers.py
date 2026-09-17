from nanotron.logging.timers import TimerType, Timers


def _reset_timers() -> Timers:
    timers = Timers()
    timers._timers.clear()
    Timers.disable()
    return timers


def test_global_enable_state_applies_to_new_and_existing_timers():
    timers = _reset_timers()

    existing = timers("existing", timer_type=TimerType.CPU)
    assert existing.enabled is False

    Timers.enable()
    assert existing.enabled is True
    assert timers("created-after-enable", timer_type=TimerType.CPU).enabled is True

    Timers.disable()
    assert existing.enabled is False
    assert timers("created-after-disable", timer_type=TimerType.CPU).enabled is False


def test_explicit_enabled_setting_overrides_global_state_at_creation():
    timers = _reset_timers()

    forced_on = timers("forced-on", timer_type=TimerType.CPU, enabled=True)
    assert forced_on.enabled is True

    Timers.enable()
    forced_off = timers("forced-off", timer_type=TimerType.CPU, enabled=False)
    assert forced_off.enabled is False

    Timers.disable()
