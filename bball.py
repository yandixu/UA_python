"""
    Author: Yandi Xu
    
    File: bball.py
    
    Purpose: Read the file to find which conference has the highest win ratio.
    
"""

import sys

"""this class is to parse the line information and calculate
the win ratio of each team.

Attribute : self._line: the line.
            self._name: the team name.
            self._conf: the conference name.
            self._win_ratio: the win ratio."""
class Team:
    
    def __init__(self, line):
        #assert the type of line.
        assert type(line) == str
        
        leftp = line.rfind("(")
        rightp = line.rfind(")")
        lpart = line[:leftp].strip()
        rpart = line[rightp+1:].strip()
        self._conf = line[leftp+1:rightp]
        self._name = lpart
        
        win = int(rpart.split()[0])
        lose = int(rpart.split()[1])
        
        self._win_ratio = win/(win+lose)

           
    def name(self):
        """this method return team name""" 
        return self._name

    def conf(self):
        """this method return conference name"""
        return self._conf

    def win_ratio(self):
        """this method return win ratio"""
        return self._win_ratio

    def __str__(self):
        name = self._name
        win_ratio_str = self._win_ratio
        return "{} : {}".format(name, win_ratio_str)


"""this class is to add the team into the list and
calculate the win ratio average.

Attribute : self._conf: the conference name.
            self._teams: an empty to store the team object.
"""
class Conference:

    def __init__(self, conf):
        assert type(conf) == str
        
        self._conf = conf
        self._teams = []
            
    def __contains__(self, team):
        """this method check it the team object in the list

        Returns:
            if the team in the conference"""
        
        assert type(team) == Team
        
        return team in self._teams
   
    def name(self):
        """this method return conference name""" 
        return self._conf

    def add(self, team):
        """this method is used to add the team into the self._list.

        Parameters: team: the team object."""
        self._teams.append(team)
        
    def win_ratio_avg(self):
        """this method is used to calculate the average win ratio.

        Returns:
            avergae: the average win ratio of a conference"""
        if self._teams == []:
            return 0
        total = 0
        for team in self._teams:
            total += team.win_ratio()
        
        average = total/len(self._teams)
        return average
    
    def __str__(self):
        name = self.name()
        win_ratio_str = self.win_ratio_avg()     
        return "{} : {}".format(name, win_ratio_str)
    
"""this class is to create a conference set to collect the conferene and
find the best conference which get the highest win ratio average.

Attribute : Self._confs, an empty list to store the conference.
"""
class ConferenceSet:
    def __init__(self):
        self._confs = []

    def add(self, team):
        """this method is used to add the team into the approprtiate conference in the list
            of conference. If the list does not exist, create a new list.

            Parameters: team: the team object."""

        #assert the type of team.
        assert type(team) == Team

        #define the conf_set name.
        confs_name = [conf.name() for conf in self._confs]
        
        if team.conf() in confs_name:
            for conf in self._confs:
                if conf.name() == team.conf():
                    conf.add(team)
                
        else:
            new_conf = Conference(team.conf())
            new_conf.add(team)
            self._confs.append(new_conf)
       
    def best(self):
        """Find which conference has best win ratio average.

        Returns：
            best: a list with the conferences has the best win_ratio_avg value""" 
        best = []
        maxmm = 0
        for conf in self._confs:
            #asser teh type of confernece.
            assert type(conf) == Conference
            
            if conf.win_ratio_avg() > maxmm:
                best = [conf]
                maxmm = conf.win_ratio_avg() 
            elif conf.win_ratio_avg() == maxmm:
                best.append(conf)
                
        ### INVARIANT: the conference in the best_list has the best win ratio.

        return best       

def main():
    """Input the file and read it line by line. Create a conferenceSet
    class. Add each line information into class and get the best win ratio
    conference."""

    fname = input()
    try:
        file = open(fname)
    except FileNotFoundError:
        print("ERROR: Could not open file " + fname)
        sys.exit(1)
    
    lines = file.readlines()
    confs = ConferenceSet()
    
    for line in lines:
        line = line.strip()
        if line[0] !="#":
            team = Team(line)
            confs.add(team)
            
    for team in confs.best():
        print(team)
        
    file.close()
    
main()
    


        
