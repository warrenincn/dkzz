#!/usr/bin/python

class Game_Exception(Exception):
	def __init__(self, m):
		self.value = m
	def __str__(self):
		return repr(self.value)

class Game_Rule:
	GAME_FREEDOM_WARRIOR_WIN = 1
	GAME_FREEDOM_WARRIOR_LOSS = 0

	round_max = 5
	mession_max = 5
	game_win_mession_count = 3
	group_rule = ((2,2,2,3,3), (2,3,4,3,4))
	mession_success_rule = ((0,0,0,0,0), (0,0,0,0,0))
	@staticmethod
	def get_group_rule(player_num):
		if(player_num >=5 and player_num <= 10):
			return Game_Rule.group_rule[player_num - 5]
	@staticmethod
	def get_mession_rule(player_num):
		if(player_num >=5 and player_num <= 10):
			return Game_Rule.mession_success_rule[player_num - 5]

class Player:
	def __init__(self, role, ID):
		self.player_role = role
		self.player_ID	= ID
		self.has_item = 0
	def vote_team(self):
		print 'Player', self.player_ID,' ',
		vote_result = input("Vote for team. Agree 1, Disagree 0. ")
		return vote_result
	def vote_mession(self):
		print 'Player', self.player_ID,' ',
		vote_result = input("Vote for mession. Agree 1, Disagree 0. ")
		return vote_result
	def add_item(self, item):
		self.has_item = 1
		self.item = item 
	def choose_team_member(self):
		chosen_id = 0
		chosen_id = input("Choose player_ID: ")
		return chosen_id
	def player_speek(self):
		p_speech = raw_input("Say: ")
		return p_speech 

class Mession:
	def __init__(self, mession_team, max_v_fail):
		self.mession_team = mession_team
		self.max_v_fail = max_v_fail
	def start_mession(self):
		mession_v_fail = 0
		for player in self.mession_team:
			if(player.vote_mession() == 0):
				mession_v_fail += 1
		if(mession_v_fail < self.max_v_fail):
			print 'Mession success.'
			return 1
		else:
			print 'Mession failed'
			return 0
	
class Game:
	def __init__(self, player_list):
		self.player_list = player_list;
		self.player_nums = len(player_list);
		self.current_mession = 0;
	#def start_vote_team(self, mession):
		
	def get_next_leader(self, leader):
		index = self.player_list.index(leader)
		index = (index + 1) % len(self.player_list)
		return self.player_list[index]
		
	def game_start(self, fisrt_leader):
		self.mession_succ_count = 0
		gp_role = Game_Rule.get_group_rule(self.player_nums);
		leader = fisrt_leader
		for m_count in range(0, Game_Rule.mession_max):
			team_player_num = gp_role[m_count]
			for m_round in range(0, Game_Rule.round_max):
				team_candidate = []
				team_member = []
				team_v_suc = 0
				p_num = team_player_num
				cand_num = p_num
				while cand_num > 0:
					team_candidate.append(leader.choose_team_member())
					cand_num -= 1
				"display candidate_member"
				print team_candidate
				for pl in self.player_list:
					pl.player_speek()

				while p_num > 0:
					team_member.append(self.player_list[leader.choose_team_member()])
					p_num -= 1
				for pl in self.player_list:
					if(pl.vote_team() != 0):
						team_v_suc += 1
				if(team_v_suc > self.player_nums - team_v_suc ):
					print 'Build team OK..'
					mession = Mession(team_member, Game_Rule.get_mession_rule(self.\
							player_nums))
					if(mession.start_mession()):
						self.mession_succ_count += 1
				else:
					if m_round == Game_Rule.round_max - 1:
						print 'failed to build team in 5 rounds. Game Over'
						raise Game_Exception(Game_Rule.GAME_FREEDOM_WARRIOR_LOSS)
					else:
						leader = get_next_leader(leader) 
				if(self.mession_succ_count >= 3 ):
					raise Game_Exception(Game_Rule.GAME_FREEDOM_WARRIOR_WIN)
				elif(m_count - self.mession_succ_count >= 3):
					raise Game_Exception(Game_Rule.GAME_FREEDOM_WARRIOR_LOSS)



