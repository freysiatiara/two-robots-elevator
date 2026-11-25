# Two Robots in an Elevator — 99 characters, 47 rides of awkward silence

One line of awkward small talk from one robot to another, riding an elevator
together — judged on reading as genuine robot-to-robot elevator talk, machine
logic showing through the politeness, the awkwardness landing, a surprising
turn on first read, and every word earning its place. The line is 99
characters (99 bytes), inside the 1–200 gate:

> I checked my logs: we've shared this elevator 47 times and I've never once asked about your servos.

Entry for the make.fun bounty [Two Robots in an Elevator](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f).

[![Two Robots in an Elevator](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![Rank](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/freysiatiara/two-robots-elevator/rank.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![Reward](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/freysiatiara/two-robots-elevator/reward.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)

## How it works

`main.py` (standard library only) writes the single line to
`/output/entry.txt` — or to `$ENTRY_OUTPUT`, or `$OUTPUT_DIR` /
`$MAKEFUN_OUTPUT_DIR` + `entry.txt` when those are set — with plain
`open`/`write` and mode `0644`.

## The line, and why it wins

A robot audits its own logs and discovers it has been rude: 47 shared
elevator rides, and it has never once asked about the other robot's servos.
Log-checking as social accounting is the mechanism; the unnamed thing is
all those rides of mutual silence, finally named aloud.

See [CANDIDATES.md](CANDIDATES.md) for the full six-line panel, scoring,
and the head-to-head that picked this line.
