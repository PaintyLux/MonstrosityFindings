# Attack

### Current Working Formula

*The attack job for **MON** players appears to use the same calculations for monsters.* \
*Formula courtesy of [Operation Bluffalo](https://docs.google.com/spreadsheets/d/1i-Z4A4GLfhvKg_3QFQDA9WZ-M8Gb-g1v_KyHNa24G7s/edit?gid=224123492#gid=224123492).*

---

`Attack` = 
⌊`Base Attack` × `(1 + Species Bonus)` × `(1 + Instinct Attack% Bonus Total)`⌋

Where: \
`Base Attack` is equal to:  \
(`8` + `Combat Skill` + ⌊`STR/2`⌋ + `Attack Bonus Trait` + `Instinct Flat Attack Bonus`)

---

Similar to other Attack-boosting multipliers (e.g. Corsair's **Chaos Roll**), it's believed that the **Species Bonus** is not an exact percentage, but an approximation in the form `x/1024`.

*The following values have been proven by attempting to isolate unique values using instincts to manipulate the attack value.*

| Species/Family    | Species Bonus | Approximation |
|:-----------------:|:-------------:|:-------------:|
| Behemoth Family   | `512/1024`    | 50%           |
| Coeurl Family     | `100/1024`    | 10%           |
| Eft Family        | `100/1024`    | 10%           |
| Opo-opo Family    | `100/1024`    | 10%           |
| Rabbit Family     | `100/1024`    | 10%           |
| Tiger Family      | `204/1024`    | 20%           |

*A working example would be as follows:*

A **LV75 Smilodon** has the following:

`+8` ATK from the universal attack constant\
`+276` ATK from **Combat Skill**\
`+45` ATK from **90** STR\
`+22` ATK from **WAR's Attack Bonus II**\

![alt text](/img/stats_smilodon_base.png)

Resulting in a **Base Attack** of `351`, with a **Displayed Attack** of `420`.  \
This limits the possible **Species Bonus** to `202/1024`, `203/1024`, and `204/1024`.

By adding an additional `+1` ATK (using a **Hume's Instinct I** for `+2` STR), the **Displayed Attack** increases to `422`.

This separates the `204/1024` coefficient, while matching up with values displayed in-game.

`352` × `(1 + 202/1024)` = ⌊`421.43750`⌋ = `421`  \
`352` × `(1 + 203/1024)` = ⌊`421.78125`⌋ = `421` \
`352` × `(1 + 204/1024)` = ⌊`422.12500`⌋ = `422`

![alt text](/img/instinct_smilodon_2status.png)

*This works better at higher levels as the much larger base attack value from combat skill disperses possible results significantly more than lower base attack values can.* \
*There is also potential to prove values with the inverse of this logic, by it **not** providing the expected values in game, it may be possible to exclude coefficients from consideration. Will explore at a later point if necessary, but positive proof for values is currently personally preferred.*

*Gnoles are a whole kettle of fish on their own.*