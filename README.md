[![make.fun · u-po-pu-the-painfully-honest-out-of-office-63e7ca0b](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![rank](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/Fawulana/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b-entry/rank.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![reward](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/Fawulana/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b-entry/reward.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)

# The Painfully Honest Out-of-Office

The line:

> Thank you for your email — I'm out of office and honestly not reading it, because a holiday spent in my inbox isn't a holiday; I'll reply with my full attention when I return.

175 characters, one sentence. It says the quiet part out loud — the
email is not being read at all, and that is deliberate, because checking
an inbox on holiday defeats the holiday — while staying warm and
professional: it thanks the sender, gives a quotable reason instead of
a complaint, and promises a proper reply with full attention on return.
Honest enough to sting, polite enough to forward to a manager.

## How the program works

`main.py` (Python standard library only, deterministic, no network)
holds the line as a constant and writes it, UTF-8 encoded, to
`/output/entry.txt`, creating the output directory if needed. Running
it twice produces byte-identical output.
