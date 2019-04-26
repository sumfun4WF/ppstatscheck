import requests


def getMembers(clan,server):
	member_list=[]
	if server.upper()=='NA':
		scode='na'
	elif server.upper()=='EU':
		scode='europe'
	body=str(requests.get('https://wfts.su/clans/%s/%s/members'%(scode,clan)).content)
	parsed=body.split('position_')
	for x in parsed:
		if '/profile/' in x:
				xsplited=x.split(' ')
				for i in xsplited:
					if '/profile/' in i:
						member_list.append((i[15:len(i)-1]))
	return member_list
	
def checkboost(username,server):
	print('%s, %s'%(username,server.upper()))
	if server.upper()=='NA':
		scode=2
	elif server.upper()=='EU':
		scode=1
	numStats=requests.get('http://api.wf.my.com/user/stat/?name=%s&server=%s'%(username,scode)).json()
	if "code" in numStats:
		if numStats['message']=='Игрок скрыл свою статистику':
			print('%s has hidden his numeric statistics.'%username)
			proceed=True
		elif numStats['message']=='Персонаж неактивен':
			print('%s did not login in a while and thus statistics are not available at this moment.'%username)
			proceed=False
		elif numStats['message']=='Пользователь не найден':
			print('%s does not exist.'%username)
			proceed=True
		else:
			print('API server is under maintenance. Statstics are temporarily unavailable.')
			proceed=False
	else:
		full_response=numStats['full_response']
		parsed=full_response.split('\n')
		for x in parsed:
			if 'chernobylhard' in x and 'player_sessions_won' in x:
					won=x.split(' ')[6]
			if 'chernobylhard' in x and 'player_sessions_lost' in x:
					lost=x.split(' ')[6]
		if 'won' not in locals():
			won=0
		if 'lost' not in locals():
			lost=0
		print('Pripyat Hard Won:%s\nPripyat Hard Loss:%s'%(won,lost))
		print('\n')
		proceed=True
	if proceed:
		stats=requests.get('http://api.wf.my.com/user/achievements/?name=%s&server=%s'%(username,scode)).json()
		for x in stats:
			if x['achievement_id']=='chernobyl_stripe_rifleman':
				print('Rifleman Stripe: %s'%x['completion_time'])
			elif x['achievement_id']=='chernobyl_stripe_medic':
				print('Medic Stripe: %s'%x['completion_time'])
			elif x['achievement_id']=='chernobyl_stripe_recon':
				print('Sniper Stripe: %s'%x['completion_time'])
			elif x['achievement_id']=='chernobyl_stripe_engineer':
				print('Engineer Stripe: %s'%x['completion_time'])
			else:
				continue
		print('\n')
		for x in stats:
			if x['achievement_id']=='chernobyl_stripe_hardcore':
				print('Zero Death Stripe: %s'%x['completion_time'])
			elif x['achievement_id']=='chernobyl_secret_badge_03':
				print('Golden Nut Badge: %s'%x['completion_time'])
			elif x['achievement_id']=='chernobyl_badge_boss':
				print('Mantis Down Stripe: %s'%x['completion_time'])
			else:
				continue
def checkBatch(member_list,server):
	for x in member_list:
		checkboost(x, server)
		print('\n------\n')
while True:	
	choice=input("Would you like you check for a clan or a player?\n")
	if choice.lower()=='clan':
		clan=input("Clan name: ")
		server=input("Server: ")
		print("\n")
		thelist=getMembers(clan, server)
		checkBatch(thelist, server)
		print('Players who hid their statistics cannot be checked by their clan name, please check with their username individually.')
	elif choice.lower()=='player':
		username=input("Username: ")
		server=input("Server: ")
		print("\n")
		checkboost(username, server)
	input("\nPress Enter to continue...\n")
