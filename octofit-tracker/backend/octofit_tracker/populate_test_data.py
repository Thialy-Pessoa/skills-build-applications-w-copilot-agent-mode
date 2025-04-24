from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime

# Conectar ao MongoDB
client = MongoClient('localhost', 27017)
db = client['octofit_db']

# Limpar coleções existentes
db.users.drop()
db.teams.drop()
db.activity.drop()
db.leaderboard.drop()
db.workouts.drop()

# Criar usuários
test_users = [
    {"_id": ObjectId(), "username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
    {"_id": ObjectId(), "username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
    {"_id": ObjectId(), "username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
    {"_id": ObjectId(), "username": "crashoverride", "email": "crashoverride@mhigh.edu", "password": "crashoverridepassword"},
]
db.users.insert_many(test_users)

# Criar times
test_teams = [
    {"_id": ObjectId(), "name": "Team Alpha", "members": [test_users[0]["_id"], test_users[1]["_id"]]},
    {"_id": ObjectId(), "name": "Team Beta", "members": [test_users[2]["_id"], test_users[3]["_id"]]},
]
db.teams.insert_many(test_teams)

# Criar atividades
test_activities = [
    {"_id": ObjectId(), "user": test_users[0]["_id"], "activity_type": "run", "duration": 30},
    {"_id": ObjectId(), "user": test_users[1]["_id"], "activity_type": "walk", "duration": 45},
    {"_id": ObjectId(), "user": test_users[2]["_id"], "activity_type": "cycle", "duration": 60},
    {"_id": ObjectId(), "user": test_users[3]["_id"], "activity_type": "swim", "duration": 25},
]
db.activity.insert_many(test_activities)

# Criar leaderboard
test_leaderboard = [
    {"_id": ObjectId(), "user": test_users[0]["_id"], "score": 100},
    {"_id": ObjectId(), "user": test_users[1]["_id"], "score": 80},
    {"_id": ObjectId(), "user": test_users[2]["_id"], "score": 120},
    {"_id": ObjectId(), "user": test_users[3]["_id"], "score": 90},
]
db.leaderboard.insert_many(test_leaderboard)

# Criar workouts
test_workouts = [
    {"_id": ObjectId(), "name": "Pushups", "description": "Do 20 pushups", "date": datetime.utcnow()},
    {"_id": ObjectId(), "name": "Situps", "description": "Do 30 situps", "date": datetime.utcnow()},
]
db.workouts.insert_many(test_workouts)

print("Banco de dados octofit_db populado com dados de teste!")
