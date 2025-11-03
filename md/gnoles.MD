# Gnoles

According to various sources, Gnoles are a particularly involved monster type.  \
Their stats and TP moves are alleged to change depending on how close a full moon is in-game.  \
Additionally, they have two stances: four-legged (default for **MON**), and two-legged, that they can swap between using a monsterskill.

### Alleged Behaviour Changes

- Attack varies with moon phase
- Accuracy varies with moon phase
- Evasion varies with moon phase
- Attack Speed varies with moon phase
- Base damage varies with stance
- Attack varies with stance (increased during quadruped)
- Traits change with stance
- Silver bullets/arrows force gnole to quadrupedal stance
- Gain Auto-Regen during night time

#### Attack varies with moon phase
*Confirmed, but I don't fully understand exactly how just yet.*  \
*There appears to be both a larger flat attack boost, as well as an increase in their species bonus ATK%, the closer the full moon is.*  \
*The fact that Biped attack multiplier didn't decrease between full moon and waning gibbous, but there was still a notable attack drop implies the existence of the previously mentioned flat attack boost.*

###### Observed Attack Values
*Observations were made with a LV78 Gnole that had zero instincts equipped, and instincts totalling to a flat value of +20ATK.* \
The moon phase percentage updates only at midnight Vana'diel time, it does not change in the middle of a day. \
*Numeric ranges in the Moon Phase column were reported by the `/clock on` command.*

| Moon Phase                 | Quadruped (**+0** ATK) | Quadruped (**+20** ATK) | Quadruped Boost | Biped (**+0** ATK) | Biped (**+20** ATK) | Biped Boost |
|--------------:|:-------:|:-------:|:---------:|:-------:|:-------:|:---------:|
| Full Moon                  | **524** | **554** | 30 (+50%) | **489** | **517** | 28 (+40%) |
| Waning Gibbous             | **504** | **533** | 29 (+45%) | **468** | **496** | 28 (+40%) |
| Last Quarter               | **483** | **511** | 28 (+40%) | **448** | **474** | 26 (+30%) |
| Waning Crescent *(43%-14%)*| **463** | **490** | 27 (+35%) | **428** | **453** | 25 (+25%) |
| New Moon | Not yet | Not yet | Not yet | Not yet | Not yet| Not yet |

###### Better Approximation with x/1024 Species Bonus
*The above observation obtained an approximation of the **Species Attack Bonus**, but there were one or two inconsistencies after gathering more data, and the additional fraction of a point of attack when adding `+20` Attack often was truncated with no visible impact.*  \
*With the realization that the attack buffs were also based on a 1/1024 scale instead of exact percentages, the following values were obtained.*  \
*As bipedal gnoles seem to use **Hand-to-Hand** formulae, they will likely benefit from the **Smite** trait. Currently testing whether or not the varying **Species Boost** is additive or multiplicative with **Smite**. This will likely assist with determining attack for other **MNK**-based monsters.*

The boost from the **Smite** trait seems to be additive with the **Species Bonus**, as there is an additional `52/1024` loss in the attack term between level 60 (via **Belligerency**) and 80 (obtaining **Smite II**).  \
There is unfortunately another `8/1024` loss in attack for both forms (totalling to a `60/1024` loss in attack in bipedal form) between level 60 and 80 that remains unaccounted for. \
*Tracking these down is going to be a NIGHTMARE.*

*For some reason there have also been some very slight variations (`+-1/1024`) but tracking those down is going to take time. Maybe moon phase stuff? egh*

| Stance|🌑|🌒|🌓|🌔|🌕|
|:--------:|:-------:|:-------:|:-------:|:-------:|:-------:|
| Quadruped Stance `LV80` |`+296/1024`|`+356/1024`|`+416/1024`|`+476/1024`|`+536/1024`|
| Quadruped Stance `LV60` |🌑|🌒|🌓|`+468/1024`|`+528/1024`|
| Quadruped Stance `LV30` |🌑|🌒|🌓|🌔|`+528/1024`|
| Biped Stance `LV80` |🌑|🌒|🌓|🌔| `+484/1024` |
| Biped Stance `LV60` |🌑|🌒|🌓|🌔| `+424/1024` |
| Biped Stance `LV30` |🌑|🌒|🌓|🌔| `+324/1024` |


#### Accuracy varies with moon phase
*Not tested yet.* \
`/checkparam <me>` *does not function when targeting **MON** players.*
#### Evasion varies with moon phase
*Not tested yet.*
#### Attack Speed varies with moon phase
*Not tested yet.*  \
*If there is a change in attack speed, it is likely some form of haste.*  \
*Quadrupedal gnoles have been observed to gain **+75** TP/hit regardless of moon phase so far.*
#### Base damage varies with stance
*Not tested yet.*  \
*Relying on obtaining MON damage formulae*.
#### Attack varies with stance (increased during quadruped)
[See above.](#observed-attack-values)
#### Traits change with stance
*Not tested yet.* \
*Anecdotally can agree with this assertion, have remembered only really seeing counter attacks in bipedal stance.*
#### Silver bullets/arrows force gnole to quadrupedal stance
*Not tested yet.*
#### Gain Auto-Regen during night time
*Confirmed, have not tested if potencies depend on moon phase.*  \
*Observed +20HP/tick during full moon.* \
*Observed +10HP/tick during gibbous moon.*