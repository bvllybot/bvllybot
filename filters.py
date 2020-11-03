import re

## kimbo
def morocco_filter(message):
    match = re.search('m[o-p0-9][r-s0-5]+[o-s0-5][c-e0-5]+o', message.content.lower())
    if match:
        return True

def jesus_filter(message):
    match = re.search('jesus', message.content.lower())
    if match:
         return True
    

def rules_filter(message):
    match = re.search('rules', message.content.lower())
    if match:
         return True 
 
def cuck_filter(message):
    match = re.search('cuck|sissy|gasm|gay|homosexual|femboy|transgender|submissive|femdom|bnwo|rim', message.content.lower())
    if match:
         return True
 
##kimbo

def nigger_filter(message):
    match1 = re.search('n[a-i0-9][a-g0-5][a-g0-5][a-e0-5]r', message.content.lower())
    match2 = re.search('n[a-i0-9][a-g0-5][a-g0-5][a4]', message.content.lower())
    if match1 or match2:
        return True 

def white_filter(message):
    match = message.content.lower()
    if "white" in match:
        return True