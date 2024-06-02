from flask.views import MethodView
from src.comman import top_scorers_team, top_scorers, top_wicket_taker_for_team, top_wicket_taker, most_wins
        
    
class AnalyserServices(MethodView):
    def get(self,*args, **kwargs):
        return "Its Working"

class TopRunScorerForTeam(MethodView):
    def get(self,team_name,n, *args, **kwargs):
        top_n_run_scorers = top_scorers_team(team_name=team_name, n=n)
        return top_n_run_scorers

class TopRunScorer(MethodView):
    def get(self, n, *args, **kwargs):
        top_n_run_scorers = top_scorers(n=n)
        return top_n_run_scorers

class TopWicketTakerForTeam(MethodView):
    def get(self, team_name, n, *args, **kwargs):
        top_n_wicket_taker = top_wicket_taker_for_team(team_name=team_name, n=n)
        return top_n_wicket_taker

class TopWicketTaker(MethodView):
    def get(self, n, *args, **kwargs):
        top_n_wicket_taker = top_wicket_taker(n=n)
        return top_n_wicket_taker
    
class MostWins(MethodView):
    def get(self, *args, **kwargs):
        most_matches_wins = most_wins()
        return most_matches_wins
    
