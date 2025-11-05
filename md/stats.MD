# Current Hypotheses

## Merits

Merits affect stats when the player is participating in **Monstrosity**, as they do when the player has other jobs equipped.

#### Reasoning

[See here](/md/merits.MD#merits-affecting-monsters) for supporting image evidence.

Monsters are assumed to have internal "jobs", and some are a combination of jobs with no native MP.  \
&nbsp;&nbsp;e.g. **WAR**/**WAR** or **MNK**/**MNK**  \
When neither the player's main- nor sub-job have native MP, they still gain MP from merits.  \
This behaviour was also observed in **Monstrosity**, where monsters that should not have MP, instead had maximum MP exactly matching merit contribution for their level.  \
Reducing merits in base stats (tested with **STR**) was also observed to reduce the matching stat while being a monster.

|Merits        |  HP     |  MP   |  STR |
|:------------:|:-------:|:-----:|:----:|
| Full         |**15573**|**150**|**90**|
| 13HP + 13MP  |**15517**|**130**|**90**|
| 13MP + 14STR |**15573**|**130**|**89**|

## HP

### Best Guess at Formula

$`
monsterHP = \lfloor (Innate HP + Flat HP Bonus) \cdot Species Boost _{HP} \cdot \sum Instinct HP_{\%} \rfloor
`$

$`
Flat HP Bonus = \lfloor Trait HP + Merit HP \rfloor
`$

### MON Species HP% Boosts

[See here](/md/hp.MD#species-hp-boost) for supporting image evidence.

**MON having species-dependant HP% Boosts**  \
After noticing merits affeting monster stats, removed 2 merits from HP and MP.  \
*(Changing a stat by **20** covers increments of **5%**, and will hopefully catch the most likely multipliers i.e. **5%**, **10%**, **20%**, **25%**, **30%** etc.)* \
In every case, there was **significantly** more than a **20HP** difference, but was not consistent across all species.

| Merits     | Gnole   | Coeurl  | Lynx    | Collared Lynx | Smilodon |
|:----------:|:-------:|:-------:|:-------:|:-------:|:-------:|
|  13HP      |**15517**|**14865**|**14340**|**12739**|**11661**|
|  15HP      |**15573**|**14913**|**14388**|**12785**|**11709**|
| Difference |  **56** |  **48** |  **48** |  **46** |  **48** |
| HP% Boost  |**+180%**|**+140%**|**+140%**|**+130%**|**+140%**|

### Instinct HP% Boosts
**Instinct HP%** are exact percentages as written (not **x/1024** like Gear Haste is, etc.)  \
**Instinct HP%** is applied after all flat bonuses are summed up.

#### Reasoning

[See here](/md/hp.MD#instincts) for supporting image evidence.

**Exact percentages**:  \
The +4% combined from equipping **Galka's Instinct I** and **Galka's Instinct II** equals the +4% from equipping only **Gnole Instinct II**.  \
My Gnole at the time of writing had enough HP where a difference of **1/1024** of its HP (**15**) would have been noticed.

| Base HP    | Galka I + Galka II |  Gnole II | ⌊Base HP * 1.04⌋ |
|:----------:|:------------------:|:---------:|:---------------:|
| **15517**  | **16137**          | **16137** | **16137**       |

**Instinct HP% being a single term**:
Instincts summing to **2%**, **4%**, **8%**, **10%**, **15%** and **20%** boosts were equipped.  \
The resulting maximum HP aligned with the boosts being summed into one term before multiplying the maximum HP value.

**0%** : No Instincts Equipped  \
**2%** : Equipped **Galka's Instinct I**  \
**4%** : Also equipped **Galka's Instinct II**  \
**8%** : Also equipped **Gnole Instinct II**  \
**10%** : Also equipped **Lizard Instinct I** and **Raptor Instinct I**  \
**15%** : Also equipped **Dragoon's Instinct**  \
**20%** : Also equipped **Rabbit Instinct I** and **Rabbit Instinct II**

|     |  0% |  2% |  4% |  8% | 10% | 15% | 20% |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Single Term| **15517** | **15827** | **16137** | **16758** | **17068** | **17844** | **18620** |
|All Multiplicative| **15517** | **15827** | **16143** | **16789** | **17127** | **17983** | **18893** |

## MP

### Best Guess at Formula

$`
Monster MP = \lfloor ((Innate MP * Species Boost_{MP}) + Flat MP Bonus) \cdot \sum Instinct MP_{\%} \rfloor
`$

$`
Flat MP Bonus = \lfloor Trait MP + Merit MP + \sum Instinct MP_{Flat} \rfloor
`$

### MON MP% Boost
*Untested as of yet, currently not found a way to control for innate MP.*  \
*Although monsters with "jobs" that don't have innate MP do only gain MP from merits and instincts.* \
_**1754MP** and **3437MP** from the two coeurl subspecies seem excessively high compared to player values for **WAR**/**BLM** and **RDM**/**BLM**. It seems to imply some multiplier is present, but that does not affect MP from merits nor instincts._

### Instinct MP Boosts
**Instinct MP%** are exact percentages as written (not **x/1024** like Gear Haste is, etc.)  \
**Instinct MP%** is applied after all flat bonuses are summed up.

#### Reasoning

[See here](/md/mp.MD#instincts) for supporting image evidence.

**Exact percentages**:  \
My Collared Lynx at the time of writing had enough MP where a difference of **1/1024** of its MP (**3**) would have been noticeable.

| Base | Observed | ⌊Base * 1.02⌋ | ⌊Base * (1 + 19/1024)⌋ | ⌊Base * (1 + 20/1024)⌋ | ⌊Base * (1 + 21/1024)⌋ |
|:------:|:------:|:------------:|:----------------------:|:---------------------:|:---------------------:|
|**3437**|**3505**|**3505**      |3504                    |3507                   |3510                   |

**Merit MP, Flat and Percentage Instinct Boosts**:  \
**Merits** and **Instincts** that list a flat max MP provide the same bonus regardless of **MON** species/jobs.


*Differences/contributions are calculated relative to max MP merits (15).*
| Merits                            | Gnole   | Coeurl  | Lynx    | Collared Lynx | Smilodon |
|:------------:                     |:-------:|:-------:|:-------:|:-------:|:-------:|
| 15 MP Merits                      | **150** | **150** | **1754**| **3437**| **150** |
| 13 MP Merits                      | **130** | **130** | **1734**| **3417**| **130** |
| Loss from Merits                  | **-20** | **-20** | **-20** | **-20** | **-20** |
| +100MP Instinct                   | **250** | **250** | **1854**| **3537**| **250** |
| Flat Instinct Contribution        | **100** | **100** | **100** | **100** | **100** |
| +2%MP Instinct                    | **153** | **153** | **1789**| **3505**| **153** |
| %MP Instinct Contribution         | **3**   | **3**   | **35**  | **68**  | **3**   |
| +100MP +2%MP Instincts            | **255** | **255** | **1891**| **3607**| **255** |
| Combined Instinct Contribution    | **105** | **105** | **137** | **170** | **105** |