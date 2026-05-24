# HP Boosts

## Species HP% Boost

| Merits     | Gnole   | Coeurl  | Lynx    | Collared Lynx | Smilodon |
|:----------:|:-------:|:-------:|:-------:|:-------:|:-------:|
| Level      | 78      | 90      | 90      | 90      | 75      |
|  13HP      |**15517**|**14865**|**14340**|**12739**|**11661**|
|  15HP      |**15573**|**14913**|**14388**|**12785**|**11709**|
| Difference |  **56** |  **48** |  **48** |  **46** |  **48** |
| HP% Boost  |**+180%**|**+140%**|**+140%**|**+130%**|**+140%**|


<details>
<summary>Screenshots</summary>

###### Gnole
<img src="../img/stats_gnole_13hpmp.png" title="Gnole with 13 HP and MP Merit levels">
<img src="../img/stats_gnole_base.png" title="Gnole with full merit levels">

###### Coeurl
<img src="../img/stats_coeurl_13hpmp.png" title="Coeurl with 13 HP and MP Merit levels">
<img src="../img/stats_coeurl_base.png" title="Coeurl with full merit levels">

###### Lynx
<img src="../img/stats_lynx_13hpmp.png" title="Lynx with 13 HP and MP Merit levels">
<img src="../img/stats_lynx_base.png" title="Lynx with full merit levels">

###### Collared Lynx
<img src="../img/stats_collaredlynx_13hpmp.png" title="Collared Lynx with 13 HP and MP Merit levels">
<img src="../img/stats_collaredlynx_base.png" title="Collared Lynx with full merit levels">

###### Smilodon
<img src="../img/stats_smilodon_13hpmp.png" title="Smilodon with 13 HP and MP Merit levels">
<img src="../img/stats_smilodon_base.png" title="Smilodon with full merit levels">

</details>

### Theorized Monster HP% Boost Values Based on HP Merits

Each HP merit increases player maximum HP by 10, but increases monster HP by a different amount depending on the monster.  
There appears to be a factor that multiplies max HP based upon monster family and the specific monster's main job.  
*This HP% Boost seems to be _additive_ with MNK's `Mantra` skill,  but _multiplicative_ with HP% Instincts.*

#### Theorized Max HP Formula
$$ MaxHP = BaseHP * (SpeciesHPBoost + MantraHPBoost) * \sum{InstinctHPBoost} $$

#### Theorized Base HP from Obseved Values
$$ BaseHP = MaxHP_{15M} / () $$

| Species           | Jobs      | Level| Max HP (15M) | Max HP (14M) | HP Lost | Theorized Base HP | HP Trait Boost | HP Merit Boost |
|:-----------------:|:---------:|:----:|:------------:|:------------:|:-------:|:-----------------:|:--------------:|:--------------:|
| Rabbit            | `WAR/WAR` | `75` | `10733` | `10711` | `22` | `4879` |
| Onyx Rabbit       | `WAR/BLM` | `75` | `10351` | `10329` | `22` | `4705` |
| Alabaster Rabbit  | `WAR/WHM` | `75` | `10434` | `10412` | `22` | `4743` |
| Tiger             | `WAR/WAR` | `75` | `11709` | `11685` | `24` | `4879` |
| Smilodon          | `WAR/WAR` | `75` | `11709` | `11685` | `24` | `4879` |
| Legendary Tiger   | `WHM/THF` | `75` | `9219`  | `9198`  | `21` | `4390` |
| Opo-Opo           | `WAR/WAR` | `75` | `11709` | `11685` | `24` | `4879` |
| Gnole             | `MNK/MNK` | `80` | `16058` | `16030` | `28` | `5735` |
| Coeurl            | `WAR/WAR` | `90` | `14913` | `14889` | `24` | `6213` |
| Lynx              | `WAR/BLM` | `90` | `14388` | `14364` | `24` | `5995` |
| Collared Lynx     | `RDM/BLM` | `90` | `12785` | `12762` | `23` | `5559` |

## Instincts

### HP% Boosts being exact percentages

*Demonstrating using stats for lv78 Gnole:*
| Base HP    | Galka I + Galka II |  Gnole II | ⌊Base HP * 1.04⌋ |
|:----------:|:------------------:|:---------:|:---------------:|
| **15517**  | **16137**          | **16137** | **16137**       |

<details>
<summary>Screenshots</summary>
<img src="../img/instinct_13hp_gnole_0.png" width="360" title="No instincts equipped">
<img src="../img/instinct_13hp_gnole_4.png" width="360" title="+4% (+2+2)% HP Boost from Galka Instinct I&II">
<img src="../img/instinct_13hp_gnole_4b.png" width="360" title="+4% HP Boost from Gnole Instinct II">
</details>

### HP% Boost being a single term instead of multiplicative

*Demonstrating using stats for lv78 Gnole:*
|     |  0% |  2% |  4% |  8% | 10% | 15% | 20% |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Single Term| **15517** | **15827** | **16137** | **16758** | **17068** | **17844** | **18620** |
|All Multiplicative| **15517** | **15827** | **16143** | **16789** | **17127** | **17983** | **18893** |

<details>
<summary>Screenshots</summary>
<img src="../img/instinct_13hp_gnole_0.png" width="360" title="No instincts equipped">
<img src="../img/instinct_13hp_gnole_2.png" width="360" title="+2% HP from Galka Instinct's I">
<img src="../img/instinct_13hp_gnole_4.png" width="360" title="+4% HP from Galka Instinct's I, Galka's Instinct II">
<img src="../img/instinct_13hp_gnole_8.png" width="360" title="+8% HP from Galka Instinct's I, Galka's Instinct II, Gnole Instinct II">
<img src="../img/instinct_13hp_gnole_10.png" width="360" title="+10% HP from Galka Instinct's I, Galka's Instinct II, Gnole Instinct II, Lizard Instinct I, Raptor Instinct I">
<img src="../img/instinct_13hp_gnole_15.png" width="360" title="+15% HP from Galka Instinct's I, Galka's Instinct II, Gnole Instinct II, Lizard Instinct I, Raptor Instinct I, Dragoon's Instinct">
<img src="../img/instinct_13hp_gnole_20.png" width="360" title="+15% HP from Galka Instinct's I, Galka's Instinct II, Gnole Instinct II, Lizard Instinct I, Raptor Instinct I, Dragoon's Instinct, Rabbit Instinct I, Rabbit Instinct II">
</details>