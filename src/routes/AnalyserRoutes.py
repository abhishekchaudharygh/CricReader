from .BaseRoutes import getNewRoute
from ..services.Analyser import AnalyserServices, TopRunScorerForTeam, TopRunScorer, TopWicketTakerForTeam, TopWicketTaker, MostWins

routes = getNewRoute("analyze")
routes.add_url_rule('/', view_func=AnalyserServices.as_view('ipl'), methods=['GET'])

routes.add_url_rule('/top_scorers/team/<team_name>/<int:n>', view_func=TopRunScorerForTeam.as_view('top-scorer-of-teams'), methods=['GET'])

routes.add_url_rule('/top_scorers/overall/<int:n>', view_func=TopRunScorer.as_view('top-scorer'), methods=['GET'])

routes.add_url_rule('/top_wicket_takers/team/<team_name>/<int:n>', view_func=TopWicketTakerForTeam.as_view('top-wicket-takers-for-team'), methods=['GET'])

routes.add_url_rule('/top_wicket_takers/overall/<int:n>', view_func=TopWicketTaker.as_view('top-wicket-takers'), methods=['GET'])

routes.add_url_rule('/most_wins', view_func=MostWins.as_view('most-wins'), methods=['GET'])