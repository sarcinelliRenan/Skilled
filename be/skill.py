import numpy as np

skilltable =  np.genfromtxt('data/skills.csv', delimiter=',',skip_header=1)

def cart2pol(x, y):
	rho = np.sqrt(x**2 + y**2)
	phi = np.arctan2(y, x)
	phi = np.rad2deg(phi)
	if phi < 0:
		phi = 360+phi
	return(rho, phi)

def pol2cart(rho, phi):
	phi = np.deg2rad(phi)
	x = rho * np.cos(phi)
	y = rho * np.sin(phi)
	return(x, y)
	
def reg_lin(x,t):
	x = np.c_[ np.ones(x.shape[0]),x ]
	w = np.linalg.inv(x.T.dot(x)).dot(x.T).dot(t)
	return w

def define_theta(user,game): # User:(INT,DES,WIS) GAME:(SHOTS,HIT)
	# Assuming that player who shots a lot tends to preffer less cooldown skill, a player that misses shots tends to prefer faster skills and a player with good accuracy tends to damage
	total_points = sum(user)
	user = np.array(user)/total_points
	cart_INT = pol2cart(user[0],10)
	cart_DES = pol2cart(user[1],130)
	cart_WIS = pol2cart(user[2],250)
	cart_result = np.array(cart_INT)+np.array(cart_DES)+np.array(cart_WIS)
	return cart2pol(cart_result[0],cart_result[1])[1]
	
def get_skill(lvl,user_stats,game_stats,model):
	if lvl == 11: #Generate linear regression model
		model = reglin(model,model)
	if lvl < 11: # Get from table and save data in model
		st = [x for x in skilltable if x[0] == lvl]
		theta = define_theta(user_stats,game_stats)
		newskill = np.array([x for x in st if x[4]<=theta and x[5]>theta])[0,:4]
		model.append(newskill)
	else: # Uses the model generated
		#todo
		return 0
	return newskill

print (get_skill(5,[10,2,5],None,[]))