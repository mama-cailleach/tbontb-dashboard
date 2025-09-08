# Data Dictionary for TBONTB Dashboard (First Iteration)

This document explains the columns in each CSV used for the first version of the app.

---

## TBONTB_all_batting.csv
| Column         | Description                                      | Example         |
|----------------|--------------------------------------------------|-----------------|
| match_id       | Unique match identifier                          | M001            |
| team_id        | Team code                                        | TBONTB          |
| team_name      | Team name                                        | Two Bats or Not To Bat |
| player_id      | Player code (may be blank for legacy data)       | TBONTB_0004     |
| player_name    | Name of the player                               | TGR Thorn       |
| batting_order  | Batting position (1 = opener, etc.)              | 4               |
| dismissal_mode | How the player got out (e.g., Bowled, Not Out)   | Bowled          |
| runs           | Runs scored in the match                         | 21              |
| balls          | Balls faced                                      | 14              |
| 4s             | Number of 4s hit                                 | 2               |
| 6s             | Number of 6s hit                                 | 0               |
| strike_rate    | (Runs/Balls)*100                                 | 150             |
| did_not_bat    | TRUE if player did not bat                       | FALSE           |
| Season         | Year/season                                      | 2013            |

---

## TBONTB_all_bowling.csv
| Column         | Description                                      | Example         |
|----------------|--------------------------------------------------|-----------------|
| match_id       | Unique match identifier                          | M001            |
| team_id        | Team code                                        | TBONTB          |
| team_name      | Team name                                        | Two Bats or Not To Bat |
| player_id      | Player code                                      | TBONTB_0004     |
| player_name    | Name of the player                               | TGR Thorn       |
| overs          | Overs bowled                                     | 4               |
| maidens        | Maiden overs bowled                              | 0               |
| runs_conceded  | Runs given while bowling                         | 32              |
| wickets        | Wickets taken                                    | 1               |
| economy        | Runs per over                                    | 8.00            |
| Season         | Year/season                                      | 2013            |

---

## TBONTB_all_matches.csv
| Column                  | Description                                 | Example         |
|-------------------------|---------------------------------------------|-----------------|
| Team Name               | Name of our team                            | Two Bats or Not To Bat |
| Opposition Name         | Name of opposition team                     | Dicket          |
| Tournament              | Competition or league name                  | League          |
| Date                    | Match date (DD/MM/YYYY)                     | 12/05/2013      |
| Time                    | Start time                                  | 17:00           |
| Venue                   | Ground name                                 | Clapham Common oval |
| Umpire                  | Umpire name                                 | Rezaul Karim Hiron |
| Player of the Match     | Player awarded (may be blank)               |                 |
| Result                  | Win/Loss/Tie                                | Loss            |
| Result Info             | Text summary of result                      | Dicket Won by 147 runs |
| Match ID                | Unique match identifier                     | M001            |
| Opposition Runs         | Runs scored by opposition                   | 219             |
| Opposition Wickets Fallen| Wickets lost by opposition                  | 2               |
| Opposition Overs        | Overs batted by opposition                  | 18              |
| Team Runs               | Runs scored by our team                     | 72              |
| Team Wickets Fallen     | Wickets lost by our team                    | 7               |
| Team Overs              | Overs batted by our team                    | 18              |
| Season                  | Year/season                                 | 2013            |
| Bowl First              | TRUE if we bowled first                     | TRUE            |
| difference              | Run difference (positive = loss)            | 147             |
| POTM Team               | Team of Player of the Match (if known)      | -               |

---

## TBONTB_players_id_index.csv
| Column      | Description                        | Example      |
|-------------|------------------------------------|--------------|
| player_id   | Unique player code                 | TBONTB_0004  |
| player_name | Name of the player                 | TGR Thorn    |
| match_id    | Debut match or first match ID      | M001         |
| Season      | Debut season                       | 2013         |
| matches     | Total matches played               | 9            |

---

## TBONTB_players_summary.csv
| Column         | Description                                      | Example         |
|----------------|--------------------------------------------------|-----------------|
| player_id      | Unique player code                               | TBONTB_0004     |
| player_name    | Name of the player                               | TGR Thorn       |
| roles          | Player roles (if tracked)                        | (blank)         |
| matches        | Matches played                                   | 9               |
| bat_innings    | Batting innings played                           | 9               |
| runs           | Total runs scored                                | 227             |
| balls_faced    | Balls faced in career                            | 173             |
| 4s             | Total 4s hit                                     | 0               |
| 6s             | Total 6s hit                                     | 0               |
| 50s            | 50+ scores made                                  | 1               |
| 30s            | 30+ scores made                                  | 2               |
| high_score     | Highest score (may have * for not out)           | 51              |
| strike_rate    | Career strike rate                               | 131.21          |
| bat_avg        | Career batting average                           | 32.43           |
| dismissals     | Times dismissed                                  | 7               |
| ducks          | 0s scored                                        | 0               |
| not_outs       | Not out innings                                  | 2               |
| bowl_innings   | Bowling innings played                           | 9               |
| overs_bowled   | Overs bowled                                     | 34.0            |
| runs_conceded  | Runs given while bowling                         | 336             |
| wickets        | Wickets taken                                    | 4               |
| maidens        | Maiden overs bowled                              | 0               |
| economy        | Runs per over                                    | 9.88            |
| bowl_avg       | Bowling average                                  | 84.00           |
| bbi            | Best bowling in innings (e.g., 1/39)             | 1/39            |
| 3wickets       | 3+ wicket hauls                                  | 0               |
| matches_played | Matches played (repeat of matches)               | 9               |

---

## TBONTB_venues.csv
| Column           | Description                                    | Example         |
|------------------|------------------------------------------------|-----------------|
| Venue            | Name of the ground                             | Clapham Common oval |
| Total Matches    | Matches played at this venue                   | 82              |
| Loss             | Matches lost                                   | 79              |
| Tie              | Matches tied                                   | (blank)         |
| Win              | Matches won                                    | 3               |
| Runs Scored      | Total runs scored by our team                  | 9542            |
| Wkts Fallen      | Total wickets lost by our team                 | 495             |
| Runs Conceded    | Total runs conceded to opposition              | 17441           |
| Wkts Taken       | Total wickets taken by our team                | 340             |
| Umps             | Number of different umpires                    | 7               |
| Oppos            | Number of different oppositions                | 36              |
| Ovrs Bat         | Overs batted by our team                       | 1528.2          |
| Ovrs Bowl        | Overs bowled by our team                       | 1613.1          |
| Bat Ave          | Batting average at this venue                  | 19.28           |
| Bowl Ave         | Bowling average at this venue                  | 51.30           |
| Percentage Played| % of all matches played at this venue          | 45.8            |
