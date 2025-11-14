Information largely sourced from [Jimmayus' Spreadsheet](https://docs.google.com/spreadsheets/d/1YBoveP-weMdidrirY-vPDzHyxbEI2ryECINlfCnFkLI):


# Physical Damage

$$  Damage = DMG \cdot pDIF \cdot RandomMult  $$
$$  DMG = ((Level \cdot DMG_{MULT}) + Offset + fSTR) \cdot H2H Penalty  $$
$$  fSTR = -2 \cdot (1 + \tfrac{Level}{5}) \leq fSTR_{RAW} \leq 5 + \tfrac{Level}{5} $$
$$
fSTR_{RAW} = \begin{cases}
    \frac{dSTR - 4}{4} &\text{if } dSTR \geq 36  \\
    \frac{dSTR - 3}{4} &\text{if } 26 \leq dSTR \leq 35  \\
    \frac{dSTR - 2}{4} &\text{if } 17 \leq dSTR \leq 25  \\
    \frac{dSTR - 1}{4} &\text{if } 4 \leq dSTR \leq 16  \\
    \frac{dSTR    }{4} &\text{if } -8 \leq dSTR \leq 3  \\
    \frac{dSTR + 1}{4} &\text{if } -13 \leq dSTR \leq -9  \\
    \frac{dSTR + 3}{4} &\text{if } -19 \leq dSTR \leq -14  \\
    \frac{dSTR + 4}{4} &\text{if } -32 \leq dSTR \leq -20  \\
    \frac{dSTR + 5}{4} &\text{if } -42 \leq dSTR \leq -33  \\
    \frac{dSTR + 6}{4} &\text{if } -54 \leq dSTR \leq -43  \\
    \frac{dSTR + 7}{4} &\text{if } -67 \leq dSTR \leq -55  \\
    \frac{dSTR + 8}{4} &\text{if } -76 \leq dSTR \leq -68  \\
    \frac{dSTR + 9}{4} &\text{if } dSTR \leq -77  \\
\end{cases}
$$

## pDIF Limits
It seems that (at least outgoing) physical damage in Monstrosity departs from player damage in a couple of interesting manners:

The `Damage Limit+` trait (from `WAR` job), despite allegedly being present\footnote[1], seems to have zero effect on `pDIF` cap values.
_The same damage ranges were observed for the Coeurl's (`WAR`/`WAR`) melee attacks as the Collared Lynx's (`RDM`/`BLM`)._

`Critical Hits` do _not_ seem to have a higher `pDIF` cap compared to non-critical hits.
_The same damage ranges were observed for the Collared Lynx's (`RDM`/`BLM`) regular and critical melee attacks._
_The Coeurl's (`WAR`/`WAR`) did vary between regular and critical hits, due to the `Crit. Atk. Bonus` trait, but when that was factored out, critical hits had the same range as regular melee attacks._
_Gnoles (once again are weird) in quadrupedal stance functioned similarly to above but when in bipedal stance they seemed to use player Hand-to-Hand calculations (also seems to have a Base Damage of 72)._
_This matched jimmayus' calculations for Base Damage using `Offset` of 2, `DMGMULT` of 5/3, and `H2HPENALTY` of 0.425._
_Testing in ToAU zones will need to be done, as the numbers below were obtained in early-game zones._

By attacking very low-level enemies to guarantee that the `fSTR` and `pDIF` values were capped (due to their very low `VIT` and `Defense`), a LV90 Coeurl and Collared Lynx were observed to provide these damage numbers:

[See here](/md/coeurl_attacks.MD) for the table of observed values.

| Variant | Crit? | Minimum Hit | Maximum Hit |
|:-------:|:-----:|:-----------:|:-----------:|
| LV90 Coeurl  | No    | 402 | 422 |
| LV90 Coeurl  | Yes   | 434 | 455 |
| LV90 Collared Lynx | No  | 402 | 422 |
| LV90 Collared Lynx | Yes | 402 | 422 |
| LV80 Gnole (Quadruped) | No  | 375 | 393 |
| LV80 Gnole (Quadruped) | Yes | 375 | 393 |
| LV80 Gnole (Biped) | No  | 252 | 264 |
| LV80 Gnole (Biped) | Yes | **324** | **340** |