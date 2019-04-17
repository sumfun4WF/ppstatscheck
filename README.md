# Feature
- Check the statistics of a player in Pripyat Hard, including times won/lost and time of obtaining the stripe for each class.
- You can also check the statstics of all players in a clan, however, there is a limit on this, please refer to Known Issue section.
# Usage
python3 checker.py
# Known Issue
- Some players choose to hide their in-game statistics, which means that it is not possible to obtain the times they win/lose in Pripyat. However, the list of achievement and the completion time can still be obtained. (WFTS hid it, but yes, it is possible to obtain them from the Warface API)
- Clan member list is fetched from [Warface True Sight](http://wfts.su). Warface API does not offer any method to obtain the clan member list, however, thanks to the huge database of WFTS, we can compose the clan member list as we know the clan of many individual players. **As that being said, the clan member list does not contain players that hid their statistics, and this will not be changed unless Warface change their API**
# Requirements
- python3
- python requests module
- brain
