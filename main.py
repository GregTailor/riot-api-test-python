from helper import get_summoner_data


summoner_one = "GregTailor"
summoner_two = "BenyHawk"


summoner_one_data = get_summoner_data(summoner_one)
summoner_two_data = get_summoner_data(summoner_two)
print(summoner_one_data)
print(summoner_two_data)
if summoner_one_data['summonerLevel'] > summoner_two_data['summonerLevel']:
    print(f'{summoner_one} has higher summoner level')
elif summoner_one_data['summonerLevel'] < summoner_two_data['summonerLevel']:
    print(f'{summoner_two} has higher summoner level')
else:
    print(f'You are both at level {summoner_one_data["summonerLevel"]}')