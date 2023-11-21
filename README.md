# Introduction of Demo json file

### Raw information
  variable data is the 
  <span style="color: cyan;">
  "raw data"
  </span>
  read from the json file.
:q
    > data = json.load(file)

Here list the attributes in the json file:

>__important info__: \
> 'matchID' \
> 'mapName'  \
> 'matchPhases' \  
> 'playerConnections' \
>**_'gameRounds'_**  ============>  which contains the track data\
> \
> __some redundant info__: \
> 'clientName','tickRate','playbackTicks', 'playbackFramesCount','parsedToFrameIdx',
> 'parserParameters', 'serverVars','matchmakingRanks', 'chatMessages',

<br>



### __Round information__

data['gameRounds'] is a list where each element is a dictionary with the corresponding 
round information. 

    data['gameRounds'][i] ======> i_th round information  

Here list the attributes in the __*"gameRounds"*__ branch:

    > data['gameRounds'][i].keys()

> __Important info__ :\
> 'roundNum', 
> 'startTick','endTick', 'bombPlantTick',
> 'tScore', 'ctScore', 'endTScore', 'endCTScore', 'winningTeam', 'losingTeam', 'roundEndReason',
> 'ctBuyType', 'tBuyType',\
> __'frames'__ ========> important
> 
> __some redundant info__:\
> 'isWarmup',\
>  'freezeTimeEndTick',  'endOfficialTick',  \
> 'ctTeam', 'tTeam', 'winningSide', 
> 'ctFreezeTimeEndEqVal', 'ctRoundStartEqVal', 'ctRoundSpendMoney', 
> 'tFreezeTimeEndEqVal', 'tRoundStartEqVal', 'tRoundSpendMoney','ctSide', 'tSide', 'bombEvents',
> 'grenades', 'flashes', \
> 'kills', 'damages',  'weaponFires' =============> relatively long



### __Frame_info__

```
data['gameRounds'][i]['frames'][j]              #j_th frame of i_th round
```


## Database Structure Design



