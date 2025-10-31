# Current Hypotheses

## HP

### Best Guess at Formula

Monster HP = ⌊ (**Innate HP** + **Trait HP** + **Merit HP**) * **MON HP%** * (Sum of **Instinct HP% Boosts**) ⌋

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