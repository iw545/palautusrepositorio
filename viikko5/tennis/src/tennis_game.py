class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def current_leader(self, score1, score2):
        if score1 > score2:
            return self.player1_name
        else:
            return self.player2_name

    def get_score(self):
        score = ""
        score_names = ["Love", "Fifteen", "Thirty", "Forty"]

        if self.player1_score == self.player2_score:
            if self.player1_score < 3:
                score = f"{score_names[self.player1_score]}-All"
            else:
                score = "Deuce"

        elif self.player1_score >= 4 or self.player2_score >= 4:
            leader = self.current_leader(self.player1_score, self.player2_score)
            score_difference = self.player1_score - self.player2_score

            if abs(score_difference) == 1:
                score = f"Advantage {leader}"
            else:
                score = f"Win for {leader}"

        else:
            score = f"{score_names[self.player1_score]}-{score_names[self.player2_score]}"

        return score
